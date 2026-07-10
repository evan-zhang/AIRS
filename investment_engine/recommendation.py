"""Recommendation standards for AIRS investment research outputs."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


DISCLAIMER = "仅用于 AIRS 投资研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。"
FORBIDDEN_TERMS = (
    "建议" + "买入",
    "建议" + "卖出",
    "保证" + "收益",
    "保证" + "盈利",
    "目标价" + "为",
    "应" + "买入",
    "应" + "卖出",
    "自动交易" + "指令",
)
STATEMENT_TYPES = ("Fact", "Inference", "Assumption", "Opinion")


@dataclass(frozen=True)
class Statement:
    statement_id: str
    statement_type: str
    text: str
    evidence_refs: list[str] = field(default_factory=list)
    confidence: float = 0.5
    rationale: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "statement_id": self.statement_id,
            "statement_type": self.statement_type,
            "text": self.text,
            "evidence_refs": self.evidence_refs,
            "confidence": self.confidence,
            "rationale": self.rationale,
        }


def classify_statement(text: str, evidence_refs: list[str] | None = None, confidence: float = 0.5) -> str:
    """Classify one statement as Fact, Inference, Assumption, or Opinion."""

    refs = evidence_refs or []
    lowered = text.lower()
    if refs and confidence >= 0.75 and any(token in lowered for token in ("reported", "published", "disclosed", "显示", "披露", "公告")):
        return "Fact"
    if refs and any(token in text for token in ("因此", "推导", "意味着", "可能导致", "相关")):
        return "Inference"
    if any(token in text for token in ("假设", "若", "如果", "情景")):
        return "Assumption"
    return "Opinion"


def validate_recommendation_language(text: str) -> list[str]:
    """Return forbidden recommendation-language hits."""

    return [term for term in FORBIDDEN_TERMS if term in text]


def build_recommendation(topic: str, scorecard: dict[str, Any], statements: list[Statement]) -> dict[str, Any]:
    """Build a compliance-safe recommendation summary."""

    missing_types = sorted(set(STATEMENT_TYPES) - {item.statement_type for item in statements})
    quality_gate = scorecard.get("quality_gate", "CONDITIONAL_PASS")
    return {
        "recommendation_id": f"rec-{topic.lower().replace(' ', '-')}",
        "topic": topic,
        "research_stance": "可继续研究" if quality_gate in {"PASS", "CONDITIONAL_PASS"} else "证据不足，暂不形成研究观点",
        "quality_gate": quality_gate,
        "statement_coverage": {kind: sum(1 for item in statements if item.statement_type == kind) for kind in STATEMENT_TYPES},
        "missing_statement_types": missing_types,
        "statements": [item.to_dict() for item in statements],
        "prohibited_actions": ["不提供买入/卖出指令", "不提供目标价", "不承诺收益", "不触发自动交易"],
        "disclaimer": DISCLAIMER,
    }
