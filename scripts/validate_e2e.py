#!/usr/bin/env python3
"""Validate AIRS Production E2E artifacts and reports."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SUMMARY_PATH = ROOT / "docs" / "testing" / "artifacts" / "production-test-summary.json"
REPORT_PATH = ROOT / "docs" / "testing" / "PRODUCTION_TEST_REPORT.md"
KNOWN_ISSUES_PATH = ROOT / "docs" / "testing" / "KNOWN_ISSUES.md"
REQUIRED_PRODUCTION_FIELDS = [
    "execution_log",
    "evidence_trace",
    "airs_evidence_chain",
    "kg_state",
    "scorecard",
    "committee_debate",
    "final_report",
    "memory_write_read",
    "learning_feedback",
    "stable_release_gate",
]
REQUIRED_CHECKS = {
    "planner",
    "runtime",
    "connectors",
    "evidence_trace",
    "knowledge_graph",
    "scorecard",
    "committee",
    "report_taxonomy",
    "stable_release_gate",
    "memory",
    "learning",
}


def check(condition: bool, ok: str, fail: str, failures: list[str]) -> None:
    if condition:
        print(f"PASS: {ok}")
    else:
        print(f"FAIL: {fail}")
        failures.append(fail)


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_summary(failures: list[str]) -> dict[str, Any] | None:
    check(SUMMARY_PATH.exists(), "production summary exists", f"missing {SUMMARY_PATH.relative_to(ROOT)}", failures)
    check(REPORT_PATH.exists(), "production test report exists", f"missing {REPORT_PATH.relative_to(ROOT)}", failures)
    check(KNOWN_ISSUES_PATH.exists(), "known issues exists", f"missing {KNOWN_ISSUES_PATH.relative_to(ROOT)}", failures)
    if not SUMMARY_PATH.exists():
        return None
    summary = read_json(SUMMARY_PATH)
    check(summary.get("overall_status") == "PASS", "overall production E2E status is PASS", "overall production E2E status is not PASS", failures)
    check(summary.get("production_counts", {}).get("TOTAL") == 8, "8 production E2E cases recorded", "production E2E case count is not 8", failures)
    check(summary.get("failure_counts", {}).get("TOTAL") >= 3, "failure injection cases recorded", "failure injection cases missing", failures)
    return summary


def validate_production_artifact(item: dict[str, Any], failures: list[str]) -> None:
    case_id = item.get("case_id", "")
    artifact_path = ROOT / "docs" / "testing" / "artifacts" / "production-e2e" / f"{case_id}.json"
    check(artifact_path.exists(), f"{case_id} artifact exists", f"missing production artifact for {case_id}", failures)
    if not artifact_path.exists():
        return
    artifact = read_json(artifact_path)
    check(artifact.get("status") == "PASS", f"{case_id} status PASS", f"{case_id} status is not PASS", failures)
    for field in REQUIRED_PRODUCTION_FIELDS:
        check(field in artifact and artifact[field], f"{case_id} has {field}", f"{case_id} missing {field}", failures)
    check({check_item["name"] for check_item in artifact.get("checks", [])} >= REQUIRED_CHECKS, f"{case_id} has all required checks", f"{case_id} missing required checks", failures)
    check(artifact.get("kg_state", {}).get("validation", {}).get("passed") is True, f"{case_id} KG validation passed", f"{case_id} KG validation failed", failures)
    report = artifact.get("final_report", "")
    check("Facts/Inference/Assumption/Opinion" in report, f"{case_id} report separates statement taxonomy", f"{case_id} report missing statement taxonomy", failures)
    check("不构成投资建议" in report, f"{case_id} report has disclaimer", f"{case_id} report missing disclaimer", failures)


def validate_failure_artifact(item: dict[str, Any], failures: list[str]) -> None:
    case_id = item.get("case_id", "")
    artifact_path = ROOT / "docs" / "testing" / "artifacts" / "failure-injection" / f"{case_id}.json"
    check(artifact_path.exists(), f"{case_id} artifact exists", f"missing failure artifact for {case_id}", failures)
    if artifact_path.exists():
        artifact = read_json(artifact_path)
        check(artifact.get("status") == "PASS", f"{case_id} expected failure behavior PASS", f"{case_id} did not pass expected failure behavior", failures)


def validate_docs(failures: list[str]) -> None:
    for path in [REPORT_PATH, KNOWN_ISSUES_PATH, ROOT / "docs" / "testing" / "TEST_PLAN.md"]:
        check(path.exists(), f"{path.relative_to(ROOT)} exists", f"missing {path.relative_to(ROOT)}", failures)
        if path.exists():
            text = path.read_text(encoding="utf-8")
            check("不构成投资建议" in text, f"{path.relative_to(ROOT)} has disclaimer", f"{path.relative_to(ROOT)} missing disclaimer", failures)


def main() -> int:
    failures: list[str] = []
    print("AIRS Production E2E Artifact Validation")
    print("=======================================")
    summary = validate_summary(failures)
    if summary:
        for item in summary.get("production_results", []):
            validate_production_artifact(item, failures)
        for item in summary.get("failure_results", []):
            validate_failure_artifact(item, failures)
    validate_docs(failures)
    print("=======================================")
    if failures:
        print("RESULT: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("RESULT: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
