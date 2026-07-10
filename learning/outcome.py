"""Outcome Tracker for comparing research expectations with later observations."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .feedback import DISCLAIMER


@dataclass
class OutcomeRecord:
    outcome_id: str
    research_ref: str
    expected_result: str
    observed_result: str
    horizon: str
    variance_level: str
    evidence_refs: list[str] = field(default_factory=list)
    lessons: list[str] = field(default_factory=list)
    disclaimer: str = DISCLAIMER

    def to_dict(self) -> dict[str, Any]:
        return {
            "outcome_id": self.outcome_id,
            "research_ref": self.research_ref,
            "expected_result": self.expected_result,
            "observed_result": self.observed_result,
            "horizon": self.horizon,
            "variance_level": self.variance_level,
            "evidence_refs": list(self.evidence_refs),
            "lessons": list(self.lessons),
            "disclaimer": self.disclaimer,
        }


class OutcomeTracker:
    """Tracks outcome deltas without turning them into price predictions."""

    def track(self, items: list[dict[str, Any]]) -> list[OutcomeRecord]:
        outcomes: list[OutcomeRecord] = []
        for index, item in enumerate(items, start=1):
            outcomes.append(
                OutcomeRecord(
                    outcome_id=item.get("outcome_id", f"OUT-{index:04d}"),
                    research_ref=item.get("research_ref", "unknown"),
                    expected_result=item.get("expected_result", ""),
                    observed_result=item.get("observed_result", ""),
                    horizon=item.get("horizon", "post_review"),
                    variance_level=item.get("variance_level", "medium"),
                    evidence_refs=list(item.get("evidence_refs", [])),
                    lessons=list(item.get("lessons", [])),
                )
            )
        return outcomes

