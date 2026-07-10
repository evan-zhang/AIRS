"""Shared Planner -> Runtime production contract.

The Planner owns task graph generation. The Runtime owns concrete agent
execution. This module is the single production boundary that translates
Planner task roles into Runtime registry `agent_id` values.
"""

from __future__ import annotations

from typing import Any


CONTRACT_VERSION = "planner-runtime-contract-v1"
DEFAULT_AGENT_ID = "methodology_selector"
RUNTIME_REF = "docs/runtime/runtime-architecture.md"
RUNTIME_AGENT_IDS = {
    "methodology_selector",
    "evidence_collector",
    "parallel_researcher",
    "long_running_researcher",
    "human_reviewer",
    "report_composer",
}

TASK_AGENT_CONTRACT: dict[str, str] = {
    "goal_analysis": "methodology_selector",
    "scope": "methodology_selector",
    "methodology_selection": "methodology_selector",
    "connector_plan": "evidence_collector",
    "skill_plan": "parallel_researcher",
    "evidence_plan": "evidence_collector",
    "knowledge_graph_plan": "parallel_researcher",
    "score_plan": "report_composer",
    "report_plan": "report_composer",
    "review_plan": "human_reviewer",
    "runtime_plan": "report_composer",
}

ROLE_AGENT_CONTRACT: dict[str, str] = {
    "research agent": "parallel_researcher",
    "review agent": "human_reviewer",
    "verification agent": "human_reviewer",
    "code agent": "methodology_selector",
    "researcher": "parallel_researcher",
    "analyst": "evidence_collector",
    "evidence": "evidence_collector",
    "reviewer": "human_reviewer",
    "reporter": "report_composer",
    "default": DEFAULT_AGENT_ID,
}

AGENT_CONTRACT: dict[str, str] = {
    **TASK_AGENT_CONTRACT,
    **ROLE_AGENT_CONTRACT,
}


def _normalize(value: str | None) -> str:
    return (value or "").strip().lower().replace("-", "_")


def resolve_agent_id(role: str | None, *, task_id: str | None = None) -> str:
    """Resolve a Planner role or task id to a Runtime registry agent id."""

    if task_id:
        normalized_task = _normalize(task_id)
        if normalized_task in TASK_AGENT_CONTRACT:
            return TASK_AGENT_CONTRACT[normalized_task]

    normalized_role = _normalize(role)
    if normalized_role in RUNTIME_AGENT_IDS:
        return normalized_role
    if normalized_role in TASK_AGENT_CONTRACT:
        return TASK_AGENT_CONTRACT[normalized_role]
    if normalized_role in ROLE_AGENT_CONTRACT:
        return ROLE_AGENT_CONTRACT[normalized_role]
    if role in AGENT_CONTRACT:
        return AGENT_CONTRACT[role]
    return DEFAULT_AGENT_ID


def runtime_task_from_planner_task(task: dict[str, Any], *, plan_id: str, case_id: str | None = None) -> dict[str, Any]:
    """Return a RuntimeCore-ready task using the shared production contract."""

    task_id = task["task_id"]
    runtime_task = dict(task)
    runtime_task["agent_id"] = resolve_agent_id(task.get("agent_role") or task.get("agent_id"), task_id=task_id)
    task_input = dict(runtime_task.get("input", {}))
    task_input.setdefault("planner_task", task)
    task_input.setdefault("plan_id", plan_id)
    if case_id:
        task_input["case_id"] = case_id
    runtime_task["input"] = task_input
    refs = list(runtime_task.get("refs", []))
    if RUNTIME_REF not in refs:
        refs.append(RUNTIME_REF)
    runtime_task["refs"] = refs
    runtime_task["contract_version"] = CONTRACT_VERSION
    return runtime_task
