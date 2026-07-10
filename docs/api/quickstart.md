# AIRS API Quick Start

免责声明：本 Quick Start 仅用于 AIRS API 工程演示，不构成投资建议。

## 1. Start

```bash
python3 api/server.py
```

## 2. Health Check

```bash
curl http://localhost:8765/health
```

## 3. Run Research

```bash
curl -X POST http://localhost:8765/research \
  -H 'Content-Type: application/json' \
  -d '{"symbol":"NVDA","market":"US","research_question":"分析 NVIDIA 的财务、估值、供应链和风险"}'
```

## 4. Open Web UI

```bash
cd web
python3 -m http.server 8080
```

访问 `http://localhost:8080`，在 Settings 中确认 API Base URL 为 `http://localhost:8765`。

