# Planning Engine

免责声明：本文档仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## 职责

Planning Engine 是 `planner/engine.py` 的统一入口。它按固定顺序调用 Goal Parser、Intent Analyzer、Scope Builder、Dependency Planner、Workflow Planner、Resource Planner、Budget Planner、Confidence Planner、Runtime Planner 和 Plan Optimizer。

## 输入输出

输入可以是自然语言目标或结构化 Research Goal。输出是完整 Research Plan，包含：

- Goal Analysis
- Scope
- Required Connectors / Methodologies / Skills / Runtime
- Expected Evidence / KG
- Execution Order
- Estimated Cost / Time
- Expected Deliverables
- Confidence
- Risks

## 顺序

Planner 必须先生成 Scope 和 Dependency，再生成 Workflow 和 Runtime。Runtime Plan 是 Planning Engine 的下游产物，不能反向驱动 Planner。

## 质量门禁

Planning Engine 输出必须包含 `required_runtime.planner_generated=true` 与 `required_runtime.raw_user_request_allowed=false`。缺少任一字段，Verification Agent 应判定为失败。
