"""Collaboration registry for AIRS Workspace."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any
from uuid import uuid4

from .audit import AuditLog, DISCLAIMER


@dataclass
class CollaborationNote:
    project_id: str
    session_id: str
    author_role: str
    note_type: str
    content: str
    refs: list[str] = field(default_factory=list)
    note_id: str = field(default_factory=lambda: f"note-{uuid4().hex[:12]}")
    disclaimer: str = DISCLAIMER

    def to_dict(self) -> dict[str, Any]:
        return {
            "note_id": self.note_id,
            "project_id": self.project_id,
            "session_id": self.session_id,
            "author_role": self.author_role,
            "note_type": self.note_type,
            "content": self.content,
            "refs": list(self.refs),
            "disclaimer": self.disclaimer,
        }


class CollaborationManager:
    """Capture handoffs, review notes, and human decisions."""

    def __init__(self, audit: AuditLog | None = None) -> None:
        self.audit = audit or AuditLog()
        self._notes: list[CollaborationNote] = []

    def add_note(self, project_id: str, session_id: str, author_role: str, note_type: str, content: str, refs: list[str] | None = None) -> CollaborationNote:
        note = CollaborationNote(project_id, session_id, author_role, note_type, content, refs or [])
        self._notes.append(note)
        self.audit.record("COLLABORATION_NOTE_ADDED", author_role, "session", session_id, note.to_dict())
        return note

    def list_notes(self, project_id: str | None = None) -> list[dict[str, Any]]:
        notes = self._notes
        if project_id:
            notes = [note for note in notes if note.project_id == project_id]
        return [note.to_dict() for note in notes]
