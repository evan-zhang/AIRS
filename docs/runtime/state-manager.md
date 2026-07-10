# State Manager（状态管理）

## 1. 职责

State Manager 保存 Runtime、Task 和 Agent Session 的当前状态与历史快照。它是暂停、恢复、失败排查和最终报告复核的基础。

## 2. 状态对象

状态对象包括 runtime_id、workflow_id、task_states、agent_states、context_snapshots、final_state 和 quality_gate。

## 3. 快照策略

每个 Task 完成、失败、暂停或恢复时都生成 Context Snapshot。快照记录输入、输出、引用路径、消息计数、事件计数和免责声明状态。

## 4. 一致性

State Manager 不保存不可追溯的投资结论。所有研究判断必须指向 Evidence Card、Evidence Chain、Scorecard 或 Report Section。

## Workflow 边界

本组件只服务 Runtime 调度后的 Workflow 执行链路，不允许 Workflow 绕过 Runtime 直接驱动业务模块。

---

免责声明：本文档和示例仅用于 AIRS 工程开发、投资研究流程编排与质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。
