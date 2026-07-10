"""Agent Session for AIRS Runtime."""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any
from uuid import uuid4
from .agent_context import AgentContext
from .agent_registry import AgentDefinition, AgentType
@dataclass
class AgentSession:
    definition: AgentDefinition
    context: AgentContext
    session_id: str = field(default_factory=lambda: f"ses-{uuid4().hex[:12]}")
    status: str = "CREATED"
    attempts: int = 0
    def initialize(self) -> None: self.status = "INITIALIZED"
    def pause(self) -> None: self.status = "PAUSED"
    def resume(self) -> None: self.status = "RESUMED"
    def run(self) -> dict[str, Any]:
        self.attempts += 1; self.status = "RUNNING"
        output = {"agent_id": self.definition.agent_id, "agent_type": self.definition.agent_type.value, "task_id": self.context.task_id, "refs": self.context.refs + self.definition.required_refs, "result": f"{self.definition.description} 已由 Runtime 调度完成", "disclaimer": self.context.disclaimer}
        if self.definition.agent_type is AgentType.ASYNC: output["async_state"] = "READY_FOR_RESUME"
        elif self.definition.agent_type is AgentType.PARALLEL: output["parallel_branches"] = self.context.input_data.get("branches", ["branch-a", "branch-b"])
        elif self.definition.agent_type is AgentType.LONG_RUNNING: output["checkpoint"] = {"step": self.attempts, "status": "CHECKPOINT_RECORDED"}
        elif self.definition.agent_type is AgentType.HUMAN_IN_THE_LOOP:
            self.status = "WAITING_FOR_HUMAN"; output["human_prompt"] = self.context.input_data.get("human_prompt", "请确认研究边界和证据缺口。"); self.context.output_data = output; return output
        self.status = "COMPLETED"; self.context.output_data = output; return output
    def destroy(self) -> None: self.status = "DESTROYED"
