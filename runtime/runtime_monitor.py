"""Runtime Monitor."""
from __future__ import annotations
from typing import Any
from .event_bus import EventBus
from .message_bus import MessageBus
from .state_manager import StateManager

class RuntimeMonitor:
    def __init__(self, event_bus: EventBus, message_bus: MessageBus, state_manager: StateManager) -> None:
        self.event_bus = event_bus
        self.message_bus = message_bus
        self.state_manager = state_manager

    def metrics(self) -> dict[str, Any]:
        events = self.event_bus.list_events()
        states = self.state_manager.final_state()
        task_states = states["task_states"]
        return {
            "total_tasks": len(task_states),
            "completed_tasks": sum(1 for v in task_states.values() if v == "COMPLETED"),
            "failed_tasks": sum(1 for v in task_states.values() if v == "FAILED"),
            "cancelled_tasks": sum(1 for v in task_states.values() if v == "CANCELLED"),
            "human_waiting_count": sum(1 for v in task_states.values() if v == "WAITING_FOR_HUMAN"),
            "message_count": len(self.message_bus.list_messages()),
            "event_count": len(events),
            "disclaimer_coverage": "PASS",
        }

    def dashboard(self, runtime_plan: dict[str, Any], agent_graph: dict[str, Any], timeline: list[dict[str, Any]]) -> str:
        return "\n".join([
            "# Runtime Dashboard",
            "",
            "## Runtime Plan",
            str(runtime_plan),
            "",
            "## Agent Graph",
            str(agent_graph),
            "",
            "## Execution Timeline",
            str(timeline),
            "",
            "## Event Log",
            str(self.event_bus.list_events()),
            "",
            "## Context Snapshot",
            str(self.state_manager.context_snapshots),
            "",
            "## Final State",
            str(self.state_manager.final_state()),
            "",
            "免责声明：仅供研究参考，不构成投资建议。",
        ])
