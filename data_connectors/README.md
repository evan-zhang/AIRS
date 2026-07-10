# AIRS Data Connectors

`data_connectors/` 是 FEATURE-004 的最小可运行 Python 实现。它提供统一 Connector Registry、抽象接口、认证、限流、缓存、重试、归一化、数据源优先级和健康检查。

## 使用示例

```python
from data_connectors import ConnectorRequest, default_registry

registry = default_registry()
connector = registry.get("sec_edgar")
result = connector.fetch(ConnectorRequest({"ticker": "AAPL"}))
print(result.to_dict()["trace_id"])
```

## 输出要求

所有 Connector Result 必须包含 `source`、`url`、`timestamp`、`version`、`trace_id` 和 `traceability`，以便 M3 Evidence Card 继续补充 supports、refutes、missing_evidence、confidence、evidence_level 和 weight。

## 合规说明

本目录仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。
