"""Comparative research planner example."""

from planner import plan_research


def run():
    return plan_research({
        "goal_id": "comparative-cloud-vs-edge",
        "raw_goal": "对比研究：比较云端 AI 与边缘 AI 的证据链和风险",
        "goal_type": "comparative",
        "subject": "云端 AI 与边缘 AI",
        "time_horizon": "近 12 个月",
        "success_criteria": ["形成横向比较计划", "规划可比指标", "生成反方观点清单"],
    })
