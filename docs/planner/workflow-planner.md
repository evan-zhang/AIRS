# Workflow Planner

免责声明：本文档仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## 职责

Workflow Planner 将 Dependency Planner 的关键路径转换为 Orchestrator Workflow。Workflow 只描述阶段、任务、依赖、Agent Role 和期望输出，不执行任何外部数据访问。

## 输出字段

- `workflow_id`
- `description`
- `tasks`
- `orchestrator_ref`
- `runtime_entry_condition`
- `required_methodologies`
- `required_skills`

## Runtime Entry Condition

Workflow 必须写明 Runtime 入口条件：只允许接收 `planner_generated_runtime_plan`。这个条件由 Runtime Planner 转换为可执行约束。

## 与 Orchestrator 的关系

Orchestrator 负责描述 Workflow，Runtime 负责执行 Workflow。Planner 只负责生成 Workflow，不创建 Agent Session。
