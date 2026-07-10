#!/usr/bin/env python3
"""Milestone wrapper validation for M10 Autonomous Investment Committee."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def check(condition: bool, ok: str, fail: str, failures: list[str]) -> None:
    if condition:
        print(f"PASS: {ok}")
    else:
        print(f"FAIL: {fail}")
        failures.append(fail)


def main() -> int:
    failures: list[str] = []
    print("AIRS M10 Wrapper Validation")
    print("===========================")
    required = [
        "scripts/validate_committee.py",
        "docs/production/M10_COMPLETION_REPORT.md",
        "docs/review/M10_SELF_REVIEW.md",
        "docs/adr/ADR-0010-autonomous-investment-committee.md",
    ]
    for rel in required:
        check((ROOT / rel).exists(), f"{rel} exists", f"missing {rel}", failures)
    report = (ROOT / "docs/production/M10_COMPLETION_REPORT.md").read_text(encoding="utf-8")
    check("Autonomous Investment Committee" in report, "M10 report documents AIC", "M10 report missing AIC", failures)
    check("不构成投资建议" in report, "M10 report has disclaimer", "M10 report missing disclaimer", failures)
    print("===========================")
    if failures:
        print("RESULT: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("RESULT: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())

