"""Resource planner."""

from __future__ import annotations

from typing import Any


def plan_resources(intent: dict[str, Any], scope: dict[str, Any]) -> dict[str, Any]:
    depth = intent["report_depth"]
    connector_count = len(intent["required_connectors"])
    return {
        "resource_profile": "deep_research" if depth == "deep" else "standard_research",
        "connectors": intent["required_connectors"],
        "methodologies": intent["required_methodologies"],
        "skills": intent["required_skills"],
        "workspace_artifacts": ["research_goal", "research_plan", "evidence_plan", "kg_plan", "score_plan", "report_plan"],
        "max_concurrency": min(4, max(2, connector_count)),
        "human_review_required": True,
        "scope_subject": scope["subject"],
    }
