"""Structured Message Bus for Runtime sessions."""
from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
from uuid import uuid4
from .event_bus import EventBus
@dataclass
class RuntimeMessage:
    source_session_id: str
    target_session_id: str
    message_type: str
    payload: dict[str, Any] = field(default_factory=dict)
    trace_id: str | None = None
    message_id: str = field(default_factory=lambda: f"msg-{uuid4().hex[:12]}")
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    def to_dict(self) -> dict[str, Any]: return self.__dict__.copy()
class MessageBus:
    def __init__(self, event_bus: EventBus | None = None) -> None:
        self._messages: list[RuntimeMessage] = []; self.event_bus = event_bus
    def publish(self, message: RuntimeMessage) -> RuntimeMessage:
        self._messages.append(message)
        if self.event_bus: self.event_bus.publish("MESSAGE_PUBLISHED", session_id=message.source_session_id, payload=message.to_dict(), trace_id=message.trace_id)
        return message
    def list_messages(self) -> list[dict[str, Any]]: return [message.to_dict() for message in self._messages]
