# Financial Skill（财务分析）

## 1. Purpose（目的）

Financial Skill 用于识别财报异常、经营质量变化和财务口径风险。它调用 M4 财报异常 Prompt，引用 M2 财报异常方法论，并使用 M3 Evidence Card 记录财报来源、指标口径和反方证据。

## 2. Inputs（输入）

- `company_or_group`：公司或同业组。
- `financial_periods`：年度、季度或滚动期间。
- `statements`：利润表、资产负债表、现金流量表摘要或来源。
- `comparison_scope`：历史、同业或行业基准。
- `evidence_context`：已有 Evidence Card 或缺失证据清单。

## 3. Outputs（输出）

- 财务异常候选项。
- 指标变化解释和证据来源。
- 同业或历史对比结论。
- 反方解释和不确定性。
- Evidence Card / Evidence Chain 引用。

## 4. Dependencies（依赖，包括引用的 Prompt/Methodology/Evidence）

- Prompt：`prompts/financial/anomaly-analysis.md`。
- Methodology：`docs/methodology/financial-anomaly.md`。
- Evidence：`docs/evidence/evidence-card-specification.md`、`schemas/evidence/evidence-card.schema.json`。

## 5. Invoked Prompt（调用的 Prompt，引用 M4 Prompt Library）

调用 `prompts/financial/anomaly-analysis.md`，传入公司、期间、财务数据摘要、比较范围和证据约束。不得复制 Prompt 正文。

## 6. Invoked Methodology（调用的方法论，引用 M2）

引用 `docs/methodology/financial-anomaly.md`。异常识别、失效场景、反证要求和置信度判断以该方法论为准。

## 7. Invoked Evidence（调用的 Evidence Engine 组件，引用 M3）

财务证据必须记录来源、报告期、采集时间、口径和 traceability。对每个异常命题，Evidence Card 必须区分 `supports`、`refutes` 和 `missing_evidence`。

## 8. Workflow（工作流程）

1. 校验财务期间和口径。
2. 调用 M4 财报异常 Prompt。
3. 按 M2 方法论识别收入、利润、现金流、应收、存货等异常。
4. 生成 Evidence Card 需求或复用已有证据。
5. 输出异常解释、反方解释和不确定性。

## 9. Failure Handling（失效处理）

- 财务数据缺期：返回 `FAIL_INPUT_INCOMPLETE`。
- 口径不可比：返回 PARTIAL 并标注原因。
- 来源不可追溯：返回 `FAIL_SOURCE_MISSING`。
- 用户要求交易动作：返回 `FAIL_COMPLIANCE`。

## 10. Review Checklist（审查清单）

- 是否引用 `prompts/financial/anomaly-analysis.md`。
- 是否引用 `docs/methodology/financial-anomaly.md`。
- 是否记录财务数据来源和口径。
- 是否有反方解释和缺失证据。
- 是否说明不构成投资建议。

