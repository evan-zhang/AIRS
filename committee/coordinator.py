"""Autonomous Investment Committee coordinator."""

from __future__ import annotations

from typing import Any

from .analysts import BearAnalyst, BullAnalyst, FinancialAnalyst, IndustryAnalyst
from .consensus_engine import ConsensusEngine
from .experts import IndustryExpert, PortfolioExpert, RiskExpert
from .moderator import CommitteeModerator
from .recorder import DecisionRecorder
from .reviewer import DevilsAdvocate, EvidenceReviewer
from .role_registry import DISCLAIMER, default_role_registry
from .voting_engine import VotingEngine


class AutonomousInvestmentCommittee:
    """Planner 之后、Research Engine 之前的多角色审议门禁。"""

    infrastructure_refs = {
        "planner": "docs/planner/planner-architecture.md",
        "runtime": "docs/runtime/runtime-architecture.md",
        "orchestrator": "docs/orchestrator/orchestrator-architecture.md",
        "investment_engine": "docs/investment-engine/engine-architecture.md",
        "evidence": "schemas/evidence/evidence-chain.schema.json",
        "score": "schemas/score/scorecard.schema.json",
        "recommendation": "schemas/investment/recommendation.schema.json",
        "report": "templates/report/research-report-template.md",
    }

    def __init__(self) -> None:
        self.roles = default_role_registry()
        self.moderator = CommitteeModerator()
        self.voting_engine = VotingEngine()
        self.consensus_engine = ConsensusEngine()
        self.recorder = DecisionRecorder()

    def run(self, plan: dict[str, Any]) -> dict[str, Any]:
        planner_ref = plan.get("plan_id", "external-plan")
        session = {
            "session_id": f"aic-{planner_ref}",
            "planner_ref": planner_ref,
            "committee_position": "after_planner_before_research_engine",
            "participants": list(self.roles),
            "agenda": self.moderator.build_agenda(plan),
            "opinions": [
                BullAnalyst().opinion(plan),
                BearAnalyst().opinion(plan),
                FinancialAnalyst().opinion(plan),
                IndustryAnalyst().opinion(plan),
                IndustryExpert().review({"plan": plan}),
                RiskExpert().review({"plan": plan}),
                PortfolioExpert().review({"plan": plan}),
            ],
            "evidence_review": {
                "required_refs": ["schemas/evidence/evidence-card.schema.json", "schemas/evidence/evidence-chain.schema.json"],
                "gaps": ["等待 Research Engine 执行后补充原始证据卡。"],
            },
            "unresolved_questions": ["关键证据尚未由 Connector 采集验证。", "Scorecard 尚未由 M6 计算。"],
            "minority_report": ["Bear Analyst 要求在证据不足时降级结论。"],
            "follow_up_tasks": ["Research Engine 执行证据采集。", "Review Agent 复核 Minority Report。"],
            "final_recommendation": "允许在限定范围内进入 Research Engine 继续研究，所有结论仅供研究质量控制。",
            "infrastructure_refs": self.infrastructure_refs,
            "disclaimer": DISCLAIMER,
        }
        session["challenges"] = [EvidenceReviewer().challenge(session), DevilsAdvocate().challenge(session)]
        boundary = self.moderator.enforce_boundaries(session["final_recommendation"])
        session["boundary_check"] = boundary
        vote = self.voting_engine.vote(session)
        consensus = self.consensus_engine.build(session, vote)
        decision = self.recorder.record(session, vote, consensus)
        return {"session": session, "vote": vote, "consensus": consensus, "decision": decision, "disclaimer": DISCLAIMER}


def run_committee(plan: dict[str, Any]) -> dict[str, Any]:
    return AutonomousInvestmentCommittee().run(plan)
