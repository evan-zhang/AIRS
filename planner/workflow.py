"""Workflow planner."""

from __future__ import annotations

from typing import Any


def plan_workflow(goal: dict[str, Any], intent: dict[str, Any], dependencies: dict[str, Any]) -> dict[str, Any]:
    tasks = []
    for index, component in enumerate(dependencies["critical_path"], start=1):
        deps = [] if index == 1 else [dependencies["critical_path"][index - 2]]
        tasks.append(
            {
                "task_id": component,
                "agent_role": "Research Agent" if component not in {"review_plan", "runtime_plan"} else "Review Agent",
                "dependencies": deps,
                "expected_output": component,
                "quality_gate": "planner_gate",
            }
        )
    return {
        "workflow_id": f"workflow-{goal['goal_id']}",
        "description": f"{goal['subject']} 的 Planner Workflow",
        "tasks": tasks,
        "orchestrator_ref": "docs/orchestrator/orchestrator-architecture.md",
        "runtime_entry_condition": "只允许接收 planner_generated_runtime_plan",
        "required_methodologies": intent["required_methodologies"],
        "required_skills": intent["required_skills"],
    }
