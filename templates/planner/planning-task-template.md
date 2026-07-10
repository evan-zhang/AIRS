# Planning Task Template

免责声明：本模板仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## Task Metadata

- `task_id`
- `agent_role`
- `dependencies`
- `expected_output`
- `quality_gate`

## Planner Gate

所有 Planning Task 必须属于 Research Plan 的一部分。Runtime Task 只能由 Planner 输出派生，不能直接来自用户目标。

## Review Checklist

- 是否保留依赖关系。
- 是否保留 Evidence、KG、Score 和 Report 引用。
- 是否明确反方证据和缺失证据。
- 是否避免交易动作、目标价和收益承诺。
