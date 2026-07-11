"""Pipeline entrypoint for AIRS Research Report Generator."""

from __future__ import annotations

from typing import Any

from .composer import ReportComposer
from .model import DISCLAIMER, REQUIRED_SECTION_TITLES, ResearchReport


class ReportPipeline:
    """Normalize M1-M6/FEATURE-002 inputs and render a report."""

    required_payload_fields = {
        "report_id",
        "title",
        "research_question",
        "methodology_refs",
        "evidence_cards",
        "knowledge_graph",
        "scorecard",
    }

    def __init__(self) -> None:
        self.composer = ReportComposer()

    def run(self, payload: dict[str, Any]) -> ResearchReport:
        normalized = self._normalize(payload)
        self._validate(normalized)
        return self.composer.compose(normalized)

    def render_markdown(self, payload: dict[str, Any]) -> str:
        return self.run(payload).to_markdown()

    def _normalize(self, payload: dict[str, Any]) -> dict[str, Any]:
        normalized = dict(payload)
        graph = dict(normalized["knowledge_graph"])
        graph_cards = dict(graph.get("evidence_cards", {}))
        cards = dict(normalized.get("evidence_cards") or graph_cards)
        normalized["evidence_cards"] = cards
        normalized.setdefault("methodology_refs", graph.get("methodology_refs", []))
        normalized.setdefault("prompt_ref", "prompts/report/generation.md")
        normalized.setdefault("skill_ref", "skills/report/report-skill.md")
        normalized.setdefault("disclaimer", DISCLAIMER)
        normalized.setdefault("version", "1.0.0")
        return normalized

    def _validate(self, payload: dict[str, Any]) -> None:
        missing = sorted(self.required_payload_fields - set(payload))
        if missing:
            raise ValueError(f"missing report payload fields: {', '.join(missing)}")
        if "不构成投资建议" not in payload.get("disclaimer", ""):
            raise ValueError("report disclaimer must state 不构成投资建议")
        if len(payload["evidence_cards"]) < 2:
            raise ValueError("report requires at least two Evidence Cards")
        if not payload["methodology_refs"]:
            raise ValueError("report requires M2 methodology_refs")
        graph_refs = set(payload["knowledge_graph"].get("evidence_cards", {}))
        card_refs = set(payload["evidence_cards"])
        if graph_refs and not graph_refs.issubset(card_refs):
            raise ValueError("report evidence_cards must include Knowledge Graph evidence_cards")
        score_refs = set(payload["scorecard"].get("evidence_chain_refs", []))
        if score_refs and not score_refs.issubset(card_refs):
            raise ValueError("scorecard evidence_chain_refs must exist in evidence_cards")
        if payload["scorecard"].get("quality_gate") not in {"PASS", "CONDITIONAL_PASS", "FAIL"}:
            raise ValueError("scorecard quality_gate is invalid")
        if payload["scorecard"].get("disclaimer") != "仅供研究参考，不构成投资建议":
            raise ValueError("scorecard disclaimer must match M6 schema")

    @staticmethod
    def required_sections() -> list[str]:
        return list(REQUIRED_SECTION_TITLES)
