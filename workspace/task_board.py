"""Task Board for AIRS Workspace."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any
from uuid import uuid4

from .audit import AuditLog, DISCLAIMER


@dataclass
class WorkspaceTask:
    project_id: str
    session_id: str
    title: str
    agent_role: str
    status: str = "TODO"
    refs: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)
    task_id: str = field(default_factory=lambda: f"wst-{uuid4().hex[:12]}")
    disclaimer: str = DISCLAIMER

    def to_dict(self) -> dict[str, Any]:
        return {
            "task_id": self.task_id,
            "project_id": self.project_id,
            "session_id": self.session_id,
            "title": self.title,
            "agent_role": self.agent_role,
            "status": self.status,
            "refs": list(self.refs),
            "metadata": dict(self.metadata),
            "disclaimer": self.disclaimer,
        }


class TaskBoard:
    """Kanban-style task registry for research execution."""

    def __init__(self, audit: AuditLog | None = None) -> None:
        self.audit = audit or AuditLog()
        self._tasks: dict[str, WorkspaceTask] = {}

    def add_task(self, project_id: str, session_id: str, title: str, agent_role: str, refs: list[str] | None = None) -> WorkspaceTask:
        task = WorkspaceTask(project_id, session_id, title, agent_role, refs=refs or [])
        self._tasks[task.task_id] = task
        self.audit.record("TASK_ADDED", agent_role, "workspace_task", task.task_id, task.to_dict())
        return task

    def move_task(self, task_id: str, status: str, actor: str = "workspace-user") -> WorkspaceTask:
        task = self._tasks[task_id]
        task.status = status
        self.audit.record("TASK_MOVED", actor, "workspace_task", task_id, {"status": status})
        return task

    def list_tasks(self, project_id: str | None = None) -> list[dict[str, Any]]:
        tasks = self._tasks.values()
        if project_id:
            tasks = [task for task in tasks if task.project_id == project_id]
        return [task.to_dict() for task in tasks]
