# Session Management（会话管理）

## 1. 职责

Session Manager 管理用户在 Workspace 中启动的研究会话。每个 Session 对应一次 Runtime Workflow 执行或一次可复核的人机协作过程。

## 2. Session 字段

Session 包含 session_id、project_id、runtime_id、workflow_id、intent、status、refs、created_at、updated_at 和 disclaimer。

Session 产出的 Evidence、Knowledge Graph、Scorecard、Report、Review 和 Export 都必须作为 Artifact 登记，Session 本身只保留引用和状态。

## 3. 状态

推荐状态包括 OPEN、RUNNING、WAITING_FOR_HUMAN、REVIEWING、COMPLETED、FAILED 和 CLOSED。

## 4. Runtime 边界

Session 可以记录 Runtime Plan 引用和 Runtime 输出摘要，但不能直接调用 Agent 业务逻辑。Agent 执行仍由 Runtime Core、Task Dispatcher 和 Agent Session 完成。

## 5. 审计

会话打开、状态变化、人工确认、Review 结论、Snapshot 和 Export 都必须写入 Audit Log。需要复盘时，Verification Agent 使用 Snapshot 与 Replay Plan 复核会话。

---

免责声明：本文档和示例仅用于 AIRS 工程开发、投资研究流程编排与质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。
