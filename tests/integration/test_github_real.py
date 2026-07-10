from __future__ import annotations

import pytest

from data_connectors.base import ConnectorRequest
from data_connectors.connectors.github import GitHubConnector
from data_connectors.real_payload import REQUIRED_REAL_FIELDS


def test_github_real_fetch_contains_required_fields() -> None:
    connector = GitHubConnector()
    request = ConnectorRequest({"repo": "openai/openai-python", "action": "repo"})
    try:
        raw = connector.fetch_real(request)
    except Exception as exc:  # noqa: BLE001
        pytest.skip(f"GitHub API unavailable or rate limited: {exc}")
    assert raw.get("mode") == "real"
    for field in REQUIRED_REAL_FIELDS:
        assert raw.get(field) is not None
    assert raw["payload"]["response"].get("full_name") == "openai/openai-python"
