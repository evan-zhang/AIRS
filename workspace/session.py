"""Session Manager for AIRS Workspace."""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
from uuid import uuid4

from .audit import AuditLog, DISCLAIMER


@dataclass
class WorkspaceSession:
    project_id: str
    runtime_id: str
    workflow_id: str
    intent: dict[str, Any] = field(default_factory=dict)
    session_id: str = field(default_factory=lambda: f"wss-{uuid4().hex[:12]}")
    status: str = "OPEN"
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    updated_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    refs: list[str] = field(default_factory=list)
    disclaimer: str = DISCLAIMER

    def to_dict(self) -> dict[str, Any]:
        return {
            "session_id": self.session_id,
            "project_id": self.project_id,
            "runtime_id": self.runtime_id,
            "workflow_id": self.workflow_id,
            "intent": dict(self.intent),
            "status": self.status,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "refs": list(self.refs),
            "disclaimer": self.disclaimer,
        }


class SessionManager:
    """Track Workspace sessions that wrap Runtime execution."""

    def __init__(self, audit: AuditLog | None = None) -> None:
        self.audit = audit or AuditLog()
        self._sessions: dict[str, WorkspaceSession] = {}

    def open_session(
        self,
        project_id: str,
        runtime_id: str,
        workflow_id: str,
        intent: dict[str, Any] | None = None,
        refs: list[str] | None = None,
        actor: str = "workspace-user",
    ) -> WorkspaceSession:
        session = WorkspaceSession(project_id, runtime_id, workflow_id, intent or {}, refs=refs or [])
        self._sessions[session.session_id] = session
        self.audit.record("SESSION_OPENED", actor, "session", session.session_id, session.to_dict())
        return session

    def transition(self, session_id: str, status: str, actor: str = "workspace-user") -> WorkspaceSession:
        session = self.get_session(session_id)
        session.status = status
        session.updated_at = datetime.now(timezone.utc).isoformat()
        self.audit.record("SESSION_STATUS_UPDATED", actor, "session", session_id, {"status": status})
        return session

    def get_session(self, session_id: str) -> WorkspaceSession:
        try:
            return self._sessions[session_id]
        except KeyError as exc:
            raise KeyError(f"unknown workspace session: {session_id}") from exc

    def list_sessions(self, project_id: str | None = None) -> list[dict[str, Any]]:
        sessions = self._sessions.values()
        if project_id:
            sessions = [session for session in sessions if session.project_id == project_id]
        return [session.to_dict() for session in sessions]
