"""Shared learning example builder."""
from __future__ import annotations

from typing import Any

from learning import ContinuousImprovementEngine


def build_payload(case_id: str, topic: str, module: str, issue: str) -> dict[str, Any]:
    return {
        "learning_id": f"LEARN-{case_id}",
        "source_refs": [
            "docs/runtime/memory-manager.md",
            "docs/committee/committee-architecture.md",
            "docs/investment-engine/engine-architecture.md",
            "schemas/report/report.schema.json",
        ],
        "feedback": [
            {
                "feedback_id": f"FB-{case_id}-001",
                "source_type": "review",
                "source_ref": f"docs/review/{case_id}.md",
                "target_module": module,
                "issue_type": issue,
                "severity": "high",
                "observation": f"{topic} 案例中 {module} 出现 {issue}，需要补充可复核来源。",
                "evidence_refs": ["schemas/evidence/evidence-chain.schema.json"],
            },
            {
                "feedback_id": f"FB-{case_id}-002",
                "source_type": "committee",
                "source_ref": "schemas/committee/committee-decision.schema.json",
                "target_module": module,
                "issue_type": issue,
                "severity": "medium",
                "observation": f"Committee 对 {topic} 的反方观点要求更明确的证据等级。",
                "evidence_refs": ["schemas/committee/committee-vote.schema.json"],
            },
        ],
        "outcomes": [
            {
                "outcome_id": f"OUT-{case_id}-001",
                "research_ref": f"REPORT-{case_id}",
                "expected_result": "研究结论应被后续证据支持",
                "observed_result": "后续复核发现部分假设需要降级为不确定性",
                "horizon": "post_report_review",
                "variance_level": "high",
                "evidence_refs": ["schemas/score/scorecard.schema.json"],
                "lessons": ["提高缺失证据惩罚", "强化反方观点入口"],
            }
        ],
    }


def run_case(case_id: str, topic: str, module: str, issue: str) -> dict[str, Any]:
    return ContinuousImprovementEngine().run(build_payload(case_id, topic, module, issue))

