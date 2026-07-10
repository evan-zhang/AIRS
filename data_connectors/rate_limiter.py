"""Simple per-connector rate limit manager."""
from __future__ import annotations
from dataclasses import dataclass, field
from time import monotonic


@dataclass
class RateLimitManager:
    min_interval_seconds: float = 0.0
    _last_call: dict[str, float] = field(default_factory=dict)

    def allow(self, connector_id: str) -> bool:
        now = monotonic()
        last = self._last_call.get(connector_id)
        if last is not None and now - last < self.min_interval_seconds:
            return False
        self._last_call[connector_id] = now
        return True
