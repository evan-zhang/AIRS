#!/usr/bin/env python3
"""Validate AIRS FEATURE-012 Autonomous Learning Engine deliverables."""
from __future__ import annotations

import importlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DOCS = [
    "docs/learning/learning-architecture.md",
    "docs/learning/feedback-loop.md",
    "docs/learning/outcome-tracking.md",
    "docs/learning/pattern-mining.md",
    "docs/learning/rule-generation.md",
    "docs/learning/prompt-evolution.md",
    "docs/learning/methodology-evolution.md",
    "docs/learning/skill-evolution.md",
    "docs/learning/score-optimization.md",
    "docs/learning/continuous-improvement.md",
    "docs/learning/learning-governance.md",
]
CORE = [
    "learning/__init__.py",
    "learning/manager.py",
    "learning/feedback.py",
    "learning/outcome.py",
    "learning/pattern.py",
    "learning/rules.py",
    "learning/prompt_opt.py",
    "learning/methodology_opt.py",
    "learning/skill_opt.py",
    "learning/score_opt.py",
    "learning/consolidation.py",
    "learning/engine.py",
    "learning/README.md",
]
EXAMPLES = [
    ("learning/examples/company_learning.py", "learning/examples/company-learning.md"),
    ("learning/examples/industry_learning.py", "learning/examples/industry-learning.md"),
    ("learning/examples/theme_learning.py", "learning/examples/theme-learning.md"),
    ("learning/examples/supply_chain_learning.py", "learning/examples/supply-chain-learning.md"),
    ("learning/examples/evidence_learning.py", "learning/examples/evidence-learning.md"),
    ("learning/examples/committee_report_learning.py", "learning/examples/committee-report-learning.md"),
]
SCHEMAS = [
    "schemas/learning/learning.schema.json",
    "schemas/learning/feedback.schema.json",
    "schemas/learning/outcome.schema.json",
    "schemas/learning/optimization.schema.json",
]
BUILDER = [
    "builder/requests/feature-request-autonomous-learning-engine.yaml",
    "builder-output/autonomous-learning-engine/ISSUE.md",
    "builder-output/autonomous-learning-engine/ADR.md",
    "builder-output/autonomous-learning-engine/FEATURE_SPEC.md",
    "builder-output/autonomous-learning-engine/skill/autonomous-learning-engine-skill.md",
    "builder-output/autonomous-learning-engine/prompt/autonomous-learning-engine-prompt.md",
    "builder-output/autonomous-learning-engine/schema/autonomous-learning-engine.schema.json",
    "builder-output/autonomous-learning-engine/tests/test-autonomous-learning-engine.md",
    "builder-output/autonomous-learning-engine/benchmark/autonomous-learning-engine-benchmark.md",
    "builder-output/autonomous-learning-engine/PR_CHECKLIST.md",
    "builder-output/autonomous-learning-engine/RELEASE_NOTES.md",
]
REPORTS = [
    "docs/adr/ADR-012-autonomous-learning-engine.md",
    "docs/production/FEATURE_012_COMPLETION_REPORT.md",
    "docs/review/FEATURE_012_SELF_REVIEW.md",
]
REQUIRED_EXAMPLE_KEYS = [
    "feedback",
    "outcomes",
    "patterns",
    "rules",
    "optimizations",
    "governance",
    "memory_consolidation",
]
FORBIDDEN = ["建议买入", "建议卖出", "保证收益", "保证盈利", "目标价为", "应买入", "应卖出", "自动交易指令"]


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
        value = text(rel, failures, 260)
        check(any(term in value for term in ["Learning", "Feedback", "Outcome", "Pattern", "Rule", "Optimizer"]), f"{rel} references learning concepts", f"{rel} missing learning concepts", failures)
    for rel in CORE:
        value = text(rel, failures, 20, disclaimer=rel.endswith(".md"))
        check("class " in value or "def " in value or "DISCLAIMER" in value or rel.endswith("__init__.py") or rel.endswith(".md"), f"{rel} contains learning logic", f"{rel} missing learning logic", failures)
    for rel in SCHEMAS:
        json_file(rel, failures)
    for rel in BUILDER + REPORTS:
        if rel.endswith(".json"):
            json_file(rel, failures)
        else:
            text(rel, failures, 120, disclaimer=not rel.endswith(".yaml"))
    schema_readme = read("schemas/README.md")
    changelog = read("CHANGELOG.md")
    check("schemas/learning/" in schema_readme and "learning.schema.json" in schema_readme, "schemas/README documents learning schemas", "schemas/README missing learning schemas", failures)
    check("FEATURE-012" in changelog and "Autonomous Learning Engine" in changelog, "CHANGELOG documents FEATURE-012", "CHANGELOG missing FEATURE-012", failures)


def validate_examples(failures: list[str]) -> None:
    sys.path.insert(0, str(ROOT))
    check((ROOT / "learning/examples/__init__.py").exists(), "learning examples package exists", "missing learning examples __init__.py", failures)
    for py_rel, md_rel in EXAMPLES:
        text(py_rel, failures, 50, disclaimer=False)
        markdown = text(md_rel, failures, 360)
        for section in ["Feedback Input", "Pattern Mining", "Rule Generation", "Optimization Suggestions"]:
            check(section in markdown, f"{md_rel} contains {section}", f"{md_rel} missing {section}", failures)
        module = importlib.import_module(py_rel[:-3].replace("/", "."))
        result = module.run()
        blob = json.dumps(result, ensure_ascii=False)
        for key in REQUIRED_EXAMPLE_KEYS:
            check(key in result, f"{py_rel} outputs {key}", f"{py_rel} missing {key}", failures)
        check(result["governance"]["auto_apply"] is False, f"{py_rel} does not auto apply", f"{py_rel} auto applies changes", failures)
        check(result["rules"], f"{py_rel} generates rules", f"{py_rel} missing rules", failures)
        check(result["optimizations"], f"{py_rel} generates optimizations", f"{py_rel} missing optimizations", failures)
        check("不构成投资建议" in blob, f"{py_rel} carries disclaimer", f"{py_rel} missing disclaimer", failures)


def validate_consistency(failures: list[str]) -> None:
    combined = "\n".join(read(rel) for rel in DOCS + ["learning/manager.py", "learning/README.md"])
    for ref in [
        "docs/runtime/memory-manager.md",
        "docs/committee/committee-architecture.md",
        "docs/investment-engine/engine-architecture.md",
        "schemas/report/report.schema.json",
    ]:
        check(ref in combined or ref in read("builder/requests/feature-request-autonomous-learning-engine.yaml"), f"Learning references {ref}", f"Learning missing {ref}", failures)
    code = "\n".join(read(rel) for rel in CORE if rel.endswith(".py"))
    for token in ["requests.", "urllib", "http.client", "yfinance", "longbridge"]:
        check(token not in code, f"learning avoids direct data access {token}", f"learning directly accesses data via {token}", failures)
    check("auto_apply" in code and "False" in code, "learning proposals are not auto applied", "learning auto apply guard missing", failures)


def validate_regressions(failures: list[str]) -> None:
    scripts = sorted(p for p in (ROOT / "scripts").glob("validate_*.py") if p.name != "validate_learning.py")
    all_scripts = sorted((ROOT / "scripts").glob("validate_*.py"))
    expected_script_count = 23
    check(len(all_scripts) == expected_script_count, f"found all {expected_script_count} validate_* scripts including validate_learning.py", f"expected {expected_script_count} validate_* scripts, found {len(all_scripts)}", failures)
    check((ROOT / "scripts" / "validate_e2e.py").exists(), "validate_e2e.py is included in regression validation", "validate_e2e.py missing from regression validation", failures)
    for script in scripts:
        result = subprocess.run([sys.executable, str(script)], cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False)
        ok = result.returncode == 0 and ("RESULT: PASS" in result.stdout or "最终结果: PASS" in result.stdout or "FINAL RESULT: PASS" in result.stdout)
        check(ok, f"{script.name} PASS", f"{script.name} FAIL\n{result.stdout}", failures)


def main() -> int:
    failures: list[str] = []
    print("AIRS FEATURE-012 Autonomous Learning Engine Validation")
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
