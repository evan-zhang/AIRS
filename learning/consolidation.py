"""Memory consolidation for learning artifacts."""
from __future__ import annotations

from typing import Any

from .feedback import DISCLAIMER


class MemoryConsolidator:
    """Builds a compact auditable memory packet from learning results."""

    def consolidate(self, learning_result: dict[str, Any]) -> dict[str, Any]:
        return {
            "memory_type": "learning_consolidation",
            "source_refs": learning_result.get("source_refs", []),
            "pattern_count": len(learning_result.get("patterns", [])),
            "rule_count": len(learning_result.get("rules", [])),
            "optimization_count": len(learning_result.get("optimizations", [])),
            "governance_status": "pending_human_review",
            "retention": "保留规则候选、证据引用和回滚计划；不保留无来源结论。",
            "disclaimer": DISCLAIMER,
        }

