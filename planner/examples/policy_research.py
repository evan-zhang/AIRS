"""Policy research planner example."""

from planner import plan_research


def run():
    return plan_research({
        "goal_id": "policy-semiconductor",
        "raw_goal": "政策研究：分析半导体政策变化对产业链的研究路径",
        "goal_type": "policy",
        "subject": "半导体政策变化",
        "time_horizon": "近 24 个月",
        "success_criteria": ["形成政策事件研究计划", "规划监管证据", "标注不确定性"],
    })
