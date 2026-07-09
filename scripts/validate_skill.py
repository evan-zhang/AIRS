#!/usr/bin/env python3
"""Validate AIRS M5 Skill Engine deliverables."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

SKILL_ENGINE_DOCS = [
    "skill-architecture.md",
    "skill-lifecycle.md",
    "skill-registry.md",
    "skill-invocation.md",
    "skill-composition.md",
    "skill-versioning.md",
    "skill-governance.md",
]

PRODUCTION_SKILLS = [
    "skills/master/master-skill.md",
    "skills/hot-topic/research-skill.md",
    "skills/supply-chain/supply-chain-skill.md",
    "skills/evidence/evidence-skill.md",
    "skills/financial/financial-skill.md",
    "skills/news/news-skill.md",
    "skills/valuation/valuation-skill.md",
    "skills/risk/risk-skill.md",
    "skills/report/report-skill.md",
    "skills/verification/verification-skill.md",
]

REQUIRED_SKILL_SECTIONS = [
    "Purpose",
    "Inputs",
    "Outputs",
    "Dependencies",
    "Invoked Prompt",
    "Invoked Methodology",
    "Invoked Evidence",
    "Workflow",
    "Failure Handling",
    "Review Checklist",
]

REQUIRED_SCHEMAS = [
    "schemas/skills/skill.schema.json",
    "schemas/skills/skill-registry.schema.json",
]

REQUIRED_SUPPORTING_PATHS = [
    "templates/skill-template.md",
    "docs/production/M5_COMPLETION_REPORT.md",
    "docs/review/M5_SELF_REVIEW.md",
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
    "## 1. System Prompt",
    "## System Prompt",
]

REQUIRED_EVIDENCE_TERMS = [
    "Evidence Card",
    "Evidence Chain",
    "supports",
    "refutes",
    "missing_evidence",
    "traceability",
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


def markdown_refs(text: str, prefix: str) -> set[str]:
    return set(re.findall(rf"{re.escape(prefix)}[A-Za-z0-9_./-]+\.md", text))


def schema_refs(text: str, prefix: str) -> set[str]:
    return set(re.findall(rf"{re.escape(prefix)}[A-Za-z0-9_./-]+\.schema\.json", text))


def validate_skill_engine_docs(failures: list[str]) -> None:
    base = ROOT / "docs" / "skill-engine"
    check(base.is_dir(), "docs/skill-engine directory exists", "missing docs/skill-engine directory", failures)
    for filename in SKILL_ENGINE_DOCS:
        path = base / filename
        check(path.exists(), f"{filename} exists", f"missing skill engine doc: {filename}", failures)
        if not path.exists():
            continue
        text = read_text(path)
        check(len(text) >= 700, f"{filename} has substantive content", f"{filename} content too thin", failures)
        check("免责声明" in text and "不构成投资建议" in text, f"{filename} has disclaimer", f"{filename} missing disclaimer", failures)


def validate_schemas(failures: list[str]) -> None:
    for rel in REQUIRED_SCHEMAS:
        path = ROOT / rel
        check(path.exists(), f"{rel} exists", f"missing schema: {rel}", failures)
        if not path.exists():
            continue
        schema = load_json(path, failures)
        check(bool(schema.get("$schema")), f"{rel} declares $schema", f"{rel} missing $schema", failures)
        check(schema.get("type") == "object", f"{rel} top-level type is object", f"{rel} top-level type is not object", failures)

    schemas_readme = read_text(ROOT / "schemas" / "README.md")
    check(
        "schemas/skills/" in schemas_readme and "skill-registry.schema.json" in schemas_readme,
        "schemas/README.md documents skill schemas",
        "schemas/README.md missing skill schema description",
        failures,
    )


def validate_supporting_files(failures: list[str]) -> None:
    for rel in REQUIRED_SUPPORTING_PATHS:
        path = ROOT / rel
        check(path.exists(), f"{rel} exists", f"missing required file: {rel}", failures)
        if path.exists():
            check(path.stat().st_size > 500, f"{rel} has substantive content", f"{rel} content too thin", failures)

    template = ROOT / "templates" / "skill-template.md"
    if template.exists():
        text = read_text(template)
        for section in REQUIRED_SKILL_SECTIONS:
            body = section_body(text, section)
            check(len(body) >= 30, f"skill template section {section} has content", f"skill template missing or thin section: {section}", failures)


def validate_production_skills(failures: list[str]) -> None:
    for rel in PRODUCTION_SKILLS:
        path = ROOT / rel
        check(path.exists(), f"{rel} exists", f"missing production skill: {rel}", failures)
        if not path.exists():
            continue

        text = read_text(path)
        check("免责声明" in text or "不构成投资建议" in text, f"{rel} has compliance boundary", f"{rel} missing disclaimer boundary", failures)

        for section in REQUIRED_SKILL_SECTIONS:
            body = section_body(text, section)
            check(len(body) >= 35, f"{rel} section {section} has substantive content", f"{rel} section {section} missing or too thin", failures)

        prompt_refs = markdown_refs(text, "prompts/")
        methodology_refs = markdown_refs(text, "docs/methodology/")
        evidence_doc_refs = markdown_refs(text, "docs/evidence/")
        evidence_schema_refs = schema_refs(text, "schemas/evidence/")

        check(bool(prompt_refs), f"{rel} references M4 Prompt", f"{rel} missing M4 Prompt reference", failures)
        check(bool(methodology_refs), f"{rel} references M2 Methodology", f"{rel} missing M2 Methodology reference", failures)
        check(bool(evidence_doc_refs or evidence_schema_refs), f"{rel} references M3 Evidence Engine", f"{rel} missing M3 Evidence reference", failures)

        for ref in sorted(prompt_refs):
            check((ROOT / ref).exists(), f"{rel} prompt ref exists: {ref}", f"{rel} invalid prompt ref: {ref}", failures)
        for ref in sorted(methodology_refs):
            check((ROOT / ref).exists(), f"{rel} methodology ref exists: {ref}", f"{rel} invalid methodology ref: {ref}", failures)
        for ref in sorted(evidence_doc_refs | evidence_schema_refs):
            check((ROOT / ref).exists(), f"{rel} evidence ref exists: {ref}", f"{rel} invalid evidence ref: {ref}", failures)

        for term in REQUIRED_EVIDENCE_TERMS:
            check(term in text, f"{rel} uses M3 term: {term}", f"{rel} missing M3 term: {term}", failures)

        for forbidden in FORBIDDEN_PATTERNS:
            check(forbidden not in text, f"{rel} avoids forbidden pattern: {forbidden}", f"{rel} contains forbidden pattern: {forbidden}", failures)


def validate_cross_milestone_consistency(failures: list[str]) -> None:
    for rel in [
        "docs/production/M1_COMPLETION_REPORT.md",
        "docs/production/M2_COMPLETION_REPORT.md",
        "docs/production/M3_COMPLETION_REPORT.md",
        "docs/production/M4_COMPLETION_REPORT.md",
        "scripts/validate_m1.py",
        "scripts/validate_m2.py",
        "scripts/validate_evidence.py",
        "scripts/validate_prompt.py",
    ]:
        check((ROOT / rel).exists(), f"prior milestone artifact exists: {rel}", f"missing prior milestone artifact: {rel}", failures)

    combined = "\n".join(read_text(ROOT / rel) for rel in PRODUCTION_SKILLS if (ROOT / rel).exists())
    for term in ["Prompt Engine", "Methodology", "Evidence Engine", "反方", "不确定性", "不构成投资建议"]:
        check(term in combined, f"M5 skills include cross-milestone principle: {term}", f"M5 skills missing principle: {term}", failures)


def main() -> int:
    failures: list[str] = []

    print("AIRS M5 Skill Engine Validation")
    print("================================")
    validate_skill_engine_docs(failures)
    validate_schemas(failures)
    validate_supporting_files(failures)
    validate_production_skills(failures)
    validate_cross_milestone_consistency(failures)

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

