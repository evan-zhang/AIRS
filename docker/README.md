# AIRS Docker

免责声明：AIRS Docker 部署仅用于本地或内网研究流程演示和工程验证，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## Run

```bash
cd docker
AIRS_API_KEY="$(openssl rand -hex 24)" docker compose up
```

- API: `http://localhost:8765`
- Web: `http://localhost:8080`

Compose 会挂载 `airs-workspace` 和 `airs-cache` 两个卷，并默认使用 Mock Connector 模式。API 容器以 `0.0.0.0` 暴露端口，因此必须设置 `AIRS_API_KEY`；未设置时拒绝启动，避免把无鉴权研究接口暴露到公网。
