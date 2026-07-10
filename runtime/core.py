"""Runtime Core main entrypoint."""
from __future__ import annotations
from datetime import datetime, timezone
from typing import Any
from uuid import uuid4
from .agent_registry import AgentRegistry, default_registry
from .event_bus import EventBus
from .message_bus import MessageBus
from .resource_manager import ResourceManager
from .runtime_monitor import RuntimeMonitor
from .state_manager import StateManager
from .task_dispatcher import TaskDispatcher
class RuntimeCore:
    def __init__(self, registry: AgentRegistry | None = None) -> None:
        self.registry = registry or default_registry(); self.event_bus = EventBus(); self.message_bus = MessageBus(self.event_bus); self.state_manager = StateManager(); self.resource_manager = ResourceManager(); self.dispatcher = TaskDispatcher(self.registry, self.event_bus, self.state_manager, self.resource_manager); self.monitor = RuntimeMonitor(self.event_bus, self.message_bus, self.state_manager)
    def run_workflow(self, workflow: dict[str, Any]) -> dict[str, Any]:
        runtime_id = workflow.get("runtime_id") or f"rt-{uuid4().hex[:12]}"; workflow_id = workflow.get("workflow_id", "workflow-runtime"); tasks = workflow.get("tasks", [])
        self.state_manager.set_runtime(runtime_id=runtime_id, workflow_id=workflow_id, started_at=datetime.now(timezone.utc).isoformat(), status="RUNNING"); self.event_bus.publish("RUNTIME_STARTED", payload={"runtime_id": runtime_id, "workflow_id": workflow_id})
        outputs = self.dispatcher.dispatch(runtime_id, workflow_id, tasks)
        self.state_manager.set_runtime(status="COMPLETED", completed_at=datetime.now(timezone.utc).isoformat()); self.event_bus.publish("RUNTIME_COMPLETED", payload={"runtime_id": runtime_id, "workflow_id": workflow_id})
        timeline = self.event_bus.list_events(); agent_graph = {"nodes": self.registry.list_ids(), "edges": [{"from": t.get("dependencies", []), "to": t["task_id"]} for t in tasks]}; final_state = self.state_manager.final_state()
        return {"runtime_plan": workflow, "agent_graph": agent_graph, "execution_timeline": timeline, "event_log": timeline, "context_snapshot": final_state["context_snapshots"], "outputs": outputs, "final_state": final_state, "metrics": self.monitor.metrics()}
