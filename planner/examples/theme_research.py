"""Theme research planner example."""

from planner import plan_research


def run():
    return plan_research({
        "goal_id": "theme-ai-compute",
        "raw_goal": "主题研究：分析 AI 算力主题扩散路径",
        "goal_type": "theme",
        "subject": "AI 算力主题",
        "time_horizon": "近 6 个月",
        "success_criteria": ["形成主题扩散计划", "规划反共识验证", "生成证据缺口清单"],
    })
