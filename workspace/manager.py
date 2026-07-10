"""Workspace Manager for AIRS AI Research Workspace."""
from __future__ import annotations

from typing import Any
from uuid import uuid4

from .artifact import ArtifactManager
from .audit import AuditLog, DISCLAIMER
from .collaboration import CollaborationManager
from .export import WorkspaceExport
from .memory import WorkspaceMemory
from .project import ProjectManager, ResearchProject
from .replay import ReplayManager
from .session import SessionManager, WorkspaceSession
from .snapshot import SnapshotManager
from .task_board import TaskBoard
from .timeline import ResearchTimeline
from .version import VersionManager


class ResearchWorkspace:
    """Unified entrypoint for AIRS projects, sessions, artifacts, and audits."""

    def __init__(self, name: str = "AIRS Research Workspace", owner: str = "workspace-user") -> None:
        self.workspace_id = f"ws-{uuid4().hex[:12]}"
        self.name = name
        self.owner = owner
        self.audit = AuditLog()
        self.projects = ProjectManager(self.audit)
        self.sessions = SessionManager(self.audit)
        self.timeline = ResearchTimeline()
        self.artifacts = ArtifactManager(self.audit)
        self.task_board = TaskBoard(self.audit)
        self.memory = WorkspaceMemory(self.audit)
        self.snapshots = SnapshotManager(self.audit)
        self.versions = VersionManager(self.audit)
        self.replay = ReplayManager(self.audit)
        self.exporter = WorkspaceExport(self.audit)
        self.collaboration = CollaborationManager(self.audit)
        self.audit.record("WORKSPACE_CREATED", owner, "workspace", self.workspace_id, {"name": name})

    def create_project(self, name: str, research_question: str, scope: dict[str, Any] | None = None, refs: list[str] | None = None) -> ResearchProject:
        return self.projects.create_project(name, research_question, scope, self.owner, refs)

    def open_session(self, project_id: str, workflow_id: str, intent: dict[str, Any] | None = None, refs: list[str] | None = None) -> WorkspaceSession:
        runtime_id = f"rt-{uuid4().hex[:10]}"
        session = self.sessions.open_session(project_id, runtime_id, workflow_id, intent, refs, self.owner)
        self.timeline.append(project_id, session.session_id, "SESSION_OPENED", "Workspace session opened", {"workflow_id": workflow_id, "runtime_id": runtime_id})
        return session

    def register_artifact(self, project_id: str, session_id: str, artifact_type: str, title: str, uri: str, refs: list[str] | None = None) -> dict[str, Any]:
        artifact = self.artifacts.register(project_id, session_id, artifact_type, title, uri, refs, actor=self.owner)
        self.timeline.append(project_id, session_id, "ARTIFACT_REGISTERED", title, {"artifact_id": artifact.artifact_id, "artifact_type": artifact_type})
        return artifact.to_dict()

    def dashboard(self, project_id: str) -> str:
        project = self.projects.get_project(project_id).to_dict()
        sessions = self.sessions.list_sessions(project_id)
        artifacts = self.artifacts.list_artifacts(project_id)
        tasks = self.task_board.list_tasks(project_id)
        events = self.timeline.list_events(project_id)
        return "\n".join(
            [
                f"# {project['name']} Workspace Dashboard",
                "",
                "## Project",
                f"- Project ID: {project_id}",
                f"- Research Question: {project['research_question']}",
                f"- Status: {project['status']}",
                "",
                "## Sessions",
                f"- Count: {len(sessions)}",
                "",
                "## Task Board",
                f"- Count: {len(tasks)}",
                "",
                "## Artifacts",
                f"- Count: {len(artifacts)}",
                "",
                "## Timeline",
                f"- Count: {len(events)}",
                "",
                f"免责声明：{DISCLAIMER}",
            ]
        )

    def state(self) -> dict[str, Any]:
        return {
            "workspace_id": self.workspace_id,
            "name": self.name,
            "owner": self.owner,
            "projects": self.projects.list_projects(),
            "sessions": self.sessions.list_sessions(),
            "tasks": self.task_board.list_tasks(),
            "artifacts": self.artifacts.list_artifacts(),
            "timeline": self.timeline.list_events(),
            "snapshots": self.snapshots.list_snapshots(),
            "audit_log": self.audit.list_records(),
            "disclaimer": DISCLAIMER,
        }

    def export(self) -> dict[str, Any]:
        return self.exporter.export_bundle(self.state(), self.owner)
