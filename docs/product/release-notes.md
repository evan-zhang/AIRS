# AIRS v1.0.0 Release Notes

发布日期：2026-07-11

免责声明：本 Release Notes 仅记录 AIRS 工程产品化交付内容，不构成投资建议，不提供荐股、交易指令、目标价或收益承诺。

## Summary

AIRS v1.0.0 是首个 Stable 发布版本。该版本将 AIRS 从方法论与规范仓库推进到可运行、可验证、可 Docker 部署的本地研究质量控制平台。

本次 Stable 放行依据为 Release Readiness V5 和 GitHub Actions Docker Release Gate：

- Workflow Run ID：`29134227516`
- Workflow URL：`https://github.com/evan-zhang/AIRS/actions/runs/29134227516`
- 验证提交：`9dbe5477165817fbea16cdb9494bf8b81bc5f477`
- PR 合并提交：`5ffcad8671309fbf0edbf59a1995f1c2535063cc`
- Base image：official `docker.io/library/python:3.11-slim`
- Base image digest：`python@sha256:e031123e3d85762b141ad1cbc56452ba69c6e722ebf2f042cc0dc86c47c0d8b3`

## Highlights

- CLI：`airs init`、`airs run`、`airs demo`、`airs validate`。
- REST API：`/health`、`/workspace`、`/memory`、`/research`、`/company`、`/theme`、`/report`。
- Web UI：静态控制台，支持 Dashboard、研究创建、历史、Workspace、Knowledge Graph、Memory 和 Settings。
- Docker：标准 Dockerfile 与 Compose 配置，API 端口 `8765`，Web 端口 `8080`。
- APP-001：股票研究工作流，串联 Planner、Orchestrator、Runtime、Committee、Investment Engine、Evidence、KG、Score、Report、Memory 和 Learning。
- Stable Release Gate：Mock、SKIP、Fallback、Unknown 数据源不会计入真实生产 PASS。
- API 安全：API key、非本地绑定保护、CORS allowlist、body limit、rate limit 和错误脱敏。
- Real Connector：RSS real probe 已纳入 Stable validator；real-mode fallback 明确标记为 `fallback_mock`。

## Installation

```bash
git clone https://github.com/evan-zhang/AIRS.git
cd AIRS
git checkout v1.0.0
python3 cli/airs.py init
python3 cli/airs.py validate --all
```

## Docker Quick Start

```bash
git checkout v1.0.0
cd docker
AIRS_API_KEY=change-me docker compose build --no-cache
AIRS_API_KEY=change-me docker compose up -d
curl -H "X-AIRS-API-Key: change-me" http://127.0.0.1:8765/health
```

Shutdown:

```bash
AIRS_API_KEY=change-me docker compose down -v
```

## Verification

Final release verification includes:

- `python3 -m pytest -q`
- `python3 scripts/production_check.py`
- `AIRS_RUN_REAL_CONNECTOR_PROBE=1 python3 scripts/validate_stable_release.py`
- `python3 cli/airs.py validate --all`
- `python3 scripts/run_production_tests.py`
- GitHub Actions Docker Release Gate run `29134227516`

## Known Limitations

- AIRS is a research workflow orchestration and quality-control platform, not an investment advisory service.
- Real connector coverage is limited; credentials or external endpoints may be required for some real data providers.
- Default local demo flows may use degraded data, but Stable gates explicitly mark and block degraded real-data claims.
- Runtime agent execution remains a minimal governed workflow runtime, not a distributed production agent service.
- No automatic trading, order execution, target price generation, or return guarantee is provided.

## Security Notes

- Do not expose the API on non-local interfaces without `AIRS_API_KEY`.
- Treat API keys and connector tokens as secrets; use environment variables or local `.env` files.
- Invalid JSON and internal exceptions are redacted by default unless `AIRS_EXPOSE_ERRORS=true`.
- Docker healthcheck uses `X-AIRS-API-Key`.

## Disclaimer

AIRS v1.0.0 is for investment research workflow orchestration, evidence traceability, and quality control only. It does not constitute investment advice and must not be used as a trading instruction system.

