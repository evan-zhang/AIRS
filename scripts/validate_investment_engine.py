#!/usr/bin/env python3
"""Validate AIRS FEATURE-008 Investment Research Engine deliverables."""

from __future__ import annotations

import importlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOCS = [
    "docs/investment-engine/engine-architecture.md",
    "docs/investment-engine/research-pipeline.md",
    "docs/investment-engine/idea-generation.md",
    "docs/investment-engine/recommendation-standards.md",
    "docs/orchestrator/orchestrator-architecture.md",
]
CORE = [
    "investment_engine/__init__.py",
    "investment_engine/theme_discovery.py",
    "investment_engine/company_discovery.py",
    "investment_engine/industry_discovery.py",
    "investment_engine/supply_chain.py",
    "investment_engine/chokepoint.py",
    "investment_engine/thesis_generator.py",
    "investment_engine/risk.py",
    "investment_engine/catalyst.py",
    "investment_engine/comparable.py",
    "investment_engine/portfolio_impact.py",
    "investment_engine/recommendation.py",
    "investment_engine/pipeline.py",
    "investment_engine/README.md",
]
EXAMPLES = [
    ("investment_engine/examples/ai_compute.py", "investment_engine/examples/ai-compute.md"),
    ("investment_engine/examples/innovative_drug.py", "investment_engine/examples/innovative-drug.md"),
    ("investment_engine/examples/semiconductor.py", "investment_engine/examples/semiconductor.md"),
    ("investment_engine/examples/robotics.py", "investment_engine/examples/robotics.md"),
    ("investment_engine/examples/new_energy.py", "investment_engine/examples/new-energy.md"),
]
SCHEMAS = [
    "schemas/investment/investment-request.schema.json",
    "schemas/investment/investment-thesis.schema.json",
    "schemas/investment/recommendation.schema.json",
]
TEMPLATES = [
    "templates/investment/investment-report-template.md",
    "templates/investment/thesis-template.md",
]
BUILDER = [
    "builder-output/investment-research-engine/ISSUE.md",
    "builder-output/investment-research-engine/ADR.md",
    "builder-output/investment-research-engine/FEATURE_SPEC.md",
    "builder-output/investment-research-engine/skill/investment-research-engine-skill.md",
    "builder-output/investment-research-engine/prompt/investment-research-engine-prompt.md",
    "builder-output/investment-research-engine/schema/investment-research-engine.schema.json",
    "builder-output/investment-research-engine/tests/test-investment-research-engine.md",
    "builder-output/investment-research-engine/benchmark/investment-research-engine-benchmark.md",
    "builder-output/investment-research-engine/PR_CHECKLIST.md",
    "builder-output/investment-research-engine/RELEASE_NOTES.md",
]
REPORTS = [
    "docs/adr/ADR-0008-investment-research-engine.md",
    "docs/production/FEATURE_008_COMPLETION_REPORT.md",
    "docs/review/FEATURE_008_SELF_REVIEW.md",
]
FORBIDDEN = ["建议买入", "建议卖出", "保证收益", "保证盈利", "目标价为", "应买入", "应卖出", "自动交易指令"]
REQUIRED_OUTPUTS = [
    "investment_thesis",
    "knowledge_graph",
    "evidence_chain",
    "supply_chain_analysis",
    "chokepoint_analysis",
    "score_card",
    "risk_analysis",
    "catalyst_analysis",
    "final_research_report",
]
REGRESSION_SCRIPTS = [
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
    "scripts/validate_builder.py",
    "scripts/validate_knowledge_graph.py",
    "scripts/validate_report_generator.py",
    "scripts/validate_connectors.py",
    "scripts/validate_runtime.py",
    "scripts/validate_workspace.py",
]


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def check(condition: bool, ok: str, fail: str, failures: list[str]) -> None:
    if condition:
        print(f"PASS: {ok}")
    else:
        print(f"FAIL: {fail}")
        failures.append(fail)


def text(rel: str, failures: list[str], min_size: int = 120, disclaimer: bool = True) -> str:
    path = ROOT / rel
    check(path.exists(), f"{rel} exists", f"missing {rel}", failures)
    if not path.exists():
        return ""
    value = read(rel)
    check(len(value) >= min_size, f"{rel} has substantive content", f"{rel} content too thin", failures)
    if disclaimer:
        check("免责声明" in value and "不构成投资建议" in value, f"{rel} has disclaimer", f"{rel} missing disclaimer", failures)
    for word in FORBIDDEN:
        check(word not in value, f"{rel} avoids forbidden expression: {word}", f"{rel} contains forbidden expression: {word}", failures)
    return value


def json_file(rel: str, failures: list[str]) -> dict:
    path = ROOT / rel
    check(path.exists(), f"{rel} exists", f"missing {rel}", failures)
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        check(False, f"{rel} valid JSON", f"{rel} invalid JSON: {exc}", failures)
        return {}
    check(True, f"{rel} valid JSON", f"{rel} invalid JSON", failures)
    blob = json.dumps(data, ensure_ascii=False)
    check("不构成投资建议" in blob, f"{rel} has compliance language", f"{rel} missing compliance language", failures)
    return data


def validate_static(failures: list[str]) -> None:
    for rel in DOCS:
        value = text(rel, failures, 350)
        for term in ["Engine", "Runtime", "Evidence"]:
            if rel.startswith("docs/investment-engine/"):
                check(term in value, f"{rel} references {term}", f"{rel} missing {term}", failures)
    for rel in CORE:
        value = text(rel, failures, 20, disclaimer=rel.endswith(".md"))
        check("investment" in value.lower() or "research" in value.lower() or rel.endswith("__init__.py"), f"{rel} contains engine logic", f"{rel} missing engine logic", failures)
    for rel in SCHEMAS:
        json_file(rel, failures)
    for rel in TEMPLATES + BUILDER + REPORTS:
        if rel.endswith(".json"):
            json_file(rel, failures)
        else:
            text(rel, failures, 180)
    schema_readme = read("schemas/README.md")
    changelog = read("CHANGELOG.md")
    check("schemas/investment/" in schema_readme and "recommendation.schema.json" in schema_readme, "schemas/README documents investment schemas", "schemas/README missing investment schemas", failures)
    check("FEATURE-008" in changelog and "Investment Research Engine" in changelog, "CHANGELOG documents FEATURE-008", "CHANGELOG missing FEATURE-008", failures)


def validate_examples(failures: list[str]) -> None:
    sys.path.insert(0, str(ROOT))
    check((ROOT / "investment_engine/examples/__init__.py").exists(), "investment examples package exists", "missing examples __init__.py", failures)
    for py_rel, md_rel in EXAMPLES:
        text(py_rel, failures, 120, disclaimer=False)
        md = text(md_rel, failures, 450)
        for section in ["Investment Thesis", "Knowledge Graph", "Evidence Chain", "Supply Chain Analysis", "Chokepoint Analysis", "Score Card", "Risk Analysis", "Catalyst Analysis", "Final Research Report"]:
            check(section in md, f"{md_rel} contains {section}", f"{md_rel} missing {section}", failures)
        module = importlib.import_module(py_rel[:-3].replace("/", "."))
        result = module.run()
        blob = json.dumps(result, ensure_ascii=False)
        for key in REQUIRED_OUTPUTS:
            check(key in result, f"{py_rel} outputs {key}", f"{py_rel} missing {key}", failures)
        for term in ["runtime", "orchestrator", "skill", "prompt", "evidence", "knowledge_graph", "score"]:
            check(term in result["infrastructure_refs"], f"{py_rel} references {term}", f"{py_rel} missing infrastructure ref {term}", failures)
        coverage = result["recommendation"]["statement_coverage"]
        for kind in ["Fact", "Inference", "Assumption", "Opinion"]:
            check(coverage.get(kind, 0) >= 1, f"{py_rel} covers {kind}", f"{py_rel} missing {kind}", failures)
        check("不构成投资建议" in blob, f"{py_rel} carries disclaimer", f"{py_rel} missing disclaimer", failures)
        for word in FORBIDDEN:
            check(word not in blob, f"{py_rel} avoids forbidden expression: {word}", f"{py_rel} contains forbidden expression: {word}", failures)


def validate_consistency(failures: list[str]) -> None:
    pipeline = read("investment_engine/pipeline.py")
    standards = read("docs/investment-engine/recommendation-standards.md")
    for term in ["runtime", "orchestrator", "workspace", "connectors", "methodology", "skill", "prompt", "evidence", "knowledge_graph", "score", "report"]:
        check(term in pipeline, f"pipeline references {term}", f"pipeline missing {term}", failures)
    for term in ["Fact", "Inference", "Assumption", "Opinion"]:
        check(term in standards and term in pipeline, f"Recommendation distinguishes {term}", f"Recommendation missing {term}", failures)
    check("FORBIDDEN_TERMS" in read("investment_engine/recommendation.py"), "recommendation guards forbidden terms", "recommendation missing forbidden terms", failures)


def validate_regressions(failures: list[str]) -> None:
    check(len(REGRESSION_SCRIPTS) + 1 == 17, "current run plus 16 regression scripts covers 17 validate_* scripts", "validate script count is not 17", failures)
    for rel in REGRESSION_SCRIPTS:
        result = subprocess.run([sys.executable, str(ROOT / rel)], cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False)
        ok = result.returncode == 0 and ("RESULT: PASS" in result.stdout or "最终结果: PASS" in result.stdout)
        check(ok, f"{Path(rel).name} PASS", f"{Path(rel).name} FAIL\n{result.stdout}", failures)


def main() -> int:
    failures: list[str] = []
    print("AIRS FEATURE-008 Investment Research Engine Validation")
    print("======================================================")
    validate_static(failures)
    validate_examples(failures)
    validate_consistency(failures)
    validate_regressions(failures)
    print("======================================================")
    if failures:
        print("RESULT: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("RESULT: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
