#!/usr/bin/env python3
"""Validate AIRS M2 Methodology Core deliverables."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

METHODOLOGY_DOCS = [
    "supply-chain-chokepoint.md",
    "theme-expansion.md",
    "evidence-chain.md",
    "counter-consensus.md",
    "industry-lifecycle.md",
    "financial-anomaly.md",
    "management-quality.md",
    "policy-driven.md",
    "valuation.md",
    "risk.md",
]

REQUIRED_SECTIONS = [
    "Purpose",
    "Theory",
    "Background",
    "Applicable Scenarios",
    "Non-applicable Scenarios",
    "Inputs",
    "Outputs",
    "Workflow",
    "Required Evidence",
    "Counter Evidence",
    "Failure Cases",
    "Confidence",
    "Benchmark Mapping",
    "Future Prompt Mapping",
    "Future Skill Mapping",
    "Future Score Mapping",
]

REQUIRED_PATHS = [
    "docs/adr/README.md",
    "docs/rfc/README.md",
    "docs/methodology/DSL.md",
    "schemas/methodology/methodology.schema.json",
    "templates/methodology-template.md",
    "evaluation/rubrics/methodology-review-checklist.md",
    "docs/production/M2_COMPLETION_REPORT.md",
    "docs/review/M2_SELF_REVIEW.md",
]

M1_REFERENCE_PATHS = [
    "README.md",
    "ARCHITECTURE.md",
    "AGENTS.md",
    "SKILL.md",
    "ROADMAP.md",
    "docs/production/M1_COMPLETION_REPORT.md",
]

M1_CONSISTENCY_TERMS = [
    "证据",
    "反方",
    "不确定性",
    "免责声明",
    "不构成投资建议",
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def section_body(text: str, section: str) -> str:
    pattern = re.compile(
        rf"^##\s+\d+\.\s+{re.escape(section)}[^\n]*\n(?P<body>.*?)(?=^##\s+\d+\.|\Z)",
        re.MULTILINE | re.DOTALL,
    )
    match = pattern.search(text)
    return match.group("body").strip() if match else ""


def check(condition: bool, ok: str, fail: str, failures: list[str]) -> None:
    if condition:
        print(f"PASS: {ok}")
    else:
        print(f"FAIL: {fail}")
        failures.append(fail)


def validate_methodology_docs(failures: list[str]) -> None:
    base = ROOT / "docs" / "methodology"
    for filename in METHODOLOGY_DOCS:
        path = base / filename
        check(path.exists(), f"{filename} exists", f"missing methodology doc: {filename}", failures)
        if not path.exists():
            continue

        text = read_text(path)
        check(
            "免责声明" in text and "不构成投资建议" in text,
            f"{filename} has disclaimer",
            f"{filename} missing required disclaimer",
            failures,
        )

        for section in REQUIRED_SECTIONS:
            body = section_body(text, section)
            check(
                len(body) >= 20,
                f"{filename} section {section} has substantive content",
                f"{filename} section {section} missing or too thin",
                failures,
            )


def validate_supporting_files(failures: list[str]) -> None:
    for rel in REQUIRED_PATHS:
        path = ROOT / rel
        check(path.exists(), f"{rel} exists", f"missing required file: {rel}", failures)
        if path.exists() and path.suffix in {".md", ".json"}:
            check(path.stat().st_size > 200, f"{rel} has content", f"{rel} content too thin", failures)

    for dirname in ["docs/adr", "docs/rfc", "schemas/methodology", "docs/review"]:
        path = ROOT / dirname
        check(path.is_dir(), f"{dirname} directory exists", f"missing directory: {dirname}", failures)


def validate_schema(failures: list[str]) -> None:
    path = ROOT / "schemas" / "methodology" / "methodology.schema.json"
    if not path.exists():
        return

    try:
        schema = json.loads(read_text(path))
        print("PASS: methodology.schema.json is valid JSON")
    except json.JSONDecodeError as exc:
        failures.append(f"methodology.schema.json invalid JSON: {exc}")
        print(f"FAIL: methodology.schema.json invalid JSON: {exc}")
        return

    serialized = json.dumps(schema, ensure_ascii=False)
    for field in [
        "purpose",
        "theory",
        "background",
        "applicable_scenarios",
        "non_applicable_scenarios",
        "inputs",
        "outputs",
        "workflow",
        "required_evidence",
        "counter_evidence",
        "failure_cases",
        "confidence",
        "benchmark_mapping",
        "future_prompt_mapping",
        "future_skill_mapping",
        "future_score_mapping",
    ]:
        check(field in serialized, f"schema contains {field}", f"schema missing field: {field}", failures)


def validate_m1_consistency(failures: list[str]) -> None:
    for rel in M1_REFERENCE_PATHS:
        check((ROOT / rel).exists(), f"M1 reference exists: {rel}", f"missing M1 reference: {rel}", failures)

    combined_m2 = "\n".join(
        read_text(path)
        for path in (ROOT / "docs" / "methodology").glob("*.md")
        if path.name != "README.md"
    )
    combined_m2 += "\n" + read_text(ROOT / "evaluation" / "rubrics" / "methodology-review-checklist.md")

    for term in M1_CONSISTENCY_TERMS:
        check(term in combined_m2, f"M2 content includes M1 principle: {term}", f"M2 missing M1 principle: {term}", failures)

    forbidden_patterns = ["建议买入", "建议卖出", "应买入", "应卖出", "给予目标价", "目标价为", "预计涨到", "保证盈利"]
    for pattern in forbidden_patterns:
        check(
            pattern not in combined_m2,
            f"M2 avoids forbidden expression: {pattern}",
            f"M2 contains forbidden expression: {pattern}",
            failures,
        )

    schemas_readme = read_text(ROOT / "schemas" / "README.md")
    check(
        "methodology/" in schemas_readme and "methodology.schema.json" in schemas_readme,
        "schemas/README.md documents methodology schema",
        "schemas/README.md missing methodology schema description",
        failures,
    )


def main() -> int:
    failures: list[str] = []

    print("AIRS M2 Validation")
    print("===================")
    validate_methodology_docs(failures)
    validate_supporting_files(failures)
    validate_schema(failures)
    validate_m1_consistency(failures)

    print("===================")
    if failures:
        print("RESULT: FAIL")
        for item in failures:
            print(f"- {item}")
        return 1

    print("RESULT: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
