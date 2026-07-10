# Confidence Planner

免责声明：本文档仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## 职责

Confidence Planner 在执行前估算计划置信度。它评估的是“计划是否足够可执行和可复核”，不是投资结论是否正确。

## 维度

- Evidence Confidence：证据源覆盖和反方证据要求。
- Methodology Fit：目标类型与方法论匹配度。
- Budget Fit：预算是否足以支撑计划。

## 输出

- `evidence_confidence`
- `methodology_fit`
- `budget_fit`
- `overall_confidence`
- `confidence_gate`
- `uncertainties`

## 使用方式

当 `overall_confidence` 低于阈值时，Plan Optimizer 应增加风险提示，Review Agent 应要求补充证据或收窄范围。

## 与 Planner / Runtime 的关系

Confidence Planner 是 Planner 内部的前置评估器。它在 Runtime 启动之前判断计划可执行性，帮助决定是否需要补充证据、降低报告深度或增加人工复核。Runtime 不能把执行成功率直接写成研究置信度，也不能用 Runtime 状态替代 Planner 的置信度评估。

## 审计要求

置信度必须拆分为 Evidence Confidence、Methodology Fit 和 Budget Fit。若任一维度低于阈值，Research Plan 需要在 Risks 中记录原因，并在 Expected Deliverables 中保留复核清单。
