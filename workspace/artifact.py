"""Artifact Manager for AIRS Workspace."""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
from uuid import uuid4

from .audit import AuditLog, DISCLAIMER


@dataclass
class WorkspaceArtifact:
    project_id: str
    session_id: str
    artifact_type: str
    title: str
    uri: str
    refs: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)
    artifact_id: str = field(default_factory=lambda: f"art-{uuid4().hex[:12]}")
    status: str = "DRAFT"
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    disclaimer: str = DISCLAIMER

    def to_dict(self) -> dict[str, Any]:
        return {
            "artifact_id": self.artifact_id,
            "project_id": self.project_id,
            "session_id": self.session_id,
            "artifact_type": self.artifact_type,
            "title": self.title,
            "uri": self.uri,
            "refs": list(self.refs),
            "metadata": dict(self.metadata),
            "status": self.status,
            "created_at": self.created_at,
            "disclaimer": self.disclaimer,
        }


class ArtifactManager:
    """Register evidence, knowledge graph, scorecard, report, and export artifacts."""

    def __init__(self, audit: AuditLog | None = None) -> None:
        self.audit = audit or AuditLog()
        self._artifacts: dict[str, WorkspaceArtifact] = {}

    def register(
        self,
        project_id: str,
        session_id: str,
        artifact_type: str,
        title: str,
        uri: str,
        refs: list[str] | None = None,
        metadata: dict[str, Any] | None = None,
        actor: str = "workspace-user",
    ) -> WorkspaceArtifact:
        artifact = WorkspaceArtifact(project_id, session_id, artifact_type, title, uri, refs or [], metadata or {})
        self._artifacts[artifact.artifact_id] = artifact
        self.audit.record("ARTIFACT_REGISTERED", actor, "artifact", artifact.artifact_id, artifact.to_dict())
        return artifact

    def publish(self, artifact_id: str, actor: str = "workspace-user") -> WorkspaceArtifact:
        artifact = self.get_artifact(artifact_id)
        artifact.status = "PUBLISHED"
        self.audit.record("ARTIFACT_PUBLISHED", actor, "artifact", artifact_id, {"status": artifact.status})
        return artifact

    def get_artifact(self, artifact_id: str) -> WorkspaceArtifact:
        try:
            return self._artifacts[artifact_id]
        except KeyError as exc:
            raise KeyError(f"unknown artifact: {artifact_id}") from exc

    def list_artifacts(self, project_id: str | None = None, session_id: str | None = None) -> list[dict[str, Any]]:
        artifacts = self._artifacts.values()
        if project_id:
            artifacts = [artifact for artifact in artifacts if artifact.project_id == project_id]
        if session_id:
            artifacts = [artifact for artifact in artifacts if artifact.session_id == session_id]
        return [artifact.to_dict() for artifact in artifacts]
