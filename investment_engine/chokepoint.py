"""Chokepoint analysis component for investment research."""

from __future__ import annotations

from typing import Any


def analyze_chokepoints(supply_chain: dict[str, Any]) -> dict[str, Any]:
    constraints = []
    for idx, node in enumerate(supply_chain["nodes"][:2], start=1):
        constraints.append(
            {
                "chokepoint_id": f"cp-{idx:02d}",
                "node_id": node["node_id"],
                "label": node["label"],
                "severity": 0.72 - idx * 0.06,
                "evidence_refs": [f"ev-{idx:02d}"],
                "counter_evidence_refs": [f"ev-counter-{idx:02d}"],
                "missing_evidence": ["需要更多订单、产能、价格或政策证据交叉验证"],
            }
        )
    return {
        "component": "chokepoint",
        "methodology_refs": ["docs/methodology/supply-chain-chokepoint.md"],
        "knowledge_graph_refs": ["schemas/knowledge-graph/knowledge-graph.schema.json"],
        "chokepoints": constraints,
    }
