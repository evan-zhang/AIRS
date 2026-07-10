from __future__ import annotations

import pytest

from data_connectors.base import ConnectorRequest
from data_connectors.connectors.news import NewsConnector
from data_connectors.real_payload import REQUIRED_REAL_FIELDS


def test_news_real_fetch_contains_required_fields() -> None:
    connector = NewsConnector()
    if not connector.env.get("NEWS_API_ENDPOINT"):
        pytest.skip("NEWS_API_ENDPOINT is not configured")
    request = ConnectorRequest({"query": "AI servers", "language": "en", "limit": 3})
    try:
        raw = connector.fetch_real(request)
    except Exception as exc:  # noqa: BLE001
        pytest.skip(f"News API unavailable or credentials missing: {exc}")
    assert raw.get("mode") == "real"
    for field in REQUIRED_REAL_FIELDS:
        assert raw.get(field) is not None
    assert "response" in raw["payload"]
