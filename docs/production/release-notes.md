# AIRS V1.0.0 Release Notes（发布说明）

**版本**：v1.0.0
**发布日期**：2026-07-11
**状态**：Stable

免责声明：本 Release Notes 仅记录 AIRS 工程产品化交付内容，不构成投资建议，不提供荐股、交易指令、目标价或收益承诺。

## 1. 发布摘要

AIRS v1.0.0 完成 Stable 发布。项目形成可阅读、可审查、可验证、可本地运行、可 Docker 部署的 AI 投资研究流程编排与质量控制平台。

最终放行依据：

- Release Readiness V5：Approve
- GitHub Actions Docker Release Gate：PASS
- Workflow Run ID：`29134227516`
- Base image digest：`python@sha256:e031123e3d85762b141ad1cbc56452ba69c6e722ebf2f042cc0dc86c47c0d8b3`

## 2. 本次发布内容

- CLI：初始化、运行研究、内置 Demo、全量验证。
- REST API：健康检查、Workspace、Memory、Research、Company、Theme、Report。
- Web UI：本地静态控制台。
- Docker：API + Web compose 部署，带 API key healthcheck。
- APP-001：股票研究工作流，串联 Planner、Orchestrator、Runtime、Committee、Investment Engine、Evidence、KG、Score、Report、Memory 和 Learning。
- Stable Release Gate：Mock、SKIP、Fallback、Unknown 数据不会计入真实生产 PASS。
- API 安全：API key、非本地绑定保护、CORS allowlist、body limit、rate limit 和错误脱敏。
- Real Connector：RSS real probe 纳入 Stable validator；fallback 明确标记。

## 3. 质量状态

以下验证均已通过：

- `python3 -m pytest -q`
- `python3 scripts/production_check.py`
- `AIRS_RUN_REAL_CONNECTOR_PROBE=1 python3 scripts/validate_stable_release.py`
- `python3 cli/airs.py validate --all`
- `python3 scripts/run_production_tests.py`
- CI Docker Release Gate run `29134227516`

## 4. 已知限制

- AIRS 不是投资顾问系统，不提供荐股、自动交易、目标价或收益承诺。
- 部分真实数据源需要网络和凭证；不可用时必须标记为未验证或降级。
- 本地 Demo 可使用 Mock/Fallback 数据，但 Stable gate 不允许其冒充真实生产 PASS。
- Runtime 是本地治理型工作流 runtime，不是多租户分布式服务。

## 5. 升级建议

后续 v1.x 可继续加强真实数据源覆盖、Score Engine 收敛、运行时可观测性、更多生产基准和更完整的部署 profile。

## 6. 免责声明

AIRS v1.0.0 仅用于投资研究流程编排、证据追溯、质量控制和教育研究，不构成投资建议，不提供荐股、交易指令、目标价或收益承诺。所有投资决策应由使用者独立判断并自行承担风险。
