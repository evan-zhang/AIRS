"""Audit log for AIRS Workspace actions."""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
from uuid import uuid4


DISCLAIMER = "仅供研究参考，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。"


@dataclass
class AuditRecord:
    action: str
    actor: str
    target_type: str
    target_id: str
    payload: dict[str, Any] = field(default_factory=dict)
    trace_id: str | None = None
    record_id: str = field(default_factory=lambda: f"audit-{uuid4().hex[:12]}")
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    disclaimer: str = DISCLAIMER

    def to_dict(self) -> dict[str, Any]:
        return {
            "record_id": self.record_id,
            "action": self.action,
            "actor": self.actor,
            "target_type": self.target_type,
            "target_id": self.target_id,
            "payload": dict(self.payload),
            "trace_id": self.trace_id,
            "created_at": self.created_at,
            "disclaimer": self.disclaimer,
        }


class AuditLog:
    """Append-only in-memory audit log."""

    def __init__(self) -> None:
        self._records: list[AuditRecord] = []

    def record(
        self,
        action: str,
        actor: str,
        target_type: str,
        target_id: str,
        payload: dict[str, Any] | None = None,
        trace_id: str | None = None,
    ) -> AuditRecord:
        item = AuditRecord(action, actor, target_type, target_id, payload or {}, trace_id)
        self._records.append(item)
        return item

    def list_records(self, target_id: str | None = None) -> list[dict[str, Any]]:
        records = self._records
        if target_id:
            records = [record for record in records if record.target_id == target_id]
        return [record.to_dict() for record in records]
