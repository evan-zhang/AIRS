"""Portfolio research planner example."""

from planner import plan_research


def run():
    return plan_research({
        "goal_id": "portfolio-ai-exposure",
        "raw_goal": "组合研究：分析 AI 主题暴露和风险复核计划",
        "goal_type": "portfolio",
        "subject": "AI 主题组合暴露",
        "time_horizon": "近 3 个月",
        "success_criteria": ["形成组合风险研究计划", "规划压力情景", "不输出仓位动作"],
    })
