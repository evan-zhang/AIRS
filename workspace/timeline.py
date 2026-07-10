"""Research Timeline for AIRS Workspace."""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
from uuid import uuid4

from .audit import DISCLAIMER


@dataclass
class TimelineEvent:
    project_id: str
    session_id: str
    event_type: str
    title: str
    payload: dict[str, Any] = field(default_factory=dict)
    event_id: str = field(default_factory=lambda: f"tl-{uuid4().hex[:12]}")
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    disclaimer: str = DISCLAIMER

    def to_dict(self) -> dict[str, Any]:
        return {
            "event_id": self.event_id,
            "project_id": self.project_id,
            "session_id": self.session_id,
            "event_type": self.event_type,
            "title": self.title,
            "payload": dict(self.payload),
            "created_at": self.created_at,
            "disclaimer": self.disclaimer,
        }


class ResearchTimeline:
    """Append research milestones and Runtime references."""

    def __init__(self) -> None:
        self._events: list[TimelineEvent] = []

    def append(self, project_id: str, session_id: str, event_type: str, title: str, payload: dict[str, Any] | None = None) -> TimelineEvent:
        event = TimelineEvent(project_id, session_id, event_type, title, payload or {})
        self._events.append(event)
        return event

    def list_events(self, project_id: str | None = None, session_id: str | None = None) -> list[dict[str, Any]]:
        events = self._events
        if project_id:
            events = [event for event in events if event.project_id == project_id]
        if session_id:
            events = [event for event in events if event.session_id == session_id]
        return [event.to_dict() for event in events]
