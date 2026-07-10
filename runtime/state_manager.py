"""Runtime State Manager."""
from __future__ import annotations
from copy import deepcopy
from typing import Any
class StateManager:
    def __init__(self) -> None:
        self.runtime_state: dict[str, Any] = {}; self.task_states: dict[str, str] = {}; self.agent_states: dict[str, str] = {}; self.context_snapshots: list[dict[str, Any]] = []
    def set_runtime(self, **values: Any) -> None: self.runtime_state.update(values)
    def set_task_state(self, task_id: str, state: str) -> None: self.task_states[task_id] = state
    def set_agent_state(self, session_id: str, state: str) -> None: self.agent_states[session_id] = state
    def snapshot(self, snapshot: dict[str, Any]) -> None: self.context_snapshots.append(deepcopy(snapshot))
    def final_state(self) -> dict[str, Any]:
        status = "PASS" if self.task_states and all(v in {"COMPLETED", "WAITING_FOR_HUMAN"} for v in self.task_states.values()) else "PARTIAL"
        return {"runtime_state": deepcopy(self.runtime_state), "task_states": deepcopy(self.task_states), "agent_states": deepcopy(self.agent_states), "context_snapshots": deepcopy(self.context_snapshots), "quality_gate": status}
