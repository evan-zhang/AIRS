"""Risk analysis component for investment research."""

from __future__ import annotations

from typing import Any


def analyze_risks(thesis: dict[str, Any]) -> dict[str, Any]:
    topic = thesis["topic"]
    risks = [
        {"risk_id": "risk-demand", "name": "需求兑现风险", "severity": "medium", "evidence_refs": ["ev-counter-01"]},
        {"risk_id": "risk-margin", "name": "竞争和利润率风险", "severity": "medium", "evidence_refs": ["ev-counter-02"]},
        {"risk_id": "risk-policy", "name": "政策或监管变化风险", "severity": "low", "evidence_refs": ["ev-03"]},
    ]
    return {
        "component": "risk",
        "topic": topic,
        "methodology_refs": ["docs/methodology/risk.md", "skills/risk/risk-skill.md"],
        "risks": risks,
        "risk_summary": f"{topic} 的主要风险来自需求、利润率、政策和证据缺口，需要持续复核。",
    }
