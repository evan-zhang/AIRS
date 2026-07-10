"""Plan optimizer."""

from __future__ import annotations

from typing import Any


def optimize_plan(plan: dict[str, Any]) -> dict[str, Any]:
    optimized = dict(plan)
    risks = list(optimized.get("risks", []))
    if optimized["confidence"]["overall_confidence"] < 0.75:
        risks.append("整体置信度未达到高置信区间，需要增加证据采集或人工复核。")
    optimized["optimization"] = {
        "deduplicated_connectors": sorted(set(plan["required_connectors"])),
        "parallelizable_tasks": ["connector_plan", "evidence_plan", "knowledge_graph_plan"],
        "must_not_bypass": ["planner", "evidence", "review"],
        "optimization_note": "优先并行 Connector 和 Evidence 规划，但 Runtime 启动必须等待 Planner Gate 完成。",
    }
    optimized["risks"] = risks
    return optimized
