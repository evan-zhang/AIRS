#!/usr/bin/env python3
"""Validate APP-001 Equity Research App deliverables."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

APP_FILES = [
    "apps/__init__.py",
    "apps/equity_research/__init__.py",
    "apps/equity_research/app.py",
    "apps/equity_research/request_parser.py",
    "apps/equity_research/company_resolver.py",
    "apps/equity_research/data_collector.py",
    "apps/equity_research/analyzer.py",
    "apps/equity_research/report_exporter.py",
    "apps/equity_research/README.md",
]

DOC_FILES = [
    "docs/apps/equity-research/app-architecture.md",
    "docs/apps/equity-research/user-guide.md",
    "docs/apps/equity-research/output-specification.md",
]

SCHEMA_FILES = [
    "schemas/apps/equity-research/research-request.schema.json",
    "schemas/apps/equity-research/research-result.schema.json",
]

EXAMPLES = [
    "apps/equity_research/examples/nvidia.md",
    "apps/equity_research/examples/tsmc.md",
    "apps/equity_research/examples/concord-medical.md",
    "apps/equity_research/examples/peer-comparison.md",
]

GOVERNANCE_FILES = [
    "docs/adr/ADR-0014-equity-research-app.md",
    "docs/production/APP_001_COMPLETION_REPORT.md",
    "docs/review/APP_001_SELF_REVIEW.md",
]

SECTION_TITLES = [
    "Executive Summary",
    "Company Profile",
    "Industry Position",
    "Supply Chain / Chokepoint",
    "Financial Analysis",
    "Valuation",
    "Catalysts",
    "Risks",
    "Counter View",
    "Evidence Chain",
    "Knowledge Graph",
    "Score Card",
    "Committee Decision",
    "Final Report",
    "Appendix (Sources / Traceability)",
]

STATEMENT_MARKERS = ["### Facts", "### Inference", "### Assumption", "### Opinion"]
FORBIDDEN = ["建议买入", "建议卖出", "保证收益", "保证盈利", "应买入", "应卖出", "自动交易指令"]


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def check(condition: bool, ok: str, fail: str, failures: list[str]) -> None:
    if condition:
        print(f"PASS: {ok}")
    else:
        print(f"FAIL: {fail}")
        failures.append(fail)


def validate_text(rel: str, failures: list[str], min_size: int = 80) -> str:
    path = ROOT / rel
    check(path.exists(), f"{rel} exists", f"missing {rel}", failures)
    if not path.exists():
        return ""
    text = read(rel)
    check(len(text) >= min_size, f"{rel} has substantive content", f"{rel} content too thin", failures)
    check("不构成投资建议" in text, f"{rel} has investment disclaimer", f"{rel} missing investment disclaimer", failures)
    for word in FORBIDDEN:
        check(word not in text, f"{rel} avoids forbidden expression: {word}", f"{rel} contains forbidden expression: {word}", failures)
    return text


def validate_json(rel: str, failures: list[str]) -> dict:
    path = ROOT / rel
    check(path.exists(), f"{rel} exists", f"missing {rel}", failures)
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        check(True, f"{rel} is valid JSON", f"{rel} invalid JSON", failures)
        return data
    except json.JSONDecodeError as exc:
        check(False, f"{rel} is valid JSON", f"{rel} invalid JSON: {exc}", failures)
        return {}


def validate_static(failures: list[str]) -> None:
    for rel in APP_FILES:
        text = validate_text(rel, failures, min_size=20 if rel.endswith("__init__.py") else 500 if rel.endswith(".md") else 600)
        if rel.endswith(".py") and "equity_research" in rel:
            for term in ["DISCLAIMER", "不构成投资建议"]:
                check(term in text, f"{rel} contains {term}", f"{rel} missing {term}", failures)
    for rel in DOC_FILES:
        text = validate_text(rel, failures, min_size=800)
        for term in ["Planner", "Committee", "Runtime", "Connector", "Evidence", "Knowledge Graph", "Score"]:
            check(term in text, f"{rel} references {term}", f"{rel} missing {term}", failures)
    for rel in SCHEMA_FILES:
        data = validate_json(rel, failures)
        blob = json.dumps(data, ensure_ascii=False)
        for term in ["request_id", "disclaimer", "不构成投资建议"]:
            check(term in blob, f"{rel} contains {term}", f"{rel} missing {term}", failures)
    validate_text("templates/apps/equity-research/equity-research-report-template.md", failures, min_size=1200)
    for rel in GOVERNANCE_FILES:
        validate_text(rel, failures, min_size=500)


def validate_examples(failures: list[str]) -> None:
    for rel in EXAMPLES:
        text = validate_text(rel, failures, min_size=2500)
        for index, title in enumerate(SECTION_TITLES, start=1):
            check(f"## {index}. {title}" in text, f"{rel} contains section {index}: {title}", f"{rel} missing section {index}: {title}", failures)
        for marker in STATEMENT_MARKERS:
            check(text.count(marker) >= 15, f"{rel} repeats {marker} for all sections", f"{rel} missing repeated {marker}", failures)
        check("SKIP" in text or "Mock 降级" in text or "mock" in text.lower(), f"{rel} records SKIP/mock degradation", f"{rel} missing degradation note", failures)


def validate_runtime(failures: list[str]) -> None:
    sys.path.insert(0, str(ROOT))
    from apps.equity_research import run_equity_research

    result = run_equity_research({"symbol": "NVDA", "market": "US", "research_question": "分析 NVIDIA 的财务、估值、供应链和风险"})
    sections = result["report"]["sections"]
    check(len(sections) == 15, "runtime result has 15 sections", "runtime result does not have 15 sections", failures)
    for title in SECTION_TITLES:
        check(any(section["title"] == title for section in sections), f"runtime contains {title}", f"runtime missing {title}", failures)
    for section in sections:
        for key in ["facts", "inference", "assumption", "opinion"]:
            check(key in section and isinstance(section[key], list), f"{section['title']} has {key}", f"{section['title']} missing {key}", failures)
    check(result["data_collection"]["evidence_cards"], "runtime creates evidence cards", "runtime missing evidence cards", failures)
    check("不构成投资建议" in result["disclaimer"], "runtime result has disclaimer", "runtime missing disclaimer", failures)


def validate_changelog(failures: list[str]) -> None:
    changelog = read("CHANGELOG.md")
    check("APP-001" in changelog and "Equity Research App" in changelog, "CHANGELOG documents APP-001", "CHANGELOG missing APP-001", failures)


def main() -> int:
    failures: list[str] = []
    print("AIRS APP-001 Equity Research App Validation")
    print("===========================================")
    validate_static(failures)
    validate_examples(failures)
    validate_runtime(failures)
    validate_changelog(failures)
    print("===========================================")
    if failures:
        print("RESULT: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("RESULT: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())

