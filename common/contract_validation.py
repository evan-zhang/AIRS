"""Cross-module contract validation for AIRS research artifacts."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


DISCLAIMER = "AIRS 契约校验仅用于研究质量控制，不构成投资建议。"


@dataclass
class ContractValidationResult:
    passed: bool
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "passed": self.passed,
            "errors": self.errors,
            "warnings": self.warnings,
            "disclaimer": DISCLAIMER,
        }


def validate_research_contract(analysis: dict[str, Any], report: dict[str, Any]) -> ContractValidationResult:
    errors: list[str] = []
    warnings: list[str] = []
    evidence_chain = analysis.get("evidence_chain", {})
    evidence_cards = evidence_chain.get("evidence_cards", {})
    knowledge_graph = analysis.get("knowledge_graph", {})
    score_card = analysis.get("score_card", {})

    if not evidence_cards:
        errors.append("evidence_chain.evidence_cards is empty")
    kg_cards = knowledge_graph.get("evidence_cards", {})
    if kg_cards and not set(kg_cards).issubset(set(evidence_cards)):
        errors.append("knowledge_graph evidence cards are not a subset of evidence_chain cards")
    for node in knowledge_graph.get("nodes", []):
        missing = set(node.get("evidence_refs", [])) - set(evidence_cards)
        if missing:
            errors.append(f"knowledge_graph node {node.get('node_id')} references missing evidence: {sorted(missing)}")
    for edge in knowledge_graph.get("edges", []):
        missing = set(edge.get("evidence_refs", [])) - set(evidence_cards)
        if missing:
            errors.append(f"knowledge_graph edge {edge.get('edge_id')} references missing evidence: {sorted(missing)}")
    score_refs = set(score_card.get("evidence_chain_refs", []))
    if score_refs and not score_refs.issubset(set(evidence_cards)):
        errors.append("score_card evidence_chain_refs contain missing evidence ids")
    if score_card.get("quality_gate") not in {"PASS", "CONDITIONAL_PASS", "FAIL"}:
        errors.append("score_card.quality_gate is invalid")
    if "report_generator_output" in report and str(report["report_generator_output"]).startswith("SKIP"):
        errors.append("report_generator_output is a SKIP fallback")
    if len(report.get("sections", [])) != 15:
        errors.append("APP-001 report must contain 15 sections")
    if report.get("report_quality_gate") == "FAILED":
        errors.append("report quality gate failed")

    for evidence_id, card in evidence_cards.items():
        mode = str(card.get("traceability", {}).get("mode") or card.get("data_mode") or "").lower()
        statement_type = card.get("statement_type")
        if mode in {"mock", "skip"} and statement_type == "Fact":
            errors.append(f"{evidence_id} marks mock/skip evidence as Fact")
        if mode in {"mock", "skip", "mock_or_static"}:
            warnings.append(f"{evidence_id} is degraded evidence: {mode}")

    return ContractValidationResult(passed=not errors, errors=errors, warnings=warnings)


def summarize_data_lineage(connector_results: list[dict[str, Any]]) -> dict[str, Any]:
    real_sources: list[str] = []
    mock_sources: list[str] = []
    skipped_sources: list[str] = []
    fallback_sources: list[str] = []
    unknown_sources: list[str] = []
    for result in connector_results:
        connector_id = str(result.get("connector_id", "unknown"))
        mode = str(result.get("data", {}).get("mode") or result.get("traceability", {}).get("mode") or "unknown").lower()
        if mode == "real":
            real_sources.append(connector_id)
        elif mode.startswith("mock"):
            mock_sources.append(connector_id)
        elif mode.startswith("skip"):
            skipped_sources.append(connector_id)
        elif "fallback" in mode:
            fallback_sources.append(connector_id)
        else:
            unknown_sources.append(connector_id)
    degraded_sources = sorted(set(mock_sources + skipped_sources + fallback_sources + unknown_sources))
    return {
        "real_sources": sorted(set(real_sources)),
        "mock_sources": sorted(set(mock_sources)),
        "skipped_sources": sorted(set(skipped_sources)),
        "fallback_sources": sorted(set(fallback_sources)),
        "unknown_sources": sorted(set(unknown_sources)),
        "degraded_sources": degraded_sources,
        "real_source_count": len(set(real_sources)),
        "degraded_source_count": len(degraded_sources),
        "disclaimer": DISCLAIMER,
    }


def classify_research_status(validation: ContractValidationResult, lineage: dict[str, Any], *, require_real_data: bool = False) -> str:
    if not validation.passed:
        return "failed_quality_gate"
    degraded = bool(lineage.get("mock_sources") or lineage.get("skipped_sources") or lineage.get("fallback_sources"))
    if require_real_data and degraded:
        return "failed_quality_gate"
    if degraded:
        return "completed_with_degradation"
    return "completed"
