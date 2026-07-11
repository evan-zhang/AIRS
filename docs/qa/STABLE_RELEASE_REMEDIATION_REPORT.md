# AIRS Stable Release Remediation Report

日期：2026-07-10

免责声明：本报告仅用于 AIRS 工程质量检查和发布治理，不构成投资建议。

## Scope

本轮 QA Sprint 3 基于当前 AIRS Git Repository、PR #10 和 `docs/release/RELEASE_READINESS_REVIEW.md` 执行 Stable 发布阻塞项修复。

约束：

- 不新增投资研究业务功能。
- 不重构核心业务模型。
- 不自动合并 PR。
- Mock、SKIP、Fallback 必须显式标记，不得计入真实生产 PASS。
- 无法在当前环境验证的项目必须记录为未验证。

## Issue Matrix

### B1 / Blocker: Production E2E 不证明真实生产行为

- 涉及文件：`tests/production-e2e/e2e_harness.py`、`scripts/validate_e2e.py`、`common/release_gate.py`
- 修复方案：新增 Stable release gate；Production E2E artifact 必须包含 `stable_release_gate`；真实源要求开启时，mock/SKIP/fallback 会导致 gate FAIL。
- 验证方式：`python3 scripts/run_production_tests.py`、`python3 scripts/validate_e2e.py`、`python3 scripts/validate_stable_release.py`
- 当前结果：已修复结构性缺陷；真实外部源 release gate 仍需在 Docker/网络可用环境执行。

### B2 / Blocker: 默认配置是 demo/mock

- 涉及文件：`config/airs.yaml`、`config/airs.stable.yaml`、`config/README.md`
- 修复方案：保留 `airs.yaml` 为本地 demo profile；新增 `airs.stable.yaml` 作为 Stable gate profile，默认 real connector mode。
- 验证方式：`python3 scripts/validate_productization.py`、`python3 cli/airs.py validate --all`
- 当前结果：已修复配置语义混淆。

### B3 / Blocker: Runtime 容易被误解为真实研究执行引擎

- 涉及文件：`apps/equity_research/app.py`、`api/routes/research.py`、`cli/commands/run.py`、`docs/release/RELEASE_READINESS_REVIEW_V2.md`
- 修复方案：不扩展 Runtime 业务功能；通过 `stable_release_gate`、`data_lineage`、CLI exit code 和 V2 报告明确区分结构性 runtime trace 与真实数据发布门禁。
- 验证方式：`python3 cli/airs.py --json run ... --real-data` 返回 exit 1；API 顶层返回 `stable_release_gate`。
- 当前结果：已降低误读风险；Runtime 完整业务执行能力仍延期。

### B4 / Blocker: Release 文档结论冲突

- 涉及文件：`docs/production/FINAL_REVIEW.md`、`docs/release/RELEASE_READINESS_REVIEW_V2.md`
- 修复方案：旧 `FINAL_REVIEW` 标记为历史 M8 Review；Stable 判断以 V2 readiness 为准。
- 验证方式：人工审阅。
- 当前结果：已修复治理冲突。

### H4 / High: Real connector fallback 冒充普通 mock

- 涉及文件：`data_connectors/connectors/news.py`、`sec_edgar.py`、`rss.py`、`github.py`、`yahoo_finance.py`、`data_connectors/real_payload.py`
- 修复方案：real-mode fallback 标记为 `fallback_mock`；Yahoo Finance 增加公开 chart endpoint real fetch，失败时进入 fallback。
- 验证方式：`python3 scripts/validate_stable_release.py`、`pytest tests/integration`
- 当前结果：已修复 fallback 标识；真实网络可用性按环境记录。

### H5 / High: validate_* 信号偏结构

- 涉及文件：`scripts/validate_stable_release.py`、`scripts/production_check.py`
- 修复方案：新增 Stable remediation validator，验证 degraded lineage 不能进入 Stable PASS；纳入 `production_check.py`。
- 验证方式：`python3 scripts/production_check.py`
- 当前结果：已修复核心门禁缺口。

### H6 / High: API 安全硬化不足

- 涉及文件：`api/server.py`、`api/README.md`、`.env.example`、`docker/docker-compose.yml`
- 修复方案：新增 rate limit；invalid JSON 默认脱敏；保留 API key、CORS allowlist、body limit；Docker healthcheck 使用 `X-AIRS-API-Key`。
- 验证方式：本地 API 测试覆盖 401、200、429、413、invalid JSON 脱敏。
- 当前结果：本地验证通过；Docker daemon 不可用，容器级验证未完成。

### H7 / High: 生成物混入源码

- 涉及文件：`.gitignore`
- 修复方案：新增 `.gitignore`，忽略 `__pycache__`、`.pytest_cache`、`.cache`、`.airs`、`demo/output`、`workspace-data`。
- 验证方式：`git status --short`
- 当前结果：已避免新增缓存进入 PR；历史生成物是否清理由维护者决定。

## Verification Summary

已执行并通过：

- `git fetch origin main qa/architecture-stabilization && git merge --no-edit origin/main`
- `python3 scripts/validate_stable_release.py`
- `AIRS_RUN_REAL_CONNECTOR_PROBE=1 python3 scripts/validate_stable_release.py`
- `python3 scripts/run_production_tests.py`
- `python3 scripts/validate_e2e.py`
- `python3 cli/airs.py init --output .airs/qa-sprint3.yaml --force`
- `python3 cli/airs.py demo nvidia --output-dir demo/output/qa-sprint3`
- `python3 cli/airs.py validate --all`
- `python3 -m pytest -q`
- API local checks：401、200、429、413、invalid JSON 脱敏
- `AIRS_API_KEY=qa-secret docker compose -f docker/docker-compose.yml config`

明确未验证：

- `docker build -f docker/Dockerfile -t airs-qa-sprint3 .`：Docker daemon 不可用。
- `docker compose up`、container `/health`：Docker daemon 不可用。

## Result

Blocker remediation: materially addressed.

Remaining release condition: Docker daemon 可用环境中完成 image build、compose up 和容器 health check 后，才能进入人工 Stable 发布复核。
