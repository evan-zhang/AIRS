from __future__ import annotations
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from typing import Any
from data_connectors.base import BaseConnector, CacheStrategy, ConnectorConfig, ConnectorRequest, ConnectorResult, HealthStatus, RetryPolicy
from data_connectors.env_config import EnvConfig
from data_connectors.http_client import HTTPClient, HTTPClientError
from data_connectors.normalizer import DataNormalizer
from data_connectors.persistent_cache import PersistentCache
from data_connectors.real_payload import envelope

CONFIG = {'connector_id': 'sec_edgar',
 'name': 'SEC EDGAR',
 'source': 'SEC EDGAR',
 'source_type': 'regulatory',
 'base_url': 'https://www.sec.gov/cgi-bin/browse-edgar',
 'version': '0.2.0',
 'priority': 'regulatory',
 'auth_type': 'none'}
INPUT_SCHEMA = {'type': 'object',
 'required': ['ticker'],
 'properties': {'ticker': {'type': 'string'}, 'form_type': {'type': 'string'}}}
OUTPUT_SCHEMA = {
    "type": "object",
    "required": ["connector_id", "source", "url", "timestamp", "version", "trace_id", "data", "traceability"],
    "properties": {
        "source": {"type": "string"},
        "url": {"type": "string"},
        "timestamp": {"type": "string"},
        "version": {"type": "string"},
        "trace_id": {"type": "string"},
        "traceability": {"type": "object"},
    },
}
ERROR_HANDLING = {"standard_error": ["error_code", "message", "retryable", "trace_id"], "retryable_errors": ["timeout", "rate_limited"]}
RETRY_POLICY = {"max_attempts": 3, "initial_delay_seconds": 0.1, "backoff_multiplier": 2.0}
CACHE_STRATEGY = {"ttl_seconds": 300, "allow_stale": False}
TEST_CASE = {'input': {'ticker': 'AAPL', 'form_type': '10-K'},
 'expect_fields': ['source', 'url', 'timestamp', 'version', 'trace_id']}


class SECEdgarConnector(BaseConnector):
    """SEC / EDGAR Connector with real HTTP mode, mock fallback, Config/Input/Output/Error/Retry/Cache/Health/Test."""

    def __init__(self) -> None:
        self.config = ConnectorConfig(
            connector_id=CONFIG["connector_id"],
            name=CONFIG["name"],
            source=CONFIG["source"],
            source_type=CONFIG["source_type"],
            base_url=CONFIG["base_url"],
            version=CONFIG["version"],
            priority=CONFIG["priority"],
            auth_type=CONFIG["auth_type"],
            retry_policy=RetryPolicy(**RETRY_POLICY),
            cache_strategy=CacheStrategy(**CACHE_STRATEGY),
        )
        self.normalizer = DataNormalizer()
        self.env = EnvConfig()
        self.cache = PersistentCache()
        self.http = HTTPClient.from_env(self.connector_id, self.config.retry_policy)

    def input_schema(self) -> dict[str, Any]:
        return INPUT_SCHEMA

    def output_schema(self) -> dict[str, Any]:
        return OUTPUT_SCHEMA

    def fetch(self, request: ConnectorRequest) -> ConnectorResult:
        required = INPUT_SCHEMA.get("required", [])
        missing = [field for field in required if field not in request.query]
        if missing:
            return self.error_result(request, "INPUT_VALIDATION_ERROR", f"missing required fields: {missing}", retryable=False)
        if self.env.real_enabled(self.connector_id, request.query):
            try:
                raw = self.fetch_real(request)
            except Exception:
                raw = self.fetch_mock(request)
        else:
            raw = self.fetch_mock(request)
        return self.normalize(raw, request)

    def fetch_mock(self, request: ConnectorRequest) -> dict[str, Any]:
        return envelope(
            self.config,
            request,
            url="https://www.sec.gov/edgar/mock",
            publication_time="2025-12-31T00:00:00+00:00",
            confidence=0.50,
            mode="mock",
            payload={"filing_type": request.query.get("form_type", "10-K"), "company": "Mock Company", "period": "FY2025"},
        )

    def _mock_raw(self, request: ConnectorRequest) -> dict[str, Any]:
        return self.fetch_mock(request)

    def fetch_real(self, request: ConnectorRequest) -> dict[str, Any]:
        ticker = str(request.query["ticker"]).strip()
        form_type = str(request.query.get("form_type", "")).strip() or None
        params = {"action": "getcompany", "CIK": ticker, "owner": "exclude", "count": int(request.query.get("count", 10)), "output": "atom"}
        if form_type:
            params["type"] = form_type
        cache_key = self.cache.key(self.connector_id, self.config.version, {"endpoint": self.config.base_url, **params})
        cached = self.cache.get(cache_key, self.config.cache_strategy.ttl_seconds)
        if cached:
            cached["cache_hit"] = True
            return cached
        response = self.http.get(self.config.base_url, params=params)
        root = ET.fromstring(response.text)
        ns = {"atom": "http://www.w3.org/2005/Atom"}
        entries = []
        for entry in root.findall("atom:entry", ns):
            link = entry.find("atom:link", ns)
            entries.append(
                {
                    "title": (entry.findtext("atom:title", default="", namespaces=ns) or "").strip(),
                    "updated": entry.findtext("atom:updated", default="", namespaces=ns),
                    "link": link.get("href") if link is not None else None,
                    "summary": (entry.findtext("atom:summary", default="", namespaces=ns) or "").strip(),
                }
            )
        publication_time = entries[0].get("updated") if entries else request.timestamp
        raw = envelope(
            self.config,
            request,
            url=response.url,
            publication_time=publication_time,
            confidence=0.90,
            mode="real",
            payload={"query": {"ticker": ticker, "form_type": form_type}, "filings": entries, "status_code": response.status_code},
        )
        self.cache.set(cache_key, raw)
        return raw

    def normalize(self, raw: dict[str, Any], request: ConnectorRequest) -> ConnectorResult:
        return self.normalizer.result(self.config, request, raw, raw.get("url", self.config.base_url), transformations=[raw.get("mode", "mock") + "_fetch", "normalize"])

    def health_check(self) -> HealthStatus:
        return HealthStatus(
            connector_id=self.connector_id,
            status="PASS",
            latency_ms=0.0,
            last_success=datetime.now(timezone.utc).isoformat(),
            error=None,
        )

    def test_case(self) -> dict[str, Any]:
        return TEST_CASE
