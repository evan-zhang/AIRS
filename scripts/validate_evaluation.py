#!/usr/bin/env python3
"""Validate AIRS M6 Evaluation Engine deliverables."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

EVALUATION_ENGINE_DOCS = [
    "docs/evaluation-engine/evaluation-architecture.md",
    "docs/evaluation-engine/evaluation-workflow.md",
    "docs/evaluation-engine/quality-gate.md",
    "docs/evaluation-engine/regression-strategy.md",
]

EVALUATION_DOCS = [
    "evaluation/production-review-checklist.md",
    "evaluation/quality-gate.md",
    "evaluation/regression-checklist.md",
]

SUPPORTING = [
    "templates/evaluation-template.md",
    "schemas/score/evaluation.schema.json",
    "docs/production/M6_COMPLETION_REPORT.md",
    "docs/review/M6_SELF_REVIEW.md",
]

FORBIDDEN = ["建议买入", "建议卖出", "目标价为", "保证收益", "保证盈利"]


def read_text(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def check(condition: bool, ok: str, fail: str, failures: list[str]) -> None:
    if condition:
        print(f"PASS: {ok}")
    else:
        print(f"FAIL: {fail}")
        failures.append(fail)


def validate_markdown(rel: str, failures: list[str], min_size: int = 400) -> None:
    path = ROOT / rel
    check(path.exists(), f"{rel} exists", f"missing {rel}", failures)
    if not path.exists():
        return
    text = read_text(rel)
    check(len(text) >= min_size, f"{rel} has substantive content", f"{rel} content too thin", failures)
    check("免责声明" in text and "不构成投资建议" in text, f"{rel} has disclaimer", f"{rel} missing disclaimer", failures)
    for forbidden in FORBIDDEN:
        check(forbidden not in text, f"{rel} avoids forbidden expression: {forbidden}", f"{rel} contains forbidden expression: {forbidden}", failures)


def validate_gate_terms(failures: list[str]) -> None:
    combined = "\n".join(read_text(rel) for rel in EVALUATION_ENGINE_DOCS + EVALUATION_DOCS if (ROOT / rel).exists())
    for term in ["PASS", "CONDITIONAL_PASS", "FAIL", "Evidence", "Score", "Quality Gate", "Regression"]:
        check(term in combined, f"Evaluation docs include {term}", f"Evaluation docs missing {term}", failures)
    for rel in [
        "scripts/validate_m1.py",
        "scripts/validate_m2.py",
        "scripts/validate_evidence.py",
        "scripts/validate_prompt.py",
        "scripts/validate_skill.py",
        "scripts/validate_score.py",
    ]:
        check((ROOT / rel).exists(), f"regression dependency exists: {rel}", f"missing regression dependency: {rel}", failures)


def main() -> int:
    failures: list[str] = []
    print("AIRS M6 Evaluation Engine Validation")
    print("====================================")

    for rel in EVALUATION_ENGINE_DOCS:
        validate_markdown(rel, failures)
    for rel in EVALUATION_DOCS:
        validate_markdown(rel, failures, min_size=250)
    for rel in SUPPORTING:
        validate_markdown(rel, failures, min_size=250)
    validate_gate_terms(failures)

    print("====================================")
    if failures:
        print("RESULT: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("RESULT: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
