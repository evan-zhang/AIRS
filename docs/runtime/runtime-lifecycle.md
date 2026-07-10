# Agent Lifecycle（生命周期）

## 1. 生命周期状态

Agent Session 使用统一状态机：CREATED -> INITIALIZED -> RUNNING -> PAUSED -> RESUMED -> COMPLETED -> DESTROYED。失败路径为 RUNNING -> FAILED -> DESTROYED，取消路径为 RUNNING -> CANCELLED -> DESTROYED。

## 2. 创建

Runtime Core 根据 Agent Registry 中的 AgentDefinition 创建 Session。创建阶段只分配 session_id、agent_id、task_id 和初始 Context，不执行业务逻辑。

## 3. 初始化

AgentLifecycle.initialize 会校验输入、资源预算、依赖任务和免责声明要求。初始化成功后写入 AGENT_INITIALIZED 事件。

## 4. 运行

运行阶段由 Task Dispatcher 调用 Session.run。Sync Agent 立即返回；Async Agent 返回可后续恢复的状态；Parallel Agent 由 Dispatcher 批量调度；Long-running Agent 按 checkpoint 更新；Human-in-the-loop Agent 进入 WAITING_FOR_HUMAN。

## 5. 暂停与恢复

暂停只冻结 Session 状态和 Context Snapshot，不删除消息、事件或 Memory。恢复时 Runtime 使用同一 session_id 读取上次 checkpoint，并写入 AGENT_RESUMED。

## 6. 完成与销毁

完成时 Session 输出 final_state，并由 State Manager 固化。销毁只释放临时资源，不删除审计事件。

## Workflow 边界

本组件只服务 Runtime 调度后的 Workflow 执行链路，不允许 Workflow 绕过 Runtime 直接驱动业务模块。

---

免责声明：本文档和示例仅用于 AIRS 工程开发、投资研究流程编排与质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。
