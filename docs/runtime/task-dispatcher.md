# Task Dispatcher（任务分发）

## 1. 职责

Task Dispatcher 负责把 Runtime Plan 中的 Task 按依赖关系、Agent 类型和资源预算派发给 Agent Session。它只调度任务，不直接调用 Methodology、Evidence、Skill 或 Report 业务模块。

## 2. 调度流程

1. 读取 Runtime Plan。
2. 验证 task_id、agent_id、dependencies 和 expected_output。
3. 对无依赖任务创建 Session。
4. 根据 Agent 类型选择同步、异步、并行、长任务或人工等待策略。
5. 将状态变化写入 Event Bus 和 State Manager。

## 3. 失败处理

失败任务由 Retry Scheduler 判断是否重试；超时任务由 Timeout Manager 标记；取消任务由 Cancellation Manager 广播取消事件。

## 4. 输出

Dispatcher 输出 Execution Timeline、Event Log 和 Final State，供 Review Agent 与 Verification Agent 复核。

## Workflow 边界

本组件只服务 Runtime 调度后的 Workflow 执行链路，不允许 Workflow 绕过 Runtime 直接驱动业务模块。

---

免责声明：本文档和示例仅用于 AIRS 工程开发、投资研究流程编排与质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。
