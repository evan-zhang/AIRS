"""Project Manager for AIRS Workspace."""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
from uuid import uuid4

from .audit import AuditLog, DISCLAIMER


@dataclass
class ResearchProject:
    name: str
    research_question: str
    scope: dict[str, Any] = field(default_factory=dict)
    owner: str = "workspace-user"
    project_id: str = field(default_factory=lambda: f"prj-{uuid4().hex[:12]}")
    status: str = "ACTIVE"
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    updated_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    refs: list[str] = field(default_factory=list)
    disclaimer: str = DISCLAIMER

    def to_dict(self) -> dict[str, Any]:
        return {
            "project_id": self.project_id,
            "name": self.name,
            "research_question": self.research_question,
            "scope": dict(self.scope),
            "owner": self.owner,
            "status": self.status,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "refs": list(self.refs),
            "disclaimer": self.disclaimer,
        }


class ProjectManager:
    """Create and update research projects without producing investment advice."""

    def __init__(self, audit: AuditLog | None = None) -> None:
        self.audit = audit or AuditLog()
        self._projects: dict[str, ResearchProject] = {}

    def create_project(
        self,
        name: str,
        research_question: str,
        scope: dict[str, Any] | None = None,
        owner: str = "workspace-user",
        refs: list[str] | None = None,
    ) -> ResearchProject:
        project = ResearchProject(name, research_question, scope or {}, owner, refs=refs or [])
        self._projects[project.project_id] = project
        self.audit.record("PROJECT_CREATED", owner, "project", project.project_id, project.to_dict())
        return project

    def get_project(self, project_id: str) -> ResearchProject:
        try:
            return self._projects[project_id]
        except KeyError as exc:
            raise KeyError(f"unknown project: {project_id}") from exc

    def update_status(self, project_id: str, status: str, actor: str = "workspace-user") -> ResearchProject:
        project = self.get_project(project_id)
        project.status = status
        project.updated_at = datetime.now(timezone.utc).isoformat()
        self.audit.record("PROJECT_STATUS_UPDATED", actor, "project", project_id, {"status": status})
        return project

    def list_projects(self) -> list[dict[str, Any]]:
        return [project.to_dict() for project in self._projects.values()]
