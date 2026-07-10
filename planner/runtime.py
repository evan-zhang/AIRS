"""Runtime plan generator."""

from __future__ import annotations

from typing import Any


def plan_runtime(goal: dict[str, Any], workflow: dict[str, Any], budget: dict[str, Any]) -> dict[str, Any]:
    return {
        "runtime_id": f"runtime-from-planner-{goal['goal_id']}",
        "workflow_id": workflow["workflow_id"],
        "planner_generated": True,
        "raw_user_request_allowed": False,
        "runtime_boundary": "Runtime 只能执行 Planner 生成的 Workflow、Task Graph 和 Context，不直接接收用户请求。",
        "agent_types": ["sync", "parallel", "long_running", "human_in_the_loop"],
        "max_concurrency": budget["max_concurrency"],
        "timeout_minutes": budget["estimated_time_minutes"] + 20,
        "tasks": workflow["tasks"],
        "expected_outputs": ["event_log", "state_snapshot", "artifact_refs", "final_state"],
    }
