#!/usr/bin/env python3
"""Validate AIRS FEATURE-003 Research Report Generator deliverables."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOCS = [
    "docs/report-generator/report-generator-architecture.md",
    "docs/report-generator/report-generator-workflow.md",
    "docs/report-generator/report-generator-pipeline.md",
]

PYTHON_FILES = [
    "report_generator/__init__.py",
    "report_generator/model.py",
    "report_generator/evidence_citation.py",
    "report_generator/kg_summary.py",
    "report_generator/score_summary.py",
    "report_generator/composer.py",
    "report_generator/pipeline.py",
]

SCHEMAS = [
    "schemas/report/report.schema.json",
]

TEMPLATES = [
    "templates/report/research-report-template.md",
    "templates/builder/feature-request-research-report-generator.yaml",
]

BUILDER_PACKAGE = [
    "builder-output/research-report-generator/ISSUE.md",
    "builder-output/research-report-generator/ADR.md",
    "builder-output/research-report-generator/FEATURE_SPEC.md",
    "builder-output/research-report-generator/skill/research-report-generator-skill.md",
    "builder-output/research-report-generator/prompt/research-report-generator-prompt.md",
    "builder-output/research-report-generator/schema/research-report-generator.schema.json",
    "builder-output/research-report-generator/tests/test-research-report-generator.md",
    "builder-output/research-report-generator/benchmark/research-report-generator-benchmark.md",
    "builder-output/research-report-generator/PR_CHECKLIST.md",
    "builder-output/research-report-generator/RELEASE_NOTES.md",
]

EXAMPLES = [
    "examples/reports/ai-compute-industry-research-report.md",
    "examples/reports/innovative-drug-industry-research-report.md",
]

EXAMPLE_ARTIFACTS = [
    "examples/reports/ai-compute-industry-research-report.json",
    "examples/reports/innovative-drug-industry-research-report.json",
]

REPORTS = [
    "docs/production/FEATURE_003_COMPLETION_REPORT.md",
    "docs/review/FEATURE_003_SELF_REVIEW.md",
]

REQUIRED_SECTIONS = [
    "报告元数据",
    "研究问题与范围",
    "方法论引用",
    "核心观点",
    "Evidence 引用表",
    "Evidence Chain 汇总",
    "Knowledge Graph 汇总",
    "Score Summary",
    "反方观点",
    "不确定性与缺口",
    "风险提示",
    "免责声明",
]

REQUIRED_SOURCE_REFS = [
    "M2_methodology",
    "M3_evidence",
    "FEATURE_002_knowledge_graph",
    "M4_prompt",
    "M5_skill",
    "M6_score_eval",
]

FORBIDDEN = ["建议买入", "建议卖出", "保证收益", "保证盈利", "目标价为", "应买入", "应卖出", "自动交易指令"]


def read_text(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def check(condition: bool, ok: str, fail: str, failures: list[str]) -> None:
    if condition:
        print(f"PASS: {ok}")
    else:
        print(f"FAIL: {fail}")
        failures.append(fail)


def validate_text_file(rel: str, failures: list[str], min_size: int = 200, require_disclaimer: bool = True) -> str:
    path = ROOT / rel
    check(path.exists(), f"{rel} exists", f"missing {rel}", failures)
    if not path.exists():
        return ""
    text = read_text(rel)
    check(len(text) >= min_size, f"{rel} has substantive content", f"{rel} content too thin", failures)
    if require_disclaimer:
        check("免责声明" in text and "不构成投资建议" in text, f"{rel} has disclaimer", f"{rel} missing disclaimer", failures)
    for forbidden in FORBIDDEN:
        check(forbidden not in text, f"{rel} avoids forbidden expression: {forbidden}", f"{rel} contains forbidden expression: {forbidden}", failures)
    return text


def validate_json_file(rel: str, failures: list[str]) -> dict:
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


def validate_static_files(failures: list[str]) -> None:
    for rel in DOCS:
        text = validate_text_file(rel, failures, min_size=650)
        for term in ["M2", "M3", "FEATURE-002", "M4", "M5", "M6"]:
            check(term in text, f"{rel} references {term}", f"{rel} missing {term}", failures)
    for rel in PYTHON_FILES:
        path = ROOT / rel
        check(path.exists(), f"{rel} exists", f"missing {rel}", failures)
        if path.exists():
            text = read_text(rel)
            check("Report" in text or "Evidence" in text or "Score" in text or "KG" in text, f"{rel} contains report generator logic", f"{rel} missing report generator logic", failures)
    for rel in SCHEMAS:
        schema = validate_json_file(rel, failures)
        serialized = json.dumps(schema, ensure_ascii=False)
        for term in ["methodology_refs", "evidence_cards", "knowledge_graph_summary", "score_summary", "sections", "source_refs", "不构成投资建议"]:
            check(term in serialized, f"{rel} contains {term}", f"{rel} missing {term}", failures)
    for rel in TEMPLATES:
        validate_text_file(rel, failures, min_size=180, require_disclaimer=rel.endswith(".md"))
    for rel in BUILDER_PACKAGE:
        if rel.endswith(".json"):
            validate_json_file(rel, failures)
        else:
            validate_text_file(rel, failures, min_size=220)
    for rel in REPORTS:
        validate_text_file(rel, failures, min_size=500)


def validate_examples(failures: list[str]) -> None:
    for rel in EXAMPLES:
        text = validate_text_file(rel, failures, min_size=2000)
        for index, section in enumerate(REQUIRED_SECTIONS, start=1):
            check(f"## {index}. {section}" in text, f"{rel} contains section {index}: {section}", f"{rel} missing section {index}: {section}", failures)
        for term in ["Evidence 引用表", "Knowledge Graph 汇总", "Score Summary", "Quality Gate", "Scorecard", "不构成投资建议"]:
            check(term in text, f"{rel} contains {term}", f"{rel} missing {term}", failures)

    for rel in EXAMPLE_ARTIFACTS:
        data = validate_json_file(rel, failures)
        if not data:
            continue
        check(len(data.get("sections", [])) == 12, f"{rel} has exactly 12 sections", f"{rel} does not have exactly 12 sections", failures)
        check("不构成投资建议" in data.get("disclaimer", ""), f"{rel} has disclaimer", f"{rel} missing disclaimer", failures)
        source_refs = data.get("source_refs", {})
        for ref in REQUIRED_SOURCE_REFS:
            check(ref in source_refs and source_refs[ref], f"{rel} has source ref {ref}", f"{rel} missing source ref {ref}", failures)
        evidence_ids = set(data.get("evidence_cards", {}))
        kg_refs = set(data.get("knowledge_graph_summary", {}).get("evidence_refs", []))
        score_refs = set(data.get("score_summary", {}).get("evidence_chain_refs", []))
        check(kg_refs.issubset(evidence_ids), f"{rel} KG evidence refs resolve", f"{rel} has unresolved KG evidence refs", failures)
        check(score_refs.issubset(evidence_ids), f"{rel} Score evidence refs resolve", f"{rel} has unresolved Score evidence refs", failures)
        check(data.get("score_summary", {}).get("quality_gate") in {"PASS", "CONDITIONAL_PASS", "FAIL"}, f"{rel} has valid quality gate", f"{rel} invalid quality gate", failures)


def validate_runtime(failures: list[str]) -> None:
    sys.path.insert(0, str(ROOT))
    from report_generator import ReportPipeline

    kg = validate_json_file("examples/knowledge-graph/ai-compute-supply-chain.json", failures)
    if not kg:
        return
    evidence_ids = list(kg["evidence_cards"])
    payload = {
        "report_id": "REPORT-20260710-RUNTIME-CHECK",
        "title": "运行时校验研究报告",
        "research_question": "运行时校验是否能把 Evidence、KG 和 Score 自动编排进报告？",
        "methodology_refs": kg["methodology_refs"],
        "evidence_cards": kg["evidence_cards"],
        "knowledge_graph": kg,
        "scorecard": {
            "scorecard_id": "SCORECARD-RUNTIME-CHECK",
            "version": "0.1.0",
            "artifact_type": "report",
            "methodology_refs": kg["methodology_refs"],
            "evidence_chain_refs": evidence_ids,
            "scores": [
                {"score_id": "SCORE-RUNTIME", "dimension": "Report Score", "score": 82, "weight": 1.0, "rationale": "运行时结构校验"}
            ],
            "overall_score": 82,
            "overall_grade": "B",
            "confidence_score": 76,
            "quality_gate": "PASS",
            "disclaimer": "仅供研究参考，不构成投资建议",
        },
    }
    report = ReportPipeline().run(payload)
    markdown = report.to_markdown()
    check(len(report.sections) == 12, "ReportPipeline creates 12 sections", "ReportPipeline did not create 12 sections", failures)
    check("Evidence 引用表" in markdown, "runtime markdown contains Evidence citations", "runtime markdown missing Evidence citations", failures)
    check(kg["graph_id"] in markdown, "runtime markdown contains KG ID", "runtime markdown missing KG ID", failures)
    check("SCORECARD-RUNTIME-CHECK" in markdown, "runtime markdown contains Scorecard ID", "runtime markdown missing Scorecard ID", failures)
    check("不构成投资建议" in markdown, "runtime markdown contains disclaimer", "runtime markdown missing disclaimer", failures)


def main() -> int:
    failures: list[str] = []
    print("AIRS FEATURE-003 Research Report Generator Validation")
    print("=====================================================")
    validate_static_files(failures)
    validate_examples(failures)
    validate_runtime(failures)
    print("=====================================================")
    if failures:
        print("RESULT: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("RESULT: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
