"""Investment thesis generation component."""

from __future__ import annotations

from typing import Any

from .recommendation import Statement


def generate_thesis(theme: dict[str, Any], industry: dict[str, Any], chokepoints: dict[str, Any]) -> dict[str, Any]:
    topic = theme["topic"]
    statements = [
        Statement("st-fact-01", "Fact", f"公开披露信息显示 {topic} 产业链包含需求、供给和政策三类证据来源。", ["ev-01"], 0.82, "来自 Evidence Card 的可追溯事实。"),
        Statement("st-infer-01", "Inference", f"因此 {topic} 的瓶颈强度需要与产能、订单和价格证据联合推导。", ["ev-01", "ev-02"], 0.68, "由供应链节点和证据关系推导。"),
        Statement("st-assume-01", "Assumption", f"假设需求扩张持续，{topic} 上游约束可能提高研究关注度。", ["ev-03"], 0.55, "依赖尚需验证的需求情景。"),
        Statement("st-opinion-01", "Opinion", f"{topic} 当前更适合作为研究主题跟踪，而非形成交易动作。", [], 0.45, "分析观点，不代表确定性结论。"),
    ]
    return {
        "component": "thesis_generator",
        "thesis_id": f"thesis-{topic.lower().replace(' ', '-')}",
        "topic": topic,
        "core_thesis": f"{topic} 的研究价值来自需求驱动、供应链瓶颈和风险反证之间的动态平衡。",
        "industry_context": industry,
        "key_chokepoints": chokepoints["chokepoints"],
        "statements": statements,
        "methodology_refs": ["docs/methodology/theme-expansion.md", "docs/methodology/evidence-chain.md"],
    }
