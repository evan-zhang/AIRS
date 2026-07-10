"""Evidence citation helpers for report composition."""

from __future__ import annotations

from typing import Any


class EvidenceCitationBuilder:
    """Build compact citations from M3 Evidence Cards."""

    def __init__(self, evidence_cards: dict[str, dict[str, Any]]) -> None:
        self.evidence_cards = evidence_cards

    def cite(self, evidence_id: str) -> str:
        card = self.evidence_cards[evidence_id]
        title = card.get("title", "未命名证据")
        level = card.get("evidence_level", "NA")
        confidence = card.get("confidence", "NA")
        source = card.get("source", "未标注来源")
        return f"[{evidence_id}] {title}（来源：{source}；等级：{level}；置信度：{confidence}）"

    def citation_table(self) -> str:
        lines = [
            "| Evidence ID | 标题 | 类别 | 来源类型 | 等级 | 权重 | 支持命题 | 反方或限制 |",
            "|---|---|---|---|---|---:|---|---|",
        ]
        for evidence_id, card in self.evidence_cards.items():
            supports = self._claim_text(card.get("supports", []))
            refutes = self._claim_text(card.get("refutes", []))
            lines.append(
                "| "
                + " | ".join(
                    [
                        evidence_id,
                        str(card.get("title", "")),
                        str(card.get("category", "")),
                        str(card.get("source_type", "")),
                        str(card.get("evidence_level", "")),
                        str(card.get("weight", "")),
                        supports,
                        refutes,
                    ]
                )
                + " |"
            )
        return "\n".join(lines)

    def missing_evidence_summary(self) -> list[str]:
        missing: list[str] = []
        for evidence_id, card in self.evidence_cards.items():
            for item in card.get("missing_evidence", []):
                missing.append(f"{evidence_id}: {item}")
        return missing

    @staticmethod
    def _claim_text(claims: list[dict[str, Any]]) -> str:
        if not claims:
            return "已检查，暂无直接记录"
        return "；".join(str(item.get("statement", "")) for item in claims)
