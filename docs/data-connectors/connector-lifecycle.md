# Connector Lifecycle（连接器生命周期）

**Feature**：FEATURE-004 Data Connector Framework  
**版本**：v0.1.0  
**最后更新**：2026-07-10

免责声明：本文档和代码仅用于 AIRS 工程开发、研究质量控制和数据接入治理，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## 1. 生命周期总览

Connector 生命周期采用统一七步：Register → Authenticate → Fetch → Normalize → Validate → Cache → Publish。任何 Connector 必须按此顺序暴露状态，便于 Review Agent 和 Verification Agent 复核。

## 2. Register

注册阶段由 `ConnectorRegistry` 完成。注册信息包括 Connector ID、名称、版本、Source Type、优先级、配置、输入 Schema、输出 Schema、重试策略、缓存策略和健康检查端点。Registry 是唯一发现入口，下游模块不得直接 import 某个外部数据 SDK。

## 3. Authenticate

认证阶段由 `AuthConfig` 和 `Authenticator` 完成。认证输出仅是请求头或认证上下文，不写入报告正文，不进入 Evidence Card。若认证失败，Connector 必须返回标准错误对象，包含 `error_code`、`message`、`retryable` 和 `trace_id`。

## 4. Fetch

抓取阶段执行最小必要请求。Connector 必须遵守 Rate Limit Manager，并为每次请求生成 `trace_id`。本 Feature 的六个官方 Connector 均为 Mock 实现，不访问真实外部网络。

## 5. Normalize

归一化阶段把来源字段映射为统一 envelope：`connector_id`、`source`、`source_type`、`url`、`timestamp`、`version`、`trace_id`、`data`、`traceability`、`disclaimer`。归一化只改变结构，不改写原始事实含义。

## 6. Validate

校验阶段检查输入 Schema、输出 Schema、必需追溯字段和合规字段。校验失败时不得发布结果；错误必须留在 Connector Result 中，供 Verification Agent 复现。

## 7. Cache

缓存阶段由 `CacheManager` 按 Connector ID、输入参数、版本和缓存策略生成键。缓存命中必须在 `traceability` 中记录 `cache_hit=true`，避免下游误以为每次都是实时抓取。

## 8. Publish

发布阶段输出 Connector Result。下游可以把 Result 转为 Evidence Card，但必须补充 supports、refutes、missing_evidence、confidence、evidence_level 和 weight。Connector 不负责投资判断，也不生成荐股或交易动作。

## 9. 失败处理

- 认证失败：返回不可重试错误，提示配置问题。
- 限流失败：返回可重试错误，记录下一次可用时间。
- 来源失败：按 Retry Policy 指数退避。
- Schema 失败：返回不可发布结果，要求修复 Connector 或输入。
- 缓存失败：允许降级为非缓存执行，但必须记录 warning。

## Traceability 对齐

Connector 输出必须保留 Source、URL、Timestamp、Version、Trace ID 和 Traceability，并传递给 Evidence Card 的追溯字段。
