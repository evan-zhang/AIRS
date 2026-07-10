# Real Data Integration（真实数据接入指南）

**Feature**：FEATURE-013 Real Data Integration
**版本**：v0.2.0
**最后更新**：2026-07-10

免责声明：本文档和代码仅用于 AIRS 工程开发、研究质量控制和数据接入治理，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## 1. 目标

FEATURE-013 将原有 Mock Connector 升级为双模式 Connector。SEC EDGAR、RSS、GitHub 和 News 可以在真实模式下访问外部 HTTP 数据源，也可以在默认 Mock 模式下完成离线回归。Yahoo Finance 和 Alpha Vantage 在本阶段保持 Mock，避免引入未治理的行情依赖。

真实数据接入只负责采集、解析、归一化和追溯，不生成投资观点。下游 Evidence、Knowledge Graph 和 Report 继续通过 Connector Result 消费数据，并保留 Source、URL、Trace ID 与采集时间。

## 2. 双模式配置

默认模式是 `mock`，不访问网络：

```text
AIRS_CONNECTOR_MODE=mock
```

全局真实模式：

```text
AIRS_CONNECTOR_MODE=real
```

单个 Connector 覆盖：

```text
AIRS_SEC_EDGAR_MODE=real
AIRS_RSS_MODE=real
AIRS_GITHUB_MODE=real
AIRS_NEWS_MODE=real
```

请求级也可以传入 `{"mode": "real"}` 或 `{"mode": "mock"}`。如果真实模式因网络、限流、凭证或解析失败不可用，`fetch()` 自动降级为 `fetch_mock()`，并保持统一输出结构。集成测试直接调用 `fetch_real()`，失败时 SKIP，而不是把 Mock 伪装成真实成功。

## 3. 基础设施

- `data_connectors/http_client.py`：基于 `urllib` 的统一 HTTP Client，支持 timeout、retry、简单 rate limit、User-Agent 和错误脱敏。
- `data_connectors/env_config.py`：从环境变量或 `.env` 读取配置，环境变量优先。
- `data_connectors/persistent_cache.py`：基于文件系统的 JSON 缓存，用 connector、version 和 query 指纹生成缓存键。
- `data_connectors/secret_masking.py`：递归脱敏 key、token、secret、authorization 等字段。
- `.env.example`：本地配置模板，不包含真实密钥。

## 4. 真实输出字段

四个真实 Connector 的 `data` 必须包含 8 个字段：

- `source`：来源名称。
- `url`：实际请求或来源 URL。
- `publication_time`：来源发布时间；缺失时使用请求时间。
- `collection_time`：Connector 采集时间。
- `trace_id`：贯穿本次请求的 Trace ID。
- `connector_version`：Connector 归一化版本。
- `raw_hash`：脱敏后原始 payload 的 SHA-256。
- `confidence`：仅表示接入层对来源与解析完整性的置信度，不代表投资结论。

外层 Connector Result 仍保留 `source`、`url`、`timestamp`、`version`、`trace_id`、`traceability` 和免责声明，以兼容 FEATURE-004 以及生产 E2E。

## 5. Connector 范围

SEC EDGAR 使用 `https://www.sec.gov/cgi-bin/browse-edgar`，支持 ticker/CIK 和 filing type 检索，解析 Atom feed。

RSS 使用 `urllib` 获取 feed，并用 `xml.etree.ElementTree` 解析 RSS 2.0 或 Atom 条目。

GitHub 使用 `https://api.github.com`，支持 repo 详情、issue 列表、release 列表和 repo search。`GITHUB_TOKEN` 可选，用于提高 rate limit，输出中不得出现 token。

News 是通用 JSON News Connector。`NEWS_API_ENDPOINT` 必须显式配置；`NEWS_API_KEY` 可选，参数名由 `NEWS_API_KEY_NAME` 控制。未配置 endpoint 时保持 Mock。

## 6. 测试策略

`scripts/validate_connectors.py` 覆盖文件、双模式方法、Mock 默认路径、8 个追溯字段和 `.env.example`。`tests/integration/` 覆盖真实 SEC EDGAR、RSS、GitHub、News，以及 Connector 到 Evidence、KG、Report 的链路。真实网络或凭证不可用时测试必须 SKIP。

## 7. 安全与治理

真实密钥只允许来自环境变量或本地 `.env`。`.env` 不应进入版本库；`.env.example` 只提供空值模板。缓存和 raw hash 生成前会执行脱敏，避免把 token 写入报告、日志或缓存。

Connector 的输出仍仅用于 AIRS 工程开发、研究质量控制和数据接入治理，不构成投资建议。
