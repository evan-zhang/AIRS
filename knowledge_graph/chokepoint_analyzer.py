"""Supply-chain chokepoint analysis for AIRS knowledge graphs."""

from __future__ import annotations

from .model import KnowledgeGraph


class ChokepointAnalyzer:
    """Score supply-chain nodes by constraint attributes and graph position."""

    WEIGHTS = {
        "scarcity": 0.22,
        "substitutability": 0.18,
        "capacity_expansion_difficulty": 0.2,
        "certification_cycle": 0.14,
        "bargaining_power": 0.14,
        "evidence_quality": 0.12,
    }

    def analyze(self, graph: KnowledgeGraph, top_n: int = 5) -> list[dict[str, object]]:
        rows: list[dict[str, object]] = []
        for node in graph.nodes.values():
            if node.node_type not in {"supply_chain_node", "product"}:
                continue
            attrs = node.attributes
            score = 0.0
            for key, weight in self.WEIGHTS.items():
                score += float(attrs.get(key, 0.5)) * weight
            upstream = len(graph.incoming(node.node_id))
            downstream = len(graph.outgoing(node.node_id))
            position_bonus = min((upstream + downstream) / 10, 0.12)
            score = round(min(score + position_bonus, 1), 4)
            rows.append(
                {
                    "node_id": node.node_id,
                    "label": node.label,
                    "chokepoint_score": score,
                    "risk_level": self._risk_level(score),
                    "drivers": self._drivers(attrs),
                    "evidence_refs": sorted({binding.evidence_id for binding in node.evidence_bindings} | set(node.source_refs)),
                    "counter_evidence_refs": sorted(self._counter_evidence_for_node(graph, node.node_id)),
                    "missing_evidence": attrs.get("missing_evidence", ["需要持续跟踪产能、交期、良率和替代路线。"]),
                }
            )
        return sorted(rows, key=lambda item: float(item["chokepoint_score"]), reverse=True)[:top_n]

    def _counter_evidence_for_node(self, graph: KnowledgeGraph, node_id: str) -> set[str]:
        refs: set[str] = set()
        for edge in graph.incoming(node_id) + graph.outgoing(node_id):
            refs.update(edge.counter_evidence_refs)
        return refs

    def _drivers(self, attrs: dict[str, object]) -> list[str]:
        labels = {
            "scarcity": "供给稀缺",
            "substitutability": "替代难度高",
            "capacity_expansion_difficulty": "扩产难度高",
            "certification_cycle": "认证周期长",
            "bargaining_power": "议价能力强",
            "evidence_quality": "证据质量较高",
        }
        drivers = [label for key, label in labels.items() if float(attrs.get(key, 0.0)) >= 0.7]
        return drivers or ["当前证据不足以形成高强度卡点判断"]

    def _risk_level(self, score: float) -> str:
        if score >= 0.75:
            return "HIGH"
        if score >= 0.55:
            return "MEDIUM"
        return "LOW"
