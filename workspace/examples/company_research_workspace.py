"""公司研究 Workspace example."""
from __future__ import annotations

from workspace import ResearchWorkspace


def run() -> dict:
    ws = ResearchWorkspace("公司研究 Workspace")
    project = ws.create_project("公司研究项目", "分析示例公司的收入质量和证据链", {"company": "示例公司", "period": "近三年"}, ["docs/runtime/runtime-architecture.md"])
    session = ws.open_session(project.project_id, "company-research-workflow", {"research_question": project.research_question})
    ws.task_board.add_task(project.project_id, session.session_id, "选择方法论", "Research Agent", ["docs/methodology/DSL.md"])
    ws.register_artifact(project.project_id, session.session_id, "evidence_bundle", "公司研究证据包", "artifacts/company/evidence.json", ["schemas/evidence/evidence-chain.schema.json"])
    report = ws.register_artifact(project.project_id, session.session_id, "research_report", "公司研究报告草稿", "reports/company.md", ["templates/report/research-report-template.md"])
    ws.versions.add_version(report["artifact_id"], "0.1.0", "登记公司研究报告草稿", ["reports/company.md"])
    snapshot = ws.snapshots.create_snapshot(project.project_id, session.session_id, {"runtime_plan_ref": "runtime/examples/company_research_runtime.py", "artifact_refs": [report["artifact_id"]]}, "example checkpoint")
    return {"workspace": ws.state(), "dashboard": ws.dashboard(project.project_id), "replay_plan": ws.replay.build_replay_plan(snapshot.to_dict())}


if __name__ == "__main__":
    import json
    print(json.dumps(run(), ensure_ascii=False, indent=2))
