# Memory Manager（内存管理）

## 1. 职责

Memory Manager 管理 Agent 执行过程中的短期记忆、跨任务上下文和可审计摘要。Memory 服务执行效率，但不替代 Evidence Engine。

## 2. Memory 类型

- session_memory：单个 Agent Session 内的临时上下文。
- workflow_memory：同一 Runtime Plan 内跨 Agent 共享的结构化摘要。
- audit_memory：供 Review Agent 复核的不可变摘要。

## 3. 写入规则

Memory 必须记录来源字段，如 source_task_id、source_event_id 或 evidence_ref。禁止把 Memory 中的摘要直接作为报告证据。

## 4. 清理规则

Runtime 完成后只保留 audit_memory 和 final snapshot，临时 session_memory 可释放。

## Workflow 边界

本组件只服务 Runtime 调度后的 Workflow 执行链路，不允许 Workflow 绕过 Runtime 直接驱动业务模块。

---

免责声明：本文档和示例仅用于 AIRS 工程开发、投资研究流程编排与质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。
