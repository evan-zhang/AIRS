#!/usr/bin/env python3
"""Validate Stable release remediation gates.

This validator checks that degraded data cannot be counted as Stable real-data
PASS. It records unavailable external-source verification as UNVERIFIED instead
of pretending the real-data gate passed.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path
from types import SimpleNamespace


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

DISCLAIMER = "本验证仅用于 AIRS Stable 发布阻塞项修复检查，不构成投资建议。"


def check(condition: bool, ok: str, fail: str, failures: list[str]) -> None:
    if condition:
        print(f"PASS: {ok}")
    else:
        print(f"FAIL: {fail}")
        failures.append(fail)


def validate_real_gate_blocks_degraded_app(failures: list[str]) -> None:
    from apps.equity_research import run_equity_research

    result = run_equity_research(
        {
            "symbol": "NVDA",
            "market": "US",
            "research_question": "使用真实数据 real_data 验证 NVIDIA 研究链路",
            "require_real_data": True,
        }
    )
    gate = result["stable_release_gate"]
    lineage = result["data_lineage"]
    check(gate["status"] == "FAIL" or gate["passed"] is False, "Stable gate blocks degraded real-data APP result", f"Stable gate unexpectedly passed: {gate}", failures)
    check(result["quality_gate"] == "FAIL", "APP quality gate fails when required real data is degraded", f"APP quality gate did not fail: {result['quality_gate']}", failures)
    check(lineage["degraded_source_count"] >= 1, "APP lineage records degraded sources", f"APP lineage missing degraded sources: {lineage}", failures)


def validate_mock_demo_remains_degraded(failures: list[str]) -> None:
    from apps.equity_research import run_equity_research

    result = run_equity_research({"symbol": "NVDA", "market": "US", "research_question": "分析 NVIDIA 的财务、估值、供应链和风险"})
    check(result["status"] == "completed_with_degradation", "Mock demo is marked completed_with_degradation", f"Mock demo status was {result['status']}", failures)
    check(result["stable_release_gate"]["passed"] is True, "Stable gate is not required for demo-mode request", f"Demo gate should not block: {result['stable_release_gate']}", failures)


def validate_api_security_contract(failures: list[str]) -> None:
    from api.server import AIRSRequestHandler, RATE_BUCKETS, validate_bind_security

    previous_key = os.environ.pop("AIRS_API_KEY", None)
    try:
        validate_bind_security("127.0.0.1")
        try:
            validate_bind_security("0.0.0.0")
        except RuntimeError:
            check(True, "Public API bind is rejected without API key", "Public bind was not rejected", failures)
        else:
            check(False, "Public API bind is rejected without API key", "Public bind was not rejected", failures)
    finally:
        if previous_key is not None:
            os.environ["AIRS_API_KEY"] = previous_key

    handler = object.__new__(AIRSRequestHandler)
    handler.server = SimpleNamespace(security_config={"rate_limit_per_minute": 1})  # type: ignore[attr-defined]
    handler.client_address = ("127.0.0.1", 12345)
    handler.headers = {"X-AIRS-API-Key": "test-key"}
    RATE_BUCKETS.clear()
    first = handler._rate_limited()  # type: ignore[attr-defined]
    second = handler._rate_limited()  # type: ignore[attr-defined]
    check(first is False and second is True, "API rate limiter blocks second request over limit", "API rate limiter did not block as expected", failures)


def validate_connector_fallback_modes(failures: list[str]) -> None:
    from common.contract_validation import summarize_data_lineage
    from common.release_gate import evaluate_connector_lineage

    lineage = summarize_data_lineage(
        [
            {"connector_id": "rss", "data": {"mode": "real"}},
            {"connector_id": "news", "data": {"mode": "fallback_mock"}},
            {"connector_id": "yahoo_finance", "data": {"mode": "mock"}},
        ]
    )
    gate = evaluate_connector_lineage(lineage, require_real_sources=True, min_real_sources=1, allow_degraded=False)
    check("news" in lineage["fallback_sources"], "Fallback source is recorded separately", f"Fallback lineage missing: {lineage}", failures)
    check("yahoo_finance" in lineage["mock_sources"], "Mock source is recorded separately", f"Mock lineage missing: {lineage}", failures)
    check(not gate.passed, "Stable gate rejects degraded lineage even with one real source", f"Stable gate unexpectedly passed: {gate.to_dict()}", failures)


def validate_real_connector_probe() -> list[str]:
    """Best-effort probe. UNVERIFIED is reported, not converted into PASS."""

    unverified: list[str] = []
    if os.environ.get("AIRS_RUN_REAL_CONNECTOR_PROBE") != "1":
        return ["AIRS_RUN_REAL_CONNECTOR_PROBE is not set; real external connector probe not executed"]
    try:
        from data_connectors.base import ConnectorRequest
        from data_connectors.connectors.rss import RSSConnector

        raw = RSSConnector().fetch_real(ConnectorRequest({"feed_url": "https://hnrss.org/frontpage", "limit": 1}))
        if raw.get("mode") != "real":
            unverified.append(f"RSS real probe returned non-real mode: {raw.get('mode')}")
    except Exception as exc:  # noqa: BLE001
        unverified.append(f"RSS real probe unavailable: {exc}")
    return unverified


def main() -> int:
    failures: list[str] = []
    print("AIRS Stable Release Remediation Validation")
    print("==========================================")
    validate_connector_fallback_modes(failures)
    validate_api_security_contract(failures)
    validate_mock_demo_remains_degraded(failures)
    validate_real_gate_blocks_degraded_app(failures)
    unverified = validate_real_connector_probe()
    for item in unverified:
        print(f"UNVERIFIED: {item}")
    print("==========================================")
    if failures:
        print("RESULT: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("RESULT: PASS")
    if unverified:
        print(f"UNVERIFIED COUNT: {len(unverified)}")
    print(f"免责声明：{DISCLAIMER}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
