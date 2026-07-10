"""Builder helpers for creating AIRS knowledge graphs."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .model import GraphEdge, GraphNode, KnowledgeGraph


class KnowledgeGraphBuilder:
    """Fluent builder around the KnowledgeGraph data model."""

    def __init__(
        self,
        graph_id: str,
        title: str,
        research_question: str,
        methodology_refs: list[str] | None = None,
        evidence_cards: dict[str, dict[str, Any]] | None = None,
    ) -> None:
        self.graph = KnowledgeGraph(
            graph_id=graph_id,
            title=title,
            research_question=research_question,
            methodology_refs=methodology_refs or [],
            evidence_cards=evidence_cards or {},
        )

    def add_evidence_card(self, card: dict[str, Any]) -> "KnowledgeGraphBuilder":
        evidence_id = str(card["evidence_id"])
        self.graph.evidence_cards[evidence_id] = card
        return self

    def add_node(self, node: GraphNode | dict[str, Any]) -> "KnowledgeGraphBuilder":
        self.graph.add_node(node if isinstance(node, GraphNode) else GraphNode.from_dict(node))
        return self

    def add_edge(self, edge: GraphEdge | dict[str, Any]) -> "KnowledgeGraphBuilder":
        self.graph.add_edge(edge if isinstance(edge, GraphEdge) else GraphEdge.from_dict(edge))
        return self

    def build(self) -> KnowledgeGraph:
        return self.graph

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "KnowledgeGraphBuilder":
        builder = cls(
            graph_id=str(data["graph_id"]),
            title=str(data["title"]),
            research_question=str(data["research_question"]),
            methodology_refs=list(data.get("methodology_refs", [])),
            evidence_cards=dict(data.get("evidence_cards", {})),
        )
        for node in data.get("nodes", []):
            builder.add_node(node)
        for edge in data.get("edges", []):
            builder.add_edge(edge)
        builder.graph.path_analysis = list(data.get("path_analysis", []))
        builder.graph.chokepoint_analysis = list(data.get("chokepoint_analysis", []))
        builder.graph.metadata = dict(data.get("metadata", {}))
        builder.graph.disclaimer = str(data.get("disclaimer", builder.graph.disclaimer))
        builder.graph.version = str(data.get("version", builder.graph.version))
        return builder

    @classmethod
    def from_json_file(cls, path: str | Path) -> "KnowledgeGraphBuilder":
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        return cls.from_dict(data)
