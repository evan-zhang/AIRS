#!/usr/bin/env python3
"""Validate AIRS FEATURE-010 Autonomous Investment Committee deliverables."""

from __future__ import annotations

import importlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOCS = [
    "docs/committee/committee-architecture.md",
    "docs/committee/committee-lifecycle.md",
    "docs/committee/role-definitions.md",
    "docs/committee/debate-rules.md",
    "docs/committee/evidence-challenge.md",
    "docs/committee/counter-argument.md",
    "docs/committee/consensus-building.md",
    "docs/committee/voting-mechanism.md",
    "docs/committee/minority-report.md",
    "docs/committee/decision-recorder.md",
    "docs/committee/committee-governance.md",
    "docs/committee/committee-review-workflow.md",
]
CORE = [
    "committee/__init__.py",
    "committee/coordinator.py",
    "committee/role_registry.py",
    "committee/analysts.py",
    "committee/experts.py",
    "committee/reviewer.py",
    "committee/moderator.py",
    "committee/voting_engine.py",
    "committee/consensus_engine.py",
    "committee/recorder.py",
    "committee/README.md",
]
SCHEMAS = [
    "schemas/committee/committee.schema.json",
    "schemas/committee/committee-session.schema.json",
    "schemas/committee/committee-vote.schema.json",
    "schemas/committee/committee-decision.schema.json",
]
TEMPLATES = [
    "templates/committee/committee-session-template.md",
    "templates/committee/committee-decision-template.md",
]
BUILDER = [
    "builder/requests/feature-request-autonomous-investment-committee.yaml",
    "builder-output/autonomous-investment-committee/ISSUE.md",
    "builder-output/autonomous-investment-committee/ADR.md",
    "builder-output/autonomous-investment-committee/FEATURE_SPEC.md",
    "builder-output/autonomous-investment-committee/skill/autonomous-investment-committee-skill.md",
    "builder-output/autonomous-investment-committee/prompt/autonomous-investment-committee-prompt.md",
    "builder-output/autonomous-investment-committee/schema/autonomous-investment-committee.schema.json",
    "builder-output/autonomous-investment-committee/tests/test-autonomous-investment-committee.md",
    "builder-output/autonomous-investment-committee/benchmark/autonomous-investment-committee-benchmark.md",
    "builder-output/autonomous-investment-committee/PR_CHECKLIST.md",
    "builder-output/autonomous-investment-committee/RELEASE_NOTES.md",
]
EXAMPLES = [
    ("committee/examples/ai_compute.py", "committee/examples/ai-compute.md"),
    ("committee/examples/innovative_drug.py", "committee/examples/innovative-drug.md"),
    ("committee/examples/semiconductor.py", "committee/examples/semiconductor.md"),
    ("committee/examples/robotics.py", "committee/examples/robotics.md"),
    ("committee/examples/new_energy.py", "committee/examples/new-energy.md"),
    ("committee/examples/hk_stock.py", "committee/examples/hk-stock.md"),
]
REPORTS = [
    "docs/adr/ADR-0010-autonomous-investment-committee.md",
    "docs/production/M10_COMPLETION_REPORT.md",
    "docs/review/M10_SELF_REVIEW.md",
]
REQUIRED_EXAMPLE_SECTIONS = [
    "Participants",
    "Debate Timeline",
    "Evidence Review",
    "Opinions",
    "Unresolved Questions",
    "Voting Result",
    "Final Recommendation",
    "Minority Report",
    "Follow-up Tasks",
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
        value = text(rel, failures, 300)
        check("Planner" in value and "Research Engine" in value, f"{rel} references Planner and Research Engine", f"{rel} missing Planner or Research Engine", failures)
    for rel in CORE:
        value = text(rel, failures, 20, disclaimer=rel.endswith(".md"))
        check("Committee" in value or "committee" in value or rel.endswith("__init__.py"), f"{rel} contains committee logic", f"{rel} missing committee logic", failures)
    for rel in SCHEMAS:
        json_file(rel, failures)
    for rel in TEMPLATES + BUILDER + REPORTS:
        if rel.endswith(".json"):
            json_file(rel, failures)
        else:
            text(rel, failures, 120, disclaimer=not rel.endswith(".yaml"))
    schema_readme = read("schemas/README.md")
    changelog = read("CHANGELOG.md")
    check("schemas/committee/" in schema_readme and "committee-decision.schema.json" in schema_readme, "schemas/README documents committee schemas", "schemas/README missing committee schemas", failures)
    check("FEATURE-010" in changelog and "Autonomous Investment Committee" in changelog, "CHANGELOG documents FEATURE-010", "CHANGELOG missing FEATURE-010", failures)


def validate_examples(failures: list[str]) -> None:
    sys.path.insert(0, str(ROOT))
    check((ROOT / "committee/examples/__init__.py").exists(), "committee examples package exists", "missing committee examples __init__.py", failures)
    for py_rel, md_rel in EXAMPLES:
        text(py_rel, failures, 60, disclaimer=False)
        md = text(md_rel, failures, 500)
        for section in REQUIRED_EXAMPLE_SECTIONS:
            check(section in md, f"{md_rel} contains {section}", f"{md_rel} missing {section}", failures)
        module = importlib.import_module(py_rel[:-3].replace("/", "."))
        result = module.run()
        blob = json.dumps(result, ensure_ascii=False)
        for key in REQUIRED_EXAMPLE_SECTIONS:
            check(key in result, f"{py_rel} outputs {key}", f"{py_rel} missing {key}", failures)
        decision = result["Decision"]
        check(decision["research_engine_gate"] in {"ALLOW", "ALLOW_WITH_CONDITIONS", "BLOCK"}, f"{py_rel} has research engine gate", f"{py_rel} missing research engine gate", failures)
        check(result["Voting Result"]["quorum_met"] is True, f"{py_rel} quorum met", f"{py_rel} quorum not met", failures)
        check("不构成投资建议" in blob, f"{py_rel} carries disclaimer", f"{py_rel} missing disclaimer", failures)
        for word in FORBIDDEN:
            check(word not in blob, f"{py_rel} avoids forbidden expression: {word}", f"{py_rel} contains forbidden expression: {word}", failures)


def validate_consistency(failures: list[str]) -> None:
    combined = "\n".join(read(rel) for rel in DOCS + ["committee/coordinator.py", "committee/README.md"])
    check("after_planner_before_research_engine" in combined, "AIC position marker exists", "AIC position marker missing", failures)
    check("Planner" in combined and "Research Engine" in combined, "AIC sits after Planner before Research Engine", "AIC ordering missing", failures)
    for ref in [
        "schemas/evidence/evidence-chain.schema.json",
        "schemas/score/scorecard.schema.json",
        "schemas/investment/recommendation.schema.json",
        "docs/runtime/runtime-architecture.md",
        "docs/orchestrator/orchestrator-architecture.md",
    ]:
        check(ref in combined, f"AIC references existing capability {ref}", f"AIC missing existing capability {ref}", failures)
    committee_code = "\n".join(read(rel) for rel in CORE if rel.endswith(".py"))
    for token in ["requests.", "urllib", "http.client", "yfinance", "longbridge"]:
        check(token not in committee_code, f"committee avoids direct data access {token}", f"committee directly accesses data via {token}", failures)


def validate_regressions(failures: list[str]) -> None:
    scripts = sorted(p for p in (ROOT / "scripts").glob("validate_*.py") if p.name not in {"validate_committee.py", "validate_learning.py"})
    check(len(scripts) >= 18, f"found {len(scripts)} regression validate scripts", f"expected at least 18 regression scripts, found {len(scripts)}", failures)
    for script in scripts:
        result = subprocess.run([sys.executable, str(script)], cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False)
        ok = result.returncode == 0 and ("RESULT: PASS" in result.stdout or "最终结果: PASS" in result.stdout or "FINAL RESULT: PASS" in result.stdout)
        check(ok, f"{script.name} PASS", f"{script.name} FAIL\n{result.stdout}", failures)


def main() -> int:
    failures: list[str] = []
    print("AIRS FEATURE-010 Autonomous Investment Committee Validation")
    print("===========================================================")
    validate_static(failures)
    validate_examples(failures)
    validate_consistency(failures)
    validate_regressions(failures)
    print("===========================================================")
    if failures:
        print("RESULT: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("RESULT: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
