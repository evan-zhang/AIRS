# Research Agent Runtime

`runtime/` 是 FEATURE-006 的最小可运行实现，提供 Runtime Core、Agent Registry、Lifecycle、Session、Dispatcher、Message Bus、Event Bus、State、Memory、Resource、Retry、Timeout、Cancellation 和 Monitor。

## 支持的 Agent 类型

- Sync Agent：同步短任务。
- Async Agent：异步任务，可恢复。
- Parallel Agent：并行拆分任务。
- Long-running Agent：长周期任务，保留 checkpoint。
- Human-in-the-loop Agent：等待人工确认。

## 使用方式

```python
from runtime import RuntimeCore
result = RuntimeCore().run_workflow({"workflow_id": "demo", "tasks": [{"task_id": "t1", "agent_id": "methodology_selector"}]})
```

Runtime 只调度 Workflow 与 Agent Session，不直接驱动 Methodology、Evidence、Skill、Score 或 Report 业务模块。

免责声明：本文档和示例仅用于 AIRS 工程开发、投资研究流程编排与质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。
