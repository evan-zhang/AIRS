"""APP-001 Equity Research App 主入口。"""

from __future__ import annotations

from typing import Any

from committee import run_committee
from common.contract_validation import classify_research_status, summarize_data_lineage, validate_research_contract
from common.release_gate import evaluate_connector_lineage
from learning import ContinuousImprovementEngine
from orchestrator import run_planned_workflow
from planner import plan_research
from runtime.memory_manager import MemoryManager

from .analyzer import EquityResearchAnalyzer
from .company_resolver import resolve_company
from .data_collector import EquityDataCollector
from .report_exporter import EquityResearchReportExporter
from .request_parser import parse_research_request


DISCLAIMER = "APP-001 仅用于股票研究流程编排和研究质量控制，不构成投资建议。"


class EquityResearchApp:
    """用户输入股票代码/公司名称/研究问题后，执行 AIRS 全链路研究流程。"""

    def __init__(self) -> None:
        self.collector = EquityDataCollector()
        self.analyzer = EquityResearchAnalyzer()
        self.exporter = EquityResearchReportExporter()
        self.memory = MemoryManager()
        self.learning = ContinuousImprovementEngine()

    def run(self, user_input: str | dict[str, Any]) -> dict[str, Any]:
        request = parse_research_request(user_input)
        company = resolve_company(request)
        plan = plan_research(
            {
                "goal_id": request.request_id,
                "raw_goal": request.research_question,
                "goal_type": "company_research",
                "subject": company.company_name,
                "time_horizon": request.time_range,
                "constraints": ["必须区分 Facts/Inference/Assumption/Opinion", "不得输出投资建议或交易指令"],
                "success_criteria": ["生成 15 段股票研究报告", "保留证据链、KG、Score 和 Committee Decision"],
            }
        )
        first_committee = run_committee(plan)
        orchestration = run_planned_workflow(plan, case_id=request.request_id)
        runtime_result = orchestration["runtime"]
        data_bundle = self.collector.collect(request, company)
        analysis = self.analyzer.analyze(request, company, data_bundle)
        second_committee = run_committee({**plan, "evidence_chain": analysis["evidence_chain"], "score_card": analysis["score_card"]})
        report = self.exporter.export(request, company, analysis, second_committee)
        contract_validation = validate_research_contract(analysis, report)
        data_lineage = summarize_data_lineage(data_bundle.connector_results)
        require_real_data = request.require_real_data or any(item["query"].get("mode") == "real" for item in data_bundle.plan)
        stable_gate = evaluate_connector_lineage(
            data_lineage,
            require_real_sources=require_real_data,
            min_real_sources=2 if require_real_data else 0,
            allow_degraded=False,
        )
        status = classify_research_status(contract_validation, data_lineage, require_real_data=require_real_data)
        if require_real_data and not stable_gate.passed:
            status = "failed_quality_gate"
        self.memory.remember(request.request_id, "equity_research_result", {"company": company.to_dict(), "score_card": analysis["score_card"]}, source_event_id=runtime_result.get("event_log", [{}])[-1].get("event_id"))
        learning_result = self.learning.run(
            {
                "learning_id": f"learn-{request.request_id}",
                "source_refs": [request.request_id, analysis["score_card"]["scorecard_id"]],
                "feedback": [
                    {
                        "source_type": "app_self_check",
                        "source_ref": request.request_id,
                        "target_module": "apps/equity_research",
                        "issue_type": "data_degradation",
                        "severity": "medium" if data_bundle.degradation_notes else "low",
                        "observation": "记录 Connector Mock/SKIP 降级，等待真实源补充。",
                        "evidence_refs": list(analysis["evidence_chain"]["evidence_cards"]),
                    }
                ],
                "outcomes": [],
            }
        )
        return {
            "app_id": "APP-001",
            "app_version": "1.0.0",
            "status": status,
            "quality_gate": "PASS" if status == "completed" else "CONDITIONAL_PASS" if status == "completed_with_degradation" else "FAIL",
            "request": request.to_dict(),
            "company": company.to_dict(),
            "planner": plan,
            "committee_initial": first_committee,
            "orchestrator": orchestration,
            "runtime": runtime_result,
            "data_collection": data_bundle.to_dict(),
            "data_lineage": data_lineage,
            "stable_release_gate": stable_gate.to_dict(),
            "analysis": analysis,
            "contract_validation": contract_validation.to_dict(),
            "committee_final": second_committee,
            "report": report,
            "memory": self.memory.recall(request.request_id),
            "learning": learning_result,
            "disclaimer": DISCLAIMER,
        }


def run_equity_research(user_input: str | dict[str, Any]) -> dict[str, Any]:
    return EquityResearchApp().run(user_input)


if __name__ == "__main__":
    import argparse
    import json

    parser = argparse.ArgumentParser(description="运行 APP-001 Equity Research App。")
    parser.add_argument("query", help="股票代码、公司名称或研究问题")
    parser.add_argument("--markdown", help="可选：导出 Markdown 路径")
    args = parser.parse_args()
    result = run_equity_research(args.query)
    if args.markdown:
        EquityResearchReportExporter().write_markdown(result["report"], args.markdown)
        print(args.markdown)
    else:
        print(json.dumps(result, ensure_ascii=False, indent=2))
