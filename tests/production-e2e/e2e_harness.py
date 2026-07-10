"""Production E2E harness for AIRS v1.0.0-rc1 validation.

The harness intentionally calls the real AIRS module entrypoints instead of
reading static examples: planner -> runtime -> connectors -> KG -> investment
engine -> committee -> memory -> learning.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from committee.coordinator import run_committee
from common.contract import CONTRACT_VERSION, runtime_task_from_planner_task
from common.contract_validation import summarize_data_lineage
from common.release_gate import evaluate_connector_lineage
from data_connectors.base import ConnectorRequest
from data_connectors.registry import default_registry as default_connector_registry
from investment_engine.pipeline import run_research
from knowledge_graph.builder import KnowledgeGraphBuilder
from knowledge_graph.model import EvidenceBinding
from knowledge_graph.validator import KnowledgeGraphValidator
from learning.engine import ContinuousImprovementEngine
from planner.engine import plan_research
from orchestrator import run_planned_workflow
from workspace.memory import WorkspaceMemory


ROOT = Path(__file__).resolve().parents[2]
ARTIFACT_ROOT = ROOT / "docs" / "testing" / "artifacts"
DISCLAIMER_FRAGMENT = "不构成投资建议"
STATEMENT_TYPES = {"Fact", "Inference", "Assumption", "Opinion"}


@dataclass(frozen=True)
class E2ECase:
    case_id: str
    title: str
    topic: str
    scope: str
    time_horizon: str
    connectors: list[dict[str, Any]]
    expectations: dict[str, Any]


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")


def build_investment_request(case: E2ECase) -> dict[str, Any]:
    return {
        "request_id": case.case_id,
        "topic": case.topic,
        "scope": case.scope,
        "time_horizon": case.time_horizon,
        "compliance": {
            "no_recommendation": True,
            "statement_types_required": sorted(STATEMENT_TYPES),
        },
    }


def runtime_plan_for_core(plan: dict[str, Any], case_id: str) -> dict[str, Any]:
    """Attach case metadata while preserving the production contract."""

    runtime_plan = dict(plan["required_runtime"])
    runtime_plan["contract_version"] = CONTRACT_VERSION
    runtime_plan["tasks"] = [
        runtime_task_from_planner_task(task, plan_id=plan["plan_id"], case_id=case_id)
        for task in runtime_plan.get("tasks", [])
    ]
    return runtime_plan


def fetch_connector_trace(case: E2ECase) -> list[dict[str, Any]]:
    registry = default_connector_registry()
    trace: list[dict[str, Any]] = []
    for spec in case.connectors:
        connector = registry.get(spec["connector_id"])
        result = connector.fetch(ConnectorRequest(spec["query"]))
        trace.append(
            {
                "case_id": case.case_id,
                "connector_id": connector.connector_id,
                "request": spec["query"],
                "result": result.to_dict(),
                "required_output_fields": connector.output_schema().get("required", []),
            }
        )
    return trace


def assert_connector_trace(trace: list[dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    for item in trace:
        result = item["result"]
        if result.get("error"):
            errors.append(f"{item['connector_id']} returned error: {result['error']}")
        for field in item["required_output_fields"]:
            if field not in result:
                errors.append(f"{item['connector_id']} missing required field: {field}")
        if DISCLAIMER_FRAGMENT not in result.get("disclaimer", ""):
            errors.append(f"{item['connector_id']} missing investment disclaimer")
    return errors


def build_validated_kg(case: E2ECase, engine_result: dict[str, Any], connector_trace: list[dict[str, Any]]) -> dict[str, Any]:
    evidence_cards = dict(engine_result["evidence_chain"]["evidence_cards"])
    first_trace = connector_trace[0]["result"]["trace_id"] if connector_trace else case.case_id
    builder = KnowledgeGraphBuilder(
        graph_id=f"prod-kg-{case.case_id}",
        title=f"{case.title} Production KG",
        research_question=case.scope,
        methodology_refs=["docs/methodology/evidence-chain.md", "docs/methodology/supply-chain-chokepoint.md"],
        evidence_cards=evidence_cards,
    )
    builder.add_node(
        {
            "node_id": "topic",
            "node_type": "industry",
            "label": case.topic,
            "source_refs": [f"connector-trace:{first_trace}"],
            "confidence": 0.82,
            "evidence_bindings": [
                EvidenceBinding("ev-01", "st-fact-01", "supports", "strong").to_dict(),
            ],
            "attributes": {"case_id": case.case_id},
        }
    )
    builder.add_node(
        {
            "node_id": "claim",
            "node_type": "claim",
            "label": engine_result["investment_thesis"]["core_thesis"],
            "source_refs": [engine_result["evidence_chain"]["chain_id"]],
            "confidence": engine_result["evidence_chain"]["overall_confidence"],
            "evidence_bindings": [
                EvidenceBinding("ev-02", "st-infer-01", "supports", "medium").to_dict(),
                EvidenceBinding("ev-counter-01", "st-infer-01", "refutes", "medium").to_dict(),
            ],
            "attributes": {"statement_type": "Inference"},
        }
    )
    builder.add_node(
        {
            "node_id": "risk",
            "node_type": "risk",
            "label": "counter evidence and missing evidence risk",
            "source_refs": [engine_result["evidence_chain"]["chain_id"]],
            "confidence": 0.64,
            "evidence_bindings": [
                EvidenceBinding("ev-counter-02", "st-assume-01", "refutes", "medium").to_dict(),
            ],
            "attributes": {"missing_evidence": engine_result["evidence_chain"]["missing_evidence"]},
        }
    )
    builder.add_edge(
        {
            "edge_id": "edge-topic-claim",
            "from_node": "topic",
            "to_node": "claim",
            "relation_type": "supports",
            "evidence_refs": ["ev-01", "ev-02"],
            "counter_evidence_refs": ["ev-counter-01"],
            "missing_evidence": ["connector raw source freshness check"],
            "confidence": 0.68,
        }
    )
    builder.add_edge(
        {
            "edge_id": "edge-risk-claim",
            "from_node": "risk",
            "to_node": "claim",
            "relation_type": "refutes",
            "evidence_refs": ["ev-counter-01", "ev-counter-02"],
            "counter_evidence_refs": ["ev-01"],
            "missing_evidence": ["validated operating metrics"],
            "confidence": 0.58,
        }
    )
    graph = builder.build()
    validation = KnowledgeGraphValidator().validate(graph)
    return {
        "graph": graph.to_dict(),
        "validation": {
            "passed": validation.passed,
            "errors": validation.errors,
            "warnings": validation.warnings,
        },
    }


def assert_report_taxonomy(engine_result: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    recommendation = engine_result["recommendation"]
    coverage = recommendation.get("statement_coverage", {})
    missing = [kind for kind in STATEMENT_TYPES if coverage.get(kind, 0) < 1]
    if missing:
        errors.append(f"recommendation missing statement types: {', '.join(sorted(missing))}")
    statements = recommendation.get("statements", [])
    for item in statements:
        if item.get("statement_type") not in STATEMENT_TYPES:
            errors.append(f"invalid statement type: {item}")
    report = engine_result.get("final_research_report", "")
    if "Facts/Inference/Assumption/Opinion" not in report:
        errors.append("final report does not explicitly mention Facts/Inference/Assumption/Opinion coverage")
    if DISCLAIMER_FRAGMENT not in report:
        errors.append("final report missing disclaimer")
    return errors


def run_production_case(case_data: dict[str, Any]) -> dict[str, Any]:
    case = E2ECase(**case_data)
    started_at = now_iso()
    request = build_investment_request(case)
    plan = plan_research(
        {
            "goal_id": case.case_id,
            "raw_goal": f"{case.topic}: {case.scope}",
            "goal_type": "comparative" if "对比" in case.scope else "supply_chain",
            "subject": case.topic,
            "time_horizon": case.time_horizon,
            "constraints": ["no direct recommendation", "trace all evidence"],
            "success_criteria": ["complete production E2E trace", "separate Fact/Inference/Assumption/Opinion"],
        }
    )
    runtime_plan = runtime_plan_for_core(plan, case.case_id)
    orchestration = run_planned_workflow({**plan, "required_runtime": runtime_plan}, case_id=case.case_id)
    runtime = orchestration["runtime"]
    connector_trace = fetch_connector_trace(case)
    engine_result = run_research(request)
    kg_state = build_validated_kg(case, engine_result, connector_trace)
    committee = run_committee(plan)

    memory = WorkspaceMemory()
    memory.remember(
        "airs-production-e2e",
        case.case_id,
        {
            "plan_id": plan["plan_id"],
            "scorecard": engine_result["score_card"],
            "committee_decision": committee["decision"],
        },
        source_ref=engine_result["evidence_chain"]["chain_id"],
        actor="production-e2e-runner",
    )
    memory_read = memory.recall("airs-production-e2e", case.case_id)

    learning = ContinuousImprovementEngine().run(
        {
            "learning_id": f"learn-{case.case_id}",
            "source_refs": [engine_result["evidence_chain"]["chain_id"], kg_state["graph"]["graph_id"]],
            "feedback": [
                {
                    "source_type": "production_e2e",
                    "source_ref": case.case_id,
                    "target_module": "report",
                    "issue_type": "traceability_check",
                    "severity": "low",
                    "observation": "Production E2E verified traceability through planner, runtime, connectors, KG, committee, memory, and learning.",
                    "evidence_refs": list(engine_result["evidence_chain"]["evidence_cards"]),
                }
            ],
            "outcomes": [
                {
                    "outcome_id": f"outcome-{case.case_id}",
                    "source_ref": case.case_id,
                    "metric_name": "production_e2e_quality_gate",
                    "metric_value": 1.0 if engine_result["score_card"]["quality_gate"] in {"PASS", "CONDITIONAL_PASS"} else 0.0,
                    "expected_value": 1.0,
                    "metadata": {"case_title": case.title},
                }
            ],
        }
    )

    checks = []
    errors = []
    connector_errors = assert_connector_trace(connector_trace)
    connector_lineage = summarize_data_lineage([item["result"] for item in connector_trace])
    stable_gate = evaluate_connector_lineage(
        connector_lineage,
        require_real_sources=bool(case.expectations.get("require_real_sources")),
        min_real_sources=int(case.expectations.get("min_real_sources", 1)),
        allow_degraded=bool(case.expectations.get("allow_degraded_sources", False)),
    )
    report_errors = assert_report_taxonomy(engine_result)
    kg_errors = [] if kg_state["validation"]["passed"] else kg_state["validation"]["errors"]
    runtime_errors = [] if runtime["final_state"]["runtime_state"].get("status") == "COMPLETED" else ["runtime did not complete"]
    memory_errors = [] if memory_read and memory_read.get("source_ref") == engine_result["evidence_chain"]["chain_id"] else ["memory read/write mismatch"]
    learning_errors = [] if learning.get("feedback") and learning.get("memory_consolidation") else ["learning feedback missing"]

    check_map = {
        "planner": bool(plan.get("execution_order") and plan.get("required_runtime")),
        "runtime": not runtime_errors,
        "connectors": not connector_errors,
        "connector_lineage": bool(connector_lineage["real_sources"] or connector_lineage["mock_sources"] or connector_lineage["skipped_sources"]),
        "stable_release_gate": stable_gate.passed if case.expectations.get("require_real_sources") else True,
        "evidence_trace": len(engine_result["evidence_chain"]["evidence_cards"]) >= case.expectations.get("min_evidence_cards", 4),
        "knowledge_graph": not kg_errors,
        "scorecard": engine_result["score_card"]["quality_gate"] in {"PASS", "CONDITIONAL_PASS"},
        "committee": bool(committee.get("vote") and committee.get("decision")),
        "report_taxonomy": not report_errors,
        "memory": not memory_errors,
        "learning": not learning_errors,
    }
    for name, passed in check_map.items():
        checks.append({"name": name, "status": "PASS" if passed else "FAIL"})
    errors.extend(connector_errors + report_errors + kg_errors + runtime_errors + memory_errors + learning_errors)
    errors.extend(stable_gate.errors)
    if not check_map["planner"]:
        errors.append("planner did not produce runtime plan and execution order")

    status = "PASS" if all(item["status"] == "PASS" for item in checks) else "FAIL"
    artifact = {
        "case_id": case.case_id,
        "title": case.title,
        "status": status,
        "started_at": started_at,
        "completed_at": now_iso(),
        "checks": checks,
        "errors": errors,
        "execution_log": runtime["event_log"],
        "orchestrator": orchestration,
        "evidence_trace": connector_trace,
        "connector_lineage": connector_lineage,
        "stable_release_gate": stable_gate.to_dict(),
        "airs_evidence_chain": engine_result["evidence_chain"],
        "kg_state": kg_state,
        "scorecard": engine_result["score_card"],
        "committee_debate": committee,
        "final_report": engine_result["final_research_report"],
        "memory_write_read": memory_read,
        "learning_feedback": learning,
        "disclaimer": engine_result["disclaimer"],
    }
    write_json(ARTIFACT_ROOT / "production-e2e" / f"{case.case_id}.json", artifact)
    return artifact
