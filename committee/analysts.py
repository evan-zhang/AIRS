"""委员会分析师角色。"""

from __future__ import annotations

from typing import Any

from .role_registry import DISCLAIMER


def _subject(plan: dict[str, Any]) -> str:
    return plan.get("goal_analysis", {}).get("subject") or plan.get("topic") or "研究对象"


class BullAnalyst:
    role_id = "bull_analyst"

    def opinion(self, plan: dict[str, Any]) -> dict[str, Any]:
        subject = _subject(plan)
        return {
            "role_id": self.role_id,
            "stance": "support_with_conditions",
            "opinion": f"{subject} 的正向命题只有在证据链、供需数据和评分结果一致时才可保留。",
            "required_evidence": ["M3 Evidence Chain", "M6 Scorecard", "FEATURE-008 Thesis"],
            "confidence": 0.68,
            "disclaimer": DISCLAIMER,
        }


class BearAnalyst:
    role_id = "bear_analyst"

    def opinion(self, plan: dict[str, Any]) -> dict[str, Any]:
        subject = _subject(plan)
        return {
            "role_id": self.role_id,
            "stance": "challenge",
            "opinion": f"{subject} 的主要风险在于共识交易、数据滞后和替代技术路线，结论必须保留失败情景。",
            "required_evidence": ["Counter Evidence", "Missing Evidence", "Risk Methodology"],
            "confidence": 0.72,
            "disclaimer": DISCLAIMER,
        }


class FinancialAnalyst:
    role_id = "financial_analyst"

    def opinion(self, plan: dict[str, Any]) -> dict[str, Any]:
        return {
            "role_id": self.role_id,
            "stance": "verify_financials",
            "opinion": "财务口径必须区分事实、推断、假设和观点，并与 Recommendation Schema 对齐。",
            "required_evidence": ["financial statements", "valuation methodology", "scorecard refs"],
            "confidence": 0.64,
            "disclaimer": DISCLAIMER,
        }


class IndustryAnalyst:
    role_id = "industry_analyst"

    def opinion(self, plan: dict[str, Any]) -> dict[str, Any]:
        return {
            "role_id": self.role_id,
            "stance": "verify_industry_structure",
            "opinion": "产业判断必须复用 M2 方法论和 FEATURE-002 Knowledge Graph，不在 Committee 内重复定义产业图谱。",
            "required_evidence": ["methodology refs", "knowledge graph refs", "connector refs"],
            "confidence": 0.7,
            "disclaimer": DISCLAIMER,
        }
