"""Agent Context for AIRS Research Agent Runtime."""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any
from copy import deepcopy
DISCLAIMER = "仅供研究参考，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。"
@dataclass
class AgentContext:
    runtime_id: str
    workflow_id: str
    task_id: str
    input_data: dict[str, Any] = field(default_factory=dict)
    refs: list[str] = field(default_factory=list)
    memory: dict[str, Any] = field(default_factory=dict)
    output_data: dict[str, Any] = field(default_factory=dict)
    disclaimer: str = DISCLAIMER
    def snapshot(self) -> dict[str, Any]:
        return {"runtime_id": self.runtime_id, "workflow_id": self.workflow_id, "task_id": self.task_id, "input_data": deepcopy(self.input_data), "refs": list(self.refs), "memory": deepcopy(self.memory), "output_data": deepcopy(self.output_data), "disclaimer": self.disclaimer}
