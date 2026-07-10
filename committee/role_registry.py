"""委员会角色注册表。"""

from __future__ import annotations

from dataclasses import dataclass


DISCLAIMER = "仅用于 AIRS 投资研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。"


@dataclass(frozen=True)
class CommitteeRole:
    role_id: str
    role_name: str
    role_type: str
    responsibility: str
    required_refs: tuple[str, ...]


def default_role_registry() -> dict[str, CommitteeRole]:
    """返回 AIC 标准角色，角色只引用既有 AIRS 能力。"""
    refs = (
        "schemas/planner/research-plan.schema.json",
        "schemas/evidence/evidence-chain.schema.json",
        "schemas/score/scorecard.schema.json",
        "schemas/investment/recommendation.schema.json",
    )
    roles = [
        CommitteeRole("bull_analyst", "Bull Analyst", "analyst", "提出支持性命题并标注证据依赖。", refs),
        CommitteeRole("bear_analyst", "Bear Analyst", "analyst", "提出反方命题、替代解释和失败情景。", refs),
        CommitteeRole("financial_analyst", "Financial Analyst", "analyst", "复核财务数据、估值假设和口径一致性。", refs),
        CommitteeRole("industry_analyst", "Industry Analyst", "analyst", "复核产业链位置、供需结构和竞争格局。", refs),
        CommitteeRole("industry_expert", "Industry Expert", "expert", "补充行业机制、周期和政策背景。", refs),
        CommitteeRole("risk_expert", "Risk Expert", "expert", "识别数据、模型、市场、政策和执行风险。", refs),
        CommitteeRole("portfolio_expert", "Portfolio Expert", "expert", "检查组合暴露、相关性和跟踪优先级。", refs),
        CommitteeRole("evidence_reviewer", "Evidence Reviewer", "reviewer", "根据 Evidence Schema 复核证据链完整性。", refs),
        CommitteeRole("devils_advocate", "Devil's Advocate", "reviewer", "强制挑战共识、寻找反证和遗漏。", refs),
        CommitteeRole("moderator", "Moderator", "moderator", "控制议程、冲突升级、投票和结论边界。", refs),
    ]
    return {role.role_id: role for role in roles}
