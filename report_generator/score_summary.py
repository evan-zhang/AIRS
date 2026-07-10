"""Score summary helpers for AIRS reports."""

from __future__ import annotations

from typing import Any


class ScoreSummaryBuilder:
    """Summarize M6 Score/Evaluation outputs without changing scores."""

    def __init__(self, scorecard: dict[str, Any]) -> None:
        self.scorecard = scorecard

    def build(self) -> dict[str, Any]:
        scores = self.scorecard.get("scores", [])
        dimensions = {
            str(item.get("dimension", item.get("score_id", "unknown"))): item.get("score", item.get("value"))
            for item in scores
        }
        return {
            "scorecard_id": self.scorecard.get("scorecard_id"),
            "overall_score": self.scorecard.get("overall_score"),
            "overall_grade": self.scorecard.get("overall_grade"),
            "confidence_score": self.scorecard.get("confidence_score"),
            "quality_gate": self.scorecard.get("quality_gate"),
            "methodology_refs": self.scorecard.get("methodology_refs", []),
            "evidence_chain_refs": self.scorecard.get("evidence_chain_refs", []),
            "dimensions": dimensions,
            "disclaimer": self.scorecard.get("disclaimer"),
        }

    def to_markdown(self) -> str:
        summary = self.build()
        dimensions = "；".join(f"{key}: {value}" for key, value in summary["dimensions"].items())
        return "\n".join(
            [
                f"- Scorecard ID：`{summary['scorecard_id']}`",
                f"- Overall Score / Grade：{summary['overall_score']} / {summary['overall_grade']}",
                f"- Confidence Score：{summary['confidence_score']}",
                f"- Quality Gate：`{summary['quality_gate']}`",
                f"- 维度分：{dimensions}",
                f"- Score Evidence Refs：{', '.join(f'`{item}`' for item in summary['evidence_chain_refs'])}",
                f"- Score Disclaimer：{summary['disclaimer']}",
            ]
        )
