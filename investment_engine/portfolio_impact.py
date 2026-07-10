"""Portfolio impact component for investment research."""

from __future__ import annotations

from typing import Any


def analyze_portfolio_impact(theme: dict[str, Any], risk: dict[str, Any]) -> dict[str, Any]:
    return {
        "component": "portfolio_impact",
        "topic": theme["topic"],
        "exposure_view": "watchlist-only",
        "risk_channels": [item["name"] for item in risk["risks"]],
        "stress_scenarios": [
            {"scenario": "需求延后", "impact": "降低主题置信度", "action": "补充证据，不生成交易动作"},
            {"scenario": "供应释放", "impact": "削弱瓶颈溢价", "action": "复核 Chokepoint Score"},
        ],
        "disclaimer": "组合影响仅用于研究质量控制，不构成仓位建议。",
    }
