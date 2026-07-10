"""Committee 委员会专家角色。"""

from __future__ import annotations

from typing import Any

from .role_registry import DISCLAIMER


class IndustryExpert:
    role_id = "industry_expert"

    def review(self, session: dict[str, Any]) -> dict[str, Any]:
        return {
            "role_id": self.role_id,
            "finding": "产业专家确认议题需覆盖产业生命周期、供应链卡点、政策驱动和反共识四类既有方法论。",
            "required_refs": ["docs/methodology/industry-lifecycle.md", "docs/methodology/supply-chain-chokepoint.md"],
            "confidence": 0.69,
            "disclaimer": DISCLAIMER,
        }


class RiskExpert:
    role_id = "risk_expert"

    def review(self, session: dict[str, Any]) -> dict[str, Any]:
        return {
            "role_id": self.role_id,
            "finding": "风险专家要求所有 Final Recommendation 仅表达研究跟踪结论，并保留数据、模型、市场和执行风险。",
            "required_refs": ["docs/methodology/risk.md", "schemas/score/evaluation.schema.json"],
            "confidence": 0.74,
            "disclaimer": DISCLAIMER,
        }


class PortfolioExpert:
    role_id = "portfolio_expert"

    def review(self, session: dict[str, Any]) -> dict[str, Any]:
        return {
            "role_id": self.role_id,
            "finding": "组合专家仅评估组合暴露、相关性和优先级，不输出仓位、买卖或交易动作。",
            "required_refs": ["schemas/investment/investment-request.schema.json", "templates/investment/thesis-template.md"],
            "confidence": 0.62,
            "disclaimer": DISCLAIMER,
        }
