# AIRS REST API

免责声明：AIRS REST API 仅用于投资研究流程编排、证据追溯和质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## Run

```bash
python3 api/server.py
```

默认监听 `0.0.0.0:8765`。

## Endpoints

- `GET /health`：服务健康检查。
- `GET /workspace`：返回 Workspace 示例状态。
- `GET /memory`：返回 Memory 示例状态。
- `POST /research`：运行通用研究请求。
- `POST /company`：运行公司研究请求。
- `POST /theme`：运行主题研究请求。
- `POST /report`：生成报告型研究结果。

所有接口返回 JSON，并固定包含免责声明。

