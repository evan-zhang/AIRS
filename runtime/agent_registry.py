"""Agent Registry for AIRS Research Agent Runtime."""
from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum
from typing import Any
class AgentType(str, Enum):
    SYNC = "sync"
    ASYNC = "async"
    PARALLEL = "parallel"
    LONG_RUNNING = "long_running"
    HUMAN_IN_THE_LOOP = "human_in_the_loop"
@dataclass(frozen=True)
class AgentDefinition:
    agent_id: str
    agent_type: AgentType
    description: str
    capabilities: list[str] = field(default_factory=list)
    input_schema: dict[str, Any] = field(default_factory=dict)
    output_schema: dict[str, Any] = field(default_factory=dict)
    required_refs: list[str] = field(default_factory=list)
    timeout_seconds: int = 60
    max_retries: int = 1
    human_required: bool = False
class AgentRegistry:
    def __init__(self) -> None:
        self._agents: dict[str, AgentDefinition] = {}
    def register(self, definition: AgentDefinition) -> None:
        if not definition.agent_id: raise ValueError("agent_id is required")
        self._agents[definition.agent_id] = definition
    def get(self, agent_id: str) -> AgentDefinition:
        try: return self._agents[agent_id]
        except KeyError as exc: raise KeyError(f"unknown agent: {agent_id}") from exc
    def list_ids(self) -> list[str]: return sorted(self._agents)
    def to_dict(self) -> dict[str, Any]: return {k: {**v.__dict__, "agent_type": v.agent_type.value} for k, v in self._agents.items()}
def default_registry() -> AgentRegistry:
    registry = AgentRegistry()
    registry.register(AgentDefinition("methodology_selector", AgentType.SYNC, "选择 M2 方法论引用", ["methodology_ref"]))
    registry.register(AgentDefinition("evidence_collector", AgentType.ASYNC, "采集并登记证据引用", ["evidence_ref"], required_refs=["docs/evidence/evidence-architecture.md"]))
    registry.register(AgentDefinition("parallel_researcher", AgentType.PARALLEL, "并行拆分研究子任务", ["parallel_research"]))
    registry.register(AgentDefinition("long_running_researcher", AgentType.LONG_RUNNING, "长周期研究和 checkpoint", ["checkpoint"]))
    registry.register(AgentDefinition("human_reviewer", AgentType.HUMAN_IN_THE_LOOP, "人工确认或补充输入", ["human_review"], human_required=True))
    registry.register(AgentDefinition("report_composer", AgentType.SYNC, "汇总 Runtime 输出为报告输入", ["report_ref"], required_refs=["templates/report/research-report-template.md"]))
    return registry
