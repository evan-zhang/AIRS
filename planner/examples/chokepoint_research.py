"""Chokepoint research planner example."""

from planner import plan_research


def run():
    return plan_research({
        "goal_id": "chokepoint-hbm",
        "raw_goal": "卡点研究：分析 HBM 供给瓶颈和反方证据",
        "goal_type": "chokepoint",
        "subject": "HBM 供给瓶颈",
        "time_horizon": "近 12 个月",
        "success_criteria": ["形成卡点研究计划", "规划反方证据", "生成风险复核路径"],
    })
