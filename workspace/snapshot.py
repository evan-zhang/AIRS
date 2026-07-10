"""Snapshot Manager for AIRS Workspace."""
from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
from uuid import uuid4

from .audit import AuditLog, DISCLAIMER


@dataclass
class WorkspaceSnapshot:
    project_id: str
    session_id: str
    state: dict[str, Any]
    reason: str
    snapshot_id: str = field(default_factory=lambda: f"snap-{uuid4().hex[:12]}")
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    disclaimer: str = DISCLAIMER

    def to_dict(self) -> dict[str, Any]:
        return {
            "snapshot_id": self.snapshot_id,
            "project_id": self.project_id,
            "session_id": self.session_id,
            "state": deepcopy(self.state),
            "reason": self.reason,
            "created_at": self.created_at,
            "disclaimer": self.disclaimer,
        }


class SnapshotManager:
    """Create immutable snapshots for pause, review, and replay."""

    def __init__(self, audit: AuditLog | None = None) -> None:
        self.audit = audit or AuditLog()
        self._snapshots: dict[str, WorkspaceSnapshot] = {}

    def create_snapshot(self, project_id: str, session_id: str, state: dict[str, Any], reason: str, actor: str = "workspace-user") -> WorkspaceSnapshot:
        snapshot = WorkspaceSnapshot(project_id, session_id, deepcopy(state), reason)
        self._snapshots[snapshot.snapshot_id] = snapshot
        self.audit.record("SNAPSHOT_CREATED", actor, "snapshot", snapshot.snapshot_id, {"project_id": project_id, "reason": reason})
        return snapshot

    def get_snapshot(self, snapshot_id: str) -> WorkspaceSnapshot:
        return self._snapshots[snapshot_id]

    def list_snapshots(self, project_id: str | None = None) -> list[dict[str, Any]]:
        snapshots = self._snapshots.values()
        if project_id:
            snapshots = [snapshot for snapshot in snapshots if snapshot.project_id == project_id]
        return [snapshot.to_dict() for snapshot in snapshots]
