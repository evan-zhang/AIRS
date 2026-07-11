# AIRS Stable Release Self Review

日期：2026-07-10

免责声明：本自审仅用于 AIRS 工程质量检查，不构成投资建议。

## Review Scope

本自审覆盖 QA Sprint 3 Stable Release Remediation：

- Stable release gate
- Mock/SKIP/Fallback lineage policy
- CLI/API/App 与真实数据要求契约
- API 鉴权、请求限制、错误脱敏
- Docker compose healthcheck
- Release 文档一致性

## What Changed

- 新增 `common/release_gate.py`，统一 Stable gate。
- `summarize_data_lineage()` 增加 degraded source 明细和计数。
- APP-001 支持 `require_real_data` 并输出 `stable_release_gate`。
- CLI `airs run --real-data` 在真实门禁失败时返回非 0。
- API research response 顶层暴露 `data_lineage` 和 `stable_release_gate`。
- Connector fallback 统一使用 `fallback_mock`。
- Yahoo Finance 增加 real fetch 尝试。
- API 新增 rate limit，invalid JSON 默认脱敏。
- Docker compose 新增 API key healthcheck。
- 新增 stable profile、ADR、remediation report 和 readiness V2。

## Self Review Findings

### Fixed

- Mock/SKIP/Fallback 不再能被 Stable gate 计入真实生产 PASS。
- Demo/mock 仍可用于本地结构验证，但会显示 degraded 状态。
- CLI/API 自动化调用可以看到质量门禁结果。
- `production_check.py` 不再只跑 M1-M8 结构门禁，也包含 Stable remediation gate。
- Release 文档不再以旧 `FINAL_REVIEW` 作为最终 Stable 判断。

### Remaining Risks

- APP-001 仍是 Core-assisted，不是完全 Core-driven；Evidence/KG/Score 的完整统一 builder 后续仍需处理。
- Score Engine runtime consolidation 仍未完成。
- Docker daemon 当前不可用，build/compose/health 未验证。
- News real connector 仍依赖外部 endpoint 和凭证。

## Verification

通过：

- `python3 scripts/validate_stable_release.py`
- `AIRS_RUN_REAL_CONNECTOR_PROBE=1 python3 scripts/validate_stable_release.py`
- `python3 scripts/run_production_tests.py`
- `python3 scripts/validate_e2e.py`
- `python3 cli/airs.py init --output .airs/qa-sprint3.yaml --force`
- `python3 cli/airs.py demo nvidia --output-dir demo/output/qa-sprint3`
- `python3 cli/airs.py validate --all`
- `python3 scripts/production_check.py`
- `python3 -m pytest -q`
- Docker compose config 解析
- API 本地鉴权、rate limit、body limit、错误脱敏测试

未验证：

- Docker image build
- Docker compose up
- Docker container health check

原因：当前环境无法连接 Docker daemon。

## Self Review Conclusion

QA Sprint 3 已修复 Stable 发布审核中的主要 Blocker，并把无法验证项显式留在报告中。当前 PR 可以进入人工复核，但不应自动合并或自动打 Stable tag。
