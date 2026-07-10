"""Industry research planner example."""

from planner import plan_research


def run():
    return plan_research({
        "goal_id": "industry-humanoid-robot",
        "raw_goal": "行业研究：分析人形机器人产业阶段和关键证据",
        "goal_type": "industry",
        "subject": "人形机器人行业",
        "time_horizon": "近 18 个月",
        "success_criteria": ["形成行业生命周期研究计划", "规划政策和产业证据", "生成报告提纲"],
    })
