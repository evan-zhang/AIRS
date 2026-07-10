#!/usr/bin/env python3
"""Run AIRS Production E2E and failure-injection validation suites."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
import traceback
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PRODUCTION_TEST_DIR = ROOT / "tests" / "production-e2e"
FAILURE_TEST_DIR = ROOT / "tests" / "failure-injection"
DOCS_DIR = ROOT / "docs" / "testing"
ARTIFACT_DIR = DOCS_DIR / "artifacts"
REPORT_PATH = DOCS_DIR / "PRODUCTION_TEST_REPORT.md"
KNOWN_ISSUES_PATH = DOCS_DIR / "KNOWN_ISSUES.md"
SUMMARY_PATH = ARTIFACT_DIR / "production-test-summary.json"


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def discover(test_dir: Path) -> list[Path]:
    return sorted(path for path in test_dir.glob("test_*.py") if path.name not in {"e2e_harness.py", "failure_harness.py"})


def load_module(path: Path) -> Any:
    sys.path.insert(0, str(path.parent))
    sys.path.insert(0, str(ROOT))
    module_name = f"airs_{path.parent.name.replace('-', '_')}_{path.stem}"
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"cannot load test module: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_test_file(path: Path) -> dict[str, Any]:
    started_at = now_iso()
    try:
        module = load_module(path)
        if not hasattr(module, "run_case"):
            raise AttributeError(f"{path} does not expose run_case()")
        result = module.run_case()
        result.setdefault("status", "PASS")
        result["test_file"] = str(path.relative_to(ROOT))
        result.setdefault("started_at", started_at)
        result.setdefault("completed_at", now_iso())
        return result
    except Exception as exc:  # noqa: BLE001
        return {
            "case_id": path.stem,
            "title": path.stem,
            "status": "FAIL",
            "test_file": str(path.relative_to(ROOT)),
            "started_at": started_at,
            "completed_at": now_iso(),
            "errors": [str(exc)],
            "traceback": traceback.format_exc(),
        }


def status_counts(results: list[dict[str, Any]]) -> dict[str, int]:
    return {
        "PASS": sum(1 for item in results if item.get("status") == "PASS"),
        "FAIL": sum(1 for item in results if item.get("status") == "FAIL"),
        "TOTAL": len(results),
    }


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")


def write_report(summary: dict[str, Any]) -> None:
    lines = [
        "# AIRS Production E2E Test Report",
        "",
        "免责声明：本报告仅用于 AIRS 工程验证和研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。",
        "",
        f"- Version under test: v1.0.0-rc1",
        f"- Branch: test/production-e2e-validation",
        f"- Generated at: {summary['completed_at']}",
        f"- Overall status: {summary['overall_status']}",
        f"- Production E2E: {summary['production_counts']['PASS']} PASS / {summary['production_counts']['FAIL']} FAIL / {summary['production_counts']['TOTAL']} total",
        f"- Failure Injection: {summary['failure_counts']['PASS']} PASS / {summary['failure_counts']['FAIL']} FAIL / {summary['failure_counts']['TOTAL']} total",
        "",
        "## Production E2E Cases",
        "",
    ]
    for item in summary["production_results"]:
        lines.extend(
            [
                f"### {item.get('case_id', item.get('test_file'))}",
                f"- Status: {item.get('status')}",
                f"- Test file: `{item.get('test_file')}`",
                f"- Artifact: `docs/testing/artifacts/production-e2e/{item.get('case_id')}.json`",
                f"- Checks: {', '.join(check['name'] + '=' + check['status'] for check in item.get('checks', []))}",
                f"- Failure reason: {'; '.join(item.get('errors', [])) if item.get('errors') else 'None'}",
                "",
            ]
        )
    lines.extend(["## Failure Injection Cases", ""])
    for item in summary["failure_results"]:
        artifact = f"docs/testing/artifacts/failure-injection/{item.get('case_id')}.json"
        lines.extend(
            [
                f"### {item.get('case_id', item.get('test_file'))}",
                f"- Status: {item.get('status')}",
                f"- Test file: `{item.get('test_file')}`",
                f"- Artifact: `{artifact}`",
                f"- Expected behavior: {item.get('expected', 'See artifact')}",
                f"- Failure reason: {'; '.join(item.get('errors', [])) if item.get('errors') else 'None'}",
                "",
            ]
        )
    lines.extend(
        [
            "## Evidence Trace Coverage",
            "",
            "- Execution Log: stored in each production artifact under `execution_log`.",
            "- Evidence Trace: stored under `evidence_trace` and `airs_evidence_chain`.",
            "- KG State: stored under `kg_state` with validator result.",
            "- Scorecard: stored under `scorecard`.",
            "- Committee Debate: stored under `committee_debate`.",
            "- Final Report: stored under `final_report`.",
            "- Memory Write/Read: stored under `memory_write_read`.",
            "- Learning Feedback: stored under `learning_feedback`.",
            "",
            "## Known Issues",
            "",
            f"See `{KNOWN_ISSUES_PATH.relative_to(ROOT)}`.",
            "",
        ]
    )
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")


def write_known_issues(summary: dict[str, Any]) -> None:
    failures = [item for item in summary["production_results"] + summary["failure_results"] if item.get("status") != "PASS"]
    lines = [
        "# AIRS Production E2E Known Issues",
        "",
        "免责声明：本文件仅记录 AIRS 工程验证问题，不构成投资建议。",
        "",
        f"- Generated at: {summary['completed_at']}",
        f"- Open issue count: {len(failures)}",
        "",
    ]
    if not failures:
        lines.extend(["## Open Issues", "", "No open production E2E issues were observed in this run.", ""])
    else:
        lines.extend(["## Open Issues", ""])
        for item in failures:
            lines.extend(
                [
                    f"### {item.get('case_id', item.get('test_file'))}",
                    f"- Status: {item.get('status')}",
                    f"- Test file: `{item.get('test_file')}`",
                    f"- Failure reason: {'; '.join(item.get('errors', [])) if item.get('errors') else 'Unknown'}",
                    "- Owner: Code Agent",
                    "- Next action: inspect artifact and repair failing module or test harness.",
                    "",
                ]
            )
    KNOWN_ISSUES_PATH.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--production-only", action="store_true", help="Run only production E2E cases.")
    parser.add_argument("--failure-only", action="store_true", help="Run only failure-injection cases.")
    args = parser.parse_args()

    started_at = now_iso()
    production_results: list[dict[str, Any]] = []
    failure_results: list[dict[str, Any]] = []
    if not args.failure_only:
        for path in discover(PRODUCTION_TEST_DIR):
            print(f"RUN production: {path.relative_to(ROOT)}")
            result = run_test_file(path)
            production_results.append(result)
            print(f"{result.get('status')}: {result.get('case_id')}")
    if not args.production_only:
        for path in discover(FAILURE_TEST_DIR):
            print(f"RUN failure: {path.relative_to(ROOT)}")
            result = run_test_file(path)
            failure_results.append(result)
            print(f"{result.get('status')}: {result.get('case_id')}")

    summary = {
        "started_at": started_at,
        "completed_at": now_iso(),
        "overall_status": "PASS" if all(item.get("status") == "PASS" for item in production_results + failure_results) else "FAIL",
        "production_counts": status_counts(production_results),
        "failure_counts": status_counts(failure_results),
        "production_results": production_results,
        "failure_results": failure_results,
        "report_path": str(REPORT_PATH.relative_to(ROOT)),
        "known_issues_path": str(KNOWN_ISSUES_PATH.relative_to(ROOT)),
        "disclaimer": "仅用于 AIRS 工程验证和研究质量控制，不构成投资建议。",
    }
    write_json(SUMMARY_PATH, summary)
    write_report(summary)
    write_known_issues(summary)
    print(f"SUMMARY: {SUMMARY_PATH.relative_to(ROOT)}")
    print(f"REPORT: {REPORT_PATH.relative_to(ROOT)}")
    print(f"KNOWN_ISSUES: {KNOWN_ISSUES_PATH.relative_to(ROOT)}")
    print(f"RESULT: {summary['overall_status']}")
    return 0 if summary["overall_status"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
