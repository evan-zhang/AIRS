# Runtime 模板

## 1. Runtime Metadata

- runtime_id：
- workflow_id：
- owner_agent：
- created_at：

## 2. Runtime Plan

描述 Workflow Spec、任务列表、依赖关系和输出契约。

## 3. Agent Graph

列出 Sync、Async、Parallel、Long-running、Human-in-the-loop Agent 的节点和边。

## 4. Execution Policy

说明 timeout、retry、cancellation、resource 和 human wait 策略。

## 5. Outputs

必须输出 Runtime Plan、Agent Graph、Execution Timeline、Event Log、Context Snapshot 和 Final State。

免责声明：本文档和示例仅用于 AIRS 工程开发、投资研究流程编排与质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。
