"""Workspace Memory with source references."""
from __future__ import annotations

from copy import deepcopy
from typing import Any

from .audit import AuditLog, DISCLAIMER


class WorkspaceMemory:
    """Store reusable research context while keeping evidence as external refs."""

    def __init__(self, audit: AuditLog | None = None) -> None:
        self.audit = audit or AuditLog()
        self._memory: dict[str, dict[str, Any]] = {}

    def remember(self, project_id: str, key: str, value: Any, source_ref: str, actor: str = "workspace-user") -> None:
        if not source_ref:
            raise ValueError("source_ref is required for Workspace Memory")
        bucket = self._memory.setdefault(project_id, {})
        bucket[key] = {"value": deepcopy(value), "source_ref": source_ref, "disclaimer": DISCLAIMER}
        self.audit.record("MEMORY_WRITTEN", actor, "project", project_id, {"key": key, "source_ref": source_ref})

    def recall(self, project_id: str, key: str | None = None) -> Any:
        bucket = deepcopy(self._memory.get(project_id, {}))
        if key:
            return bucket.get(key)
        return bucket
