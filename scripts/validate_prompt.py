#!/usr/bin/env python3
"""Validate AIRS M4 Prompt DSL & Prompt Library deliverables."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

PROMPT_ENGINE_DOCS = [
    "prompt-architecture.md",
    "prompt-dsl.md",
    "prompt-lifecycle.md",
    "prompt-versioning.md",
    "prompt-governance.md",
    "prompt-review-workflow.md",
]

PRODUCTION_PROMPTS = {
    "prompts/supply-chain/chokepoint-analysis.md": "docs/methodology/supply-chain-chokepoint.md",
    "prompts/hot-topic/theme-expansion.md": "docs/methodology/theme-expansion.md",
    "prompts/evidence/evidence-chain.md": "docs/methodology/evidence-chain.md",
    "prompts/evidence/counter-consensus.md": "docs/methodology/counter-consensus.md",
    "prompts/industry/lifecycle-analysis.md": "docs/methodology/industry-lifecycle.md",
    "prompts/financial/anomaly-analysis.md": "docs/methodology/financial-anomaly.md",
    "prompts/committee/management-quality.md": "docs/methodology/management-quality.md",
    "prompts/committee/policy-driven.md": "docs/methodology/policy-driven.md",
    "prompts/valuation/analysis.md": "docs/methodology/valuation.md",
    "prompts/risk/analysis.md": "docs/methodology/risk.md",
    "prompts/report/generation.md": "docs/methodology/evidence-chain.md",
}

REQUIRED_PROMPT_SECTIONS = [
    "System Prompt",
    "User Template",
    "Input Schema",
    "Output Schema",
    "Evidence Requirements",
    "Failure Cases",
    "Review Checklist",
]

REQUIRED_PATHS = [
    "prompts/_dsl/prompt-dsl.md",
    "prompts/_dsl/prompt.schema.json",
    "templates/prompt-template.md",
    "schemas/prompt/prompt.schema.json",
    "schemas/prompt/prompt-output.schema.json",
    "evaluation/rubrics/prompt-review-checklist.md",
    "docs/production/M4_COMPLETION_REPORT.md",
    "docs/review/M4_SELF_REVIEW.md",
]

FORBIDDEN_PATTERNS = [
    "建议买入",
    "建议卖出",
    "应买入",
    "应卖出",
    "给予目标价",
    "目标价为",
    "预计涨到",
    "保证盈利",
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def check(condition: bool, ok: str, fail: str, failures: list[str]) -> None:
    if condition:
        print(f"PASS: {ok}")
    else:
        print(f"FAIL: {fail}")
        failures.append(fail)


def section_body(text: str, section: str) -> str:
    pattern = re.compile(
        rf"^##\s+\d+\.\s+{re.escape(section)}[^\n]*\n(?P<body>.*?)(?=^##\s+\d+\.|\Z)",
        re.MULTILINE | re.DOTALL,
    )
    match = pattern.search(text)
    return match.group("body").strip() if match else ""


def load_json(path: Path, failures: list[str]) -> dict:
    try:
        data = json.loads(read_text(path))
    except json.JSONDecodeError as exc:
        print(f"FAIL: {path.relative_to(ROOT)} invalid JSON: {exc}")
        failures.append(f"{path.relative_to(ROOT)} invalid JSON: {exc}")
        return {}
    print(f"PASS: {path.relative_to(ROOT)} is valid JSON")
    return data


def validate_prompt_engine_docs(failures: list[str]) -> None:
    base = ROOT / "docs" / "prompt-engine"
    check(base.is_dir(), "docs/prompt-engine directory exists", "missing docs/prompt-engine directory", failures)
    for filename in PROMPT_ENGINE_DOCS:
        path = base / filename
        check(path.exists(), f"{filename} exists", f"missing prompt engine doc: {filename}", failures)
        if not path.exists():
            continue
        text = read_text(path)
        check(len(text) >= 900, f"{filename} has substantive content", f"{filename} content too thin", failures)
        check("免责声明" in text and "不构成投资建议" in text, f"{filename} has disclaimer", f"{filename} missing disclaimer", failures)


def validate_supporting_paths(failures: list[str]) -> None:
    for rel in REQUIRED_PATHS:
        path = ROOT / rel
        check(path.exists(), f"{rel} exists", f"missing required file: {rel}", failures)
        if path.exists():
            check(path.stat().st_size > 300, f"{rel} has substantive content", f"{rel} content too thin", failures)


def validate_json_schemas(failures: list[str]) -> None:
    schema_paths = [
        ROOT / "prompts" / "_dsl" / "prompt.schema.json",
        ROOT / "schemas" / "prompt" / "prompt.schema.json",
        ROOT / "schemas" / "prompt" / "prompt-output.schema.json",
    ]
    for path in schema_paths:
        if not path.exists():
            continue
        schema = load_json(path, failures)
        check(bool(schema.get("$schema")), f"{path.name} declares $schema", f"{path.name} missing $schema", failures)
        check(schema.get("type") == "object", f"{path.name} top-level type is object", f"{path.name} top-level type is not object", failures)


def validate_production_prompts(failures: list[str]) -> None:
    for rel, methodology_ref in PRODUCTION_PROMPTS.items():
        path = ROOT / rel
        check(path.exists(), f"{rel} exists", f"missing production prompt: {rel}", failures)
        if not path.exists():
            continue

        text = read_text(path)
        check(methodology_ref in text, f"{rel} references {methodology_ref}", f"{rel} missing methodology ref {methodology_ref}", failures)
        check("Evidence Card" in text and "missing_evidence" in text, f"{rel} uses M3 Evidence Card terms", f"{rel} missing M3 Evidence Card terms", failures)
        check("免责声明" in text and "不构成投资建议" in text, f"{rel} has compliance disclaimer", f"{rel} missing compliance disclaimer", failures)

        for section in REQUIRED_PROMPT_SECTIONS:
            body = section_body(text, section)
            minimum = 80 if section == "System Prompt" else 30
            check(
                len(body) >= minimum,
                f"{rel} section {section} has substantive content",
                f"{rel} section {section} missing or too thin",
                failures,
            )

        for forbidden in FORBIDDEN_PATTERNS:
            check(forbidden not in text, f"{rel} avoids forbidden expression: {forbidden}", f"{rel} contains forbidden expression: {forbidden}", failures)


def validate_m2_m3_consistency(failures: list[str]) -> None:
    for _, methodology_ref in PRODUCTION_PROMPTS.items():
        path = ROOT / methodology_ref
        check(path.exists(), f"M2 methodology exists: {methodology_ref}", f"missing M2 methodology: {methodology_ref}", failures)

    for rel in [
        "docs/evidence/evidence-card-specification.md",
        "docs/evidence/evidence-validation-workflow.md",
        "docs/evidence/evidence-architecture.md",
        "schemas/evidence/evidence-card.schema.json",
    ]:
        check((ROOT / rel).exists(), f"M3 evidence reference exists: {rel}", f"missing M3 evidence reference: {rel}", failures)

    combined = "\n".join(read_text(ROOT / rel) for rel in PRODUCTION_PROMPTS if (ROOT / rel).exists())
    for term in ["docs/methodology/", "docs/evidence/", "supports", "refutes", "missing_evidence", "traceability"]:
        check(term in combined, f"M4 prompts include compatibility term: {term}", f"M4 prompts missing compatibility term: {term}", failures)

    schemas_readme = read_text(ROOT / "schemas" / "README.md")
    check(
        "schemas/prompt/" in schemas_readme and "prompt-output.schema.json" in schemas_readme,
        "schemas/README.md documents prompt schemas",
        "schemas/README.md missing prompt schema description",
        failures,
    )


def main() -> int:
    failures: list[str] = []

    print("AIRS M4 Prompt Engine Validation")
    print("=================================")
    validate_prompt_engine_docs(failures)
    validate_supporting_paths(failures)
    validate_json_schemas(failures)
    validate_production_prompts(failures)
    validate_m2_m3_consistency(failures)

    print("=================================")
    if failures:
        print("RESULT: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("RESULT: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())

