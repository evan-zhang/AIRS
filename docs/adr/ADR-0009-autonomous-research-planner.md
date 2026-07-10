# ADR-0009: Autonomous Research Planner

免责声明：本文档仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## Status

Accepted

## Context

AIRS 已具备 Builder、Connector、Knowledge Graph、Report Generator、Runtime、Workspace 和 Investment Research Engine。FEATURE-008 让 Engine 可以编排底层能力，但仍需要一个更上层的 Planner 来接收用户目标、定义研究范围、选择方法论和资源，并在 Runtime 前形成可审计 Research Plan。

如果 Runtime 直接接收用户请求，系统会绕过目标解析、范围约束、预算、置信度和 Review Gate，导致执行链路难以复核。

## Decision

新增 `planner/` 和 `docs/planner/`，将 Autonomous Research Planner 定义为 AIRS 最上层入口。所有用户研究目标必须先进入 Planner。Planner 输出 Research Plan、Workflow Spec、Runtime Plan、Expected Evidence、Expected KG、Budget、Confidence、Risks 和 Deliverables。

Runtime Plan 必须包含：

- `planner_generated=true`
- `raw_user_request_allowed=false`

缺少这两个字段时，Runtime 不应执行。

## Consequences

- Research Agent 有统一的研究计划入口。
- Runtime 边界更清晰，只执行 Planner 产物。
- Review Agent 可以审查目标拆解、证据预期、依赖顺序、预算和风险。
- Verification Agent 可以运行 `scripts/validate_planner.py` 验证 Planner 与 M1-M8、FEATURE-001/002/003/004/006/007/008 的回归兼容。

## Alternatives Considered

让 Investment Research Engine 直接解析用户目标可以减少一个层级，但会让 Engine 同时承担规划、执行、风险预算和 Runtime 门禁职责。单独设置 Planner 可以让 Engine 保持研究编排层定位，并让 Runtime Gate 成为可验证契约。
