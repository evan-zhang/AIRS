"""委员会共识构建。"""

from __future__ import annotations

from typing import Any

from .role_registry import DISCLAIMER


class ConsensusEngine:
    def build(self, session: dict[str, Any], vote: dict[str, Any]) -> dict[str, Any]:
        unresolved = session.get("unresolved_questions", [])
        return {
            "consensus_id": f"consensus-{session['session_id']}",
            "consensus_level": "conditional_consensus" if vote["outcome"] == "CONDITIONAL_PASS" else "no_consensus",
            "agreed_points": [
                "结论必须保留证据引用和不确定性。",
                "后续 Research Engine 只能执行经 Committee 记录的任务范围。",
                "任何推荐表述必须符合 Recommendation Schema 的合规边界。",
            ],
            "unresolved_questions": unresolved,
            "decision_threshold": "无 REJECT 且达到至少 6 个角色投票。",
            "disclaimer": DISCLAIMER,
        }
