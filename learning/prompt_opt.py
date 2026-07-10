"""Prompt optimization proposals."""
from __future__ import annotations

from typing import Any

from .feedback import DISCLAIMER
from .rules import RuleCandidate


class PromptOptimizer:
    def propose(self, rules: list[RuleCandidate]) -> list[dict[str, Any]]:
        proposals: list[dict[str, Any]] = []
        for rule in rules:
            if rule.target_module in {"prompt", "report", "evidence", "committee"}:
                proposals.append({
                    "proposal_id": f"PROMPT-{rule.rule_id}",
                    "target": "prompts/",
                    "change_type": "prompt_guardrail",
                    "summary": "在 Prompt 输出要求中加入证据引用、反方观点和不确定性检查项。",
                    "source_rule": rule.rule_id,
                    "review_status": "pending_review",
                    "disclaimer": DISCLAIMER,
                })
        return proposals

