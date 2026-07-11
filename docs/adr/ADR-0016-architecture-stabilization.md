# ADR-0016: QA Sprint 2 Architecture Stabilization

日期：2026-07-10

免责声明：本文档仅用于 AIRS 工程架构治理和研究质量控制，不构成投资建议。

## Status

Accepted for QA branch `qa/architecture-stabilization`.

## Context

`docs/audit/ARCHITECTURE_AUDIT_REPORT.md` 和 `docs/audit/REFACTOR_PRIORITY.md` 标记了 Stable 发布前必须修复的 Blocker/High 问题：

- AUDIT-001：Orchestrator 是文档概念，不是可执行模块。
- AUDIT-002：APP-001 调用 Core，但重复构造 Evidence / KG / Score。
- AUDIT-003：Connector 默认 Mock，真实链路通过不等于真实数据成立。
- AUDIT-004：`validate_*` 更像交付物检查，不足以证明业务链路。
- AUDIT-008：API / CLI / Web 是薄壳，但 API 当前不适合公网。

## Decision

1. 采用薄 Orchestrator Facade，而不是在 QA Sprint 2 引入大规模调度系统。
2. Planner 继续拥有 Research Plan 和 Runtime Workflow 生成权。
3. Orchestrator 拥有 Planner -> Runtime handoff 校验权。
4. Runtime 继续拥有 Agent dispatch、state、event 和 resource 管理权。
5. APP-001 不再直接实例化 `RuntimeCore`，必须通过 Orchestrator handoff。
6. APP-001 的 Evidence/KG/Score/Report 输出必须通过 Core contract validation。
7. Connector Mock/SKIP 只能作为降级证据，不能标记为真实 Fact。
8. API 默认只绑定 localhost；非本地绑定必须启用 API key。

## Consequences

Positive:

- 架构图与代码入口开始对齐。
- APP-001 仍保持本地 demo 兼容，但显式暴露降级状态。
- 测试从纯 artifact validation 增加到 contract / behavior validation。
- 公网误暴露风险下降。

Tradeoffs:

- Score Engine 尚未完全抽成独立 runtime module。
- Real-mode release case 仍依赖外部网络和凭证，QA Sprint 2 只建立 lineage 与 policy。
- Docker compose 现在要求设置 `AIRS_API_KEY` 才能暴露 API。

## Validation

- `scripts/validate_architecture_stabilization.py`
- APP-001 runtime validation
- Production E2E harness now records Orchestrator and connector lineage

## Related Audit IDs

- AUDIT-001
- AUDIT-002
- AUDIT-003
- AUDIT-004
- AUDIT-008
- TD-001
- TD-002
- TD-003
- TD-004
- TD-006
