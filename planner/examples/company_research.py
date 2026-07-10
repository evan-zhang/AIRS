"""Company research planner example."""

from planner import plan_research


def run():
    return plan_research({
        "goal_id": "company-ai-server",
        "raw_goal": "公司研究：分析 AI 服务器供应链相关公司的研究计划",
        "goal_type": "company",
        "subject": "AI 服务器供应链公司",
        "time_horizon": "近 12 个月",
        "success_criteria": ["形成公司研究计划", "列出证据链和反方证据", "生成 Runtime Plan"],
    })
