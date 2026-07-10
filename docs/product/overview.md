# AIRS Platform 1.0 产品概览

免责声明：AIRS Platform 1.0 仅用于投资研究流程编排、证据追溯、质量控制和工程演示，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## 产品定位

AIRS Platform 1.0 将 AIRS 从方法论与工程框架升级为可安装、可部署、可运行、可演示的本地产品版本。平台保留既有 Planner、Runtime、Connector、Committee、Evidence、Knowledge Graph、Score、Report、Memory 和 Learning 能力，同时新增 CLI、REST API、Web UI、Docker、配置中心和 Demo 数据。

## 使用入口

- CLI：`python3 cli/airs.py run`、`python3 cli/airs.py demo nvidia`。
- REST API：`python3 api/server.py` 后访问 `http://localhost:8765/health`。
- Web UI：打开 `web/index.html` 或运行 `python3 -m http.server 8080 --directory web`。
- Docker：`cd docker && docker compose up`。

## 核心能力

- 以 APP-001 Equity Research App 为主产品入口，输出 15 段结构化研究报告。
- 通过 Demo 数据快速运行 NVIDIA、TSMC、康哲药业案例。
- 通过 REST API 支持 `/research`、`/company`、`/theme`、`/report`、`/workspace`、`/memory` 和 `/health`。
- 通过 Web UI 浏览 Dashboard、新建研究、历史、Workspace、Knowledge Graph、Memory 和 Settings。
- 通过 `scripts/validate_productization.py` 验证产品化交付物完整性。

## 合规边界

AIRS 不提供个人投资建议，不执行交易，不预测股价，不输出买入、卖出、持有、目标价或收益承诺。所有入口必须保留免责声明。

