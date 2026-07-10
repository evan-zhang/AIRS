"""Dependency planner for AIRS research plans."""

from __future__ import annotations

from typing import Any


BASE_COMPONENTS = [
    "goal_analysis",
    "scope",
    "methodology_selection",
    "connector_plan",
    "skill_plan",
    "evidence_plan",
    "knowledge_graph_plan",
    "score_plan",
    "report_plan",
    "review_plan",
    "runtime_plan",
]


def plan_dependencies(intent: dict[str, Any]) -> dict[str, Any]:
    edges = [
        ("goal_analysis", "scope"),
        ("scope", "methodology_selection"),
        ("methodology_selection", "connector_plan"),
        ("connector_plan", "evidence_plan"),
        ("methodology_selection", "skill_plan"),
        ("skill_plan", "knowledge_graph_plan"),
        ("evidence_plan", "knowledge_graph_plan"),
        ("knowledge_graph_plan", "score_plan"),
        ("score_plan", "report_plan"),
        ("report_plan", "review_plan"),
        ("review_plan", "runtime_plan"),
    ]
    return {
        "components": BASE_COMPONENTS,
        "edges": [{"from": left, "to": right} for left, right in edges],
        "critical_path": BASE_COMPONENTS,
        "runtime_blocked_until_planner_complete": True,
        "intent_ref": intent["primary_intent"],
    }
