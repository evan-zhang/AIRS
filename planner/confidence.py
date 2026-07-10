"""Confidence planner."""

from __future__ import annotations

from typing import Any


def plan_confidence(intent: dict[str, Any], budget: dict[str, Any]) -> dict[str, Any]:
    evidence_depth = min(0.9, 0.45 + len(intent["required_connectors"]) * 0.08)
    method_fit = min(0.9, 0.5 + len(intent["required_methodologies"]) * 0.07)
    budget_fit = 0.8 if budget["budget_gate"] == "PASS" else 0.62
    overall = round(evidence_depth * 0.45 + method_fit * 0.35 + budget_fit * 0.20, 2)
    return {
        "evidence_confidence": round(evidence_depth, 2),
        "methodology_fit": round(method_fit, 2),
        "budget_fit": budget_fit,
        "overall_confidence": overall,
        "confidence_gate": "PASS" if overall >= 0.7 else "CONDITIONAL_PASS",
        "uncertainties": ["证据时效性", "反方证据强度", "数据源覆盖范围"],
    }
