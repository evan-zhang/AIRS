#!/usr/bin/env python3
"""Validate AIRS FEATURE-001 Builder deliverables."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOCS = [
    "docs/builder/builder-architecture.md",
    "docs/builder/builder-lifecycle.md",
    "docs/builder/builder-governance.md",
    "docs/builder/builder-generation-flow.md",
]

BUILDER_FILES = [
    "builder/README.md",
    "builder/main.py",
    "builder/registry.py",
    "builder/generators/README.md",
]

SCHEMAS = [
    "schemas/builder/feature-request.schema.json",
    "schemas/builder/feature-package.schema.json",
    "schemas/builder/generated-artifact.schema.json",
]

TEMPLATES = [
    "templates/builder/issue-template.md",
    "templates/builder/adr-template.md",
    "templates/builder/feature-spec-template.md",
    "templates/builder/skill-template.md",
    "templates/builder/prompt-template.md",
    "templates/builder/schema-template.json",
    "templates/builder/test-template.md",
    "templates/builder/benchmark-template.md",
    "templates/builder/pr-checklist-template.md",
    "templates/builder/release-notes-template.md",
    "templates/builder/feature-request-template.yaml",
]

PACKAGES = {
    "builder-output/knowledge-graph-engine": [
        "ISSUE.md",
        "ADR.md",
        "FEATURE_SPEC.md",
        "skill/knowledge-graph-skill.md",
        "prompt/knowledge-graph-prompt.md",
        "schema/knowledge-graph.schema.json",
        "tests/test-knowledge-graph.md",
        "benchmark/knowledge-graph-benchmark.md",
        "PR_CHECKLIST.md",
        "RELEASE_NOTES.md",
    ],
    "builder-output/news-connector": [
        "ISSUE.md",
        "ADR.md",
        "FEATURE_SPEC.md",
        "skill/news-connector-skill.md",
        "prompt/news-connector-prompt.md",
        "schema/news-connector.schema.json",
        "tests/test-news-connector.md",
        "benchmark/news-connector-benchmark.md",
        "PR_CHECKLIST.md",
        "RELEASE_NOTES.md",
    ],
}

REPORTS = [
    "docs/adr/ADR-0003-feature-builder.md",
    "docs/production/FEATURE_001_COMPLETION_REPORT.md",
    "docs/review/FEATURE_001_SELF_REVIEW.md",
]

FORBIDDEN = ["建议买入", "建议卖出", "保证收益", "保证盈利", "目标价为"]


def read_text(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def check(condition: bool, ok: str, fail: str, failures: list[str]) -> None:
    if condition:
        print(f"PASS: {ok}")
    else:
        print(f"FAIL: {fail}")
        failures.append(fail)


def validate_markdown(rel: str, failures: list[str], min_size: int = 300) -> None:
    path = ROOT / rel
    check(path.exists(), f"{rel} exists", f"missing {rel}", failures)
    if not path.exists():
        return
    text = read_text(rel)
    check(len(text) >= min_size, f"{rel} has substantive content", f"{rel} content too thin", failures)
    check("免责声明" in text and "不构成投资建议" in text, f"{rel} has disclaimer", f"{rel} missing disclaimer", failures)
    for forbidden in FORBIDDEN:
        check(forbidden not in text, f"{rel} avoids forbidden expression: {forbidden}", f"{rel} contains forbidden expression: {forbidden}", failures)


def validate_json(rel: str, failures: list[str]) -> None:
    path = ROOT / rel
    check(path.exists(), f"{rel} exists", f"missing {rel}", failures)
    if not path.exists():
        return
    try:
        json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        check(False, f"{rel} is valid JSON", f"{rel} invalid JSON: {exc}", failures)
        return
    check(True, f"{rel} is valid JSON", f"{rel} invalid JSON", failures)


def validate_docs(failures: list[str]) -> None:
    for rel in DOCS:
        validate_markdown(rel, failures, min_size=700)


def validate_builder_files(failures: list[str]) -> None:
    for rel in BUILDER_FILES:
        path = ROOT / rel
        check(path.exists(), f"{rel} exists", f"missing {rel}", failures)
        if rel.endswith(".py") and path.exists():
            text = read_text(rel)
            check("Feature Package" in text or "ARTIFACTS" in text, f"{rel} contains builder logic", f"{rel} missing builder logic", failures)
    main_text = read_text("builder/main.py")
    check("load_request" in main_text and "generate_package" in main_text, "builder/main.py reads and generates", "builder/main.py missing core flow", failures)
    registry_text = read_text("builder/registry.py")
    check("ArtifactTemplate" in registry_text and "ARTIFACTS" in registry_text, "builder/registry.py registers templates", "builder/registry.py missing registry", failures)


def validate_schemas(failures: list[str]) -> None:
    for rel in SCHEMAS:
        validate_json(rel, failures)
        text = read_text(rel)
        check("不构成投资建议" in text, f"{rel} has compliance description", f"{rel} missing compliance description", failures)
    schema_readme = read_text("schemas/README.md")
    check("schemas/builder/" in schema_readme and "feature-request.schema.json" in schema_readme, "schemas/README documents builder schemas", "schemas/README missing builder schemas", failures)


def validate_templates(failures: list[str]) -> None:
    for rel in TEMPLATES:
        path = ROOT / rel
        check(path.exists(), f"{rel} exists", f"missing {rel}", failures)
        if not path.exists():
            continue
        if rel.endswith(".json"):
            validate_json(rel, failures)
        else:
            text = read_text(rel)
            check(len(text) >= 180, f"{rel} has content", f"{rel} content too thin", failures)
    skill = read_text("templates/builder/skill-template.md")
    prompt = read_text("templates/builder/prompt-template.md")
    benchmark = read_text("templates/builder/benchmark-template.md")
    check("templates/skill-template.md" in skill and "M5" in skill, "builder skill template references M5", "builder skill template missing M5 reference", failures)
    check("templates/prompt-template.md" in prompt and "M4" in prompt, "builder prompt template references M4", "builder prompt template missing M4 reference", failures)
    check("templates/benchmark-template.md" in benchmark and "M7" in benchmark, "builder benchmark template references M7", "builder benchmark template missing M7 reference", failures)


def validate_packages(failures: list[str]) -> None:
    for package, files in PACKAGES.items():
        package_path = ROOT / package
        check(package_path.exists(), f"{package} exists", f"missing package {package}", failures)
        for item in files:
            rel = f"{package}/{item}"
            if item.endswith(".json"):
                validate_json(rel, failures)
            else:
                validate_markdown(rel, failures, min_size=250)
        joined = "\n".join(
            (package_path / item).read_text(encoding="utf-8")
            for item in files
            if (package_path / item).exists() and not item.endswith(".json")
        )
        check("templates/skill-template.md" in joined, f"{package} references skill template", f"{package} missing skill template reference", failures)
        check("templates/prompt-template.md" in joined, f"{package} references prompt template", f"{package} missing prompt template reference", failures)
        check("templates/benchmark-template.md" in joined, f"{package} references benchmark template", f"{package} missing benchmark template reference", failures)
        check("反方" in joined and "不确定性" in joined, f"{package} includes counter view and uncertainty", f"{package} missing counter view or uncertainty", failures)


def validate_reports(failures: list[str]) -> None:
    for rel in REPORTS:
        validate_markdown(rel, failures, min_size=500)
    changelog = read_text("CHANGELOG.md")
    check("FEATURE-001" in changelog and "AIRS Builder" in changelog, "CHANGELOG documents FEATURE-001", "CHANGELOG missing FEATURE-001", failures)


def main() -> int:
    failures: list[str] = []
    print("AIRS FEATURE-001 Builder Validation")
    print("===================================")
    validate_docs(failures)
    validate_builder_files(failures)
    validate_schemas(failures)
    validate_templates(failures)
    validate_packages(failures)
    validate_reports(failures)
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
