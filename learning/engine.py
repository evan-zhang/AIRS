"""Continuous Improvement Engine entrypoint."""
from __future__ import annotations

from typing import Any

from .manager import LearningManager


class ContinuousImprovementEngine:
    """Public runtime facade for the Autonomous Learning Engine."""

    def __init__(self, manager: LearningManager | None = None) -> None:
        self.manager = manager or LearningManager()

    def improve(self, payload: dict[str, Any]) -> dict[str, Any]:
        return self.manager.run(payload)

    def run(self, payload: dict[str, Any]) -> dict[str, Any]:
        return self.improve(payload)

