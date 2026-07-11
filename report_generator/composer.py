"""Section composer for AIRS research reports."""

from __future__ import annotations

from typing import Any

from .evidence_citation import EvidenceCitationBuilder
from .kg_summary import KGSummaryBuilder
from .model import DISCLAIMER, REQUIRED_SECTION_TITLES, ReportSection, ResearchReport
from .score_summary import ScoreSummaryBuilder


class SectionComposer:
    """Compose the 12 mandatory report sections."""

    def __init__(self, payload: dict[str, Any]) -> None:
        self.payload = payload
        self.evidence_cards = dict(payload["evidence_cards"])
        self.citation = EvidenceCitationBuilder(self.evidence_cards)
        self.kg_builder = KGSummaryBuilder(dict(payload["knowledge_graph"]))
        self.score_builder = ScoreSummaryBuilder(dict(payload["scorecard"]))
        self.kg_summary = self.kg_builder.build()
        self.score_summary = self.score_builder.build()

    def compose(self) -> list[ReportSection]:
        methodology_refs = list(self.payload.get("methodology_refs", []))
        evidence_ids = list(self.evidence_cards)
        kg_refs = [str(self.kg_summary.get("graph_id"))]
        score_refs = [str(self.score_summary.get("scorecard_id"))]
        top = self.kg_summary.get("top_chokepoint") or {}
        missing_items = self.citation.missing_evidence_summary()
        counterpoints = self.payload.get("counterarguments") or self._default_counterarguments()
        risks = self.payload.get("risks") or self._default_risks()

        return [
            ReportSection("metadata", REQUIRED_SECTION_TITLES[0], self._metadata_body(), evidence_ids, kg_refs, score_refs),
            ReportSection("scope", REQUIRED_SECTION_TITLES[1], self.payload["research_question"], [], [], []),
            ReportSection(
                "methodology",
                REQUIRED_SECTION_TITLES[2],
                "\n".join(f"- `{item}`：沿用 M2 方法论，不在报告层重写研究规则。" for item in methodology_refs),
                [],
                [],
                [],
            ),
            ReportSection(
                "thesis",
                REQUIRED_SECTION_TITLES[3],
                self._thesis_body(top),
                evidence_ids[:3],
                kg_refs,
                score_refs,
            ),
            ReportSection("evidence-citations", REQUIRED_SECTION_TITLES[4], self.citation.citation_table(), evidence_ids, [], []),
            ReportSection("evidence-chain", REQUIRED_SECTION_TITLES[5], self._evidence_chain_body(), evidence_ids, [], score_refs),
            ReportSection("kg-summary", REQUIRED_SECTION_TITLES[6], self.kg_builder.to_markdown(), self.kg_summary["evidence_refs"], kg_refs, []),
            ReportSection("score-summary", REQUIRED_SECTION_TITLES[7], self.score_builder.to_markdown(), self.score_summary["evidence_chain_refs"], [], score_refs),
            ReportSection("counterarguments", REQUIRED_SECTION_TITLES[8], "\n".join(f"- {item}" for item in counterpoints), evidence_ids, kg_refs, []),
            ReportSection("uncertainty", REQUIRED_SECTION_TITLES[9], "\n".join(f"- {item}" for item in missing_items), evidence_ids, kg_refs, score_refs),
            ReportSection("risks", REQUIRED_SECTION_TITLES[10], "\n".join(f"- {item}" for item in risks), evidence_ids, kg_refs, []),
            ReportSection("disclaimer", REQUIRED_SECTION_TITLES[11], DISCLAIMER, [], [], []),
        ]

    def _metadata_body(self) -> str:
        return "\n".join(
            [
                f"- Report ID：`{self.payload['report_id']}`",
                f"- 研究主题：{self.payload['title']}",
                f"- Prompt 引用：`{self.payload.get('prompt_ref', 'prompts/report/generation.md')}`",
                f"- Skill 引用：`{self.payload.get('skill_ref', 'skills/report/report-skill.md')}`",
                f"- Evidence 数量：{len(self.evidence_cards)}",
                f"- KG 引用：`{self.kg_summary.get('graph_id')}`",
                f"- Scorecard 引用：`{self.score_summary.get('scorecard_id')}`",
            ]
        )

    def _thesis_body(self, top: dict[str, Any]) -> str:
        citation = self.citation.cite(next(iter(self.evidence_cards)))
        return (
            f"{self.payload.get('core_view', '当前结论应作为研究跟踪框架，而非投资动作依据。')} "
            f"该观点至少引用 {citation}，并由 KG 卡点 `{top.get('node_id', 'NA')}` "
            f"与 Scorecard `{self.score_summary.get('scorecard_id')}` 共同约束。"
        )

    def _evidence_chain_body(self) -> str:
        refs = self.score_summary.get("evidence_chain_refs") or list(self.evidence_cards)
        cited = [self.citation.cite(evidence_id) for evidence_id in refs if evidence_id in self.evidence_cards]
        return "\n".join(f"- {item}" for item in cited)

    def _default_counterarguments(self) -> list[str]:
        counterpoints: list[str] = []
        for evidence_id, card in self.evidence_cards.items():
            for refute in card.get("refutes", []):
                counterpoints.append(f"{evidence_id}: {refute.get('statement', '存在反方限制')}")
        return counterpoints or ["已检查反方证据，但仍需更多高等级来源验证。"]

    @staticmethod
    def _default_risks() -> list[str]:
        return [
            "证据口径、披露时点和统计样本可能不一致。",
            "Knowledge Graph 的路径与卡点结果依赖当前节点和边定义。",
            "Scorecard 是研究质量门禁，不代表投资评级或收益判断。",
        ]


class ReportComposer:
    """Create a ResearchReport object from a normalized payload."""

    def compose(self, payload: dict[str, Any]) -> ResearchReport:
        section_composer = SectionComposer(payload)
        sections = section_composer.compose()
        return ResearchReport(
            report_id=str(payload["report_id"]),
            title=str(payload["title"]),
            research_question=str(payload["research_question"]),
            methodology_refs=list(payload.get("methodology_refs", [])),
            evidence_cards=dict(payload["evidence_cards"]),
            knowledge_graph_summary=section_composer.kg_summary,
            score_summary=section_composer.score_summary,
            sections=sections,
            source_refs={
                "M2_methodology": list(payload.get("methodology_refs", [])),
                "M3_evidence": list(payload["evidence_cards"]),
                "FEATURE_002_knowledge_graph": [str(section_composer.kg_summary.get("graph_id"))],
                "M4_prompt": [str(payload.get("prompt_ref", "prompts/report/generation.md"))],
                "M5_skill": [str(payload.get("skill_ref", "skills/report/report-skill.md"))],
                "M6_score_eval": [str(section_composer.score_summary.get("scorecard_id"))],
            },
            version=str(payload.get("version", "1.0.0")),
        )
