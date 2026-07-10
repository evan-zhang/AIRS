"""供应链 Workspace example."""
from __future__ import annotations

from workspace import ResearchWorkspace


def run() -> dict:
    ws = ResearchWorkspace("供应链 Workspace")
    project = ws.create_project("供应链卡点项目", "分析示例供应链中的卡点、替代路径和证据链", {"chain": "示例供应链"}, ["docs/runtime/resource-manager.md"])
    session = ws.open_session(project.project_id, "supply-chain-workflow", {"research_question": project.research_question})
    ws.task_board.add_task(project.project_id, session.session_id, "长周期供应链节点研究", "Research Agent", ["runtime/examples/supply_chain_runtime.py"])
    ws.memory.remember(project.project_id, "key_constraint", "关键约束需要 Evidence Chain 支撑", "schemas/evidence/evidence-chain.schema.json")
    ws.register_artifact(project.project_id, session.session_id, "knowledge_graph", "供应链卡点图谱", "artifacts/supply-chain/kg.json", ["templates/knowledge-graph/chokepoint-analysis-template.md"])
    return {"workspace": ws.state(), "dashboard": ws.dashboard(project.project_id), "memory": ws.memory.recall(project.project_id)}


if __name__ == "__main__":
    import json
    print(json.dumps(run(), ensure_ascii=False, indent=2))
