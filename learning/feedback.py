"""Feedback Collector for AIRS learning records."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

DISCLAIMER = "仅用于 AIRS 研究质量改进，不构成投资建议"


@dataclass
class FeedbackRecord:
    feedback_id: str
    source_type: str
    source_ref: str
    target_module: str
    issue_type: str
    severity: str
    observation: str
    evidence_refs: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)
    disclaimer: str = DISCLAIMER

    def to_dict(self) -> dict[str, Any]:
        return {
            "feedback_id": self.feedback_id,
            "source_type": self.source_type,
            "source_ref": self.source_ref,
            "target_module": self.target_module,
            "issue_type": self.issue_type,
            "severity": self.severity,
            "observation": self.observation,
            "evidence_refs": list(self.evidence_refs),
            "metadata": dict(self.metadata),
            "disclaimer": self.disclaimer,
        }


class FeedbackCollector:
    """Collects feedback from Report, Committee, Memory, Review and Benchmark."""

    def collect(self, records: list[dict[str, Any]]) -> list[FeedbackRecord]:
        collected: list[FeedbackRecord] = []
        for index, item in enumerate(records, start=1):
            collected.append(
                FeedbackRecord(
                    feedback_id=item.get("feedback_id", f"FB-{index:04d}"),
                    source_type=item.get("source_type", "review"),
                    source_ref=item.get("source_ref", "unknown"),
                    target_module=item.get("target_module", "report"),
                    issue_type=item.get("issue_type", "quality_gap"),
                    severity=item.get("severity", "medium"),
                    observation=item.get("observation", ""),
                    evidence_refs=list(item.get("evidence_refs", [])),
                    metadata=dict(item.get("metadata", {})),
                )
            )
        return collected

