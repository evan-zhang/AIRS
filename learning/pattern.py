"""Pattern Miner for repeated research quality signals."""
from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass, field
from typing import Any

from .feedback import DISCLAIMER, FeedbackRecord
from .outcome import OutcomeRecord


@dataclass
class LearningPattern:
    pattern_id: str
    pattern_type: str
    target_module: str
    description: str
    frequency: int
    severity_mix: dict[str, int]
    evidence_refs: list[str] = field(default_factory=list)
    confidence: float = 0.6
    disclaimer: str = DISCLAIMER

    def to_dict(self) -> dict[str, Any]:
        return {
            "pattern_id": self.pattern_id,
            "pattern_type": self.pattern_type,
            "target_module": self.target_module,
            "description": self.description,
            "frequency": self.frequency,
            "severity_mix": dict(self.severity_mix),
            "evidence_refs": list(self.evidence_refs),
            "confidence": self.confidence,
            "disclaimer": self.disclaimer,
        }


class PatternMiner:
    """Mines repeated issue patterns across feedback and outcomes."""

    def mine(self, feedback: list[FeedbackRecord], outcomes: list[OutcomeRecord]) -> list[LearningPattern]:
        grouped: dict[tuple[str, str], list[FeedbackRecord]] = defaultdict(list)
        for item in feedback:
            grouped[(item.target_module, item.issue_type)].append(item)
        patterns: list[LearningPattern] = []
        for index, ((target, issue), items) in enumerate(sorted(grouped.items()), start=1):
            severity_mix = Counter(item.severity for item in items)
            refs = sorted({ref for item in items for ref in item.evidence_refs})
            confidence = min(0.95, 0.5 + len(items) * 0.1 + severity_mix.get("high", 0) * 0.05)
            patterns.append(
                LearningPattern(
                    pattern_id=f"PAT-{index:04d}",
                    pattern_type=issue,
                    target_module=target,
                    description=f"{target} 模块反复出现 {issue}，需要转化为可评审改进规则。",
                    frequency=len(items),
                    severity_mix=dict(severity_mix),
                    evidence_refs=refs,
                    confidence=round(confidence, 2),
                )
            )
        if outcomes:
            high_variance = [item for item in outcomes if item.variance_level in {"high", "critical"}]
            if high_variance:
                patterns.append(
                    LearningPattern(
                        pattern_id=f"PAT-{len(patterns)+1:04d}",
                        pattern_type="outcome_variance",
                        target_module="score",
                        description="Outcome 与研究预期出现高偏差，需要校准评分、证据权重和不确定性标注。",
                        frequency=len(high_variance),
                        severity_mix={"high": len(high_variance)},
                        evidence_refs=sorted({ref for item in high_variance for ref in item.evidence_refs}),
                        confidence=0.8,
                    )
                )
        return patterns

