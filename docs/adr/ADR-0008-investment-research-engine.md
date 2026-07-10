# ADR-0008: Investment Research Engine

免责声明：本文档仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## Status

Accepted

## Context

AIRS 已具备 Methodology、Evidence、Prompt、Skill、Score、Benchmark、Knowledge Graph、Report Generator、Data Connectors、Runtime 和 Workspace。FEATURE-008 需要把这些底层能力编排为真正可执行的投资研究全流程，同时保留可审计边界和合规约束。

## Decision

新增 `investment_engine/` 作为统一调度层。Engine 不直接抓取外部数据，不绕过 Runtime，不绕过 Workspace，不重复定义 Evidence、Knowledge Graph、Score 或 Report 规则。Engine 输出结构化研究包，并强制 Recommendation 区分 Fact、Inference、Assumption 和 Opinion。

## Consequences

- Research Agent 可以用一个入口生成 Investment Thesis、Knowledge Graph、Evidence Chain、Supply Chain Analysis、Chokepoint Analysis、Score Card、Risk Analysis、Catalyst Analysis 和 Final Research Report。
- Review Agent 可以检查四类语句、反方证据、缺失证据和合规语言。
- Verification Agent 可以运行 `scripts/validate_investment_engine.py` 执行 FEATURE-008 与 M1-M8 回归验证。

## Alternatives Considered

把研究逻辑分散在各 Skill 内部会降低可追踪性，也会让 Review Agent 难以统一复核 Recommendation 标准。将 Engine 作为编排层可以保留底层模块职责，同时提供一个可执行入口。
