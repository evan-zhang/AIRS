#!/usr/bin/env python3
"""Validate AIRS M3 Evidence Engine deliverables."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

EVIDENCE_DOCS = [
    "evidence-architecture.md",
    "evidence-card-specification.md",
    "evidence-dsl.md",
    "evidence-level-standard.md",
    "evidence-review-standard.md",
    "evidence-validation-workflow.md",
    "evidence-lifecycle.md",
    "evidence-governance.md",
]

EVIDENCE_SCHEMAS = [
    "evidence.schema.json",
    "evidence-card.schema.json",
    "evidence-chain.schema.json",
]

REQUIRED_CARD_FIELDS = [
    "evidence_id",
    "title",
    "category",
    "source",
    "source_type",
    "url",
    "publication_time",
    "collection_time",
    "confidence",
    "evidence_level",
    "supports",
    "refutes",
    "missing_evidence",
    "weight",
    "traceability",
    "version",
]

REQUIRED_SUPPORTING_PATHS = [
    "templates/evidence-card-template.md",
    "templates/evidence-chain-template.md",
    "evaluation/rubrics/evidence-review-checklist.md",
    "docs/production/M3_COMPLETION_REPORT.md",
    "docs/review/M3_SELF_REVIEW.md",
]

M2_METHODOLOGY_DOCS = [
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


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def check(condition: bool, ok: str, fail: str, failures: list[str]) -> None:
    if condition:
        print(f"PASS: {ok}")
    else:
        print(f"FAIL: {fail}")
        failures.append(fail)


def validate_docs(failures: list[str]) -> None:
    base = ROOT / "docs" / "evidence"
    check(base.is_dir(), "docs/evidence directory exists", "missing docs/evidence directory", failures)

    for filename in EVIDENCE_DOCS:
        path = base / filename
        check(path.exists(), f"{filename} exists", f"missing evidence doc: {filename}", failures)
        if not path.exists():
            continue
        text = read_text(path)
        check(len(text) >= 1200, f"{filename} has substantive content", f"{filename} content too thin", failures)
        check("免责声明" in text and "不构成投资建议" in text, f"{filename} has disclaimer", f"{filename} missing disclaimer", failures)


def load_schema(path: Path, failures: list[str]) -> dict:
    try:
        schema = json.loads(read_text(path))
    except json.JSONDecodeError as exc:
        print(f"FAIL: {path.name} invalid JSON: {exc}")
        failures.append(f"{path.name} invalid JSON: {exc}")
        return {}
    print(f"PASS: {path.name} is valid JSON")
    return schema


def validate_schemas(failures: list[str]) -> None:
    base = ROOT / "schemas" / "evidence"
    check(base.is_dir(), "schemas/evidence directory exists", "missing schemas/evidence directory", failures)

    for filename in EVIDENCE_SCHEMAS:
        path = base / filename
        check(path.exists(), f"{filename} exists", f"missing evidence schema: {filename}", failures)
        if path.exists():
            schema = load_schema(path, failures)
            check(bool(schema.get("$schema")), f"{filename} declares $schema", f"{filename} missing $schema", failures)
            check(schema.get("type") == "object", f"{filename} top-level type is object", f"{filename} top-level type is not object", failures)

    card_path = base / "evidence-card.schema.json"
    if not card_path.exists():
        return

    card_schema = load_schema(card_path, failures)
    required = set(card_schema.get("required", []))
    properties = set(card_schema.get("properties", {}).keys())

    for field in REQUIRED_CARD_FIELDS:
        check(field in required, f"evidence-card requires {field}", f"evidence-card missing required field: {field}", failures)
        check(field in properties, f"evidence-card defines {field}", f"evidence-card missing property: {field}", failures)


def validate_supporting_files(failures: list[str]) -> None:
    for rel in REQUIRED_SUPPORTING_PATHS:
        path = ROOT / rel
        check(path.exists(), f"{rel} exists", f"missing required file: {rel}", failures)
        if path.exists():
            check(path.stat().st_size > 500, f"{rel} has substantive content", f"{rel} content too thin", failures)

    template = ROOT / "templates" / "evidence-card-template.md"
    if template.exists():
        text = read_text(template)
        display_fields = [
            "Evidence ID",
            "Title",
            "Category",
            "Source",
            "Source Type",
            "URL",
            "Publication Time",
            "Collection Time",
            "Confidence",
            "Evidence Level",
            "Supports",
            "Refutes",
            "Missing Evidence",
            "Weight",
            "Traceability",
            "Version",
        ]
        for field in display_fields:
            check(field in text, f"template contains {field}", f"template missing {field}", failures)


def validate_m1_m2_consistency(failures: list[str]) -> None:
    architecture = read_text(ROOT / "ARCHITECTURE.md")
    check("Evidence Layer" in architecture and "证据卡" in architecture and "证据链" in architecture, "ARCHITECTURE.md Evidence Layer remains compatible", "ARCHITECTURE.md Evidence Layer missing expected terms", failures)

    docs_base = ROOT / "docs" / "methodology"
    for filename in M2_METHODOLOGY_DOCS:
        path = docs_base / filename
        check(path.exists(), f"M2 methodology exists: {filename}", f"missing M2 methodology doc: {filename}", failures)
        if not path.exists():
            continue
        text = read_text(path)
        check("Required Evidence" in text, f"{filename} has Required Evidence", f"{filename} missing Required Evidence", failures)
        check("Counter Evidence" in text, f"{filename} has Counter Evidence", f"{filename} missing Counter Evidence", failures)

    docs = "\n".join(read_text((ROOT / "docs" / "evidence" / name)) for name in EVIDENCE_DOCS)
    for term in ["Required Evidence", "Counter Evidence", "supports", "refutes", "missing_evidence", "不构成投资建议"]:
        check(term in docs, f"M3 docs include compatibility term: {term}", f"M3 docs missing compatibility term: {term}", failures)

    schemas_readme = read_text(ROOT / "schemas" / "README.md")
    check("evidence-card.schema.json" in schemas_readme and "evidence-chain.schema.json" in schemas_readme, "schemas/README.md documents evidence schemas", "schemas/README.md missing evidence schema description", failures)


def main() -> int:
    failures: list[str] = []

    print("AIRS M3 Evidence Engine Validation")
    print("===================================")
    validate_docs(failures)
    validate_schemas(failures)
    validate_supporting_files(failures)
    validate_m1_m2_consistency(failures)

    print("===================================")
    if failures:
        print("RESULT: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("RESULT: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
