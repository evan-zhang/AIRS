"""Committee 委员会投票机制。"""

from __future__ import annotations

from typing import Any

from .role_registry import DISCLAIMER


class VotingEngine:
    def vote(self, session: dict[str, Any]) -> dict[str, Any]:
        opinions = session.get("opinions", [])
        challenges = session.get("challenges", [])
        approve = 0
        conditional = 0
        reject = 0
        votes = []
        for item in opinions:
            role_id = item["role_id"]
            stance = item.get("stance", "")
            decision = "CONDITIONAL_APPROVE" if "challenge" in stance or "verify" in stance else "APPROVE"
            if decision == "APPROVE":
                approve += 1
            else:
                conditional += 1
            votes.append({"role_id": role_id, "vote": decision, "rationale": item.get("opinion") or item.get("finding") or "角色审议意见"})
        for item in challenges:
            decision = "CONDITIONAL_APPROVE" if item.get("pass") else "REJECT"
            conditional += int(decision == "CONDITIONAL_APPROVE")
            reject += int(decision == "REJECT")
            votes.append({"role_id": item["role_id"], "vote": decision, "rationale": item["challenge"]})
        outcome = "CONDITIONAL_PASS" if reject == 0 and approve + conditional >= 5 else "FAIL"
        return {
            "vote_id": f"vote-{session['session_id']}",
            "votes": votes,
            "summary": {"approve": approve, "conditional_approve": conditional, "reject": reject},
            "outcome": outcome,
            "quorum_met": len(votes) >= 6,
            "disclaimer": DISCLAIMER,
        }
