# AIRS Web UI

免责声明：AIRS Web UI 仅用于投资研究流程编排、证据追溯、Workspace 浏览和工程演示，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## Run

静态页面不依赖前端框架，可直接打开 `web/index.html`。如需本地 HTTP 服务：

```bash
cd web
python3 -m http.server 8080
```

默认 API 地址为 `http://localhost:8765`，可在 `settings.html` 中调整。

