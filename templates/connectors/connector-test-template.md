# Connector Test 模板

## 免责声明

本测试模板仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## 1. 正常路径

- 输入：提供最小必需字段。
- 期望：返回 `source`、`url`、`timestamp`、`version`、`trace_id`、`traceability`。
- 期望：`error` 为空，`disclaimer` 包含“不构成投资建议”。

## 2. 输入失败

- 输入：缺少必需字段。
- 期望：返回 `INPUT_VALIDATION_ERROR`，`retryable=false`。

## 3. 健康检查

- 调用：`connector.health_check()`。
- 期望：返回 `status`、`latency_ms`、`last_success`、`error`。

## 4. 缓存与追溯

- 同一请求在 TTL 内重复执行时，缓存管理器应能命中。
- Connector Result 的 `traceability.cache_hit` 必须可审计。
