"""Runtime Resource Manager."""
from __future__ import annotations
from dataclasses import dataclass
@dataclass
class ResourcePolicy:
    max_concurrency: int = 3
    default_timeout_seconds: int = 60
    max_retries: int = 1
    long_running_checkpoint_interval: int = 1
    human_wait_timeout_seconds: int = 3600
class ResourceManager:
    def __init__(self, policy: ResourcePolicy | None = None) -> None:
        self.policy = policy or ResourcePolicy(); self.active_sessions = 0
    def acquire(self) -> bool:
        if self.active_sessions >= self.policy.max_concurrency: return False
        self.active_sessions += 1; return True
    def release(self) -> None: self.active_sessions = max(0, self.active_sessions - 1)
