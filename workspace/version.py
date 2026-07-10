"""Version Manager for AIRS Workspace artifacts."""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
from uuid import uuid4

from .audit import AuditLog, DISCLAIMER


@dataclass
class ArtifactVersion:
    artifact_id: str
    version: str
    change_summary: str
    refs: list[str] = field(default_factory=list)
    version_id: str = field(default_factory=lambda: f"ver-{uuid4().hex[:12]}")
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    disclaimer: str = DISCLAIMER

    def to_dict(self) -> dict[str, Any]:
        return {
            "version_id": self.version_id,
            "artifact_id": self.artifact_id,
            "version": self.version,
            "change_summary": self.change_summary,
            "refs": list(self.refs),
            "created_at": self.created_at,
            "disclaimer": self.disclaimer,
        }


class VersionManager:
    """Track versions for reports, graph exports, and evidence bundles."""

    def __init__(self, audit: AuditLog | None = None) -> None:
        self.audit = audit or AuditLog()
        self._versions: dict[str, list[ArtifactVersion]] = {}

    def add_version(self, artifact_id: str, version: str, change_summary: str, refs: list[str] | None = None, actor: str = "workspace-user") -> ArtifactVersion:
        item = ArtifactVersion(artifact_id, version, change_summary, refs or [])
        self._versions.setdefault(artifact_id, []).append(item)
        self.audit.record("ARTIFACT_VERSION_ADDED", actor, "artifact", artifact_id, item.to_dict())
        return item

    def list_versions(self, artifact_id: str) -> list[dict[str, Any]]:
        return [item.to_dict() for item in self._versions.get(artifact_id, [])]
