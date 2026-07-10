"""Methodology optimization proposals."""
from __future__ import annotations

from typing import Any

from .feedback import DISCLAIMER
from .rules import RuleCandidate


class MethodologyOptimizer:
    def propose(self, rules: list[RuleCandidate]) -> list[dict[str, Any]]:
        return [
            {
                "proposal_id": f"METH-{rule.rule_id}",
                "target": "docs/methodology/",
                "change_type": "methodology_review_step",
                "summary": "补充适用边界、反例场景、证据最低要求和失败处理步骤。",
                "source_rule": rule.rule_id,
                "review_status": "pending_review",
                "disclaimer": DISCLAIMER,
            }
            for rule in rules
            if rule.target_module in {"methodology", "investment_engine", "score"}
        ]

