"""股票研究报告导出。"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from report_generator import ReportPipeline

from .company_resolver import CompanyInfo
from .request_parser import ResearchRequest


DISCLAIMER = "本报告仅供 AIRS 投资研究流程验证和研究参考，不构成投资建议。"

SECTION_TITLES = [
    "Executive Summary",
    "Company Profile",
    "Industry Position",
    "Supply Chain / Chokepoint",
    "Financial Analysis",
    "Valuation",
    "Catalysts",
    "Risks",
    "Counter View",
    "Evidence Chain",
    "Knowledge Graph",
    "Score Card",
    "Committee Decision",
    "Final Report",
    "Appendix (Sources / Traceability)",
]


class EquityResearchReportExporter:
    """生成 APP-001 15 段股票研究报告。"""

    def export(self, request: ResearchRequest, company: CompanyInfo, analysis: dict[str, Any], committee: dict[str, Any]) -> dict[str, Any]:
        final_report = self._render_final_report(request, company, analysis)
        sections = self._sections(request, company, analysis, committee, final_report)
        markdown = self._to_markdown(request, company, sections)
        return {
            "report_id": f"report-{request.request_id}",
            "title": f"{company.company_name} 股票研究报告",
            "sections": sections,
            "markdown": markdown,
            "report_generator_output": final_report,
            "disclaimer": DISCLAIMER,
        }

    def write_markdown(self, result: dict[str, Any], path: str | Path) -> Path:
        target = Path(path)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(result["markdown"], encoding="utf-8")
        return target

    def _render_final_report(self, request: ResearchRequest, company: CompanyInfo, analysis: dict[str, Any]) -> str:
        payload = {
            "report_id": f"reportgen-{request.request_id}",
            "title": f"{company.company_name} AIRS Report Generator 输出",
            "research_question": request.research_question,
            "methodology_refs": analysis["knowledge_graph"]["methodology_refs"],
            "evidence_cards": analysis["evidence_chain"]["evidence_cards"],
            "knowledge_graph": analysis["knowledge_graph"],
            "scorecard": analysis["score_card"],
            "counterarguments": analysis["counter_view"]["inference"] + analysis["counter_view"]["opinion"],
            "risks": analysis["risks"].get("risks", analysis["counter_view"]["assumption"]),
            "disclaimer": DISCLAIMER,
        }
        try:
            return ReportPipeline().render_markdown(payload)
        except Exception as exc:  # noqa: BLE001
            return f"SKIP：Report Generator 调用失败：{exc}\n\n免责声明：{DISCLAIMER}"

    def _sections(self, request: ResearchRequest, company: CompanyInfo, analysis: dict[str, Any], committee: dict[str, Any], final_report: str) -> list[dict[str, Any]]:
        registry = analysis["statement_registry"]
        return [
            self._section("executive_summary", SECTION_TITLES[0], registry),
            self._section("company_profile", SECTION_TITLES[1], analysis["profile"]),
            self._section("industry_position", SECTION_TITLES[2], analysis["industry_position"]),
            self._section("supply_chain", SECTION_TITLES[3], analysis["supply_chain_chokepoint"]),
            self._section("financial_analysis", SECTION_TITLES[4], analysis["financial_analysis"]),
            self._section("valuation", SECTION_TITLES[5], analysis["valuation"]),
            self._section("catalysts", SECTION_TITLES[6], self._normalize_engine_block(analysis["catalysts"])),
            self._section("risks", SECTION_TITLES[7], self._normalize_engine_block(analysis["risks"])),
            self._section("counter_view", SECTION_TITLES[8], analysis["counter_view"]),
            self._section("evidence_chain", SECTION_TITLES[9], self._evidence_block(analysis)),
            self._section("knowledge_graph", SECTION_TITLES[10], self._kg_block(analysis)),
            self._section("score_card", SECTION_TITLES[11], self._score_block(analysis)),
            self._section("committee_decision", SECTION_TITLES[12], self._committee_block(committee)),
            self._section("final_report", SECTION_TITLES[13], {"facts": [final_report[:4000]], "inference": ["完整 Report Generator 输出已纳入本节。"], "assumption": [], "opinion": []}),
            self._section("appendix", SECTION_TITLES[14], self._appendix_block(request, company, analysis, committee)),
        ]

    def _section(self, section_id: str, title: str, block: dict[str, Any]) -> dict[str, Any]:
        return {
            "section_id": section_id,
            "title": title,
            "facts": _as_list(block.get("Facts") or block.get("facts")),
            "inference": _as_list(block.get("Inference") or block.get("inference")),
            "assumption": _as_list(block.get("Assumption") or block.get("assumption")),
            "opinion": _as_list(block.get("Opinion") or block.get("opinion")),
        }

    def _to_markdown(self, request: ResearchRequest, company: CompanyInfo, sections: list[dict[str, Any]]) -> str:
        lines = [
            f"# {company.company_name} 股票研究报告",
            "",
            f"- Request ID：`{request.request_id}`",
            f"- Symbol：`{company.symbol}`",
            f"- Market：`{company.market}`",
            f"- Research Question：{request.research_question}",
            "",
            f"免责声明：{DISCLAIMER} 本应用不提供荐股、自动交易、交易指令、目标价或收益承诺。",
            "",
        ]
        for index, section in enumerate(sections, start=1):
            lines.extend([f"## {index}. {section['title']}", ""])
            for label, key in [("Facts", "facts"), ("Inference", "inference"), ("Assumption", "assumption"), ("Opinion", "opinion")]:
                values = section[key] or ["SKIP：本节暂无可验证内容，需补充证据。"]
                lines.append(f"### {label}")
                lines.extend(f"- {item}" for item in values)
                lines.append("")
        return "\n".join(lines).rstrip() + "\n"

    def _normalize_engine_block(self, block: dict[str, Any]) -> dict[str, Any]:
        return {
            "facts": [str(block)],
            "inference": ["来自 Investment Engine 的结构化分析结果，需绑定真实证据后提升置信度。"],
            "assumption": ["Engine 结果为研究框架输出，不等同于真实公司结论。"],
            "opinion": ["本节用于提示后续研究方向。"],
        }

    def _evidence_block(self, analysis: dict[str, Any]) -> dict[str, Any]:
        chain = analysis["evidence_chain"]
        return {
            "facts": [f"Evidence Chain ID：{chain['chain_id']}", f"证据卡：{', '.join(chain['evidence_cards'])}"],
            "inference": [f"整体置信度：{chain['overall_confidence']}"],
            "assumption": chain["missing_evidence"],
            "opinion": ["证据链优先用于追溯和复核，不直接推出投资动作。"],
        }

    def _kg_block(self, analysis: dict[str, Any]) -> dict[str, Any]:
        kg = analysis["knowledge_graph"]
        return {
            "facts": [f"KG ID：{kg['graph_id']}", f"节点数：{len(kg['nodes'])}；边数：{len(kg['edges'])}"],
            "inference": [str(item) for item in kg.get("path_analysis", [])],
            "assumption": ["图谱结构依赖当前证据卡，证据更新后需重建。"],
            "opinion": ["KG 适合发现研究路径和薄弱环节。"],
        }

    def _score_block(self, analysis: dict[str, Any]) -> dict[str, Any]:
        score = analysis["score_card"]
        return {
            "facts": [f"Scorecard ID：{score['scorecard_id']}", f"Quality Gate：{score['quality_gate']}"],
            "inference": [f"Overall Score：{score['overall_score']}；Confidence：{score['confidence_score']}"],
            "assumption": [item["explanation"] for item in score["scores"]],
            "opinion": ["评分用于研究质量控制，不是投资评级。"],
        }

    def _committee_block(self, committee: dict[str, Any]) -> dict[str, Any]:
        decision = committee.get("decision", {})
        session = committee.get("session", {})
        return {
            "facts": [f"Committee Session：{session.get('session_id')}", f"Vote：{committee.get('vote', {}).get('outcome')}"],
            "inference": [decision.get("final_recommendation", session.get("final_recommendation", "需要二次审议。"))],
            "assumption": session.get("unresolved_questions", []),
            "opinion": session.get("minority_report", []),
        }

    def _appendix_block(self, request: ResearchRequest, company: CompanyInfo, analysis: dict[str, Any], committee: dict[str, Any]) -> dict[str, Any]:
        return {
            "facts": [
                f"Request：{request.to_dict()}",
                f"Company Traceability：{company.traceability}",
                f"Evidence Refs：{list(analysis['evidence_chain']['evidence_cards'])}",
            ],
            "inference": ["所有章节均保留 Facts / Inference / Assumption / Opinion 标记。"],
            "assumption": ["附录中的 Connector 结果可能包含 Mock/SKIP 降级。"],
            "opinion": ["发布前应由 Review Agent 复核来源与语气。"],
        }


def _as_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item) for item in value]
    return [str(value)]

