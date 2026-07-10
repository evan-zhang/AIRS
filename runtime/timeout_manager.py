"""Timeout Manager."""
from __future__ import annotations
class TimeoutManager:
    def is_timeout(self, elapsed_seconds: float, timeout_seconds: int) -> bool:
        return elapsed_seconds > timeout_seconds
