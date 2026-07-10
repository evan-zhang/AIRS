# Message Bus（消息总线）

## 1. 目标

Message Bus 在 Agent Session 之间传递结构化消息，支持 request、response、handoff、review_request 和 human_prompt 五类消息。消息用于任务协作，事件用于审计，两者分离。

## 2. 消息结构

消息包含 message_id、source_session_id、target_session_id、message_type、payload、created_at 和 trace_id。payload 必须是可序列化对象，并保留引用路径而不是复制业务规则。

## 3. 使用约束

Message Bus 不承载无来源研究结论。涉及证据、评分或报告内容时，payload 必须携带 Evidence Chain、Scorecard 或 Report Section 的引用。

## 4. 审计

每条消息都会触发 MESSAGE_PUBLISHED 事件，Runtime Monitor 可按 trace_id 还原跨 Agent 协作链路。

## Workflow 边界

本组件只服务 Runtime 调度后的 Workflow 执行链路，不允许 Workflow 绕过 Runtime 直接驱动业务模块。

---

免责声明：本文档和示例仅用于 AIRS 工程开发、投资研究流程编排与质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。
