"""Research scope builder."""

from __future__ import annotations

from typing import Any


def build_scope(goal: dict[str, Any], intent: dict[str, Any]) -> dict[str, Any]:
    return {
        "subject": goal["subject"],
        "goal_type": goal["goal_type"],
        "time_horizon": goal["time_horizon"],
        "geography": goal.get("geography", "未限定，默认按公开资料可得性处理"),
        "constraints": goal.get("constraints", []),
        "in_scope": [
            "目标解析",
            "方法论选择",
            "证据链规划",
            "知识图谱规划",
            "评分与反方观点规划",
            "报告交付规划",
        ],
        "out_of_scope": [
            "真实交易执行",
            "确定性收益预测",
            "未追溯来源的结论",
            "绕过 Planner 直接调用 Runtime",
        ],
        "success_criteria": goal.get("success_criteria", []),
        "intent_ref": intent["primary_intent"],
    }
