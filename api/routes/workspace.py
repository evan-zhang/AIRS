"""Workspace route handler."""

from __future__ import annotations

from workspace import ResearchWorkspace


DISCLAIMER = "AIRS Workspace API 仅用于研究资产管理，不构成投资建议。"


def handle_workspace() -> dict[str, object]:
    workspace = ResearchWorkspace(name="AIRS Platform Workspace", owner="api-user")
    project = workspace.create_project(
        "AIRS Platform Demo",
        "展示 AIRS Platform 1.0 的 Workspace、Session、Artifact 和 Audit 状态。",
        scope={"mode": "demo", "release": "RELEASE-001"},
        refs=["docs/product/overview.md"],
    )
    session = workspace.open_session(project.project_id, "platform-demo")
    workspace.register_artifact(project.project_id, session.session_id, "report", "Platform overview", "docs/product/overview.md")
    state = workspace.state()
    state["disclaimer"] = DISCLAIMER
    return {"status": "ok", "workspace": state, "disclaimer": DISCLAIMER}

