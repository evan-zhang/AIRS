#!/usr/bin/env python3
"""Validate AIRS M6 Score Engine deliverables."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

SCORE_ENGINE_DOCS = [
    "docs/score-engine/score-architecture.md",
    "docs/score-engine/score-dsl.md",
    "docs/score-engine/score-lifecycle.md",
    "docs/score-engine/weight-system.md",
]

SCORING_DOCS = [
    "scoring/theme-score.md",
    "scoring/evidence-score.md",
    "scoring/methodology-score.md",
    "scoring/prompt-score.md",
    "scoring/skill-score.md",
    "scoring/report-score.md",
    "scoring/risk-score.md",
    "scoring/confidence-score.md",
    "scoring/overall-score.md",
]

SCHEMAS = [
    "schemas/score/score.schema.json",
    "schemas/score/scorecard.schema.json",
    "schemas/score/evaluation.schema.json",
]

SUPPORTING = [
    "templates/scorecard-template.md",
    "templates/evaluation-template.md",
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


def validate_schema(rel: str, failures: list[str]) -> None:
    path = ROOT / rel
    check(path.exists(), f"{rel} exists", f"missing {rel}", failures)
    if not path.exists():
        return
    try:
        schema = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        check(False, "", f"{rel} invalid JSON: {exc}", failures)
        return
    check(bool(schema.get("$schema")), f"{rel} declares $schema", f"{rel} missing $schema", failures)
    check(schema.get("type") == "object", f"{rel} top-level type is object", f"{rel} top-level type is not object", failures)
    check("不构成投资建议" in json.dumps(schema, ensure_ascii=False), f"{rel} has compliance boundary", f"{rel} missing compliance boundary", failures)


def validate_scoring_docs(failures: list[str]) -> None:
    required_terms = ["评分目的", "评分维度", "计算公式", "输入输出", "Evidence", "Methodology", "权重建议"]
    for rel in SCORING_DOCS:
        validate_markdown(rel, failures)
        if not (ROOT / rel).exists():
            continue
        text = read_text(rel)
        for term in required_terms:
            check(term in text, f"{rel} includes {term}", f"{rel} missing {term}", failures)


def validate_consistency(failures: list[str]) -> None:
    evidence_score = read_text("scoring/evidence-score.md")
    for term in ["Evidence Level", "Confidence", "Weight", "supports", "refutes", "missing_evidence"]:
        check(term in evidence_score, f"Evidence Score maps M3 term: {term}", f"Evidence Score missing M3 term: {term}", failures)

    methodology_score = read_text("scoring/methodology-score.md")
    check("Future Score Mapping" in methodology_score, "Methodology Score maps M2 Future Score Mapping", "Methodology Score missing M2 mapping", failures)

    prompt_score = read_text("scoring/prompt-score.md")
    check("M4 Prompt" in prompt_score or "M4" in prompt_score, "Prompt Score maps M4", "Prompt Score missing M4 mapping", failures)

    skill_score = read_text("scoring/skill-score.md")
    check("M5 Skill" in skill_score or "M5" in skill_score, "Skill Score maps M5", "Skill Score missing M5 mapping", failures)

    schemas_readme = read_text("schemas/README.md")
    check("score/score.schema.json" in schemas_readme, "schemas/README documents score schema", "schemas/README missing score schema", failures)


def main() -> int:
    failures: list[str] = []
    print("AIRS M6 Score Engine Validation")
    print("================================")

    for rel in SCORE_ENGINE_DOCS:
        validate_markdown(rel, failures)
    validate_scoring_docs(failures)
    for rel in SCHEMAS:
        validate_schema(rel, failures)
    for rel in SUPPORTING:
        validate_markdown(rel, failures, min_size=300)
    validate_consistency(failures)

    print("================================")
    if failures:
        print("RESULT: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("RESULT: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
