"""Knowledge Graph summary helpers."""

from __future__ import annotations

from typing import Any


class KGSummaryBuilder:
    """Summarize FEATURE-002 Knowledge Graph output for reports."""

    def __init__(self, graph: dict[str, Any]) -> None:
        self.graph = graph

    def build(self) -> dict[str, Any]:
        nodes = self.graph.get("nodes", [])
        edges = self.graph.get("edges", [])
        chokepoints = self.graph.get("chokepoint_analysis", [])
        paths = self.graph.get("path_analysis", [])
        top_chokepoint = chokepoints[0] if chokepoints else {}
        return {
            "graph_id": self.graph.get("graph_id"),
            "title": self.graph.get("title"),
            "node_count": len(nodes),
            "edge_count": len(edges),
            "path_count": len(paths),
            "chokepoint_count": len(chokepoints),
            "top_chokepoint": top_chokepoint,
            "methodology_refs": self.graph.get("methodology_refs", []),
            "evidence_refs": sorted(self._evidence_refs()),
        }

    def to_markdown(self) -> str:
        summary = self.build()
        top = summary["top_chokepoint"] or {}
        drivers = "；".join(top.get("drivers", [])) if top else "暂无卡点驱动"
        return "\n".join(
            [
                f"- KG ID：`{summary['graph_id']}`",
                f"- 图谱标题：{summary['title']}",
                f"- 节点 / 关系 / 路径：{summary['node_count']} / {summary['edge_count']} / {summary['path_count']}",
                f"- Top Chokepoint：{top.get('label', '暂无')}（节点：`{top.get('node_id', 'NA')}`；分数：{top.get('chokepoint_score', 'NA')}；风险：{top.get('risk_level', 'NA')}）",
                f"- 卡点驱动：{drivers}",
                f"- KG Evidence Refs：{', '.join(f'`{item}`' for item in summary['evidence_refs'])}",
            ]
        )

    def _evidence_refs(self) -> set[str]:
        refs: set[str] = set()
        for edge in self.graph.get("edges", []):
            refs.update(edge.get("evidence_refs", []))
            refs.update(edge.get("counter_evidence_refs", []))
        for path in self.graph.get("path_analysis", []):
            refs.update(path.get("evidence_refs", []))
        for chokepoint in self.graph.get("chokepoint_analysis", []):
            refs.update(chokepoint.get("evidence_refs", []))
            refs.update(chokepoint.get("counter_evidence_refs", []))
        return refs
