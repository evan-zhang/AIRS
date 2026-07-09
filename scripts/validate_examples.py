#!/usr/bin/env python3
"""Validate AIRS M7 Production Example deliverables."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOCS = [
    "docs/examples/example-specification.md",
    "docs/examples/regression-dataset.md",
]

EXAMPLES = [
    "examples/reports/supply-chain-report.md",
    "examples/reports/theme-expansion-report.md",
    "examples/evidence/evidence-report.md",
    "examples/reports/valuation-report.md",
    "examples/reports/risk-report.md",
    "examples/reports/complete-investment-research-report.md",
]

TEMPLATES = ["templates/example-template.md"]

FORBIDDEN = ["建议买入", "建议卖出", "保证收益", "保证盈利"]


def read_text(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def check(condition: bool, ok: str, fail: str, failures: list[str]) -> None:
    if condition:
        print(f"PASS: {ok}")
    else:
        print(f"FAIL: {fail}")
        failures.append(fail)


def validate_markdown(rel: str, failures: list[str], min_size: int = 500) -> None:
    path = ROOT / rel
    check(path.exists(), f"{rel} exists", f"missing {rel}", failures)
    if not path.exists():
        return
    text = read_text(rel)
    check(len(text) >= min_size, f"{rel} has substantive content", f"{rel} content too thin", failures)
    check("免责声明" in text and "不构成投资建议" in text, f"{rel} has disclaimer", f"{rel} missing disclaimer", failures)
    for forbidden in FORBIDDEN:
        check(forbidden not in text, f"{rel} avoids forbidden expression: {forbidden}", f"{rel} contains forbidden expression: {forbidden}", failures)


def validate_example_files(failures: list[str]) -> None:
    required_terms = ["Prompt ID", "M4 Prompt", "Evidence ID", "Evidence Level", "Confidence", "Weight", "Scorecard", "Quality Gate", "反方观点", "不确定性"]
    for rel in EXAMPLES:
        validate_markdown(rel, failures, min_size=900)
        if not (ROOT / rel).exists():
            continue
        text = read_text(rel)
        for term in required_terms:
            check(term in text, f"{rel} includes {term}", f"{rel} missing {term}", failures)


def main() -> int:
    failures: list[str] = []
    print("AIRS M7 Production Examples Validation")
    print("======================================")

    for rel in DOCS:
        validate_markdown(rel, failures)
    validate_example_files(failures)
    for rel in TEMPLATES:
        validate_markdown(rel, failures, min_size=350)

    print("======================================")
    if failures:
        print("RESULT: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("RESULT: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
