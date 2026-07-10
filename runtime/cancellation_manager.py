"""Cancellation Manager."""
from __future__ import annotations
class CancellationManager:
    def __init__(self) -> None: self.cancelled: set[str] = set()
    def cancel(self, task_id: str) -> None: self.cancelled.add(task_id)
    def is_cancelled(self, task_id: str) -> bool: return task_id in self.cancelled
