"""Path analysis for AIRS knowledge graphs."""

from __future__ import annotations

from .model import KnowledgeGraph


class PathAnalyzer:
    """Find simple directed paths and summarize evidence coverage."""

    def find_paths(self, graph: KnowledgeGraph, start_node: str, end_node: str, max_depth: int = 6) -> list[dict[str, object]]:
        paths: list[list[str]] = []

        def walk(current: str, visited: list[str]) -> None:
            if len(visited) > max_depth + 1:
                return
            if current == end_node:
                paths.append(visited[:])
                return
            for edge in graph.outgoing(current):
                if edge.to_node in visited:
                    continue
                walk(edge.to_node, visited + [edge.to_node])

        walk(start_node, [start_node])
        return [self._summarize_path(graph, path) for path in paths]

    def _summarize_path(self, graph: KnowledgeGraph, node_path: list[str]) -> dict[str, object]:
        edge_path = []
        evidence_refs: set[str] = set()
        confidence_values: list[float] = []
        relation_types: list[str] = []
        for left, right in zip(node_path, node_path[1:]):
            edge = next(item for item in graph.outgoing(left) if item.to_node == right)
            edge_path.append(edge.edge_id)
            evidence_refs.update(edge.evidence_refs)
            confidence_values.append(edge.confidence)
            relation_types.append(edge.relation_type)
        node_labels = [graph.nodes[node_id].label for node_id in node_path]
        confidence = round(sum(confidence_values) / len(confidence_values), 4) if confidence_values else 1.0
        return {
            "path_id": "PATH-" + "-".join(node_path),
            "node_path": node_path,
            "node_labels": node_labels,
            "edge_path": edge_path,
            "relation_types": relation_types,
            "evidence_refs": sorted(evidence_refs),
            "path_confidence": confidence,
            "interpretation": " -> ".join(node_labels),
        }
