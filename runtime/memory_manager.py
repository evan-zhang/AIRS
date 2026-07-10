"""Memory Manager with auditable source refs."""
from __future__ import annotations
from typing import Any
class MemoryManager:
    def __init__(self) -> None:
        self.session_memory: dict[str, dict[str, Any]] = {}; self.workflow_memory: dict[str, Any] = {}; self.audit_memory: list[dict[str, Any]] = []
    def remember(self, session_id: str, key: str, value: Any, source_event_id: str | None = None) -> None:
        self.session_memory.setdefault(session_id, {})[key] = value; self.audit_memory.append({"session_id": session_id, "key": key, "value": value, "source_event_id": source_event_id})
    def recall(self, session_id: str) -> dict[str, Any]: return dict(self.session_memory.get(session_id, {}))
