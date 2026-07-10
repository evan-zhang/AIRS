# Event Bus（事件总线）

## 1. 职责

Event Bus 是 Runtime 的审计账本，记录 Agent、Task、Session、Message、State、Retry、Timeout 和 Cancellation 的变化。

## 2. 事件类型

核心事件包括 RUNTIME_STARTED、TASK_DISPATCHED、AGENT_CREATED、AGENT_INITIALIZED、AGENT_RUNNING、AGENT_PAUSED、AGENT_RESUMED、AGENT_COMPLETED、AGENT_FAILED、TASK_RETRIED、TASK_TIMEOUT、TASK_CANCELLED、RUNTIME_COMPLETED。

## 3. 事件字段

事件包含 event_id、event_type、timestamp、session_id、task_id、agent_id、severity、payload 和 trace_id。

## 4. 质量要求

Event Bus 必须可追加、可导出、可复核。任何失败、跳过、人工介入或证据缺口都必须有事件记录。

## Workflow 边界

本组件只服务 Runtime 调度后的 Workflow 执行链路，不允许 Workflow 绕过 Runtime 直接驱动业务模块。

---

免责声明：本文档和示例仅用于 AIRS 工程开发、投资研究流程编排与质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。
