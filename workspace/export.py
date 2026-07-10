"""Export and import helpers for AIRS Workspace."""
from __future__ import annotations

from copy import deepcopy
from typing import Any

from .audit import AuditLog, DISCLAIMER


class WorkspaceExport:
    """Serialize Workspace state for review, verification, or migration."""

    def __init__(self, audit: AuditLog | None = None) -> None:
        self.audit = audit or AuditLog()

    def export_bundle(self, workspace_state: dict[str, Any], actor: str = "workspace-user") -> dict[str, Any]:
        bundle = {
            "bundle_type": "AIRS_WORKSPACE_EXPORT",
            "version": "0.1.0",
            "workspace": deepcopy(workspace_state),
            "integrity_checks": ["projects", "sessions", "artifacts", "snapshots", "audit_log"],
            "disclaimer": DISCLAIMER,
        }
        self.audit.record("WORKSPACE_EXPORTED", actor, "workspace", str(workspace_state.get("workspace_id", "workspace")), {"version": bundle["version"]})
        return bundle

    def import_bundle(self, bundle: dict[str, Any], actor: str = "workspace-user") -> dict[str, Any]:
        if bundle.get("bundle_type") != "AIRS_WORKSPACE_EXPORT":
            raise ValueError("unsupported workspace bundle")
        workspace = deepcopy(bundle.get("workspace", {}))
        self.audit.record("WORKSPACE_IMPORTED", actor, "workspace", str(workspace.get("workspace_id", "workspace")), {"version": bundle.get("version")})
        return workspace
