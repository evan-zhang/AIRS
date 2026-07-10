#!/usr/bin/env python3
"""Validate AIRS M8 Production Release deliverables."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

PRODUCTION_DOCS = [
    "docs/production/production-guide.md",
    "docs/production/deployment-guide.md",
    "docs/production/upgrade-guide.md",
    "docs/production/maintenance-guide.md",
    "docs/production/governance-guide.md",
    "docs/production/release-checklist.md",
    "docs/production/release-notes.md",
]

ADDITIONAL_PRODUCTION_DOCS = [
    "docs/production/production-acceptance-checklist.md",
    "docs/production/final-quality-gate.md",
    "docs/production/regression-test-process.md",
]

GOVERNANCE_DOCS = [
    "docs/governance/semantic-versioning.md",
    "docs/governance/release-workflow.md",
]

GITHUB_FILES = [
    ".github/ISSUE_TEMPLATE/bug_report.md",
    ".github/ISSUE_TEMPLATE/feature_request.md",
    ".github/pull_request_template.md",
    ".github/CODEOWNERS",
    ".github/SECURITY.md",
    ".github/SUPPORT.md",
]

FINAL_REPORTS = [
    "docs/production/M8_COMPLETION_REPORT.md",
    "docs/production/PROJECT_HEALTH_REPORT.md",
    "docs/production/FINAL_REVIEW.md",
]

TOP_LEVEL = [
    "README.md",
    "CONTRIBUTING.md",
    "CHANGELOG.md",
    "ROADMAP.md",
    "LICENSE",
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


def validate_markdown(rel: str, failures: list[str], min_size: int = 500, require_disclaimer: bool = True) -> None:
    path = ROOT / rel
    check(path.exists(), f"{rel} exists", f"missing {rel}", failures)
    if not path.exists():
        return
    text = read_text(rel)
    check(len(text) >= min_size, f"{rel} has substantive content", f"{rel} content too thin", failures)
    if require_disclaimer:
        check("免责声明" in text and "不构成投资建议" in text, f"{rel} has disclaimer", f"{rel} missing disclaimer", failures)
    for forbidden in FORBIDDEN:
        check(forbidden not in text, f"{rel} avoids forbidden expression: {forbidden}", f"{rel} contains forbidden expression: {forbidden}", failures)


def validate_required_files(failures: list[str]) -> None:
    for rel in PRODUCTION_DOCS + ADDITIONAL_PRODUCTION_DOCS + GOVERNANCE_DOCS + FINAL_REPORTS:
        validate_markdown(rel, failures)

    for rel in GITHUB_FILES:
        validate_markdown(rel, failures, min_size=120, require_disclaimer=rel.endswith(".md"))

    for rel in TOP_LEVEL:
        path = ROOT / rel
        check(path.exists(), f"{rel} exists", f"missing top-level file: {rel}", failures)
        if path.exists():
            check(path.stat().st_size > 500, f"{rel} has content", f"{rel} content too thin", failures)


def validate_release_terms(failures: list[str]) -> None:
    readme = read_text("README.md")
    check("v1.0.0" in readme and "Production" in readme, "README documents v1.0.0 Production", "README missing v1.0.0 Production status", failures)
    check("完整功能列表" in readme or "功能列表" in readme, "README has feature list", "README missing feature list", failures)
    check("不构成投资建议" in readme and "免责声明" in readme, "README has final disclaimer", "README missing final disclaimer", failures)

    contributing = read_text("CONTRIBUTING.md")
    check("semantic-versioning.md" in contributing, "CONTRIBUTING references semantic versioning", "CONTRIBUTING missing semantic versioning reference", failures)
    check("release-workflow.md" in contributing, "CONTRIBUTING references release workflow", "CONTRIBUTING missing release workflow reference", failures)

    changelog = read_text("CHANGELOG.md")
    check("[1.0.0]" in changelog and "M8" in changelog, "CHANGELOG documents v1.0.0 M8", "CHANGELOG missing v1.0.0 M8 release", failures)

    roadmap = read_text("ROADMAP.md")
    check("M1-M8 全部完成" in roadmap or "M8: Production" in roadmap and "✅" in roadmap, "ROADMAP marks production completion", "ROADMAP missing M8 completion status", failures)
    check("V1.x" in roadmap and "V2" in roadmap, "ROADMAP includes V1.x and V2 direction", "ROADMAP missing future direction", failures)

    license_text = read_text("LICENSE")
    check("MIT License" in license_text, "LICENSE remains MIT", "LICENSE missing MIT License", failures)
    check("不构成投资建议" in license_text and "AIRS" in license_text, "LICENSE has AIRS disclaimer", "LICENSE missing AIRS disclaimer", failures)

    adr = read_text("docs/adr/0002-m8-production-top-level-updates.md")
    check("README" in adr and "CHANGELOG" in adr and "ROADMAP" in adr, "ADR records top-level updates", "ADR missing top-level update rationale", failures)


def validate_scripts(failures: list[str]) -> None:
    required = [
        "scripts/validate_m1.py",
        "scripts/validate_m2.py",
        "scripts/validate_evidence.py",
        "scripts/validate_prompt.py",
        "scripts/validate_skill.py",
        "scripts/validate_score.py",
        "scripts/validate_evaluation.py",
        "scripts/validate_benchmark.py",
        "scripts/validate_examples.py",
        "scripts/validate_release.py",
        "scripts/production_check.py",
    ]
    for rel in required:
        path = ROOT / rel
        check(path.exists(), f"{rel} exists", f"missing validation script: {rel}", failures)
        if path.exists():
            check("PASS" in path.read_text(encoding="utf-8") or "RESULT" in path.read_text(encoding="utf-8"), f"{rel} emits result", f"{rel} missing result output", failures)


def main() -> int:
    failures: list[str] = []
    print("AIRS M8 Production Release Validation")
    print("=====================================")
    validate_required_files(failures)
    validate_release_terms(failures)
    validate_scripts(failures)

    print("=====================================")
    if failures:
        print("RESULT: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("RESULT: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
