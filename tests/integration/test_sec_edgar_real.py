from __future__ import annotations

import pytest

from data_connectors.base import ConnectorRequest
from data_connectors.connectors.sec_edgar import SECEdgarConnector
from data_connectors.real_payload import REQUIRED_REAL_FIELDS


def test_sec_edgar_real_fetch_contains_required_fields() -> None:
    connector = SECEdgarConnector()
    request = ConnectorRequest({"ticker": "AAPL", "form_type": "10-K", "count": 2})
    try:
        raw = connector.fetch_real(request)
    except Exception as exc:  # noqa: BLE001
        pytest.skip(f"SEC EDGAR network unavailable: {exc}")
    assert raw.get("mode") == "real"
    for field in REQUIRED_REAL_FIELDS:
        assert raw.get(field) is not None
    assert isinstance(raw["payload"].get("filings"), list)
