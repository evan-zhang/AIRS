"""Failure-injection tests for AIRS production E2E validation."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from common.contract import CONTRACT_VERSION, runtime_task_from_planner_task
from data_connectors.base import ConnectorConfig, ConnectorRequest, ConnectorResult, HealthStatus
from data_connectors.connectors.news import NewsConnector
from data_connectors.retry import run_with_retry
from knowledge_graph.builder import KnowledgeGraphBuilder
from knowledge_graph.validator import KnowledgeGraphValidator
from planner.engine import plan_research
from runtime.core import RuntimeCore


ROOT = Path(__file__).resolve().parents[2]
ARTIFACT_ROOT = ROOT / "docs" / "testing" / "artifacts" / "failure-injection"


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")


def runtime_plan_for_core(plan: dict[str, Any]) -> dict[str, Any]:
    runtime_plan = dict(plan["required_runtime"])
    runtime_plan["contract_version"] = CONTRACT_VERSION
    runtime_plan["tasks"] = [
        runtime_task_from_planner_task(task, plan_id=plan["plan_id"])
        for task in runtime_plan.get("tasks", [])
    ]
    return runtime_plan


class FlakyTimeoutConnector(NewsConnector):
    """Connector that fails with retryable timeouts before succeeding."""

    def __init__(self, fail_attempts: int = 2) -> None:
        super().__init__()
        self.config = ConnectorConfig(
            connector_id="flaky_timeout_news",
            name="Flaky Timeout News",
            source=self.config.source,
            source_type=self.config.source_type,
            base_url=self.config.base_url,
            version=self.config.version,
            priority=self.config.priority,
            auth_type=self.config.auth_type,
            retry_policy=self.config.retry_policy,
            cache_strategy=self.config.cache_strategy,
        )
        self.fail_attempts = fail_attempts
        self.attempts = 0

    def fetch(self, request: ConnectorRequest) -> ConnectorResult:
        self.attempts += 1
        if self.attempts <= self.fail_attempts:
            raise TimeoutError(f"simulated connector timeout attempt={self.attempts}")
        return super().fetch(request)


def connector_timeout_retry() -> dict[str, Any]:
    connector = FlakyTimeoutConnector(fail_attempts=2)
    request = ConnectorRequest({"query": "timeout retry case", "language": "zh"})
    result = run_with_retry(lambda: connector.fetch(request), connector.config.retry_policy)
    passed = connector.attempts == 3 and result.error is None and result.trace_id == request.trace_id
    artifact = {
        "case_id": "failure-connector-timeout",
        "status": "PASS" if passed else "FAIL",
        "started_at": now_iso(),
        "attempts": connector.attempts,
        "result": result.to_dict(),
        "expected": "RetryPolicy should retry two timeout failures and recover on third attempt.",
        "errors": [] if passed else ["connector retry did not recover as expected"],
    }
    write_json(ARTIFACT_ROOT / "failure-connector-timeout.json", artifact)
    return artifact


def schema_error_interception() -> dict[str, Any]:
    builder = KnowledgeGraphBuilder(
        graph_id="invalid-schema-kg",
        title="Invalid Schema KG",
        research_question="Schema validator should reject malformed KG node and edge",
        methodology_refs=["docs/methodology/evidence-chain.md"],
        evidence_cards={"ev-01": {"evidence_id": "ev-01", "title": "valid evidence"}},
    )
    builder.add_node(
        {
            "node_id": "bad-node",
            "node_type": "unsupported_type",
            "label": "bad node",
            "source_refs": [],
            "confidence": 1.2,
            "evidence_bindings": [{"evidence_id": "missing-ev", "claim_id": "claim-1", "relation": "supports"}],
        }
    )
    builder.add_edge(
        {
            "edge_id": "bad-edge",
            "from_node": "bad-node",
            "to_node": "missing-node",
            "relation_type": "invalid_relation",
            "evidence_refs": ["missing-ev"],
            "directionality": "sideways",
            "confidence": -0.1,
        }
    )
    validation = KnowledgeGraphValidator().validate(builder.build())
    required_error_fragments = ["类型非法", "缺少 source_refs", "不存在", "引用未知 Evidence", "confidence"]
    passed = not validation.passed and all(any(fragment in error for error in validation.errors) for fragment in required_error_fragments)
    artifact = {
        "case_id": "failure-schema-error",
        "status": "PASS" if passed else "FAIL",
        "started_at": now_iso(),
        "validation": {"passed": validation.passed, "errors": validation.errors, "warnings": validation.warnings},
        "expected": "KG validator should intercept malformed schema data before report generation.",
        "errors": [] if passed else ["schema validator did not surface all expected errors"],
    }
    write_json(ARTIFACT_ROOT / "failure-schema-error.json", artifact)
    return artifact


def runtime_interruption_recovery() -> dict[str, Any]:
    plan = plan_research(
        {
            "goal_id": "failure-runtime-interruption",
            "raw_goal": "AIRS runtime interruption recovery",
            "goal_type": "theme",
            "subject": "AIRS runtime",
            "time_horizon": "test",
            "constraints": ["simulate cancellation"],
            "success_criteria": ["partial state is preserved"],
        }
    )
    runtime_plan = runtime_plan_for_core(plan)
    runtime = RuntimeCore()
    tasks = runtime_plan["tasks"]
    if len(tasks) > 1:
        runtime.dispatcher.cancellation.cancel(tasks[1]["task_id"])
    result = runtime.run_workflow(runtime_plan)
    task_states = result["final_state"]["task_states"]
    cancelled = any(state == "CANCELLED" for state in task_states.values())
    blocked = any(state == "BLOCKED" for state in task_states.values())
    has_event = any(event["event_type"] in {"TASK_CANCELLED", "TASK_BLOCKED"} for event in result["event_log"])
    passed = cancelled and blocked and has_event and result["final_state"]["quality_gate"] == "PARTIAL"
    artifact = {
        "case_id": "failure-runtime-interruption",
        "status": "PASS" if passed else "FAIL",
        "started_at": now_iso(),
        "task_states": task_states,
        "event_log": result["event_log"],
        "expected": "Runtime should mark cancelled task, block dependents, and preserve resumable partial state.",
        "errors": [] if passed else ["runtime interruption did not preserve expected partial state"],
    }
    write_json(ARTIFACT_ROOT / "failure-runtime-interruption.json", artifact)
    return artifact


def run_failure_case(case_id: str) -> dict[str, Any]:
    cases = {
        "failure-connector-timeout": connector_timeout_retry,
        "failure-schema-error": schema_error_interception,
        "failure-runtime-interruption": runtime_interruption_recovery,
    }
    return cases[case_id]()
