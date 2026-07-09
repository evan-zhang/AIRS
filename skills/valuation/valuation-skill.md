# Valuation Skill（估值分析）

## 1. Purpose（目的）

Valuation Skill 用于组织估值研究、估值假设检查、同业比较和估值不确定性标注。它调用 M4 估值 Prompt，引用 M2 估值方法论，并通过 M3 Evidence Card 追踪财务、同业、增长、折现和反方证据。

本 Skill 不输出目标价、交易动作或收益承诺。

## 2. Inputs（输入）

- `company_or_asset`：研究对象。
- `valuation_context`：历史估值、同业估值、经营假设或用户提供数据。
- `time_range`：估值数据和财务数据期间。
- `peer_group`：可选同业组。
- `evidence_context`：已有证据链。

## 3. Outputs（输出）

- 估值框架选择说明。
- 关键假设列表与证据绑定。
- 同业或历史比较摘要。
- 反方估值情景和不确定性。
- Evidence Chain 与免责声明。

## 4. Dependencies（依赖，包括引用的 Prompt/Methodology/Evidence）

- Prompt：`prompts/valuation/analysis.md`。
- Methodology：`docs/methodology/valuation.md`。
- Evidence：`docs/evidence/evidence-card-specification.md`、`schemas/evidence/evidence-chain.schema.json`。

## 5. Invoked Prompt（调用的 Prompt，引用 M4 Prompt Library）

调用 `prompts/valuation/analysis.md`。Skill 只传入研究对象、估值上下文、证据链和输出约束，不复制 Prompt 正文。

## 6. Invoked Methodology（调用的方法论，引用 M2）

引用 `docs/methodology/valuation.md`。估值方法适用性、Required Evidence、Counter Evidence 和 Confidence 以 M2 文档为准。

## 7. Invoked Evidence（调用的 Evidence Engine 组件，引用 M3）

估值假设必须绑定 Evidence Card。增长假设、利润率、资本开支、折现参数和同业样本都应记录 `supports` 与 `refutes`。缺少关键假设证据时写入 `missing_evidence`，每条假设都必须保留 `traceability` 以便 Review Agent 追溯来源。

## 8. Workflow（工作流程）

1. 校验研究对象和估值范围。
2. 调用估值 Prompt 生成估值框架和关键假设。
3. 按 M2 估值方法论检查适用性。
4. 调用 Evidence Skill 绑定证据卡和反方证据。
5. 输出估值不确定性，而非价格预测。

## 9. Failure Handling（失效处理）

- 同业组不可比：返回 PARTIAL 并说明限制。
- 关键假设无证据：返回 `FAIL_EVIDENCE_INSUFFICIENT`。
- 数据期间缺失：返回补充要求。
- 用户要求目标价格或交易动作：返回 `FAIL_COMPLIANCE`。

## 10. Review Checklist（审查清单）

- 是否调用 `prompts/valuation/analysis.md`。
- 是否引用 `docs/methodology/valuation.md`。
- 是否把关键假设绑定 Evidence Card。
- 是否避免输出目标价格和交易指令。
- 是否包含反方情景、不确定性和免责声明。
