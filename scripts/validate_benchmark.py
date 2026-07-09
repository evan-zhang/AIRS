#!/usr/bin/env python3
"""Validate AIRS M7 Benchmark deliverables."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOCS = [
    "docs/benchmark/benchmark-architecture.md",
    "docs/benchmark/benchmark-lifecycle.md",
    "docs/benchmark/benchmark-classification.md",
    "docs/benchmark/benchmark-governance.md",
]

CATEGORIES = ["ai", "semiconductor", "innovative-drug", "robotics", "new-energy", "general"]
BENCHMARK_FILES = ["template.md", "gold-standard.md", "evaluation-criteria.md", "expected-output.md", "failure-cases.md"]

SCHEMAS = [
    "schemas/benchmark/benchmark.schema.json",
    "schemas/benchmark/benchmark-result.schema.json",
    "schemas/benchmark/example.schema.json",
]

TEMPLATES = [
    "templates/benchmark-case-template.md",
    "templates/benchmark-template.md",
    "templates/example-template.md",
]

FORBIDDEN = ["建议买入", "建议卖出", "保证收益", "保证盈利"]


def read_text(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def check(condition: bool, ok: str, fail: str, failures: list[str]) -> None:
    if condition:
        print(f"PASS: {ok}")
    else:
        print(f"FAIL: {fail}")
        failures.append(fail)


def validate_markdown(rel: str, failures: list[str], min_size: int = 450) -> None:
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


def validate_benchmark_files(failures: list[str]) -> None:
    required_terms = ["M3 Evidence", "Evidence ID", "Evidence Level", "Confidence", "Weight", "M6", "Scorecard", "Quality Gate", "反方观点", "不确定性"]
    for category in CATEGORIES:
        for name in BENCHMARK_FILES:
            rel = f"benchmark/{category}/{name}"
            validate_markdown(rel, failures, min_size=500)
            if not (ROOT / rel).exists():
                continue
            text = read_text(rel)
            for term in required_terms:
                check(term in text, f"{rel} includes {term}", f"{rel} missing {term}", failures)


def validate_consistency(failures: list[str]) -> None:
    schemas_readme = read_text("schemas/README.md")
    check("schemas/benchmark/benchmark.schema.json" in schemas_readme, "schemas/README documents benchmark schema", "schemas/README missing benchmark schema", failures)
    check("schemas/benchmark/example.schema.json" in schemas_readme, "schemas/README documents example schema", "schemas/README missing example schema", failures)
    template = read_text("templates/benchmark-template.md")
    check("M4 Prompt" in template and "M3 Evidence" in template and "M6" in template, "benchmark template maps M4/M3/M6", "benchmark template missing M4/M3/M6 mapping", failures)


def main() -> int:
    failures: list[str] = []
    print("AIRS M7 Benchmark Validation")
    print("============================")

    for rel in DOCS:
        validate_markdown(rel, failures)
    validate_benchmark_files(failures)
    for rel in SCHEMAS:
        validate_schema(rel, failures)
    for rel in TEMPLATES:
        validate_markdown(rel, failures, min_size=350)
    validate_consistency(failures)

    print("============================")
    if failures:
        print("RESULT: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("RESULT: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
