#!/usr/bin/env python3
"""Validate QA Sprint 2 Architecture Stabilization contracts."""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DISCLAIMER = "本验证仅用于 AIRS 架构稳定性检查，不构成投资建议。"


def check(condition: bool, ok: str, fail: str, failures: list[str]) -> None:
    if condition:
        print(f"PASS: {ok}")
    else:
        print(f"FAIL: {fail}")
        failures.append(fail)


def validate_orchestrator_boundary(failures: list[str]) -> None:
    sys.path.insert(0, str(ROOT))
    from orchestrator import run_planned_workflow
    from planner import plan_research

    plan = plan_research({"goal_id": "qa-sprint-2", "raw_goal": "QA architecture stabilization", "goal_type": "company_research", "subject": "NVIDIA"})
    result = run_planned_workflow(plan, case_id="qa-sprint-2")
    check(result["planner_ref"] == plan["plan_id"], "orchestrator preserves planner_ref", "orchestrator lost planner_ref", failures)
    check(result["runtime"]["final_state"]["runtime_state"].get("status") == "COMPLETED", "orchestrator executes runtime workflow", "runtime workflow did not complete", failures)
    app_code = (ROOT / "apps" / "equity_research" / "app.py").read_text(encoding="utf-8")
    check("RuntimeCore" not in app_code, "APP-001 avoids direct RuntimeCore import", "APP-001 directly imports RuntimeCore", failures)
    check("run_planned_workflow" in app_code, "APP-001 uses Orchestrator boundary", "APP-001 does not use Orchestrator boundary", failures)


def validate_app_core_contract(failures: list[str]) -> None:
    sys.path.insert(0, str(ROOT))
    from apps.equity_research import run_equity_research

    result = run_equity_research({"symbol": "NVDA", "market": "US", "research_question": "分析 NVIDIA 的财务、估值、供应链和风险"})
    validation = result["contract_validation"]
    lineage = result["data_lineage"]
    check(validation["passed"], f"APP-001 Core contract passes with warnings: {validation['warnings']}", f"APP-001 contract failed: {validation['errors']}", failures)
    check(result["status"] in {"completed", "completed_with_degradation"}, "APP-001 exposes explicit completion status", "APP-001 status missing or invalid", failures)
    check(lineage["mock_sources"] or lineage["real_sources"], "APP-001 exposes connector lineage", "APP-001 missing connector lineage", failures)
    cards = result["analysis"]["evidence_chain"]["evidence_cards"]
    mock_facts = [evidence_id for evidence_id, card in cards.items() if card.get("data_mode") in {"mock", "skip"} and card.get("statement_type") == "Fact"]
    check(not mock_facts, "mock/skip evidence is not marked as Fact", f"mock/skip evidence marked as Fact: {mock_facts}", failures)


def validate_api_security(failures: list[str]) -> None:
    sys.path.insert(0, str(ROOT))
    from api.server import validate_bind_security

    previous = os.environ.pop("AIRS_API_KEY", None)
    try:
        validate_bind_security("127.0.0.1")
        check(True, "localhost bind allowed without API key", "localhost bind rejected", failures)
        try:
            validate_bind_security("0.0.0.0")
        except RuntimeError:
            check(True, "public bind rejected without API key", "public bind was not rejected", failures)
        else:
            check(False, "public bind rejected without API key", "public bind was not rejected", failures)
        os.environ["AIRS_API_KEY"] = "qa-secret"
        validate_bind_security("0.0.0.0")
        check(True, "public bind allowed with API key", "public bind rejected with API key", failures)
    finally:
        if previous is not None:
            os.environ["AIRS_API_KEY"] = previous
        else:
            os.environ.pop("AIRS_API_KEY", None)


def validate_docs(failures: list[str]) -> None:
    required = [
        "docs/audit/ARCHITECTURE_AUDIT_REPORT.md",
        "docs/audit/REFACTOR_PRIORITY.md",
        "docs/audit/TECHNICAL_DEBT_REGISTER.md",
    ]
    for rel in required:
        path = ROOT / rel
        check(path.exists(), f"{rel} exists", f"missing {rel}", failures)
        if path.exists():
            text = path.read_text(encoding="utf-8")
            check("AUDIT-" in text or "P0-" in text or "TD-" in text, f"{rel} carries audit identifiers", f"{rel} missing audit identifiers", failures)


def main() -> int:
    failures: list[str] = []
    print("AIRS QA Sprint 2 Architecture Stabilization Validation")
    print("======================================================")
    validate_docs(failures)
    validate_orchestrator_boundary(failures)
    validate_app_core_contract(failures)
    validate_api_security(failures)
    print("======================================================")
    if failures:
        print("RESULT: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("RESULT: PASS")
    print(f"免责声明：{DISCLAIMER}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
