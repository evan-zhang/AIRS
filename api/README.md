# AIRS REST API

免责声明：AIRS REST API 仅用于投资研究流程编排、证据追溯和质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## Run

```bash
python3 api/server.py
```

默认监听 `127.0.0.1:8765`。

公网或容器内绑定 `0.0.0.0` 前必须设置 `AIRS_API_KEY`，否则服务会拒绝启动。可选安全配置：

- `AIRS_API_KEY`：启用 `Authorization: Bearer <key>` 或 `X-AIRS-API-Key` 鉴权。
- `AIRS_CORS_ALLOW_ORIGINS`：逗号分隔的允许来源，默认仅本地 Web。
- `AIRS_MAX_BODY_BYTES`：请求体大小上限。
- `AIRS_RATE_LIMIT_PER_MINUTE`：单客户端/单 API key 每分钟请求上限，默认 120；设为 0 可在本地测试中关闭。
- `AIRS_EXPOSE_ERRORS=false`：默认隐藏内部错误细节。

## Endpoints

- `GET /health`：服务健康检查。
- `GET /workspace`：返回 Workspace 示例状态。
- `GET /memory`：返回 Memory 示例状态。
- `POST /research`：运行通用研究请求。
- `POST /company`：运行公司研究请求。
- `POST /theme`：运行主题研究请求。
- `POST /report`：生成报告型研究结果。

所有接口返回 JSON，并固定包含免责声明。
