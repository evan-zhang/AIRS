# Connector Architecture（连接器架构总览）

**Feature**：FEATURE-004 Data Connector Framework / FEATURE-013 Real Data Integration
**版本**：v0.2.0
**最后更新**：2026-07-10

免责声明：本文档和代码仅用于 AIRS 工程开发、研究质量控制和数据接入治理，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## 1. 目标

Data Connector Framework 是 AIRS 的统一外部数据接入边界。所有外部数据源，包括 SEC/EDGAR、行情 API、新闻、GitHub、RSS 和第三方数据库，都必须先通过 Connector 完成认证、抓取、归一化、校验、缓存和发布，然后才能进入 Evidence Layer、Knowledge Graph Engine 或 Report Generator。

该框架不改变 M2 Methodology、M3 Evidence Card、FEATURE-002 Knowledge Graph 或 FEATURE-003 Report Generator 的设计。它只定义“外部数据如何进入 AIRS”，并把每次数据访问转成可追溯的 Connector Result。

## 2. 分层位置

```text
External Source
    ↓
Connector Interface
    ↓
Auth / Rate Limit / Retry / Cache
    ↓
Normalizer / Validator
    ↓
Connector Result（Source, URL, Timestamp, Version, Trace ID）
    ↓
Evidence Card / Knowledge Graph / Report
```

Methodology、Skill、Report、Knowledge Graph 不允许直接访问外部 URL、SDK 或 API Key。它们只能消费 Connector 发布的结构化结果，并在下游证据卡中保留来源、URL、采集时间、版本和追溯信息。

## 3. 核心组件

- `Connector Registry`：注册和发现 Connector，避免下游硬编码数据源。
- `Connector Interface`：规定 Config、Input Schema、Output Schema、fetch、normalize、health_check 等统一方法。
- `Authentication Framework`：统一处理 none、api_key、bearer_token 和 basic 等认证模式。
- `Rate Limit Manager`：按 Connector 维度控制请求频率。
- `Retry & Backoff`：统一处理临时失败，不让业务层散落重试逻辑。
- `Cache Manager`：按请求指纹缓存 Connector Result，减少重复访问。
- `Data Normalizer`：把不同来源输出映射到统一 envelope。
- `Source Priority Manager`：按 Official > Regulatory > Company > Exchange > Trusted Third-party > Public News > Community 排序。
- `Connector Health Check`：提供连接器可用性、延迟、错误率和最后成功时间。

## 4. 数据流原则

1. 所有外部数据先进入 Connector，不绕过 Registry。
2. 所有输出必须包含 `source`、`url`、`timestamp`、`version`、`trace_id` 和 `traceability`。
3. Connector 只采集和归一化数据，不生成投资结论。
4. Connector Result 可被 Evidence Card 引用，但不能替代 Evidence Card 的 supports、refutes、missing_evidence 和 weight。
5. 缓存、限流、重试属于接入层治理，不应由 Report 或 Skill 重复实现。

## 5. 与现有层的关系

- M2 Methodology：只声明需要什么证据，不直接访问数据源。
- M3 Evidence：把 Connector Result 转成 Evidence Card，并补充命题绑定、缺失证据和证据等级。
- FEATURE-002 Knowledge Graph：只消费 Evidence Card 或 Connector Result 引用，不直接抓取外部数据。
- FEATURE-003 Report Generator：只引用证据和图谱摘要，不直接查询数据源。

## 6. 双模式运行时

本 Feature 提供 Python 最小可运行实现。FEATURE-013 后，SEC EDGAR、RSS、GitHub 和 News 支持 `fetch_real()` 与 `fetch_mock()` 双模式；`fetch()` 根据环境变量或请求参数选择真实模式或 Mock 模式。默认仍为 Mock，便于自检、离线回归和无凭证环境运行。

真实模式统一使用 `data_connectors/http_client.py`、`env_config.py`、`persistent_cache.py` 和 `secret_masking.py`。如果网络、凭证、限流或来源解析不可用，运行时自动 fallback 到 Mock；集成测试直接调用真实方法，失败时 SKIP，避免把 Mock 结果误记为真实通过。

四个真实 Connector 的 `data` 中额外保留 `source`、`url`、`publication_time`、`collection_time`、`trace_id`、`connector_version`、`raw_hash` 和 `confidence`。这些字段用于 Evidence、Knowledge Graph 和 Report 的追溯，不代表投资判断。

## Traceability 对齐

Connector 输出必须保留 Source、URL、Timestamp、Version、Trace ID 和 Traceability，并传递给 Evidence Card 的追溯字段。
