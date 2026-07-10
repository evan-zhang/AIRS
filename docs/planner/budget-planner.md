# Budget Planner

免责声明：本文档仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## 职责

Budget Planner 根据资源数量和报告深度估算时间、成本、并发和超时。预算用于调度约束，不代表研究价值或投资结论。

## 输入

- Connector 数量。
- Methodology 数量。
- Skill 数量。
- 是否需要人工复核。
- Scope 的时间和地域边界。

## 输出

- `estimated_time_minutes`
- `estimated_cost_units`
- `max_concurrency`
- `budget_rationale`
- `budget_gate`

## 门禁

若预算过高，Planner 应返回 `CONDITIONAL_PASS`，并要求缩小 Scope 或增加人工确认。预算不足时不能让 Runtime 擅自缩短证据链。

## 与 Runtime 的关系

Budget Planner 的结果会写入 Runtime Plan 的并发和超时字段，但 Runtime 只能消费该结果，不能自行重算预算后改变 Planner 的研究范围。若 Runtime 执行时发现资源不足，应返回资源受限状态，并把问题交回 Planner 或 Review Agent，而不是绕过 Evidence Plan。

## 审计要求

预算说明必须保留 `budget_rationale`。Verification Agent 应检查预算是否与 Connector、Methodology、Skill 数量一致，并确认预算门禁不会被解释为研究结论或投资判断。
