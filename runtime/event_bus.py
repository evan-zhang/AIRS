"""Append-only Event Bus."""
from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
from uuid import uuid4
@dataclass
class RuntimeEvent:
    event_type: str
    session_id: str | None = None
    task_id: str | None = None
    agent_id: str | None = None
    severity: str = "INFO"
    payload: dict[str, Any] = field(default_factory=dict)
    trace_id: str | None = None
    event_id: str = field(default_factory=lambda: f"evt-{uuid4().hex[:12]}")
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    def to_dict(self) -> dict[str, Any]: return self.__dict__.copy()
class EventBus:
    def __init__(self) -> None: self._events: list[RuntimeEvent] = []
    def publish(self, event_type: str, **kwargs: Any) -> RuntimeEvent:
        event = RuntimeEvent(event_type=event_type, **kwargs); self._events.append(event); return event
    def list_events(self) -> list[dict[str, Any]]: return [event.to_dict() for event in self._events]
