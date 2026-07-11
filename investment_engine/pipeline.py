"""Unified Investment Research Engine pipeline."""

from __future__ import annotations

from typing import Any

from .catalyst import analyze_catalysts
from .chokepoint import analyze_chokepoints
from .company_discovery import discover_companies
from .comparable import analyze_comparables
from .industry_discovery import discover_industry
from .portfolio_impact import analyze_portfolio_impact
from .recommendation import DISCLAIMER, build_recommendation, validate_recommendation_language
from .risk import analyze_risks
from .supply_chain import analyze_supply_chain
from .theme_discovery import discover_theme
from .thesis_generator import generate_thesis


class InvestmentResearchPipeline:
    """Coordinate AIRS M1-M7 infrastructure into one executable workflow."""

    infrastructure_refs = {
        "runtime": "runtime/core.py",
        "orchestrator": "docs/orchestrator/",
        "workspace": "docs/workspace/workspace-architecture.md",
        "connectors": "docs/data-connectors/connector-interface.md",
        "methodology": "docs/methodology/",
        "skill": "skills/README.md",
        "prompt": "docs/prompt-engine/prompt-architecture.md",
        "evidence": "schemas/evidence/evidence-card.schema.json",
        "knowledge_graph": "schemas/knowledge-graph/knowledge-graph.schema.json",
        "score": "schemas/score/scorecard.schema.json",
        "report": "templates/report/research-report-template.md",
    }

    def run(self, request: dict[str, Any]) -> dict[str, Any]:
        self._validate_request(request)
        theme = discover_theme(request)
        companies = discover_companies(theme)
        industry = discover_industry(theme)
        supply_chain = analyze_supply_chain(theme, companies)
        chokepoints = analyze_chokepoints(supply_chain)
        thesis = generate_thesis(theme, industry, chokepoints)
        risk = analyze_risks(thesis)
        catalyst = analyze_catalysts(theme)
        comparable = analyze_comparables(companies)
        portfolio_impact = analyze_portfolio_impact(theme, risk)
        evidence_chain = self._build_evidence_chain(request, thesis)
        knowledge_graph = self._build_knowledge_graph(request, supply_chain, chokepoints, evidence_chain)
        scorecard = self._build_scorecard(evidence_chain, chokepoints, risk)
        recommendation = build_recommendation(request["topic"], scorecard, thesis["statements"])
        report = self._build_report(request, thesis, knowledge_graph, evidence_chain, supply_chain, chokepoints, scorecard, risk, catalyst, recommendation)
        self._validate_safe_output(report, recommendation)
        return {
            "engine_version": "1.0.0",
            "request": request,
            "runtime_plan": self._runtime_plan(request),
            "infrastructure_refs": self.infrastructure_refs,
            "theme_discovery": theme,
            "company_discovery": companies,
            "industry_discovery": industry,
            "investment_thesis": {k: v for k, v in thesis.items() if k != "statements"} | {"statements": [s.to_dict() for s in thesis["statements"]]},
            "knowledge_graph": knowledge_graph,
            "evidence_chain": evidence_chain,
            "supply_chain_analysis": supply_chain,
            "chokepoint_analysis": chokepoints,
            "score_card": scorecard,
            "risk_analysis": risk,
            "catalyst_analysis": catalyst,
            "comparable_analysis": comparable,
            "portfolio_impact": portfolio_impact,
            "recommendation": recommendation,
            "final_research_report": report,
            "disclaimer": DISCLAIMER,
        }

    def _validate_request(self, request: dict[str, Any]) -> None:
        required = {"request_id", "topic", "scope", "time_horizon"}
        missing = required - set(request)
        if missing:
            raise ValueError(f"missing investment request fields: {', '.join(sorted(missing))}")

    def _runtime_plan(self, request: dict[str, Any]) -> dict[str, Any]:
        return {
            "workflow_id": f"investment-engine-{request['request_id']}",
            "tasks": [
                {"task_id": "theme", "agent_id": "methodology_selector", "expected_output": "theme_discovery"},
                {"task_id": "evidence", "agent_id": "evidence_collector", "dependencies": ["theme"], "expected_output": "evidence_chain"},
                {"task_id": "graph", "agent_id": "parallel_researcher", "dependencies": ["evidence"], "expected_output": "knowledge_graph"},
                {"task_id": "review", "agent_id": "human_reviewer", "dependencies": ["graph"], "expected_output": "safe_recommendation"},
            ],
        }

    def _build_evidence_chain(self, request: dict[str, Any], thesis: dict[str, Any]) -> dict[str, Any]:
        cards = {
            "ev-01": {"evidence_id": "ev-01", "title": f"{request['topic']} demand signal", "evidence_level": "L2", "confidence": 0.82, "supports": ["st-fact-01"], "refutes": [], "source": "connector:news"},
            "ev-02": {"evidence_id": "ev-02", "title": f"{request['topic']} supply constraint", "evidence_level": "L2", "confidence": 0.74, "supports": ["st-infer-01"], "refutes": [], "source": "connector:industry"},
            "ev-03": {"evidence_id": "ev-03", "title": f"{request['topic']} policy or scenario input", "evidence_level": "L3", "confidence": 0.58, "supports": ["st-assume-01"], "refutes": [], "source": "connector:policy"},
            "ev-counter-01": {"evidence_id": "ev-counter-01", "title": "counter demand evidence", "evidence_level": "L3", "confidence": 0.54, "supports": [], "refutes": ["st-infer-01"], "source": "connector:news"},
            "ev-counter-02": {"evidence_id": "ev-counter-02", "title": "competition counter evidence", "evidence_level": "L3", "confidence": 0.51, "supports": [], "refutes": ["st-assume-01"], "source": "connector:financial"},
        }
        return {
            "chain_id": f"chain-{request['request_id']}",
            "claim": thesis["core_thesis"],
            "methodology_refs": ["docs/methodology/evidence-chain.md"],
            "evidence_cards": cards,
            "counter_evidence_refs": ["ev-counter-01", "ev-counter-02"],
            "missing_evidence": ["真实订单明细", "产能利用率", "价格时间序列"],
            "overall_confidence": 0.66,
            "disclaimer": DISCLAIMER,
        }

    def _build_knowledge_graph(self, request: dict[str, Any], supply_chain: dict[str, Any], chokepoints: dict[str, Any], evidence_chain: dict[str, Any]) -> dict[str, Any]:
        return {
            "graph_id": f"kg-{request['request_id']}",
            "title": f"{request['topic']} Knowledge Graph",
            "research_question": request["scope"],
            "methodology_refs": ["docs/methodology/supply-chain-chokepoint.md"],
            "evidence_cards": evidence_chain["evidence_cards"],
            "nodes": supply_chain["nodes"],
            "edges": supply_chain["edges"],
            "path_analysis": [{"path": ["upstream", "midstream", "downstream"], "confidence": 0.68}],
            "chokepoint_analysis": chokepoints["chokepoints"],
            "disclaimer": DISCLAIMER,
            "version": "1.0.0",
        }

    def _build_scorecard(self, evidence_chain: dict[str, Any], chokepoints: dict[str, Any], risk: dict[str, Any]) -> dict[str, Any]:
        evidence_score = evidence_chain["overall_confidence"] * 100
        chokepoint_score = sum(item["severity"] for item in chokepoints["chokepoints"]) / len(chokepoints["chokepoints"]) * 100
        risk_penalty = len(risk["risks"]) * 4
        overall = round((evidence_score * 0.45 + chokepoint_score * 0.35 + (100 - risk_penalty) * 0.20), 1)
        return {
            "scorecard_id": f"score-{evidence_chain['chain_id']}",
            "methodology_refs": ["docs/score-engine/score-architecture.md"],
            "evidence_chain_refs": list(evidence_chain["evidence_cards"].keys()),
            "scores": [
                {"score_type": "evidence", "raw_score": round(evidence_score, 1), "weight": 0.45},
                {"score_type": "chokepoint", "raw_score": round(chokepoint_score, 1), "weight": 0.35},
                {"score_type": "risk_control", "raw_score": 100 - risk_penalty, "weight": 0.20},
            ],
            "overall_score": overall,
            "overall_grade": "B" if overall >= 60 else "C",
            "confidence_score": evidence_chain["overall_confidence"],
            "quality_gate": "CONDITIONAL_PASS" if overall >= 60 else "FAIL",
            "disclaimer": "仅供研究参考，不构成投资建议",
        }

    def _build_report(self, request: dict[str, Any], thesis: dict[str, Any], knowledge_graph: dict[str, Any], evidence_chain: dict[str, Any], supply_chain: dict[str, Any], chokepoints: dict[str, Any], scorecard: dict[str, Any], risk: dict[str, Any], catalyst: dict[str, Any], recommendation: dict[str, Any]) -> str:
        return "\n".join(
            [
                f"# {request['topic']} Final Research Report",
                "",
                f"免责声明：{DISCLAIMER}",
                "",
                "## Investment Thesis",
                thesis["core_thesis"],
                "",
                "## Knowledge Graph",
                f"Graph: {knowledge_graph['graph_id']} with {len(knowledge_graph['nodes'])} nodes and {len(knowledge_graph['edges'])} edges.",
                "",
                "## Evidence Chain",
                f"Evidence cards: {', '.join(evidence_chain['evidence_cards'].keys())}. Counter evidence: {', '.join(evidence_chain['counter_evidence_refs'])}.",
                "",
                "## Supply Chain Analysis",
                f"Nodes: {', '.join(node['label'] for node in supply_chain['nodes'])}.",
                "",
                "## Chokepoint Analysis",
                f"Key chokepoints: {', '.join(item['label'] for item in chokepoints['chokepoints'])}.",
                "",
                "## Score Card",
                f"Overall Score: {scorecard['overall_score']} / Quality Gate: {scorecard['quality_gate']}.",
                "",
                "## Risk Analysis",
                risk["risk_summary"],
                "",
                "## Catalyst Analysis",
                f"Catalysts: {', '.join(item['name'] for item in catalyst['catalysts'])}.",
                "",
                "## Recommendation Standard",
                f"Research stance: {recommendation['research_stance']}. Facts/Inference/Assumption/Opinion coverage: {recommendation['statement_coverage']}.",
                "",
                "## Final Research Report",
                "本报告输出研究跟踪框架、证据缺口和复核路径，不输出确定性投资建议、交易指令、目标价或收益承诺。",
            ]
        )

    def _validate_safe_output(self, report: str, recommendation: dict[str, Any]) -> None:
        hits = validate_recommendation_language(report + "\n" + str(recommendation))
        if hits:
            raise ValueError(f"unsafe recommendation language: {', '.join(hits)}")
        coverage = recommendation["statement_coverage"]
        if any(coverage.get(kind, 0) < 1 for kind in ("Fact", "Inference", "Assumption", "Opinion")):
            raise ValueError("recommendation must include Facts, Inference, Assumption and Opinion")


def run_research(request: dict[str, Any]) -> dict[str, Any]:
    return InvestmentResearchPipeline().run(request)
