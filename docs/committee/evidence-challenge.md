# Evidence Challenge

免责声明：本文档仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## 目标

Evidence Challenge 用于确认研究结论是否有可追溯证据链。AIC 不采集证据，也不替代 M3 Evidence Engine；它检查 Planner 预期证据、Research Engine 阶段证据和 Final Recommendation 是否存在断裂。

## 检查项

- 每个关键命题是否绑定 Evidence Card。
- 是否存在支持证据、反方证据和缺失证据标注。
- 证据是否包含来源、时间戳、版本、URL 或可追溯信息。
- 证据等级是否足以支撑结论强度。
- 是否存在单一来源、过期数据、二手传闻或口径混用。

## 输出

Evidence Reviewer 输出 `PASS`、`CONDITIONAL_PASS` 或 `FAIL`。条件通过必须附带补证任务；失败必须阻断 Research Engine Gate，直到证据链可审计。
