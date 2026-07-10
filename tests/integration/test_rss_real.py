from __future__ import annotations

import pytest

from data_connectors.base import ConnectorRequest
from data_connectors.connectors.rss import RSSConnector
from data_connectors.real_payload import REQUIRED_REAL_FIELDS


def test_rss_real_fetch_contains_required_fields() -> None:
    connector = RSSConnector()
    request = ConnectorRequest({"feed_url": "https://hnrss.org/frontpage", "limit": 3})
    try:
        raw = connector.fetch_real(request)
    except Exception as exc:  # noqa: BLE001
        pytest.skip(f"RSS network unavailable: {exc}")
    assert raw.get("mode") == "real"
    for field in REQUIRED_REAL_FIELDS:
        assert raw.get(field) is not None
    assert isinstance(raw["payload"].get("items"), list)
