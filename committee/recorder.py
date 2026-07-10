"""Committee 委员会记录器。"""

from __future__ import annotations

from typing import Any

from .role_registry import DISCLAIMER


class DecisionRecorder:
    def record(self, session: dict[str, Any], vote: dict[str, Any], consensus: dict[str, Any]) -> dict[str, Any]:
        return {
            "decision_id": f"decision-{session['session_id']}",
            "session_id": session["session_id"],
            "planner_ref": session["planner_ref"],
            "research_engine_gate": "ALLOW_WITH_CONDITIONS" if vote["outcome"] == "CONDITIONAL_PASS" else "BLOCK",
            "voting_result": vote,
            "consensus": consensus,
            "minority_report": session.get("minority_report", []),
            "follow_up_tasks": session.get("follow_up_tasks", []),
            "final_recommendation": session.get("final_recommendation", "仅允许进入后续研究验证，不构成投资建议。"),
            "disclaimer": DISCLAIMER,
        }
