"""报告生成 Runtime example."""
from __future__ import annotations
from runtime import RuntimeCore
def build_workflow() -> dict:
    return {"workflow_id": "report-workflow", "runtime_name": "报告生成 Runtime", "tasks": [{"task_id":"t1","agent_id":"evidence_collector","dependencies":[],"input":{"research_question":"报告生成 Runtime 示例问题","branches":["证据","反证"]},"refs":["docs/methodology/DSL.md","docs/evidence/evidence-architecture.md"]},{"task_id":"t2","agent_id":"human_reviewer","dependencies":['t1'],"input":{"research_question":"报告生成 Runtime 示例问题","branches":["证据","反证"]},"refs":["docs/methodology/DSL.md","docs/evidence/evidence-architecture.md"]},{"task_id":"t3","agent_id":"report_composer","dependencies":['t2'],"input":{"research_question":"报告生成 Runtime 示例问题","branches":["证据","反证"]},"refs":["docs/methodology/DSL.md","docs/evidence/evidence-architecture.md"]}], "disclaimer": "仅供研究参考，不构成投资建议"}
def run() -> dict:
    return RuntimeCore().run_workflow(build_workflow())
if __name__ == "__main__":
    import json
    print(json.dumps(run(), ensure_ascii=False, indent=2))
