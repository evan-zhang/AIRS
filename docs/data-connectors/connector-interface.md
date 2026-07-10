# Connector Interface（统一接口规范）

**Feature**：FEATURE-004 Data Connector Framework  
**版本**：v0.1.0  
**最后更新**：2026-07-10

免责声明：本文档和代码仅用于 AIRS 工程开发、研究质量控制和数据接入治理，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## 1. 接口目标

统一接口让不同外部数据源以相同方式接入 AIRS。Connector 实现者只需要实现配置、Schema、抓取、归一化、缓存和健康检查；研究层只消费统一 Result。

## 2. 必需能力

每个 Connector 必须提供以下能力：

- Config：连接器配置，包括 source、base_url、auth、retry、cache、version。
- Input Schema：输入参数结构，说明必需字段、类型和示例。
- Output Schema：输出结构，必须包含 Source、URL、Timestamp、Version、Trace ID。
- Error Handling：统一错误对象和可重试标记。
- Retry Policy：最大次数、初始延迟、退避倍数。
- Cache Strategy：TTL、缓存键和是否允许 stale。
- Health Check：返回 status、latency、last_success、error。
- Test Case：最小测试输入和预期输出字段。

## 3. Python 抽象方法

```python
class BaseConnector(ABC):
    connector_id: str
    config: ConnectorConfig

    def input_schema(self) -> dict: ...
    def output_schema(self) -> dict: ...
    def fetch(self, request: ConnectorRequest) -> ConnectorResult: ...
    def normalize(self, raw: dict, request: ConnectorRequest) -> ConnectorResult: ...
    def health_check(self) -> HealthStatus: ...
    def test_case(self) -> dict: ...
```

## 4. 统一输出

Connector Result 的最低字段：

```json
{
  "connector_id": "sec_edgar",
  "source": "SEC EDGAR",
  "source_type": "regulatory",
  "url": "https://www.sec.gov/edgar",
  "timestamp": "2026-07-10T00:00:00+08:00",
  "version": "0.1.0",
  "trace_id": "TRACE-...",
  "data": {},
  "traceability": {
    "connector": "sec_edgar",
    "request_id": "...",
    "cache_hit": false,
    "transformations": ["mock_fetch", "normalize"]
  },
  "disclaimer": "仅供研究参考，不构成投资建议"
}
```

## 5. 下游约束

Methodology、Skill、Knowledge Graph 和 Report 只能引用 Connector Result 或 Evidence Card，不能自行补充外部请求逻辑。若需要新来源，应新增 Connector 并注册到 Registry。

## Traceability 对齐

Connector 输出必须保留 Source、URL、Timestamp、Version、Trace ID 和 Traceability，并传递给 Evidence Card 的追溯字段。
