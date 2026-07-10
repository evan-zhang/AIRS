"""Runtime Retry Scheduler."""
from __future__ import annotations

class RetryScheduler:
    """Decide whether an Agent task in the Runtime can be retried."""

    def should_retry(self, attempts: int, max_retries: int) -> bool:
        return attempts < max_retries
