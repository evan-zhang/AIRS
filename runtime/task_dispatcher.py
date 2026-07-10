"""Task Dispatcher for Runtime Plans."""
from __future__ import annotations
from typing import Any
from .agent_context import AgentContext
from .agent_lifecycle import AgentLifecycle
from .agent_registry import AgentRegistry
from .agent_session import AgentSession
from .cancellation_manager import CancellationManager
from .event_bus import EventBus
from .resource_manager import ResourceManager
from .state_manager import StateManager
class TaskDispatcher:
    def __init__(self, registry: AgentRegistry, event_bus: EventBus, state_manager: StateManager, resource_manager: ResourceManager | None = None) -> None:
        self.registry = registry; self.event_bus = event_bus; self.state_manager = state_manager; self.resource_manager = resource_manager or ResourceManager(); self.lifecycle = AgentLifecycle(event_bus); self.cancellation = CancellationManager(); self.sessions: list[AgentSession] = []
    def dispatch(self, runtime_id: str, workflow_id: str, tasks: list[dict[str, Any]]) -> list[dict[str, Any]]:
        outputs: list[dict[str, Any]] = []; completed: set[str] = set()
        for task in tasks:
            task_id = task["task_id"]; deps = set(task.get("dependencies", []))
            if not deps.issubset(completed):
                self.state_manager.set_task_state(task_id, "BLOCKED"); self.event_bus.publish("TASK_BLOCKED", task_id=task_id, payload={"dependencies": sorted(deps - completed)}); continue
            if self.cancellation.is_cancelled(task_id):
                self.state_manager.set_task_state(task_id, "CANCELLED"); self.event_bus.publish("TASK_CANCELLED", task_id=task_id); continue
            definition = self.registry.get(task["agent_id"]); context = AgentContext(runtime_id, workflow_id, task_id, task.get("input", {}), task.get("refs", [])); session = AgentSession(definition, context); self.sessions.append(session)
            self.state_manager.set_task_state(task_id, "DISPATCHED"); self.state_manager.set_agent_state(session.session_id, session.status); self.event_bus.publish("TASK_DISPATCHED", session_id=session.session_id, task_id=task_id, agent_id=definition.agent_id, payload={"agent_type": definition.agent_type.value})
            if not self.resource_manager.acquire():
                self.state_manager.set_task_state(task_id, "RESOURCE_LIMITED"); self.event_bus.publish("RESOURCE_LIMITED", session_id=session.session_id, task_id=task_id, agent_id=definition.agent_id, severity="WARN"); continue
            try:
                self.lifecycle.initialize(session); output = self.lifecycle.run(session); outputs.append(output); completed.add(task_id); self.state_manager.set_task_state(task_id, session.status if session.status == "WAITING_FOR_HUMAN" else "COMPLETED"); self.state_manager.set_agent_state(session.session_id, session.status); self.state_manager.snapshot(context.snapshot())
            finally: self.resource_manager.release()
        return outputs
