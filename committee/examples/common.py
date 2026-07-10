"""生产级 Committee 示例构造器。"""

from __future__ import annotations

from committee import run_committee
from committee.role_registry import DISCLAIMER


def build_plan(goal_id: str, subject: str, goal_type: str) -> dict:
    return {
        "plan_id": f"plan-{goal_id}",
        "goal_analysis": {
            "goal_id": goal_id,
            "goal_type": goal_type,
            "subject": subject,
            "time_horizon": "近 12 个月",
            "success_criteria": ["完成 Committee 审议", "保留反方观点", "生成后续研究任务"],
        },
        "required_methodologies": ["supply-chain-chokepoint", "counter-consensus", "risk"],
        "expected_evidence": {"minimum_cards": 6, "counter_evidence_required": True},
        "disclaimer": DISCLAIMER,
    }


def run_example(goal_id: str, subject: str, goal_type: str, minority: str) -> dict:
    result = run_committee(build_plan(goal_id, subject, goal_type))
    session = result["session"]
    decision = result["decision"]
    return {
        "example_id": goal_id,
        "subject": subject,
        "Participants": session["participants"],
        "Debate Timeline": session["agenda"],
        "Evidence Review": session["evidence_review"],
        "Opinions": session["opinions"],
        "Unresolved Questions": session["unresolved_questions"],
        "Voting Result": result["vote"],
        "Final Recommendation": decision["final_recommendation"],
        "Minority Report": [minority, *decision["minority_report"]],
        "Follow-up Tasks": decision["follow_up_tasks"],
        "Decision": decision,
        "disclaimer": DISCLAIMER,
    }
