"""Rule Generator for candidate learning rules."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .feedback import DISCLAIMER
from .pattern import LearningPattern


@dataclass
class RuleCandidate:
    rule_id: str
    pattern_id: str
    target_module: str
    rule_text: str
    rationale: str
    required_review: str = "human_review_required"
    status: str = "candidate"
    rollback_plan: str = "若回归测试失败或 Review Agent 拒绝，则保持原规则并归档候选。"
    evidence_refs: list[str] = field(default_factory=list)
    disclaimer: str = DISCLAIMER

    def to_dict(self) -> dict[str, Any]:
        return {
            "rule_id": self.rule_id,
            "pattern_id": self.pattern_id,
            "target_module": self.target_module,
            "rule_text": self.rule_text,
            "rationale": self.rationale,
            "required_review": self.required_review,
            "status": self.status,
            "rollback_plan": self.rollback_plan,
            "evidence_refs": list(self.evidence_refs),
            "disclaimer": self.disclaimer,
        }


class RuleGenerator:
    """Turns mined patterns into reviewable candidate rules."""

    def generate(self, patterns: list[LearningPattern]) -> list[RuleCandidate]:
        rules: list[RuleCandidate] = []
        for index, pattern in enumerate(patterns, start=1):
            rules.append(
                RuleCandidate(
                    rule_id=f"RULE-{index:04d}",
                    pattern_id=pattern.pattern_id,
                    target_module=pattern.target_module,
                    rule_text=(
                        f"当 {pattern.target_module} 出现 {pattern.pattern_type} 且频次达到 "
                        f"{pattern.frequency} 次时，必须增加证据复核、反方观点或不确定性标注。"
                    ),
                    rationale=f"来源模式 {pattern.pattern_id} 置信度 {pattern.confidence}，用于降低重复质量缺陷。",
                    evidence_refs=pattern.evidence_refs,
                )
            )
        return rules

