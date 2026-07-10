# AIRS Docker

免责声明：AIRS Docker 部署仅用于本地或内网研究流程演示和工程验证，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## Run

```bash
cd docker
docker compose up
```

- API: `http://localhost:8765`
- Web: `http://localhost:8080`

Compose 会挂载 `airs-workspace` 和 `airs-cache` 两个卷，并默认使用 Mock Connector 模式。

