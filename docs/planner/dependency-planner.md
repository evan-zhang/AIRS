# Dependency Planner

免责声明：本文档仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## 职责

Dependency Planner 生成 Research Plan 的组件依赖图。它决定哪些步骤必须先完成，哪些步骤可以并行，哪些步骤是 Runtime 前置门禁。

## 标准组件

标准关键路径为：

`goal_analysis -> scope -> methodology_selection -> connector_plan -> evidence_plan -> skill_plan -> knowledge_graph_plan -> score_plan -> report_plan -> review_plan -> runtime_plan`

其中 `runtime_plan` 永远位于 Planner 完成之后。

## 输出

- `components`
- `edges`
- `critical_path`
- `runtime_blocked_until_planner_complete`
- `intent_ref`

## 审查重点

Review Agent 应检查 Evidence Plan 是否在 KG Plan 之前，Review Plan 是否在 Runtime Plan 之前，以及是否存在 Runtime 直接接收用户目标的边。
