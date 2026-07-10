"""Budget planner."""

from __future__ import annotations

from typing import Any


def plan_budget(resources: dict[str, Any]) -> dict[str, Any]:
    connector_count = len(resources["connectors"])
    methodology_count = len(resources["methodologies"])
    skill_count = len(resources["skills"])
    estimated_time = 30 + connector_count * 8 + methodology_count * 6 + skill_count * 5
    cost_units = connector_count * 2 + methodology_count * 3 + skill_count * 2
    return {
        "estimated_time_minutes": estimated_time,
        "estimated_cost_units": cost_units,
        "max_concurrency": resources["max_concurrency"],
        "budget_rationale": "按 Connector 数量、Methodology 数量、Skill 数量和人工复核成本估算。",
        "budget_gate": "PASS" if estimated_time <= 120 else "CONDITIONAL_PASS",
    }
