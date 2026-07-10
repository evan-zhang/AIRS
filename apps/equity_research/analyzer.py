"""股票研究综合分析。"""

from __future__ import annotations

from typing import Any

from investment_engine import run_research

from .company_resolver import CompanyInfo
from .data_collector import DataCollectionBundle
from .request_parser import ResearchRequest


DISCLAIMER = "分析结论仅用于研究质量控制，需区分 Facts / Inference / Assumption / Opinion，不构成投资建议。"


class EquityResearchAnalyzer:
    """整合 Profile、行业、供应链、财务、估值、催化与风险分析。"""

    def analyze(self, request: ResearchRequest, company: CompanyInfo, data: DataCollectionBundle) -> dict[str, Any]:
        engine_request = {
            "request_id": request.request_id,
            "topic": f"{company.company_name} 股票研究",
            "scope": request.research_question,
            "time_horizon": request.time_range,
            "disclaimer": DISCLAIMER,
        }
        engine_result = run_research(engine_request)
        statements = self._build_statements(request, company, data, engine_result)
        kg = self._build_knowledge_graph(request, company, data, engine_result)
        score_card = self._build_score_card(data, engine_result)
        return {
            "profile": self._profile(company),
            "industry_position": self._industry(company, engine_result),
            "supply_chain_chokepoint": self._supply_chain(engine_result),
            "financial_analysis": self._financial(data),
            "valuation": self._valuation(data),
            "catalysts": engine_result["catalyst_analysis"],
            "risks": engine_result["risk_analysis"],
            "counter_view": self._counter_view(data),
            "evidence_chain": {
                "chain_id": f"chain-{request.request_id}",
                "claim": f"{company.company_name} 研究结论必须受证据质量约束。",
                "evidence_cards": data.evidence_cards,
                "counter_evidence_refs": ["APP001-EV-COUNTER-01"],
                "missing_evidence": sorted(set(sum((card.get("missing_evidence", []) for card in data.evidence_cards.values()), []))),
                "overall_confidence": score_card["confidence_score"],
                "disclaimer": DISCLAIMER,
            },
            "knowledge_graph": kg,
            "score_card": score_card,
            "statement_registry": statements,
            "engine_result": engine_result,
            "disclaimer": DISCLAIMER,
        }

    def _profile(self, company: CompanyInfo) -> dict[str, Any]:
        return {
            "facts": [
                f"公司识别状态：{company.resolver_status}",
                f"代码：{company.symbol}；市场：{company.market}；交易所：{company.exchange}",
                f"行业：{company.industry}；板块：{company.sector}",
            ],
            "inference": ["若公司识别为 NEED_REVIEW，则后续所有公司特定分析必须降级。"],
            "assumption": ["本地公司目录中的基础信息用于流程路由，仍需外部权威源复核。"],
            "opinion": ["在证据不足前，研究应以问题清单和证据缺口为主。"],
        }

    def _industry(self, company: CompanyInfo, engine: dict[str, Any]) -> dict[str, Any]:
        return {
            "facts": [f"行业分类来自 Resolver：{company.industry}", f"Engine 行业发现模块：{engine['industry_discovery'].get('industry', 'UNKNOWN')}"],
            "inference": ["行业地位需要财报、市场份额和同行数据共同验证。"],
            "assumption": ["若 Connector 未提供真实行业数据，则暂以行业方法论框架占位。"],
            "opinion": ["行业部分适合进入二次研究，而非形成确定性判断。"],
        }

    def _supply_chain(self, engine: dict[str, Any]) -> dict[str, Any]:
        return {
            "facts": engine.get("supply_chain_analysis", {}),
            "inference": engine.get("chokepoint_analysis", {}),
            "assumption": ["供应链节点来自通用 Investment Engine 模板，需公司级真实资料复核。"],
            "opinion": ["卡点分析可用于组织研究问题，不应解读为交易信号。"],
        }

    def _financial(self, data: DataCollectionBundle) -> dict[str, Any]:
        yahoo = [item for item in data.connector_results if item.get("connector_id") == "yahoo_finance"]
        return {
            "facts": yahoo or ["SKIP：未获得可用行情 Connector 结果。"],
            "inference": ["当前财务分析只能确认数据可用性与追溯性，不能替代三表分析。"],
            "assumption": data.degradation_notes or ["假设后续可接入真实财报数据。"],
            "opinion": ["财务结论应在真实财报与审计口径齐备后再提升置信度。"],
        }

    def _valuation(self, data: DataCollectionBundle) -> dict[str, Any]:
        has_real = any(item.get("data", {}).get("mode") == "real" for item in data.connector_results)
        return {
            "facts": [f"真实 Connector 数据可用：{has_real}"],
            "inference": ["缺少完整价格、盈利和现金流序列时，不计算目标价或买卖评级。"],
            "assumption": ["估值只能记录待计算指标：PE、PS、EV/EBITDA、DCF 敏感性。"],
            "opinion": ["估值章节以方法和缺口为主，避免伪造精确值。"],
        }

    def _counter_view(self, data: DataCollectionBundle) -> dict[str, Any]:
        return {
            "facts": [f"降级说明数量：{len(data.degradation_notes)}"],
            "inference": ["数据降级会降低结论强度，并要求 Committee 二次审议。"],
            "assumption": ["部分公开源可能存在延迟、抽样偏差或不可访问。"],
            "opinion": ["如果关键证据持续缺失，应输出 CONDITIONAL_PASS 或 FAIL。"],
        }

    def _build_knowledge_graph(self, request: ResearchRequest, company: CompanyInfo, data: DataCollectionBundle, engine: dict[str, Any]) -> dict[str, Any]:
        evidence_ids = list(data.evidence_cards)
        return {
            "graph_id": f"kg-{request.request_id}",
            "title": f"{company.company_name} Equity Research Knowledge Graph",
            "research_question": request.research_question,
            "methodology_refs": ["docs/methodology/evidence-chain.md", "docs/methodology/supply-chain-chokepoint.md", "docs/methodology/valuation.md", "docs/methodology/risk.md"],
            "evidence_cards": data.evidence_cards,
            "nodes": [
                {"node_id": "company", "label": company.company_name, "node_type": "company", "evidence_refs": evidence_ids[:2]},
                {"node_id": "industry", "label": company.industry, "node_type": "industry", "evidence_refs": evidence_ids},
                {"node_id": "risk", "label": "Evidence quality risk", "node_type": "risk", "evidence_refs": ["APP001-EV-COUNTER-01"]},
                {"node_id": "report", "label": "Final Research Report", "node_type": "deliverable", "evidence_refs": evidence_ids},
            ],
            "edges": [
                {"edge_id": "edge-01", "source": "company", "target": "industry", "relation": "belongs_to", "evidence_refs": evidence_ids[:1], "confidence": 0.6},
                {"edge_id": "edge-02", "source": "risk", "target": "report", "relation": "constrains", "evidence_refs": ["APP001-EV-COUNTER-01"], "confidence": 0.8},
            ],
            "path_analysis": [{"path": ["company", "industry", "report"], "confidence": 0.6}],
            "chokepoint_analysis": engine.get("knowledge_graph", {}).get("chokepoint_analysis", []),
            "disclaimer": DISCLAIMER,
            "version": "0.1.0",
        }

    def _build_score_card(self, data: DataCollectionBundle, engine: dict[str, Any]) -> dict[str, Any]:
        evidence_count = len(data.evidence_cards)
        degradation_penalty = min(len(data.degradation_notes) * 8, 40)
        base = 72 if evidence_count >= 4 else 55
        overall = max(35, base - degradation_penalty)
        return {
            "scorecard_id": "score-" + next(iter(data.evidence_cards)).lower(),
            "methodology_refs": ["docs/score-engine/score-architecture.md"],
            "evidence_chain_refs": list(data.evidence_cards),
            "scores": [
                {"score_type": "evidence_completeness", "raw_score": base, "weight": 0.45, "explanation": "按证据卡数量与追溯字段评分。"},
                {"score_type": "data_degradation", "raw_score": 100 - degradation_penalty, "weight": 0.35, "explanation": "Mock/SKIP 越多，降级越强。"},
                {"score_type": "engine_consistency", "raw_score": engine["score_card"]["overall_score"], "weight": 0.20, "explanation": "继承 Investment Engine 质量门禁。"},
            ],
            "overall_score": round(overall, 1),
            "overall_grade": "B" if overall >= 70 else "C",
            "confidence_score": round(overall / 100, 2),
            "quality_gate": "CONDITIONAL_PASS" if overall >= 60 else "FAIL",
            "disclaimer": "仅供研究参考，不构成投资建议",
        }

    def _build_statements(self, request: ResearchRequest, company: CompanyInfo, data: DataCollectionBundle, engine: dict[str, Any]) -> dict[str, list[str]]:
        return {
            "Facts": [
                f"研究请求 ID：{request.request_id}",
                f"解析对象：{company.company_name} / {company.symbol}",
                f"证据卡数量：{len(data.evidence_cards)}",
            ],
            "Inference": [
                "若真实 Connector 不可用，结论置信度必须随数据降级下降。",
                "行业、供应链、估值与风险章节需要共同引用证据链。",
            ],
            "Assumption": [
                "本次流程允许使用 Mock/SKIP 作为工程降级信号，但不得冒充真实研究证据。",
                "后续人工复核可替换或补充 Connector 证据。",
            ],
            "Opinion": [
                "当前输出适合作为研究工作底稿和二次尽调清单。",
                "不输出买入、卖出、持有、目标价或收益承诺。",
            ],
        }

