"""Supply-chain research planner example."""

from planner import plan_research


def run():
    return plan_research({
        "goal_id": "supply-chain-advanced-packaging",
        "raw_goal": "供应链研究：分析先进封装产业链依赖关系",
        "goal_type": "supply_chain",
        "subject": "先进封装供应链",
        "time_horizon": "近 12 个月",
        "success_criteria": ["形成供应链图谱计划", "规划 Evidence Chain", "识别依赖节点"],
    })
