from __future__ import annotations
from datetime import datetime, timezone
from typing import Any
from data_connectors.base import BaseConnector, CacheStrategy, ConnectorConfig, ConnectorRequest, ConnectorResult, HealthStatus, RetryPolicy
from data_connectors.normalizer import DataNormalizer

CONFIG = {'connector_id': 'news',
 'name': 'News',
 'source': 'Public News',
 'source_type': 'public_news',
 'base_url': 'https://news.example.com',
 'version': '0.1.0',
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
    """Mock News Connector with Config/Input/Output/Error/Retry/Cache/Health/Test."""

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

    def input_schema(self) -> dict[str, Any]:
        return INPUT_SCHEMA

    def output_schema(self) -> dict[str, Any]:
        return OUTPUT_SCHEMA

    def fetch(self, request: ConnectorRequest) -> ConnectorResult:
        required = INPUT_SCHEMA.get("required", [])
        missing = [field for field in required if field not in request.query]
        if missing:
            return self.error_result(request, "INPUT_VALIDATION_ERROR", f"missing required fields: {missing}", retryable=False)
        raw = self._mock_raw(request)
        return self.normalize(raw, request)

    def _mock_raw(self, request: ConnectorRequest) -> dict[str, Any]:
        return {'query': 'AI servers',
 'headline': 'Mock news headline',
 'publisher': 'Mock News',
 'url': 'https://news.example.com/mock'}

    def normalize(self, raw: dict[str, Any], request: ConnectorRequest) -> ConnectorResult:
        return self.normalizer.result(self.config, request, raw, raw.get("url", self.config.base_url))

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
