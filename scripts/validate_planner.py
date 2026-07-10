#!/usr/bin/env python3
"""Validate AIRS FEATURE-009 Autonomous Research Planner deliverables."""

from __future__ import annotations

import importlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOCS = [
    "docs/planner/planner-architecture.md",
    "docs/planner/goal-parser.md",
    "docs/planner/intent-analyzer.md",
    "docs/planner/research-scope-builder.md",
    "docs/planner/planning-engine.md",
    "docs/planner/dependency-planner.md",
    "docs/planner/workflow-planner.md",
    "docs/planner/runtime-planner.md",
    "docs/planner/resource-planner.md",
    "docs/planner/budget-planner.md",
    "docs/planner/confidence-planner.md",
    "docs/planner/plan-optimizer.md",
]
CORE = [
    "planner/__init__.py",
    "planner/goal_parser.py",
    "planner/intent_analyzer.py",
    "planner/scope_builder.py",
    "planner/engine.py",
    "planner/dependency.py",
    "planner/workflow.py",
    "planner/runtime.py",
    "planner/resource.py",
    "planner/budget.py",
    "planner/confidence.py",
    "planner/optimizer.py",
    "planner/README.md",
]
SCHEMAS = [
    "schemas/planner/research-goal.schema.json",
    "schemas/planner/research-plan.schema.json",
    "schemas/planner/planning-task.schema.json",
    "schemas/planner/planning-result.schema.json",
]
TEMPLATES = [
    "templates/planner/research-plan-template.md",
    "templates/planner/planning-task-template.md",
]
BUILDER = [
    "builder/requests/feature-request-autonomous-research-planner.yaml",
    "builder-output/autonomous-research-planner/ISSUE.md",
    "builder-output/autonomous-research-planner/ADR.md",
    "builder-output/autonomous-research-planner/FEATURE_SPEC.md",
    "builder-output/autonomous-research-planner/skill/autonomous-research-planner-skill.md",
    "builder-output/autonomous-research-planner/prompt/autonomous-research-planner-prompt.md",
    "builder-output/autonomous-research-planner/schema/autonomous-research-planner.schema.json",
    "builder-output/autonomous-research-planner/tests/test-autonomous-research-planner.md",
    "builder-output/autonomous-research-planner/benchmark/autonomous-research-planner-benchmark.md",
    "builder-output/autonomous-research-planner/PR_CHECKLIST.md",
    "builder-output/autonomous-research-planner/RELEASE_NOTES.md",
]
EXAMPLES = [
    ("planner/examples/company_research.py", "planner/examples/company-research.md", "company"),
    ("planner/examples/industry_research.py", "planner/examples/industry-research.md", "industry"),
    ("planner/examples/theme_research.py", "planner/examples/theme-research.md", "theme"),
    ("planner/examples/supply_chain_research.py", "planner/examples/supply-chain-research.md", "supply_chain"),
    ("planner/examples/chokepoint_research.py", "planner/examples/chokepoint-research.md", "chokepoint"),
    ("planner/examples/policy_research.py", "planner/examples/policy-research.md", "policy"),
    ("planner/examples/portfolio_research.py", "planner/examples/portfolio-research.md", "portfolio"),
    ("planner/examples/comparative_research.py", "planner/examples/comparative-research.md", "comparative"),
]
REPORTS = [
    "docs/adr/ADR-0009-autonomous-research-planner.md",
    "docs/production/FEATURE_009_COMPLETION_REPORT.md",
    "docs/review/FEATURE_009_SELF_REVIEW.md",
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
    "scripts/validate_investment_engine.py",
]
FORBIDDEN = ["建议买入", "建议卖出", "保证收益", "保证盈利", "目标价为", "应买入", "应卖出", "自动交易指令"]
REQUIRED_EXAMPLE_SECTIONS = [
    "Goal Analysis",
    "Scope",
    "Required Connectors/Methodologies/Skills/Runtime",
    "Expected Evidence/KG",
    "Execution Order",
    "Estimated Cost/Time",
    "Expected Deliverables",
    "Confidence",
    "Risks",
]
REQUIRED_PLAN_KEYS = [
    "goal_analysis",
    "scope",
    "required_connectors",
    "required_methodologies",
    "required_skills",
    "required_runtime",
    "expected_evidence",
    "expected_kg",
    "execution_order",
    "budget",
    "confidence",
    "expected_deliverables",
    "risks",
]


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def check(condition: bool, ok: str, fail: str, failures: list[str]) -> None:
    if condition:
        print(f"PASS: {ok}")
    else:
        print(f"FAIL: {fail}")
        failures.append(fail)


def text(rel: str, failures: list[str], min_size: int = 160, disclaimer: bool = True) -> str:
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
        value = text(rel, failures, 500)
        check("Planner" in value and "Runtime" in value, f"{rel} references Planner and Runtime", f"{rel} missing Planner or Runtime", failures)
    for rel in CORE:
        value = text(rel, failures, 20, disclaimer=rel.endswith(".md"))
        check("planner" in value.lower() or rel.endswith("__init__.py"), f"{rel} contains planner logic", f"{rel} missing planner logic", failures)
    for rel in SCHEMAS:
        json_file(rel, failures)
    for rel in TEMPLATES + BUILDER + REPORTS:
        if rel.endswith(".json"):
            json_file(rel, failures)
        else:
            text(rel, failures, 180, disclaimer=not rel.endswith(".yaml"))
    schema_readme = read("schemas/README.md")
    changelog = read("CHANGELOG.md")
    check("schemas/planner/" in schema_readme and "research-plan.schema.json" in schema_readme, "schemas/README documents planner schemas", "schemas/README missing planner schemas", failures)
    check("FEATURE-009" in changelog and "Autonomous Research Planner" in changelog, "CHANGELOG documents FEATURE-009", "CHANGELOG missing FEATURE-009", failures)


def validate_examples(failures: list[str]) -> None:
    sys.path.insert(0, str(ROOT))
    check((ROOT / "planner/examples/__init__.py").exists(), "planner examples package exists", "missing planner examples __init__.py", failures)
    seen_types: set[str] = set()
    for py_rel, md_rel, expected_type in EXAMPLES:
        text(py_rel, failures, 80, disclaimer=False)
        md = text(md_rel, failures, 500)
        for section in REQUIRED_EXAMPLE_SECTIONS:
            check(section in md, f"{md_rel} contains {section}", f"{md_rel} missing {section}", failures)
        module = importlib.import_module(py_rel[:-3].replace("/", "."))
        result = module.run()
        blob = json.dumps(result, ensure_ascii=False)
        for key in REQUIRED_PLAN_KEYS:
            check(key in result, f"{py_rel} outputs {key}", f"{py_rel} missing {key}", failures)
        seen_types.add(result["goal_analysis"]["goal_type"])
        runtime = result["required_runtime"]
        check(runtime.get("planner_generated") is True, f"{py_rel} runtime is planner generated", f"{py_rel} runtime missing planner gate", failures)
        check(runtime.get("raw_user_request_allowed") is False, f"{py_rel} blocks raw user request", f"{py_rel} allows raw user request", failures)
        check(result["goal_analysis"]["goal_type"] == expected_type, f"{py_rel} goal type {expected_type}", f"{py_rel} wrong goal type", failures)
        for term in ["runtime", "workflow", "methodology", "connector", "skill", "knowledge_graph", "evidence", "score", "report", "workspace"]:
            check(term in result["infrastructure_refs"], f"{py_rel} references {term}", f"{py_rel} missing infrastructure ref {term}", failures)
        check("不构成投资建议" in blob, f"{py_rel} carries disclaimer", f"{py_rel} missing disclaimer", failures)
        for word in FORBIDDEN:
            check(word not in blob, f"{py_rel} avoids forbidden expression: {word}", f"{py_rel} contains forbidden expression: {word}", failures)
    check(seen_types == {item[2] for item in EXAMPLES}, "all eight planner goal types covered", "planner examples do not cover eight goal types", failures)


def validate_consistency(failures: list[str]) -> None:
    engine = read("planner/engine.py")
    runtime = read("planner/runtime.py")
    architecture = read("docs/planner/planner-architecture.md")
    for term in ["Runtime", "Workflow", "Methodology", "Connector", "Skill", "Evidence", "Knowledge Graph", "Score", "Report"]:
        check(term in architecture, f"planner architecture references {term}", f"planner architecture missing {term}", failures)
    check("raw_user_request_allowed" in runtime and "False" in runtime, "runtime planner blocks raw user requests", "runtime planner does not block raw user requests", failures)
    check("infrastructure_refs" in engine and "expected_evidence" in engine and "expected_kg" in engine, "engine outputs infrastructure and expected artifacts", "engine missing expected artifacts", failures)


def validate_regressions(failures: list[str]) -> None:
    check(len(REGRESSION_SCRIPTS) + 1 == 18, "current run plus 17 regression scripts covers 18 validate_* scripts", "validate script count is not 18", failures)
    for rel in REGRESSION_SCRIPTS:
        result = subprocess.run([sys.executable, str(ROOT / rel)], cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False)
        ok = result.returncode == 0 and ("RESULT: PASS" in result.stdout or "最终结果: PASS" in result.stdout or "FINAL RESULT: PASS" in result.stdout)
        check(ok, f"{Path(rel).name} PASS", f"{Path(rel).name} FAIL\n{result.stdout}", failures)


def main() -> int:
    failures: list[str] = []
    print("AIRS FEATURE-009 Autonomous Research Planner Validation")
    print("=======================================================")
    validate_static(failures)
    validate_examples(failures)
    validate_consistency(failures)
    validate_regressions(failures)
    print("=======================================================")
    if failures:
        print("RESULT: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("RESULT: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
