"""Validation for AIRS knowledge graphs."""

from __future__ import annotations

from dataclasses import dataclass

from .model import DIRECTIONALITY, NODE_TYPES, RELATION_TYPES, KnowledgeGraph


@dataclass
class ValidationResult:
    passed: bool
    errors: list[str]
    warnings: list[str]


class KnowledgeGraphValidator:
    """Validate structural rules and M3 Evidence Engine bindings."""

    def validate(self, graph: KnowledgeGraph) -> ValidationResult:
        errors: list[str] = []
        warnings: list[str] = []

        if "不构成投资建议" not in graph.disclaimer:
            errors.append("图谱缺少合规免责声明。")
        if not graph.methodology_refs:
            errors.append("图谱缺少 M2 Methodology 引用。")
        if not graph.evidence_cards:
            errors.append("图谱缺少 M3 Evidence Card 绑定。")

        evidence_ids = set(graph.evidence_cards)
        node_ids = set(graph.nodes)

        for node in graph.nodes.values():
            if node.node_type not in NODE_TYPES:
                errors.append(f"节点 {node.node_id} 类型非法：{node.node_type}")
            if not node.source_refs:
                errors.append(f"节点 {node.node_id} 缺少 source_refs。")
            if not 0 <= node.confidence <= 1:
                errors.append(f"节点 {node.node_id} confidence 超出 0-1。")
            if node.node_type in {"evidence", "claim"} and not node.evidence_bindings:
                warnings.append(f"节点 {node.node_id} 建议绑定 Evidence。")
            for binding in node.evidence_bindings:
                if binding.evidence_id not in evidence_ids:
                    errors.append(f"节点 {node.node_id} 绑定未知 Evidence：{binding.evidence_id}")

        for edge in graph.edges.values():
            if edge.from_node not in node_ids:
                errors.append(f"边 {edge.edge_id} from_node 不存在：{edge.from_node}")
            if edge.to_node not in node_ids:
                errors.append(f"边 {edge.edge_id} to_node 不存在：{edge.to_node}")
            if edge.relation_type not in RELATION_TYPES:
                errors.append(f"边 {edge.edge_id} 关系类型非法：{edge.relation_type}")
            if edge.directionality not in DIRECTIONALITY:
                errors.append(f"边 {edge.edge_id} directionality 非法：{edge.directionality}")
            if not edge.evidence_refs:
                errors.append(f"边 {edge.edge_id} 缺少 evidence_refs。")
            for evidence_id in edge.evidence_refs + edge.counter_evidence_refs:
                if evidence_id not in evidence_ids:
                    errors.append(f"边 {edge.edge_id} 引用未知 Evidence：{evidence_id}")
            if not edge.missing_evidence:
                warnings.append(f"边 {edge.edge_id} 未记录 missing_evidence。")
            if not 0 <= edge.confidence <= 1:
                errors.append(f"边 {edge.edge_id} confidence 超出 0-1。")

        return ValidationResult(passed=not errors, errors=errors, warnings=warnings)
