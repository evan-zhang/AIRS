# Autonomous Research Planner Architecture

免责声明：本文档仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## 定位

Autonomous Research Planner 是 AIRS 的最上层入口。它接收用户研究目标，将目标拆解为 Research Plan，再把可执行链路交给 Orchestrator 和 Runtime。任何 Runtime 不允许直接接收原始用户请求，Runtime 只能接收 Planner 生成的 `runtime_plan`、`workflow`、`task_graph` 和 `context`。

## 分层关系

```text
User Goal
  -> Planner
  -> Research Plan
  -> Orchestrator Workflow
  -> Runtime Plan
  -> Agent Sessions
  -> Evidence / KG / Score / Report Artifacts
```

Planner 不替代 Methodology、Connector、Skill、Evidence、Knowledge Graph、Score、Report 或 Workspace。Planner 只负责选择、约束、排序、预算和门禁。

## 核心原则

- Goal 先结构化，才允许进入执行层。
- Runtime 只执行 Planner 产物，不解析原始用户目标。
- Research Plan 必须包含目标、范围、依赖、资源、预算、置信度、风险、证据预期和交付物。
- 所有计划都必须保留反方观点、缺失证据和不确定性。
- Planner 输出只用于研究流程与质量控制，不构成投资建议。

## 组件地图

- Goal Parser：将自然语言或结构化输入转为 Research Goal。
- Intent Analyzer：识别公司、行业、主题、供应链、卡点、政策、组合、对比研究。
- Scope Builder：定义研究边界、时间范围、地域范围和成功标准。
- Planning Engine：聚合所有 Planner 组件并输出完整 Research Plan。
- Dependency Planner：生成组件依赖和关键路径。
- Workflow Planner：生成 Orchestrator 可读的 Workflow Spec。
- Runtime Planner：生成 Runtime 可执行计划，并强制 Planner Gate。
- Resource Planner：估算 Connector、Methodology、Skill、Workspace 资源。
- Budget Planner：估算时间、成本、并发和超时。
- Confidence Planner：估算计划置信度和不确定性。
- Plan Optimizer：去重、并行化、风险提示和执行顺序优化。

## 强制边界

Planner 之后才有 Runtime。若系统发现 Runtime 输入没有 `planner_generated=true`，应拒绝执行，并返回 `PLANNER_GATE_REQUIRED`。这条规则是 FEATURE-009 的核心治理要求。
