# AIRS 5 分钟 Quick Start

免责声明：AIRS Quick Start 仅用于产品演示和研究质量控制，不构成投资建议。

## 1. 初始化

```bash
python3 cli/airs.py init
```

## 2. 运行 Demo

```bash
python3 cli/airs.py demo nvidia
```

## 3. 启动 API

```bash
python3 api/server.py
```

API 默认只监听 `127.0.0.1:8765`。如需绑定公网地址，必须先设置 `AIRS_API_KEY`。

## 4. 打开 Web

```bash
cd web
python3 -m http.server 8080
```

## 5. 验证

```bash
python3 cli/airs.py validate
```
