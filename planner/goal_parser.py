"""Goal parser for AIRS Autonomous Research Planner."""

from __future__ import annotations

from typing import Any


DISCLAIMER = "仅用于 AIRS 投资研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。"


GOAL_TYPE_KEYWORDS = {
    "company": ("公司", "个股", "企业", "Company"),
    "industry": ("行业", "产业", "赛道", "Industry"),
    "theme": ("主题", "热点", "机会", "Theme"),
    "supply_chain": ("供应链", "产业链", "Supply Chain"),
    "chokepoint": ("卡点", "瓶颈", "卡脖子", "Chokepoint"),
    "policy": ("政策", "监管", "法规", "Policy"),
    "portfolio": ("组合", "持仓", "Portfolio"),
    "comparative": ("对比", "比较", "横向", "Comparative"),
}


def _infer_goal_type(text: str) -> str:
    for goal_type, keywords in GOAL_TYPE_KEYWORDS.items():
        if any(keyword in text for keyword in keywords):
            return goal_type
    return "theme"


def parse_goal(goal: str | dict[str, Any]) -> dict[str, Any]:
    """Parse raw goal text or object into a normalized research goal."""

    if isinstance(goal, str):
        text = goal.strip()
        if not text:
            raise ValueError("research goal cannot be empty")
        return {
            "goal_id": "goal-auto",
            "raw_goal": text,
            "goal_type": _infer_goal_type(text),
            "subject": text[:80],
            "time_horizon": "近 12 个月",
            "constraints": [],
            "success_criteria": ["形成可复核 Research Plan", "列出证据缺口", "保留免责声明"],
            "disclaimer": DISCLAIMER,
        }

    required = {"goal_id", "raw_goal"}
    missing = required - set(goal)
    if missing:
        raise ValueError(f"missing research goal fields: {', '.join(sorted(missing))}")
    normalized = dict(goal)
    normalized.setdefault("goal_type", _infer_goal_type(str(goal["raw_goal"])))
    normalized.setdefault("subject", str(goal["raw_goal"])[:80])
    normalized.setdefault("time_horizon", "近 12 个月")
    normalized.setdefault("constraints", [])
    normalized.setdefault("success_criteria", ["形成可复核 Research Plan"])
    normalized["disclaimer"] = DISCLAIMER
    return normalized
