#!/usr/bin/env python3
"""Validate AIRS FEATURE-007 AI Research Workspace deliverables."""
from __future__ import annotations

import importlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOCS = [
    "docs/workspace/workspace-architecture.md",
    "docs/workspace/workspace-lifecycle.md",
    "docs/workspace/project-management.md",
    "docs/workspace/session-management.md",
    "docs/workspace/artifact-governance.md",
]

CORE = [
    "workspace/__init__.py",
    "workspace/manager.py",
    "workspace/project.py",
    "workspace/session.py",
    "workspace/timeline.py",
    "workspace/artifact.py",
    "workspace/task_board.py",
    "workspace/memory.py",
    "workspace/snapshot.py",
    "workspace/version.py",
    "workspace/replay.py",
    "workspace/export.py",
    "workspace/collaboration.py",
    "workspace/audit.py",
    "workspace/README.md",
]

EXAMPLES = [
    ("workspace/examples/company_research_workspace.py", "workspace/examples/company-research-workspace-dashboard.md"),
    ("workspace/examples/industry_research_workspace.py", "workspace/examples/industry-research-workspace-dashboard.md"),
    ("workspace/examples/hot_topic_workspace.py", "workspace/examples/hot-topic-workspace-dashboard.md"),
    ("workspace/examples/supply_chain_workspace.py", "workspace/examples/supply-chain-workspace-dashboard.md"),
    ("workspace/examples/report_workspace.py", "workspace/examples/report-workspace-dashboard.md"),
]

SCHEMAS = [
    "schemas/workspace/workspace.schema.json",
    "schemas/workspace/project.schema.json",
    "schemas/workspace/session.schema.json",
    "schemas/workspace/artifact.schema.json",
    "schemas/workspace/snapshot.schema.json",
]

TEMPLATES = ["templates/workspace-dashboard-template.md"]

BUILDER = [
    "builder-output/ai-research-workspace/ISSUE.md",
    "builder-output/ai-research-workspace/ADR.md",
    "builder-output/ai-research-workspace/FEATURE_SPEC.md",
    "builder-output/ai-research-workspace/skill/ai-research-workspace-skill.md",
    "builder-output/ai-research-workspace/prompt/ai-research-workspace-prompt.md",
    "builder-output/ai-research-workspace/schema/ai-research-workspace.schema.json",
    "builder-output/ai-research-workspace/tests/test-ai-research-workspace.md",
    "builder-output/ai-research-workspace/benchmark/ai-research-workspace-benchmark.md",
    "builder-output/ai-research-workspace/PR_CHECKLIST.md",
    "builder-output/ai-research-workspace/RELEASE_NOTES.md",
]

REPORTS = [
    "docs/adr/ADR-0007-ai-research-workspace.md",
    "docs/production/M7_COMPLETION_REPORT.md",
    "docs/review/M7_SELF_REVIEW.md",
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
    "scripts/validate_connectors.py",
    "scripts/validate_report_generator.py",
    "scripts/validate_runtime.py",
]

FORBIDDEN = ["建议买入", "建议卖出", "保证收益", "保证盈利", "目标价为", "应买入", "应卖出", "自动交易指令"]


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def check(cond: bool, ok: str, fail: str, failures: list[str]) -> None:
    if cond:
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
        check(False, f"{rel} is valid JSON", f"{rel} invalid JSON: {exc}", failures)
        return {}
    check(True, f"{rel} is valid JSON", f"{rel} invalid JSON", failures)
    return data


def validate_static(failures: list[str]) -> None:
    for rel in DOCS:
        value = text(rel, failures, 500)
        for term in ["Workspace", "Runtime", "Artifact"]:
            check(term in value, f"{rel} references {term}", f"{rel} missing {term}", failures)
    for rel in CORE:
        value = text(rel, failures, 20, disclaimer=rel.endswith(".md"))
        check("Workspace" in value or "Manager" in value or "Audit" in value or rel.endswith("__init__.py"), f"{rel} contains workspace logic", f"{rel} missing workspace logic", failures)
    for rel in SCHEMAS:
        data = json_file(rel, failures)
        blob = json.dumps(data, ensure_ascii=False)
        for term in ["$schema", "disclaimer", "不构成投资建议"]:
            check(term in blob, f"{rel} contains {term}", f"{rel} missing {term}", failures)
    for rel in TEMPLATES + BUILDER + REPORTS:
        if rel.endswith(".json"):
            json_file(rel, failures)
        else:
            text(rel, failures, 180)


def validate_examples(failures: list[str]) -> None:
    sys.path.insert(0, str(ROOT))
    check((ROOT / "workspace/examples/__init__.py").exists(), "workspace/examples/__init__.py exists", "missing workspace/examples/__init__.py", failures)
    for py_rel, md_rel in EXAMPLES:
        text(py_rel, failures, 300, disclaimer=False)
        dashboard = text(md_rel, failures, 450)
        for term in ["Project", "Sessions", "Task Board", "Artifacts", "Timeline"]:
            check(term in dashboard, f"{md_rel} contains {term}", f"{md_rel} missing {term}", failures)
        module = importlib.import_module(py_rel[:-3].replace("/", "."))
        result = module.run()
        blob = json.dumps(result, ensure_ascii=False)
        for term in ["workspace", "dashboard", "不构成投资建议"]:
            check(term in blob, f"{py_rel} outputs {term}", f"{py_rel} missing {term}", failures)
        state = result["workspace"]
        check(state["projects"], f"{py_rel} creates project", f"{py_rel} missing project", failures)
        check(state["sessions"], f"{py_rel} creates session", f"{py_rel} missing session", failures)
        check(state["artifacts"], f"{py_rel} creates artifact", f"{py_rel} missing artifact", failures)
        check(state["audit_log"], f"{py_rel} creates audit log", f"{py_rel} missing audit log", failures)


def validate_consistency(failures: list[str]) -> None:
    schema_readme = read("schemas/README.md")
    changelog = read("CHANGELOG.md")
    combined = "\n".join(read(rel) for rel in DOCS + ["workspace/README.md"])
    code = "\n".join(read(rel) for rel in CORE if rel.endswith(".py"))
    check("schemas/workspace/" in schema_readme and "workspace.schema.json" in schema_readme, "schemas/README documents workspace schemas", "schemas/README missing workspace schemas", failures)
    check("FEATURE-007" in changelog and "AI Research Workspace" in changelog, "CHANGELOG documents FEATURE-007", "CHANGELOG missing FEATURE-007", failures)
    check("Workspace 不直接" in combined or "不绕过 Runtime" in combined, "workspace states runtime boundary", "workspace missing runtime boundary", failures)
    for token in ["from skills", "import skills", "from evidence", "import evidence", "from methodology", "import methodology"]:
        check(token not in code, f"workspace avoids direct business import {token}", f"workspace directly imports business module {token}", failures)


def validate_regression_scripts(failures: list[str]) -> None:
    scripts = [ROOT / rel for rel in REGRESSION_SCRIPTS]
    check(len(scripts) + 1 == 16, "current run plus 15 regression scripts covers 16 validate_* scripts", "validate script count is not 16", failures)
    for script in scripts:
        result = subprocess.run([sys.executable, str(script)], cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False)
        ok = result.returncode == 0 and ("RESULT: PASS" in result.stdout or "最终结果: PASS" in result.stdout)
        check(ok, f"{script.name} PASS", f"{script.name} FAIL\n{result.stdout}", failures)


def main() -> int:
    failures: list[str] = []
    print("AIRS FEATURE-007 AI Research Workspace Validation")
    print("=================================================")
    validate_static(failures)
    validate_examples(failures)
    validate_consistency(failures)
    validate_regression_scripts(failures)
    print("=================================================")
    if failures:
        print("RESULT: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("RESULT: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
