"""Thin Planner -> Runtime orchestration boundary."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from common.contract import CONTRACT_VERSION
from runtime import RuntimeCore


DISCLAIMER = "AIRS Orchestrator 仅用于研究流程编排和质量控制，不构成投资建议。"


class OrchestratorError(ValueError):
    """Raised when a Planner output cannot be safely handed to Runtime."""


@dataclass(frozen=True)
class Orchestrator:
    """Validate Planner output and execute the Runtime workflow.

    The boundary is intentionally thin for QA Sprint 2: Planner owns plan
    construction, Runtime owns task execution, and Orchestrator owns handoff
    validation plus trace metadata.
    """

    runtime: RuntimeCore | None = None

    def run(self, plan: dict[str, Any], *, case_id: str | None = None) -> dict[str, Any]:
        workflow = self.workflow_from_plan(plan, case_id=case_id)
        result = (self.runtime or RuntimeCore()).run_workflow(workflow)
        return {
            "orchestrator_version": "0.1.0",
            "contract_version": CONTRACT_VERSION,
            "planner_ref": plan["plan_id"],
            "runtime": result,
            "boundary": {
                "planner_owns": "research plan and task graph",
                "orchestrator_owns": "contract validation and runtime handoff",
                "runtime_owns": "agent dispatch, state and events",
            },
            "disclaimer": DISCLAIMER,
        }

    def workflow_from_plan(self, plan: dict[str, Any], *, case_id: str | None = None) -> dict[str, Any]:
        self.validate_plan(plan)
        workflow = dict(plan["required_runtime"])
        workflow.setdefault("plan_id", plan["plan_id"])
        workflow["contract_version"] = workflow.get("contract_version", CONTRACT_VERSION)
        if case_id:
            workflow["case_id"] = case_id
        return workflow

    def validate_plan(self, plan: dict[str, Any]) -> None:
        missing = [key for key in ("plan_id", "required_runtime") if key not in plan]
        if missing:
            raise OrchestratorError(f"planner output missing required fields: {', '.join(missing)}")
        workflow = plan["required_runtime"]
        if not isinstance(workflow, dict):
            raise OrchestratorError("required_runtime must be a workflow dict")
        tasks = workflow.get("tasks")
        if not isinstance(tasks, list) or not tasks:
            raise OrchestratorError("required_runtime.tasks must be a non-empty list")
        task_ids: set[str] = set()
        for task in tasks:
            if not isinstance(task, dict):
                raise OrchestratorError("runtime task must be a dict")
            task_id = task.get("task_id")
            if not task_id:
                raise OrchestratorError("runtime task missing task_id")
            if task_id in task_ids:
                raise OrchestratorError(f"duplicate runtime task_id: {task_id}")
            task_ids.add(task_id)
        for task in tasks:
            deps = set(task.get("dependencies", []))
            unknown = sorted(deps - task_ids)
            if unknown:
                raise OrchestratorError(f"task {task['task_id']} has unknown dependencies: {', '.join(unknown)}")


def run_planned_workflow(plan: dict[str, Any], *, case_id: str | None = None) -> dict[str, Any]:
    return Orchestrator().run(plan, case_id=case_id)
