"""Autonomous Research Planner engine."""

from __future__ import annotations

from typing import Any

from .budget import plan_budget
from .confidence import plan_confidence
from .dependency import plan_dependencies
from .goal_parser import DISCLAIMER, parse_goal
from .intent_analyzer import analyze_intent
from .optimizer import optimize_plan
from .resource import plan_resources
from .runtime import plan_runtime
from .scope_builder import build_scope
from .workflow import plan_workflow


class AutonomousResearchPlanner:
    """Create AIRS Research Plans before Runtime execution."""

    infrastructure_refs = {
        "planner": "docs/planner/planner-architecture.md",
        "runtime": "docs/runtime/runtime-architecture.md",
        "workflow": "docs/orchestrator/orchestrator-architecture.md",
        "methodology": "docs/methodology/",
        "connector": "docs/data-connectors/connector-interface.md",
        "skill": "skills/README.md",
        "knowledge_graph": "schemas/knowledge-graph/knowledge-graph.schema.json",
        "evidence": "schemas/evidence/evidence-chain.schema.json",
        "score": "schemas/score/scorecard.schema.json",
        "report": "templates/report/research-report-template.md",
        "workspace": "docs/workspace/workspace-architecture.md",
    }

    def plan(self, goal: str | dict[str, Any]) -> dict[str, Any]:
        parsed_goal = parse_goal(goal)
        intent = analyze_intent(parsed_goal)
        scope = build_scope(parsed_goal, intent)
        dependencies = plan_dependencies(intent)
        workflow = plan_workflow(parsed_goal, intent, dependencies)
        resources = plan_resources(intent, scope)
        budget = plan_budget(resources)
        confidence = plan_confidence(intent, budget)
        runtime = plan_runtime(parsed_goal, workflow, budget)
        plan = {
            "planner_version": "0.1.0",
            "plan_id": f"plan-{parsed_goal['goal_id']}",
            "goal_analysis": parsed_goal,
            "intent_analysis": intent,
            "scope": scope,
            "required_connectors": intent["required_connectors"],
            "required_methodologies": intent["required_methodologies"],
            "required_skills": intent["required_skills"],
            "required_runtime": runtime,
            "expected_evidence": {
                "evidence_chain_ref": "schemas/evidence/evidence-chain.schema.json",
                "minimum_cards": 4,
                "counter_evidence_required": True,
                "missing_evidence_required": True,
            },
            "expected_kg": {
                "kg_schema_ref": "schemas/knowledge-graph/knowledge-graph.schema.json",
                "nodes": ["research_subject", "evidence", "methodology", "risk", "deliverable"],
                "edges": ["supports", "refutes", "depends_on", "produces"],
            },
            "execution_order": dependencies["critical_path"],
            "dependencies": dependencies,
            "workflow": workflow,
            "resources": resources,
            "budget": budget,
            "confidence": confidence,
            "expected_deliverables": [
                "Research Plan",
                "Runtime Plan",
                "Workflow Spec",
                "Evidence Plan",
                "Knowledge Graph Plan",
                "Scorecard Plan",
                "Final Report Outline",
                "Review Checklist",
            ],
            "risks": ["证据不足", "数据源延迟", "方法论适配偏差", "Runtime 绕过 Planner 的集成风险"],
            "infrastructure_refs": self.infrastructure_refs,
            "disclaimer": DISCLAIMER,
        }
        return optimize_plan(plan)


def plan_research(goal: str | dict[str, Any]) -> dict[str, Any]:
    return AutonomousResearchPlanner().plan(goal)
