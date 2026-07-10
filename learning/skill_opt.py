"""Skill optimization proposals."""
from __future__ import annotations

from typing import Any

from .feedback import DISCLAIMER
from .rules import RuleCandidate


class SkillOptimizer:
    def propose(self, rules: list[RuleCandidate]) -> list[dict[str, Any]]:
        return [
            {
                "proposal_id": f"SKILL-{rule.rule_id}",
                "target": "skills/",
                "change_type": "skill_workflow_gate",
                "summary": "在 Skill 工作流中增加 Review Agent 可验证的输入校验、证据检查和失败回退。",
                "source_rule": rule.rule_id,
                "review_status": "pending_review",
                "disclaimer": DISCLAIMER,
            }
            for rule in rules
            if rule.target_module in {"skill", "runtime", "planner", "committee"}
        ]

