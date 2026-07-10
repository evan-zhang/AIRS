from __future__ import annotations
from datetime import datetime, timezone
from typing import Any
from data_connectors.base import BaseConnector, CacheStrategy, ConnectorConfig, ConnectorRequest, ConnectorResult, HealthStatus, RetryPolicy
from data_connectors.env_config import EnvConfig
from data_connectors.http_client import HTTPClient
from data_connectors.normalizer import DataNormalizer
from data_connectors.persistent_cache import PersistentCache
from data_connectors.real_payload import envelope

CONFIG = {'connector_id': 'news',
 'name': 'News',
 'source': 'Public News',
 'source_type': 'public_news',
 'base_url': 'https://news.example.com',
 'version': '0.2.0',
 'priority': 'public_news',
 'auth_type': 'none'}
INPUT_SCHEMA = {'type': 'object', 'required': ['query'], 'properties': {'query': {'type': 'string'}, 'language': {'type': 'string'}}}
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
TEST_CASE = {'input': {'query': 'AI servers', 'language': 'zh'},
 'expect_fields': ['source', 'url', 'timestamp', 'version', 'trace_id']}


class NewsConnector(BaseConnector):
    """Generic News Connector with configurable real API mode, mock fallback, Config/Input/Output/Error/Retry/Cache/Health/Test."""

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
        if self.env.real_enabled(self.connector_id, request.query) and self.env.get("NEWS_API_ENDPOINT"):
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
            url="https://news.example.com/mock",
            publication_time=request.timestamp,
            confidence=0.50,
            mode="mock",
            payload={"query": request.query.get("query", "AI servers"), "headline": "Mock news headline", "publisher": "Mock News"},
        )

    def _mock_raw(self, request: ConnectorRequest) -> dict[str, Any]:
        return self.fetch_mock(request)

    def fetch_real(self, request: ConnectorRequest) -> dict[str, Any]:
        endpoint = self.env.get("NEWS_API_ENDPOINT")
        if not endpoint:
            raise RuntimeError("NEWS_API_ENDPOINT is not configured")
        api_key = self.env.get("NEWS_API_KEY")
        key_name = self.env.get("NEWS_API_KEY_NAME", "apiKey") or "apiKey"
        params = {"q": request.query["query"], "language": request.query.get("language"), "pageSize": int(request.query.get("limit", 10))}
        if api_key:
            params[key_name] = api_key
        cache_key = self.cache.key(self.connector_id, self.config.version, {"endpoint": endpoint, "params": {k: v for k, v in params.items() if k != key_name}})
        cached = self.cache.get(cache_key, self.config.cache_strategy.ttl_seconds)
        if cached:
            cached["cache_hit"] = True
            return cached
        response = self.http.get(endpoint, params=params, secrets=[api_key])
        payload = response.json()
        articles = payload.get("articles") if isinstance(payload.get("articles"), list) else []
        publication_time = (articles[0].get("publishedAt") if articles else None) or request.timestamp
        raw = envelope(self.config, request, url=response.url, publication_time=publication_time, confidence=0.70, mode="real", payload={"query": request.query["query"], "response": payload, "status_code": response.status_code})
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
