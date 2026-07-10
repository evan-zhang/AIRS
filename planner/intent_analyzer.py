"""Intent analyzer for planner goal types."""

from __future__ import annotations

from typing import Any


INTENT_LIBRARY = {
    "company": {
        "intent": "company_research",
        "methodologies": ["financial-anomaly", "management-quality", "valuation", "risk"],
        "skills": ["financial", "valuation", "risk", "report"],
        "connectors": ["company_filings", "market_news", "industry_report"],
    },
    "industry": {
        "intent": "industry_research",
        "methodologies": ["industry-lifecycle", "theme-expansion", "risk"],
        "skills": ["hot-topic", "news", "evidence", "report"],
        "connectors": ["industry_report", "policy", "market_news"],
    },
    "theme": {
        "intent": "theme_research",
        "methodologies": ["theme-expansion", "counter-consensus", "evidence-chain"],
        "skills": ["hot-topic", "evidence", "risk", "report"],
        "connectors": ["market_news", "research_report", "policy"],
    },
    "supply_chain": {
        "intent": "supply_chain_research",
        "methodologies": ["supply-chain-chokepoint", "evidence-chain"],
        "skills": ["supply-chain", "evidence", "risk", "report"],
        "connectors": ["company_filings", "industry_report", "trade_data"],
    },
    "chokepoint": {
        "intent": "chokepoint_research",
        "methodologies": ["supply-chain-chokepoint", "counter-consensus", "risk"],
        "skills": ["supply-chain", "evidence", "risk", "verification"],
        "connectors": ["industry_report", "company_filings", "expert_view"],
    },
    "policy": {
        "intent": "policy_research",
        "methodologies": ["policy-driven", "event-impact", "counter-consensus"],
        "skills": ["news", "evidence", "risk", "report"],
        "connectors": ["policy", "regulatory", "market_news"],
    },
    "portfolio": {
        "intent": "portfolio_research",
        "methodologies": ["risk", "valuation", "counter-consensus"],
        "skills": ["risk", "valuation", "verification", "report"],
        "connectors": ["portfolio_snapshot", "company_filings", "market_news"],
    },
    "comparative": {
        "intent": "comparative_research",
        "methodologies": ["valuation", "financial-anomaly", "management-quality"],
        "skills": ["financial", "valuation", "evidence", "report"],
        "connectors": ["company_filings", "industry_report", "market_news"],
    },
}


def analyze_intent(goal: dict[str, Any]) -> dict[str, Any]:
    goal_type = goal.get("goal_type", "theme")
    profile = INTENT_LIBRARY.get(goal_type, INTENT_LIBRARY["theme"])
    return {
        "goal_type": goal_type,
        "primary_intent": profile["intent"],
        "required_methodologies": profile["methodologies"],
        "required_skills": profile["skills"],
        "required_connectors": profile["connectors"],
        "report_depth": "deep" if goal_type in {"company", "portfolio", "chokepoint"} else "standard",
        "review_required": True,
    }
