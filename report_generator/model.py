"""Core models for AIRS Research Report Generator."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


DISCLAIMER = "本报告仅用于 AIRS 投资研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。"

REQUIRED_SECTION_TITLES = [
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


@dataclass(frozen=True)
class ReportSection:
    """A single rendered report section."""

    section_id: str
    title: str
    body: str
    evidence_refs: list[str] = field(default_factory=list)
    kg_refs: list[str] = field(default_factory=list)
    score_refs: list[str] = field(default_factory=list)

    def to_markdown(self, index: int) -> str:
        return f"## {index}. {self.title}\n\n{self.body.strip()}\n"

    def to_dict(self) -> dict[str, Any]:
        return {
            "section_id": self.section_id,
            "title": self.title,
            "body": self.body,
            "evidence_refs": self.evidence_refs,
            "kg_refs": self.kg_refs,
            "score_refs": self.score_refs,
        }


@dataclass
class ResearchReport:
    """Rendered report artifact with traceability metadata."""

    report_id: str
    title: str
    research_question: str
    methodology_refs: list[str]
    evidence_cards: dict[str, dict[str, Any]]
    knowledge_graph_summary: dict[str, Any]
    score_summary: dict[str, Any]
    sections: list[ReportSection]
    source_refs: dict[str, list[str]]
    disclaimer: str = DISCLAIMER
    version: str = "0.1.0"

    def to_markdown(self) -> str:
        header = [
            f"# {self.title}",
            "",
            f"**Report ID**：{self.report_id}",
            f"**版本**：{self.version}",
            f"**方法论引用**：{', '.join(f'`{item}`' for item in self.methodology_refs)}",
            "",
            f"**免责声明**：{self.disclaimer}",
            "",
        ]
        sections = [section.to_markdown(index) for index, section in enumerate(self.sections, start=1)]
        return "\n".join(header + sections).rstrip() + "\n"

    def to_dict(self) -> dict[str, Any]:
        return {
            "report_id": self.report_id,
            "title": self.title,
            "research_question": self.research_question,
            "methodology_refs": self.methodology_refs,
            "evidence_cards": self.evidence_cards,
            "knowledge_graph_summary": self.knowledge_graph_summary,
            "score_summary": self.score_summary,
            "sections": [section.to_dict() for section in self.sections],
            "source_refs": self.source_refs,
            "disclaimer": self.disclaimer,
            "version": self.version,
        }
