"""Agent Lifecycle state transitions."""
from __future__ import annotations
from .agent_session import AgentSession
from .event_bus import EventBus
class AgentLifecycle:
    def __init__(self, event_bus: EventBus) -> None: self.event_bus = event_bus
    def initialize(self, session: AgentSession) -> None:
        session.initialize(); self.event_bus.publish("AGENT_INITIALIZED", session_id=session.session_id, task_id=session.context.task_id, agent_id=session.definition.agent_id)
    def run(self, session: AgentSession) -> dict:
        self.event_bus.publish("AGENT_RUNNING", session_id=session.session_id, task_id=session.context.task_id, agent_id=session.definition.agent_id)
        output = session.run(); event = "AGENT_WAITING_FOR_HUMAN" if session.status == "WAITING_FOR_HUMAN" else "AGENT_COMPLETED"
        self.event_bus.publish(event, session_id=session.session_id, task_id=session.context.task_id, agent_id=session.definition.agent_id, payload=output); return output
    def pause(self, session: AgentSession) -> None:
        session.pause(); self.event_bus.publish("AGENT_PAUSED", session_id=session.session_id, task_id=session.context.task_id, agent_id=session.definition.agent_id)
    def resume(self, session: AgentSession) -> None:
        session.resume(); self.event_bus.publish("AGENT_RESUMED", session_id=session.session_id, task_id=session.context.task_id, agent_id=session.definition.agent_id)
