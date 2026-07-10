"""Replay Manager for AIRS Workspace snapshots."""
from __future__ import annotations

from copy import deepcopy
from typing import Any

from .audit import AuditLog, DISCLAIMER


class ReplayManager:
    """Build replay plans from Workspace snapshots without executing trades."""

    def __init__(self, audit: AuditLog | None = None) -> None:
        self.audit = audit or AuditLog()

    def build_replay_plan(self, snapshot: dict[str, Any], actor: str = "verification-agent") -> dict[str, Any]:
        plan = {
            "replay_id": f"replay-{snapshot.get('snapshot_id', 'unknown')}",
            "source_snapshot_id": snapshot.get("snapshot_id"),
            "runtime_plan_ref": snapshot.get("state", {}).get("runtime_plan_ref"),
            "artifact_refs": snapshot.get("state", {}).get("artifact_refs", []),
            "expected_checks": ["schema_validation", "artifact_integrity", "disclaimer_coverage", "audit_traceability"],
            "disclaimer": DISCLAIMER,
        }
        self.audit.record("REPLAY_PLAN_BUILT", actor, "snapshot", str(snapshot.get("snapshot_id")), deepcopy(plan))
        return plan
