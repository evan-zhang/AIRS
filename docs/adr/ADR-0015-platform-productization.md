# ADR-0015: AIRS Platform Productization

免责声明：本 ADR 仅记录 AIRS 工程架构决策，不构成投资建议。

## Status

Accepted - 2026-07-10

## Context

AIRS 已具备 Planner、Runtime、Connector、Committee、Workspace、Report、Knowledge Graph、Memory 和 Learning 等核心模块，但用户仍需要直接可运行的产品入口。RELEASE-001 要求在不大规模重构 AIRS Core 的前提下，提供 CLI、REST API、Web UI、Docker、配置中心、Demo 和产品级文档。

## Decision

- 以 APP-001 Equity Research App 作为 Platform 1.0 的主业务入口。
- CLI 使用标准库 `argparse`，API 使用标准库 `http.server`，Web 使用纯 HTML/CSS/JS。
- Docker 使用同一主镜像分别启动 API 与静态 Web 服务。
- 配置中心使用 `config/airs.yaml` 与 `.env.example`，不保存真实密钥。
- 产品化验证通过 `scripts/validate_productization.py` 独立执行，并纳入全量验证。

## Consequences

- 平台可直接运行和演示，且没有新增第三方运行依赖。
- 产品入口复用现有核心模块，避免重构风险。
- Web UI 是轻量静态控制台，不承担复杂权限或多用户会话能力。

