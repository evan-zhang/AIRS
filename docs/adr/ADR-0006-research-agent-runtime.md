# ADR-0006 Research Agent Runtime

## Status

Accepted

## Context

AIRS 已具备 Methodology、Evidence、Prompt、Skill、Score、Evaluation、Benchmark、Builder、Knowledge Graph、Report Generator 和 Connector 等模块，但缺少统一运行时。若 Workflow 直接驱动业务模块，会造成执行链路不可审计、暂停恢复困难、Agent 类型混杂和合规边界不清。

## Decision

引入 `runtime/` 作为统一 Agent Runtime。Runtime Core 接收 Workflow Spec，Task Dispatcher 根据 Agent Registry 创建 Agent Session，并通过 Message Bus、Event Bus、State Manager、Memory Manager、Resource Manager 和 Runtime Monitor 管理执行。Runtime 支持 Sync、Async、Parallel、Long-running 和 Human-in-the-loop 五类 Agent。

## Consequences

- 所有 Workflow 必须由 Runtime 调度执行。
- Runtime 不直接导入或驱动 M2-M7 业务模块，只传递引用、上下文和输出契约。
- Review Agent 可以基于 Event Log、Context Snapshot 和 Final State 复核过程。
- 后续 Orchestrator、Benchmark Runner 和 Scorecard Runner 可接入同一 Runtime。

## Compliance

免责声明：本文档和示例仅用于 AIRS 工程开发、投资研究流程编排与质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。
