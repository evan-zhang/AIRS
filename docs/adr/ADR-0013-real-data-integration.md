# ADR-0013: Real Data Integration

**状态**：Accepted
**日期**：2026-07-10
**Feature**：FEATURE-013 Real Data Integration

免责声明：本文档和代码仅用于 AIRS 工程开发、研究质量控制和数据接入治理，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## Context

FEATURE-004 建立了统一 Data Connector Framework，但六个官方 Connector 都是 Mock。AIRS 需要引入可治理的真实数据接入能力，同时不能破坏离线验证、生产 E2E、无凭证环境和合规边界。

## Decision

采用双模式 Connector：

- 默认 `mock`，保证本地和 CI 无网络也能稳定回归。
- 显式 `real` 时访问真实数据源。
- `fetch_real()` 负责真实 API 调用。
- `fetch_mock()` 保留旧 Mock 语义。
- `fetch()` 根据 `AIRS_CONNECTOR_MODE`、单 Connector 环境变量或请求 `mode` 字段选择路径。
- 真实路径失败时 fallback 到 Mock；集成测试直接调用 `fetch_real()` 并在不可用时 SKIP。

基础设施采用 Python 标准库：

- `urllib` HTTP Client。
- `.env` 与环境变量配置。
- 文件系统 JSON cache。
- 递归 Secret Masking。

## Scope

本 ADR 覆盖 SEC EDGAR、RSS、GitHub 和 News。Yahoo Finance 与 Alpha Vantage 在 FEATURE-013 中继续保持 Mock。

## Consequences

正向影响：

- 真实数据可进入 Connector Result、Evidence、Knowledge Graph 和 Report 链路。
- 无凭证环境仍可运行全部 Mock 回归。
- 真实输出保留 8 个追溯字段，便于审计和复现。
- 不引入第三方 Python 依赖。

代价：

- `urllib` 相比专用 SDK 功能更少，复杂认证和分页需要后续扩展。
- News Connector 依赖用户显式配置 endpoint，无法默认真实运行。
- SEC EDGAR 和 GitHub 受外部 rate limit 影响，真实集成测试可能 SKIP。

## Compliance

真实密钥不得提交到仓库。日志、缓存、报告和 Connector Result 不得暴露 token 或 API Key。Connector 只采集和归一化数据，不提供荐股、自动交易、交易指令、目标价或收益承诺。
