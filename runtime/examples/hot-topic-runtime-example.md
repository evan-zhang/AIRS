# 热点主题 Runtime 示例

## Runtime Plan

本示例使用 `hot-topic-workflow`，由 Runtime Core 接收 Workflow Spec，再由 Task Dispatcher 调度 Agent Session。Workflow 只描述步骤、依赖和引用，不直接调用业务模块。

## Agent Graph

- 节点：methodology_selector, parallel_researcher, human_reviewer, report_composer
- 边：按 dependencies 从前置任务流向后续任务。

## Execution Timeline

1. RUNTIME_STARTED
2. TASK_DISPATCHED
3. AGENT_INITIALIZED
4. AGENT_RUNNING
5. AGENT_COMPLETED 或 AGENT_WAITING_FOR_HUMAN
6. RUNTIME_COMPLETED

## Event Log

Event Bus 记录每个任务的 session_id、task_id、agent_id、agent_type、输出引用和免责声明状态。

## Context Snapshot

Context Snapshot 保存 research_question、refs、output_data、message_count、event_count 和 disclaimer。快照可用于暂停、恢复和 Review Agent 复核。

## Final State

Final State 汇总 task_states、agent_states、context_snapshots 和 quality_gate。Human-in-the-loop 任务允许进入 WAITING_FOR_HUMAN，表示 Runtime 已正确等待人工输入。

免责声明：本文档和示例仅用于 AIRS 工程开发、投资研究流程编排与质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。
