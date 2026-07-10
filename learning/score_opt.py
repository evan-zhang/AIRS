"""Score optimization proposals."""
from __future__ import annotations

from typing import Any

from .feedback import DISCLAIMER
from .rules import RuleCandidate


class ScoreOptimizer:
    def propose(self, rules: list[RuleCandidate]) -> list[dict[str, Any]]:
        return [
            {
                "proposal_id": f"SCORE-{rule.rule_id}",
                "target": "schemas/score/scorecard.schema.json",
                "change_type": "score_calibration",
                "summary": "降低低证据置信度样本权重，提高 Outcome 偏差、反方证据和缺失证据的惩罚权重。",
                "source_rule": rule.rule_id,
                "review_status": "pending_review",
                "disclaimer": DISCLAIMER,
            }
            for rule in rules
            if rule.target_module in {"score", "report", "investment_engine"}
        ]

