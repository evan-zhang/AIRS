# QA Architecture Self Review

日期：2026-07-10

免责声明：本自审仅用于 AIRS 工程质量检查，不构成投资建议。

## Review Scope

本次自审覆盖 QA Sprint 2 Architecture Stabilization 的 Blocker/High 修复：

- Orchestrator 边界
- APP-001 与 Core 契约
- Connector Mock/SKIP 标识
- 验证脚本业务语义
- API 安全边界

## 已修复问题

- AUDIT-001：新增 Orchestrator Facade，APP-001 不再直接实例化 Runtime。
- AUDIT-002：新增 Core contract validation，校验 Evidence/KG/Score/Report 引用闭合。
- AUDIT-003：新增 data lineage，Mock/SKIP 不再作为 Fact。
- AUDIT-004：新增架构稳定验证脚本，包含真实行为断言。
- AUDIT-008：API 默认 localhost，公网绑定强制 API key。

## 未修复问题

- Score Engine 尚未独立抽出。
- Real-mode release gate 仍需要带真实网络和凭证的环境。
- API rate limiting 仍未完成。
- Docker Web 与 API key 的产品化交互仍需下一轮处理。

## 涉及文件

- `orchestrator/*`
- `common/contract_validation.py`
- `apps/equity_research/*`
- `data_connectors/normalizer.py`
- `api/server.py`
- `api/routes/research.py`
- `scripts/validate_architecture_stabilization.py`
- `tests/production-e2e/e2e_harness.py`
- `docs/adr/ADR-0016-architecture-stabilization.md`
- `docs/qa/ARCHITECTURE_STABILIZATION_REPORT.md`

## 契约变化

- Planner -> Runtime 之间新增 Orchestrator handoff。
- APP-001 输出新增显式状态和契约验证结果。
- Connector traceability 增加 `mode`。
- API public bind 需要 API key。

## 测试结果

已执行：

- `python3 scripts/validate_architecture_stabilization.py`：PASS
- `python3 scripts/validate_equity_research_app.py`：PASS
- `python3 scripts/validate_productization.py`：PASS
- `python3 cli/airs.py validate --all`：PASS
- Production E2E harness：8/8 PASS
- Failure injection harness：3/3 PASS
- `python3 scripts/validate_e2e.py`：PASS

备注：E2E 与故障注入目录中的文件暴露 `run_case()`，不是 pytest `test_*` 函数。本轮按项目原生 harness 入口执行。

## 剩余发布风险

- 当前仍建议保持 RC，不建议 Stable。
- 若要公网测试，需要补 Web/API key 使用体验、rate limit 和部署 profile。
- 若要宣称真实研究能力，需要不可 SKIP 的 real-mode case。

## 建议

建议进入下一轮 QA：Real Data Release Gate + Score Engine Consolidation。
