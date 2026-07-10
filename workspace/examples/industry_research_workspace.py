"""行业研究 Workspace example."""
from __future__ import annotations

from workspace import ResearchWorkspace


def run() -> dict:
    ws = ResearchWorkspace("行业研究 Workspace")
    project = ws.create_project("行业研究项目", "分析示例行业的景气度、竞争格局和反方观点", {"industry": "示例行业"}, ["docs/runtime/task-dispatcher.md"])
    session = ws.open_session(project.project_id, "industry-research-workflow", {"research_question": project.research_question})
    ws.task_board.add_task(project.project_id, session.session_id, "并行拆分行业研究任务", "Research Agent", ["runtime/examples/industry_research_runtime.py"])
    ws.register_artifact(project.project_id, session.session_id, "knowledge_graph", "行业知识图谱", "artifacts/industry/kg.json", ["schemas/knowledge-graph/knowledge-graph.schema.json"])
    ws.register_artifact(project.project_id, session.session_id, "scorecard", "行业评分卡", "artifacts/industry/scorecard.json", ["schemas/score/scorecard.schema.json"])
    snapshot = ws.snapshots.create_snapshot(project.project_id, session.session_id, {"runtime_plan_ref": "industry-research-workflow", "artifact_refs": ["knowledge_graph", "scorecard"]}, "review checkpoint")
    return {"workspace": ws.state(), "dashboard": ws.dashboard(project.project_id), "export": ws.export(), "replay_plan": ws.replay.build_replay_plan(snapshot.to_dict())}


if __name__ == "__main__":
    import json
    print(json.dumps(run(), ensure_ascii=False, indent=2))
