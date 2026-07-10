# Research Scope Builder

免责声明：本文档仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## 职责

Research Scope Builder 负责把目标和意图转换为研究边界。Scope 是防止研究失控、证据污染和 Runtime 过度执行的第一道约束。

## Scope 内容

- `subject`：研究对象。
- `goal_type`：目标类型。
- `time_horizon`：时间范围。
- `geography`：地域范围。
- `constraints`：用户和系统约束。
- `in_scope`：允许执行的研究活动。
- `out_of_scope`：禁止执行的活动。
- `success_criteria`：成功标准。

## Out Of Scope

所有 Scope 都必须明确排除真实交易执行、确定性收益预测、未追溯来源的结论，以及绕过 Planner 直接调用 Runtime。

## 与 Workspace 的关系

Scope 应作为 Workspace Project 的初始化字段保存，供后续 Review、Replay 和 Audit 使用。
