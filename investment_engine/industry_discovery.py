"""Industry discovery component for investment research."""

from __future__ import annotations

from typing import Any


def discover_industry(theme: dict[str, Any]) -> dict[str, Any]:
    return {
        "component": "industry_discovery",
        "methodology_refs": ["docs/methodology/industry-lifecycle.md", "docs/methodology/policy-driven.md"],
        "industry_stage": "结构性成长阶段",
        "demand_drivers": theme["signals"][:2],
        "supply_constraints": theme["signals"][2:],
        "counter_consensus": f"{theme['topic']} 可能存在资本开支前置、需求兑现慢于预期或竞争加剧的反方情景。",
    }
