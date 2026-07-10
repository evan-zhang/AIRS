#!/usr/bin/env python3
"""Validate AIRS FEATURE-002 Knowledge Graph Engine deliverables."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOCS = [
    "docs/knowledge-graph/knowledge-graph-architecture.md",
    "docs/knowledge-graph/knowledge-graph-workflow.md",
]

PYTHON_FILES = [
    "knowledge_graph/__init__.py",
    "knowledge_graph/model.py",
    "knowledge_graph/builder.py",
    "knowledge_graph/validator.py",
    "knowledge_graph/path_analyzer.py",
    "knowledge_graph/chokepoint_analyzer.py",
]

SCHEMAS = [
    "schemas/knowledge-graph/knowledge-graph.schema.json",
]

TEMPLATES = [
    "templates/knowledge-graph/knowledge-graph-template.md",
    "templates/knowledge-graph/chokepoint-analysis-template.md",
    "templates/builder/feature-request-knowledge-graph-engine.yaml",
]

EXAMPLES = [
    "examples/knowledge-graph/ai-compute-supply-chain.json",
    "examples/knowledge-graph/innovative-drug-industry-chain.json",
]

BUILDER_PACKAGE = [
    "builder-output/knowledge-graph-engine/ISSUE.md",
    "builder-output/knowledge-graph-engine/ADR.md",
    "builder-output/knowledge-graph-engine/FEATURE_SPEC.md",
    "builder-output/knowledge-graph-engine/skill/knowledge-graph-engine-skill.md",
    "builder-output/knowledge-graph-engine/prompt/knowledge-graph-engine-prompt.md",
    "builder-output/knowledge-graph-engine/schema/knowledge-graph-engine.schema.json",
    "builder-output/knowledge-graph-engine/tests/test-knowledge-graph-engine.md",
    "builder-output/knowledge-graph-engine/benchmark/knowledge-graph-engine-benchmark.md",
    "builder-output/knowledge-graph-engine/PR_CHECKLIST.md",
    "builder-output/knowledge-graph-engine/RELEASE_NOTES.md",
]

REPORTS = [
    "docs/production/FEATURE_002_COMPLETION_REPORT.md",
    "docs/review/FEATURE_002_SELF_REVIEW.md",
]

REQUIRED_EVIDENCE_FIELDS = [
    "evidence_id",
    "title",
    "category",
    "source",
    "source_type",
    "url",
    "publication_time",
    "collection_time",
    "confidence",
    "evidence_level",
    "supports",
    "refutes",
    "missing_evidence",
    "weight",
    "traceability",
    "version",
]

FORBIDDEN = ["建议买入", "建议卖出", "保证收益", "保证盈利", "目标价为", "应买入", "应卖出"]


def read_text(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def check(condition: bool, ok: str, fail: str, failures: list[str]) -> None:
    if condition:
        print(f"PASS: {ok}")
    else:
        print(f"FAIL: {fail}")
        failures.append(fail)


def validate_text_file(rel: str, failures: list[str], min_size: int = 200, require_disclaimer: bool = True) -> None:
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
        validate_text_file(rel, failures, min_size=700)
    for rel in PYTHON_FILES:
        path = ROOT / rel
        check(path.exists(), f"{rel} exists", f"missing {rel}", failures)
        if path.exists():
            text = read_text(rel)
            check("KnowledgeGraph" in text or "Chokepoint" in text or rel.endswith("__init__.py"), f"{rel} contains graph engine logic", f"{rel} missing graph engine logic", failures)
    for rel in SCHEMAS:
        schema = validate_json_file(rel, failures)
        serialized = json.dumps(schema, ensure_ascii=False)
        for term in ["node_type", "relation_type", "evidence_refs", "path_analysis", "chokepoint_analysis", "不构成投资建议"]:
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


def validate_graph_examples(failures: list[str]) -> None:
    sys.path.insert(0, str(ROOT))
    from knowledge_graph import ChokepointAnalyzer, KnowledgeGraphBuilder, KnowledgeGraphValidator, PathAnalyzer

    for rel in EXAMPLES:
        data = validate_json_file(rel, failures)
        if not data:
            continue
        graph = KnowledgeGraphBuilder.from_dict(data).build()
        result = KnowledgeGraphValidator().validate(graph)
        check(result.passed, f"{rel} passes KnowledgeGraphValidator", f"{rel} validator errors: {result.errors}", failures)

        check(len(graph.nodes) >= 5, f"{rel} has enough nodes", f"{rel} has too few nodes", failures)
        check(len(graph.edges) >= 4, f"{rel} has enough edges", f"{rel} has too few edges", failures)
        check(bool(graph.path_analysis), f"{rel} has path analysis", f"{rel} missing path analysis", failures)
        check(bool(graph.chokepoint_analysis), f"{rel} has chokepoint analysis", f"{rel} missing chokepoint analysis", failures)
        check("不构成投资建议" in graph.disclaimer, f"{rel} has disclaimer", f"{rel} missing disclaimer", failures)

        for evidence_id, card in graph.evidence_cards.items():
            for field in REQUIRED_EVIDENCE_FIELDS:
                check(field in card, f"{rel} evidence {evidence_id} has {field}", f"{rel} evidence {evidence_id} missing {field}", failures)
            check(card["supports"], f"{rel} evidence {evidence_id} has supports", f"{rel} evidence {evidence_id} missing supports", failures)
            check(card["refutes"], f"{rel} evidence {evidence_id} has refutes", f"{rel} evidence {evidence_id} missing refutes", failures)
            check(card["missing_evidence"], f"{rel} evidence {evidence_id} has missing evidence", f"{rel} evidence {evidence_id} missing missing_evidence", failures)

        first_path = graph.path_analysis[0]
        recomputed_paths = PathAnalyzer().find_paths(graph, first_path["node_path"][0], first_path["node_path"][-1], max_depth=6)
        check(bool(recomputed_paths), f"{rel} path analyzer recomputes path", f"{rel} path analyzer found no path", failures)
        if recomputed_paths:
            check(
                set(first_path["edge_path"]) == set(recomputed_paths[0]["edge_path"]),
                f"{rel} stored path matches analyzer",
                f"{rel} stored path differs from analyzer",
                failures,
            )

        recomputed_chokepoints = ChokepointAnalyzer().analyze(graph, top_n=1)
        check(bool(recomputed_chokepoints), f"{rel} chokepoint analyzer returns result", f"{rel} chokepoint analyzer empty", failures)
        if recomputed_chokepoints:
            stored = graph.chokepoint_analysis[0]
            recomputed = recomputed_chokepoints[0]
            check(stored["node_id"] == recomputed["node_id"], f"{rel} top chokepoint node matches", f"{rel} top chokepoint node mismatch", failures)
            check(
                abs(float(stored["chokepoint_score"]) - float(recomputed["chokepoint_score"])) < 0.0001,
                f"{rel} top chokepoint score matches",
                f"{rel} top chokepoint score mismatch",
                failures,
            )
            check(stored["counter_evidence_refs"] is not None, f"{rel} chokepoint has counter evidence field", f"{rel} chokepoint missing counter evidence field", failures)
            check(stored["missing_evidence"], f"{rel} chokepoint has missing evidence", f"{rel} chokepoint missing missing evidence", failures)


def main() -> int:
    failures: list[str] = []
    print("AIRS FEATURE-002 Knowledge Graph Engine Validation")
    print("==================================================")
    validate_static_files(failures)
    validate_graph_examples(failures)
    print("==================================================")
    if failures:
        print("RESULT: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("RESULT: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
