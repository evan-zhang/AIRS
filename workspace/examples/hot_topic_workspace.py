"""热点主题 Workspace example."""
from __future__ import annotations

from workspace import ResearchWorkspace


def run() -> dict:
    ws = ResearchWorkspace("热点主题 Workspace")
    project = ws.create_project("热点主题项目", "分析示例热点主题的扩散路径和不确定性", {"topic": "示例热点"}, ["docs/runtime/event-bus.md"])
    session = ws.open_session(project.project_id, "hot-topic-workflow", {"research_question": project.research_question})
    ws.task_board.add_task(project.project_id, session.session_id, "收集主题证据与反证", "Research Agent", ["runtime/examples/hot_topic_runtime.py"])
    ws.collaboration.add_note(project.project_id, session.session_id, "Review Agent", "review_note", "需要补充反方观点证据引用", ["schemas/evidence/evidence-card.schema.json"])
    ws.register_artifact(project.project_id, session.session_id, "review_report", "热点主题复核意见", "reviews/hot-topic.md", ["docs/workspace/artifact-governance.md"])
    return {"workspace": ws.state(), "dashboard": ws.dashboard(project.project_id)}


if __name__ == "__main__":
    import json
    print(json.dumps(run(), ensure_ascii=False, indent=2))
