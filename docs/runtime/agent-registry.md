# Agent Registry（注册表）

## 1. 目标

Agent Registry 记录 Runtime 可调度的 Agent 类型、能力、输入输出契约、生命周期策略和资源限制。Registry 是 Runtime 调度的唯一入口，避免 Workflow 直接依赖业务模块。

## 2. 注册字段

每个 AgentDefinition 包含 agent_id、agent_type、description、capabilities、input_schema、output_schema、required_refs、timeout_seconds、max_retries 和 human_required。

## 3. 五类 Agent

- Sync：短任务，同步返回。
- Async：异步任务，可通过事件恢复。
- Parallel：可并行拆分的批任务。
- Long-running：长周期任务，必须有 checkpoint。
- Human-in-the-loop：需要人工确认或补充输入。

## 4. 治理

Registry 只保存执行契约，不保存 Prompt 正文、方法论理论或证据规则。所有 required_refs 必须指向 AIRS 既有文档或 Schema。

---

免责声明：本文档和示例仅用于 AIRS 工程开发、投资研究流程编排与质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。
