# Runtime Architecture（架构总览）

## 1. 定位

Research Agent Runtime 是 AIRS V1.x 的统一执行底座，位于用户意图、Orchestrator Workflow 描述和 M2-M7 研究模块之间。它不替代 Methodology、Evidence、Skill、Score、Evaluation 或 Report 的规则，而是负责把 Workflow 中的步骤转化为 Agent Session、Task、Message、Event 和 State 的可追踪执行。

## 2. 核心原则

- Runtime 调度 Workflow，Workflow 不直接驱动业务模块。
- Agent 通过 Context 获取引用路径、输入、证据链 ID 和输出契约。
- 所有执行行为写入 Event Bus，所有中间状态写入 State Manager。
- Runtime 支持 Sync、Async、Parallel、Long-running 和 Human-in-the-loop 五类 Agent。
- Runtime 输出 Runtime Plan、Agent Graph、Execution Timeline、Event Log、Context Snapshot 和 Final State。

## 3. 分层结构

```text
User Intent
  -> Orchestrator Workflow Spec
  -> Runtime Core
  -> Task Dispatcher
  -> Agent Session / Agent Context
  -> Message Bus + Event Bus
  -> State / Memory / Resource / Monitor
  -> Final State
```

## 4. 与 Orchestrator 的关系

Orchestrator 只产生或选择 Workflow Spec，包括步骤、依赖、Agent 类型和输出契约。Runtime Core 接收该 Spec 后创建 Session，并由 Task Dispatcher 调度 Agent。任何 Methodology、Evidence 或 Report 模块都只能作为 Agent 执行时引用的能力边界，不允许被 Workflow 文件直接调用。

## 5. 合规边界

Runtime 不生成投资结论，只记录和调度研究过程。研究输出必须继续遵守 M2 方法论、M3 证据、M6 评估和报告免责声明要求。

---

免责声明：本文档和示例仅用于 AIRS 工程开发、投资研究流程编排与质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。
