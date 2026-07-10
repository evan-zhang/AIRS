"""委员会主持人与议程控制。"""

from __future__ import annotations

from typing import Any

from .role_registry import DISCLAIMER


class CommitteeModerator:
    role_id = "moderator"

    def build_agenda(self, plan: dict[str, Any]) -> list[dict[str, Any]]:
        return [
            {"step": "planner_gate", "owner": "moderator", "output": "确认 Planner 产物完整。"},
            {"step": "role_opening", "owner": "all_participants", "output": "形成初始正反意见。"},
            {"step": "evidence_challenge", "owner": "evidence_reviewer", "output": "证据缺口和反方证据清单。"},
            {"step": "counter_argument", "owner": "devils_advocate", "output": "替代解释和失败场景。"},
            {"step": "consensus_building", "owner": "moderator", "output": "共识、分歧和降级条件。"},
            {"step": "vote", "owner": "voting_engine", "output": "结构化 Vote。"},
            {"step": "decision_record", "owner": "recorder", "output": "Decision Record 和后续任务。"},
        ]

    def enforce_boundaries(self, recommendation: str) -> dict[str, Any]:
        forbidden = [
            "建议" + "买入",
            "建议" + "卖出",
            "保证" + "收益",
            "保证" + "盈利",
            "目标价" + "为",
            "应" + "买入",
            "应" + "卖出",
            "自动交易" + "指令",
        ]
        hits = [word for word in forbidden if word in recommendation]
        return {
            "role_id": self.role_id,
            "allowed": not hits,
            "forbidden_hits": hits,
            "rule": "Final Recommendation 只能是研究结论覆盖范围和后续验证任务。",
            "disclaimer": DISCLAIMER,
        }
