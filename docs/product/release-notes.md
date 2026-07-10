# AIRS Platform 1.0 Release Notes

免责声明：本 Release Notes 仅记录 AIRS 工程产品化交付内容，不构成投资建议。

## v1.0.0 - RELEASE-001

### Added

- 新增标准库 CLI：`init`、`run`、`demo`、`validate`。
- 新增标准库 REST API Server，默认端口 `8765`。
- 新增纯 HTML/CSS/JS Web UI，支持 Dashboard、新建研究、历史、Workspace、Knowledge Graph、Memory 和 Settings。
- 新增 Dockerfile 与 `docker compose up` 一键启动配置。
- 新增 `config/airs.yaml` 配置中心和 `.env.example` 产品化配置项。
- 新增 NVIDIA、TSMC、康哲药业 Demo JSON 和 `demo/run_demo.py`。
- 新增 API、部署、产品文档、ADR、自检脚本、Completion Report 和 Self Review。

### Changed

- README 增加产品使用入口。
- CHANGELOG 增加 RELEASE-001 记录。

### Compliance

- 所有产品入口固定声明 AIRS 不构成投资建议。
- CLI/API/Web/Demo 不引入第三方依赖，不实现自动交易能力。

