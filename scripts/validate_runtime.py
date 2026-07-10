#!/usr/bin/env python3
"""Validate AIRS FEATURE-006 Research Agent Runtime deliverables."""
from __future__ import annotations
import importlib, json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
DOCS = ["docs/runtime/runtime-architecture.md","docs/runtime/runtime-lifecycle.md","docs/runtime/agent-registry.md","docs/runtime/task-dispatcher.md","docs/runtime/message-bus.md","docs/runtime/event-bus.md","docs/runtime/state-manager.md","docs/runtime/memory-manager.md","docs/runtime/resource-manager.md","docs/runtime/runtime-monitor.md"]
CORE = ["runtime/__init__.py","runtime/core.py","runtime/agent_registry.py","runtime/agent_lifecycle.py","runtime/agent_context.py","runtime/agent_session.py","runtime/task_dispatcher.py","runtime/message_bus.py","runtime/event_bus.py","runtime/state_manager.py","runtime/memory_manager.py","runtime/resource_manager.py","runtime/retry_scheduler.py","runtime/timeout_manager.py","runtime/cancellation_manager.py","runtime/runtime_monitor.py","runtime/README.md"]
EXAMPLES = [("runtime/examples/company_research_runtime.py","runtime/examples/company-research-runtime-example.md"),("runtime/examples/industry_research_runtime.py","runtime/examples/industry-research-runtime-example.md"),("runtime/examples/hot_topic_runtime.py","runtime/examples/hot-topic-runtime-example.md"),("runtime/examples/supply_chain_runtime.py","runtime/examples/supply-chain-runtime-example.md"),("runtime/examples/report_runtime.py","runtime/examples/report-runtime-example.md")]
SCHEMAS = ["schemas/runtime/runtime.schema.json","schemas/runtime/agent.schema.json","schemas/runtime/task.schema.json","schemas/runtime/event.schema.json","schemas/runtime/session.schema.json"]
TEMPLATES = ["templates/runtime/runtime-dashboard.md","templates/runtime/runtime-template.md","templates/runtime/agent-template.md"]
BUILDER = ["builder-output/research-agent-runtime/ISSUE.md","builder-output/research-agent-runtime/ADR.md","builder-output/research-agent-runtime/FEATURE_SPEC.md","builder-output/research-agent-runtime/skill/research-agent-runtime-skill.md","builder-output/research-agent-runtime/prompt/research-agent-runtime-prompt.md","builder-output/research-agent-runtime/schema/research-agent-runtime.schema.json","builder-output/research-agent-runtime/tests/test-research-agent-runtime.md","builder-output/research-agent-runtime/benchmark/research-agent-runtime-benchmark.md","builder-output/research-agent-runtime/PR_CHECKLIST.md","builder-output/research-agent-runtime/RELEASE_NOTES.md"]
REPORTS = ["docs/adr/ADR-0006-research-agent-runtime.md","docs/production/FEATURE_006_COMPLETION_REPORT.md","docs/review/FEATURE_006_SELF_REVIEW.md"]
FORBIDDEN = ["建议买入","建议卖出","保证收益","保证盈利","目标价为","应买入","应卖出","自动交易指令"]
def read(rel): return (ROOT/rel).read_text(encoding="utf-8")
def check(cond, ok, fail, failures):
    if cond: print(f"PASS: {ok}")
    else: print(f"FAIL: {fail}"); failures.append(fail)
def text(rel, failures, min_size=120, disclaimer=True):
    p=ROOT/rel; check(p.exists(), f"{rel} exists", f"missing {rel}", failures)
    if not p.exists(): return ""
    s=read(rel); check(len(s)>=min_size, f"{rel} has substantive content", f"{rel} content too thin", failures)
    if disclaimer: check("免责声明" in s and "不构成投资建议" in s, f"{rel} has disclaimer", f"{rel} missing disclaimer", failures)
    for w in FORBIDDEN: check(w not in s, f"{rel} avoids forbidden expression: {w}", f"{rel} contains forbidden expression: {w}", failures)
    return s
def j(rel, failures):
    p=ROOT/rel; check(p.exists(), f"{rel} exists", f"missing {rel}", failures)
    if not p.exists(): return {}
    try:
        data=json.loads(p.read_text(encoding="utf-8")); check(True, f"{rel} is valid JSON", f"{rel} invalid JSON", failures); return data
    except json.JSONDecodeError as exc:
        check(False, f"{rel} is valid JSON", f"{rel} invalid JSON: {exc}", failures); return {}
def validate_static(failures):
    for rel in DOCS:
        s=text(rel, failures, 500)
        for term in ["Runtime","Agent","Workflow"]: check(term in s, f"{rel} references {term}", f"{rel} missing {term}", failures)
    for rel in CORE:
        s=text(rel, failures, 20, disclaimer=rel.endswith(".md"))
        check("Runtime" in s or "Agent" in s or "Manager" in s or rel.endswith("__init__.py"), f"{rel} contains runtime logic", f"{rel} missing runtime logic", failures)
    for py, md in EXAMPLES:
        text(py, failures, 300, disclaimer=False); m=text(md, failures, 500)
        for term in ["Runtime Plan","Agent Graph","Execution Timeline","Event Log","Context Snapshot","Final State"]: check(term in m, f"{md} contains {term}", f"{md} missing {term}", failures)
    check((ROOT/"runtime/examples/__init__.py").exists(), "runtime/examples/__init__.py exists", "missing runtime/examples/__init__.py", failures)
    for rel in SCHEMAS:
        data=j(rel, failures); blob=json.dumps(data, ensure_ascii=False)
        for term in ["$schema","disclaimer","不构成投资建议"]: check(term in blob, f"{rel} contains {term}", f"{rel} missing {term}", failures)
    for rel in TEMPLATES + BUILDER + REPORTS:
        if rel.endswith(".json"): j(rel, failures)
        else: text(rel, failures, 180)
def validate_runtime_execution(failures):
    sys.path.insert(0, str(ROOT)); from runtime import default_registry
    registry = default_registry(); required_types = {"methodology_selector":"sync","evidence_collector":"async","parallel_researcher":"parallel","long_running_researcher":"long_running","human_reviewer":"human_in_the_loop"}
    for agent_id, agent_type in required_types.items(): check(registry.get(agent_id).agent_type.value == agent_type, f"registry supports {agent_type}", f"registry missing {agent_type}", failures)
    for mod, _ in EXAMPLES:
        module = importlib.import_module(mod[:-3].replace("/", ".")); result = module.run()
        for key in ["runtime_plan","agent_graph","execution_timeline","event_log","context_snapshot","final_state"]: check(key in result, f"{mod} outputs {key}", f"{mod} missing {key}", failures)
        check(result["event_log"], f"{mod} has event log", f"{mod} empty event log", failures)
        check("不构成投资建议" in json.dumps(result, ensure_ascii=False), f"{mod} carries disclaimer", f"{mod} missing disclaimer", failures)
def validate_consistency(failures):
    schema_readme = read("schemas/README.md"); changelog = read("CHANGELOG.md")
    check("schemas/runtime/" in schema_readme and "runtime.schema.json" in schema_readme, "schemas/README documents runtime schemas", "schemas/README missing runtime schemas", failures)
    check("FEATURE-006" in changelog and "Research Agent Runtime" in changelog, "CHANGELOG documents FEATURE-006", "CHANGELOG missing FEATURE-006", failures)
    combined = "\n".join(read(rel) for rel in DOCS + ["runtime/README.md"])
    check("Workflow 不直接驱动业务模块" in combined or "Workflow 只描述步骤" in combined, "runtime states workflow boundary", "runtime missing workflow boundary", failures)
    runtime_code = "\n".join(read(rel) for rel in CORE if rel.endswith(".py"))
    for token in ["from skills", "import skills", "from evidence", "import evidence", "from methodology", "import methodology"]: check(token not in runtime_code, f"runtime avoids direct business import {token}", f"runtime directly imports business module {token}", failures)
def main():
    failures=[]; print("AIRS FEATURE-006 Research Agent Runtime Validation"); print("===================================================")
    validate_static(failures); validate_runtime_execution(failures); validate_consistency(failures)
    print("===================================================")
    if failures:
        print("RESULT: FAIL")
        for f in failures: print(f"- {f}")
        return 1
    print("RESULT: PASS"); return 0
if __name__ == "__main__": sys.exit(main())
