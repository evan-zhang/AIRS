# Runtime Planner

免责声明：本文档仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## 职责

Runtime Planner 将 Workflow Spec 转换为 Runtime Plan，并写入 Planner Gate。Runtime Plan 是 Runtime 的唯一入口，不允许 Runtime 读取原始用户目标。

## 强制字段

- `planner_generated=true`
- `raw_user_request_allowed=false`
- `runtime_boundary`
- `workflow_id`
- `tasks`
- `expected_outputs`

## 执行边界

Runtime Planner 不执行任务，不创建证据卡，不生成研究结论。它只输出 Runtime 可消费的结构化计划，并保留 `docs/runtime/runtime-architecture.md` 引用。

## 失败处理

若 Runtime Plan 缺少 Planner Gate，Runtime 应返回失败状态。Verification Agent 应在 `validate_planner.py` 中检查该约束。
