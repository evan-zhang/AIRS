"""Learning Manager orchestration."""
from __future__ import annotations

from typing import Any

from .consolidation import MemoryConsolidator
from .feedback import DISCLAIMER, FeedbackCollector
from .methodology_opt import MethodologyOptimizer
from .outcome import OutcomeTracker
from .pattern import PatternMiner
from .prompt_opt import PromptOptimizer
from .rules import RuleGenerator
from .score_opt import ScoreOptimizer
from .skill_opt import SkillOptimizer


class LearningManager:
    """Coordinates feedback, outcome tracking, pattern mining and optimization."""

    def __init__(self) -> None:
        self.feedback_collector = FeedbackCollector()
        self.outcome_tracker = OutcomeTracker()
        self.pattern_miner = PatternMiner()
        self.rule_generator = RuleGenerator()
        self.prompt_optimizer = PromptOptimizer()
        self.methodology_optimizer = MethodologyOptimizer()
        self.skill_optimizer = SkillOptimizer()
        self.score_optimizer = ScoreOptimizer()
        self.consolidator = MemoryConsolidator()

    def run(self, payload: dict[str, Any]) -> dict[str, Any]:
        feedback = self.feedback_collector.collect(payload.get("feedback", []))
        outcomes = self.outcome_tracker.track(payload.get("outcomes", []))
        patterns = self.pattern_miner.mine(feedback, outcomes)
        rules = self.rule_generator.generate(patterns)
        optimizations = (
            self.prompt_optimizer.propose(rules)
            + self.methodology_optimizer.propose(rules)
            + self.skill_optimizer.propose(rules)
            + self.score_optimizer.propose(rules)
        )
        result = {
            "learning_id": payload.get("learning_id", "LEARN-RUN-0001"),
            "source_refs": list(payload.get("source_refs", [])),
            "feedback": [item.to_dict() for item in feedback],
            "outcomes": [item.to_dict() for item in outcomes],
            "patterns": [item.to_dict() for item in patterns],
            "rules": [item.to_dict() for item in rules],
            "optimizations": optimizations,
            "governance": {
                "approval_required": True,
                "auto_apply": False,
                "review_agent_gate": "REQUIRED",
                "rollback_required": True,
            },
            "disclaimer": DISCLAIMER,
        }
        result["memory_consolidation"] = self.consolidator.consolidate(result)
        return result

