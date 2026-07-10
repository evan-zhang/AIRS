# Connector 开发模板

**Connector ID**：`<connector_id>`  
**Source Type**：`official | regulatory | company | exchange | trusted_third_party | public_news | community`  
**Version**：`0.1.0`

## 免责声明

本模板仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## 1. Config

说明 Connector 名称、来源、base_url、认证方式、版本、优先级和启用状态。

## 2. Input Schema

列出必需字段、字段类型、示例和输入校验失败时的错误码。

## 3. Output Schema

必须包含 Source、URL、Timestamp、Version、Trace ID、Traceability 和 Disclaimer。

## 4. Error Handling

说明认证失败、限流、来源超时、Schema 校验失败和缓存失败的处理方式。

## 5. Retry Policy

说明最大重试次数、初始延迟、退避倍数和不可重试错误。

## 6. Cache Strategy

说明 TTL、缓存键、是否允许 stale，以及 cache_hit 如何写入 traceability。

## 7. Health Check

说明 status、latency_ms、last_success 和 error 字段。

## 8. Test Case

提供最小输入、预期输出字段和失败用例。测试不得访问真实交易或下单接口。
