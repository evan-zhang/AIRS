# Resource Manager（资源管理）

## 1. 职责

Resource Manager 为 Runtime 分配和限制执行资源，包括并发数、超时时间、重试次数、人工等待窗口和内存预算。

## 2. 资源模型

资源配额包括 max_concurrency、default_timeout_seconds、max_retries、long_running_checkpoint_interval 和 human_wait_timeout_seconds。

## 3. 与 Agent 类型的关系

Parallel Agent 受 max_concurrency 限制；Long-running Agent 必须提供 checkpoint；Human-in-the-loop Agent 必须有等待超时和人工输入记录。

## 4. 失败策略

资源不足时 Runtime 返回 RESOURCE_LIMITED 状态，而不是绕过调度器直接执行业务模块。

## Workflow 边界

本组件只服务 Runtime 调度后的 Workflow 执行链路，不允许 Workflow 绕过 Runtime 直接驱动业务模块。

---

免责声明：本文档和示例仅用于 AIRS 工程开发、投资研究流程编排与质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。
