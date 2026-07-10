# AIRS Docker Deployment

免责声明：本 Docker 部署文档仅用于 AIRS 本地或内网工程演示，不构成投资建议。

## Start

```bash
cd docker
AIRS_API_KEY="$(openssl rand -hex 24)" docker compose up
```

不设置 `AIRS_API_KEY` 时，API 容器会拒绝以 `0.0.0.0` 方式暴露服务。

本地仅 API 调试可以不使用 Docker，直接运行：

```bash
python3 api/server.py
```

此时默认只监听 `127.0.0.1:8765`。

## Legacy local demo

```bash
cd docker
docker compose up
```

该命令仅适合已经在 shell 中设置了 `AIRS_API_KEY` 的本地/内网演示环境。

## Ports

- API: `8765`
- Web: `8080`

## Volumes

- `airs-workspace`：研究资产和运行输出。
- `airs-cache`：Connector 与产品缓存。

默认使用 Mock Connector 模式。真实数据源需要通过环境变量显式启用。
