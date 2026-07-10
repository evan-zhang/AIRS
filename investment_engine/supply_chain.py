"""Supply-chain analysis component for investment research."""

from __future__ import annotations

from typing import Any


def analyze_supply_chain(theme: dict[str, Any], companies: dict[str, Any]) -> dict[str, Any]:
    nodes = [
        {"node_id": "upstream", "label": theme["signals"][0], "type": "supply_chain_node"},
        {"node_id": "midstream", "label": theme["signals"][1], "type": "supply_chain_node"},
        {"node_id": "downstream", "label": theme["topic"], "type": "industry"},
    ]
    edges = [
        {"from": "upstream", "to": "midstream", "relation": "depends_on", "evidence_refs": ["ev-01"]},
        {"from": "midstream", "to": "downstream", "relation": "supports", "evidence_refs": ["ev-02"]},
    ]
    return {
        "component": "supply_chain",
        "methodology_refs": ["docs/methodology/supply-chain-chokepoint.md"],
        "skill_refs": ["skills/supply-chain/supply-chain-skill.md"],
        "nodes": nodes,
        "edges": edges,
        "company_roles": companies["companies"],
    }
