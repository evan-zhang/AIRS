"""Core data model for AIRS Knowledge Graph Engine."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


DISCLAIMER = "本图谱仅用于 AIRS 投资研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。"

NODE_TYPES = {
    "company",
    "industry",
    "product",
    "supply_chain_node",
    "policy",
    "event",
    "evidence",
    "claim",
    "risk",
}

RELATION_TYPES = {
    "supports",
    "refutes",
    "depends_on",
    "belongs_to",
    "affected_by",
    "competes_with",
    "has_risk",
}

DIRECTIONALITY = {"directed", "undirected"}


@dataclass(frozen=True)
class EvidenceBinding:
    """Evidence Engine binding copied by reference into graph nodes and edges."""

    evidence_id: str
    claim_id: str
    relation: str
    strength: str = "medium"

    def to_dict(self) -> dict[str, Any]:
        return {
            "evidence_id": self.evidence_id,
            "claim_id": self.claim_id,
            "relation": self.relation,
            "strength": self.strength,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "EvidenceBinding":
        return cls(
            evidence_id=str(data["evidence_id"]),
            claim_id=str(data["claim_id"]),
            relation=str(data["relation"]),
            strength=str(data.get("strength", "medium")),
        )


@dataclass
class GraphNode:
    node_id: str
    node_type: str
    label: str
    source_refs: list[str]
    confidence: float
    evidence_bindings: list[EvidenceBinding] = field(default_factory=list)
    attributes: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "node_id": self.node_id,
            "node_type": self.node_type,
            "label": self.label,
            "source_refs": self.source_refs,
            "confidence": self.confidence,
            "evidence_bindings": [item.to_dict() for item in self.evidence_bindings],
            "attributes": self.attributes,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "GraphNode":
        return cls(
            node_id=str(data["node_id"]),
            node_type=str(data["node_type"]),
            label=str(data["label"]),
            source_refs=list(data.get("source_refs", [])),
            confidence=float(data["confidence"]),
            evidence_bindings=[EvidenceBinding.from_dict(item) for item in data.get("evidence_bindings", [])],
            attributes=dict(data.get("attributes", {})),
        )


@dataclass
class GraphEdge:
    edge_id: str
    from_node: str
    to_node: str
    relation_type: str
    evidence_refs: list[str]
    directionality: str = "directed"
    counter_evidence_refs: list[str] = field(default_factory=list)
    missing_evidence: list[str] = field(default_factory=list)
    confidence: float = 0.5
    attributes: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "edge_id": self.edge_id,
            "from_node": self.from_node,
            "to_node": self.to_node,
            "relation_type": self.relation_type,
            "evidence_refs": self.evidence_refs,
            "directionality": self.directionality,
            "counter_evidence_refs": self.counter_evidence_refs,
            "missing_evidence": self.missing_evidence,
            "confidence": self.confidence,
            "attributes": self.attributes,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "GraphEdge":
        return cls(
            edge_id=str(data["edge_id"]),
            from_node=str(data["from_node"]),
            to_node=str(data["to_node"]),
            relation_type=str(data["relation_type"]),
            evidence_refs=list(data.get("evidence_refs", [])),
            directionality=str(data.get("directionality", "directed")),
            counter_evidence_refs=list(data.get("counter_evidence_refs", [])),
            missing_evidence=list(data.get("missing_evidence", [])),
            confidence=float(data.get("confidence", 0.5)),
            attributes=dict(data.get("attributes", {})),
        )


@dataclass
class KnowledgeGraph:
    graph_id: str
    title: str
    research_question: str
    methodology_refs: list[str]
    evidence_cards: dict[str, dict[str, Any]]
    nodes: dict[str, GraphNode] = field(default_factory=dict)
    edges: dict[str, GraphEdge] = field(default_factory=dict)
    path_analysis: list[dict[str, Any]] = field(default_factory=list)
    chokepoint_analysis: list[dict[str, Any]] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)
    disclaimer: str = DISCLAIMER
    version: str = "0.1.0"

    def add_node(self, node: GraphNode) -> None:
        self.nodes[node.node_id] = node

    def add_edge(self, edge: GraphEdge) -> None:
        self.edges[edge.edge_id] = edge

    def outgoing(self, node_id: str) -> list[GraphEdge]:
        return [edge for edge in self.edges.values() if edge.from_node == node_id]

    def incoming(self, node_id: str) -> list[GraphEdge]:
        return [edge for edge in self.edges.values() if edge.to_node == node_id]

    def to_dict(self) -> dict[str, Any]:
        return {
            "graph_id": self.graph_id,
            "title": self.title,
            "research_question": self.research_question,
            "methodology_refs": self.methodology_refs,
            "evidence_cards": self.evidence_cards,
            "nodes": [node.to_dict() for node in self.nodes.values()],
            "edges": [edge.to_dict() for edge in self.edges.values()],
            "path_analysis": self.path_analysis,
            "chokepoint_analysis": self.chokepoint_analysis,
            "metadata": self.metadata,
            "disclaimer": self.disclaimer,
            "version": self.version,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "KnowledgeGraph":
        graph = cls(
            graph_id=str(data["graph_id"]),
            title=str(data["title"]),
            research_question=str(data["research_question"]),
            methodology_refs=list(data.get("methodology_refs", [])),
            evidence_cards=dict(data.get("evidence_cards", {})),
            path_analysis=list(data.get("path_analysis", [])),
            chokepoint_analysis=list(data.get("chokepoint_analysis", [])),
            metadata=dict(data.get("metadata", {})),
            disclaimer=str(data.get("disclaimer", DISCLAIMER)),
            version=str(data.get("version", "0.1.0")),
        )
        for node_data in data.get("nodes", []):
            graph.add_node(GraphNode.from_dict(node_data))
        for edge_data in data.get("edges", []):
            graph.add_edge(GraphEdge.from_dict(edge_data))
        return graph
