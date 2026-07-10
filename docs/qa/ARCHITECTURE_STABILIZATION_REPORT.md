# QA Sprint 2 Architecture Stabilization Report

日期：2026-07-10
分支：`qa/architecture-stabilization`

免责声明：本报告仅用于 AIRS 工程质量检查，不构成投资建议。

## 已修复问题

### AUDIT-001 / TD-001: Orchestrator 边界

涉及文件：

- `orchestrator/__init__.py`
- `orchestrator/core.py`
- `apps/equity_research/app.py`
- `docs/orchestrator/orchestrator-architecture.md`
- `docs/adr/ADR-0016-architecture-stabilization.md`

修复内容：

- 新增薄 Orchestrator Facade。
- APP-001 改为通过 `run_planned_workflow()` 执行 Runtime。
- Orchestrator 校验 `plan_id`、`required_runtime.tasks`、task 唯一性和依赖闭合。

### AUDIT-002 / TD-004: APP-001 与 Core 契约

涉及文件：

- `common/contract_validation.py`
- `apps/equity_research/app.py`
- `apps/equity_research/report_exporter.py`

修复内容：

- 新增 Evidence/KG/Score/Report 引用闭合校验。
- APP-001 输出 `contract_validation`、`status` 和 `quality_gate`。
- Report Generator 失败不再静默等同成功，会进入质量门禁。

### AUDIT-003 / TD-003: 数据链路和 Mock 标识

涉及文件：

- `data_connectors/normalizer.py`
- `apps/equity_research/data_collector.py`
- `apps/equity_research/app.py`
- `tests/production-e2e/e2e_harness.py`

修复内容：

- Connector traceability 增加 `mode`。
- APP-001 输出 `data_lineage`。
- Mock/SKIP evidence 不得标记为 Fact。

### AUDIT-004 / TD-002: 验证脚本业务语义

涉及文件：

- `scripts/validate_architecture_stabilization.py`

修复内容：

- 新增 Orchestrator boundary test。
- 新增 APP-Core contract test。
- 新增 mock evidence policy test。
- 新增 API public bind security test。

### AUDIT-008 / TD-006: API 安全边界

涉及文件：

- `api/server.py`
- `api/routes/research.py`
- `.env.example`
- `api/README.md`
- `docs/api/reference.md`
- `docker/docker-compose.yml`
- `docs/deployment/docker.md`

修复内容：

- API 默认绑定 `127.0.0.1`。
- 非本地绑定必须设置 `AIRS_API_KEY`。
- 支持 Bearer / `X-AIRS-API-Key`。
- 增加 CORS allowlist、请求体大小限制和错误脱敏。

## 未修复问题

- AUDIT-006：Score Engine 尚未完全独立为 runtime module。
- TD-003：不可 SKIP 的 real-mode release case 仍需真实网络/凭证环境验证。
- TD-006：速率限制和生产 profile 尚未完整实现。
- TD-008：Workspace / Runtime Memory / Learning 生命周期模型仍需后续收敛。

## 契约变化

- 新增 `orchestrator.run_planned_workflow(plan, case_id=None)` 作为 Planner -> Runtime 正式入口。
- APP-001 顶层结果新增 `status`、`quality_gate`、`orchestrator`、`data_lineage`、`contract_validation`。
- Connector result `traceability` 新增 `mode`。
- API 非本地绑定需要 `AIRS_API_KEY`。

## 删除或合并内容

- 未删除生产代码。
- 未合并 Medium/Low 范围模块。
- 旧 `docs/audit/TECHNICAL_DEBT.md` 保留为兼容指针，权威登记迁移到 `TECHNICAL_DEBT_REGISTER.md`。

## 测试结果

已完成：

- `python3 scripts/validate_architecture_stabilization.py`：PASS
- `python3 scripts/validate_equity_research_app.py`：PASS
- `python3 scripts/validate_productization.py`：PASS
- `python3 cli/airs.py validate --all`：PASS
- Production E2E harness `tests/production-e2e/test_*.py::run_case()`：8/8 PASS
- Failure injection harness `tests/failure-injection/test_*.py::run_case()`：3/3 PASS
- `python3 scripts/validate_e2e.py`：PASS

说明：`pytest tests/production-e2e` 和 `pytest tests/failure-injection` 未收集到测试函数，因为这些文件采用 `run_case()` harness 形式；本轮已按仓库实际 harness 入口逐个执行。

## 剩余发布风险

- 真实数据源在无凭证/无网络环境仍可能 fallback 或 SKIP。
- Docker Web 静态页面尚未内置 API key 注入流程。
- Score Engine 仍是 schema/methodology/local calculator 的组合形态。

## 是否建议进入下一轮 QA

建议进入下一轮 QA，但不建议直接发布 `v1.0.0 Stable`。下一轮应重点验证 real-mode 数据源、Score Engine 收敛和公网部署 profile。
