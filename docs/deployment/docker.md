# AIRS Docker Deployment

免责声明：本 Docker 部署文档仅用于 AIRS 本地或内网工程演示，不构成投资建议。

## Start

```bash
cd docker
docker compose up
```

## Ports

- API: `8765`
- Web: `8080`

## Volumes

- `airs-workspace`：研究资产和运行输出。
- `airs-cache`：Connector 与产品缓存。

默认使用 Mock Connector 模式。真实数据源需要通过环境变量显式启用。

