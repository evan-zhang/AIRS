"""报告生成 Workspace example."""
from __future__ import annotations

from workspace import ResearchWorkspace


def run() -> dict:
    ws = ResearchWorkspace("报告生成 Workspace")
    project = ws.create_project("报告生成项目", "汇总证据、评分、反方观点和不确定性生成研究报告", {"format": "structured-report"}, ["docs/runtime/runtime-monitor.md"])
    session = ws.open_session(project.project_id, "report-workflow", {"research_question": project.research_question})
    ws.task_board.add_task(project.project_id, session.session_id, "生成报告草稿", "Report Agent", ["runtime/examples/report_runtime.py"])
    artifact = ws.register_artifact(project.project_id, session.session_id, "research_report", "结构化研究报告", "reports/final.md", ["schemas/report/report.schema.json"])
    ws.artifacts.publish(artifact["artifact_id"])
    snapshot = ws.snapshots.create_snapshot(project.project_id, session.session_id, {"runtime_plan_ref": "report-workflow", "artifact_refs": [artifact["artifact_id"]]}, "final review")
    return {"workspace": ws.state(), "dashboard": ws.dashboard(project.project_id), "replay_plan": ws.replay.build_replay_plan(snapshot.to_dict())}


if __name__ == "__main__":
    import json
    print(json.dumps(run(), ensure_ascii=False, indent=2))
