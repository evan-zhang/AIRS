# Supply Chain Skill（供应链分析）

## 1. Purpose（目的）

Supply Chain Skill 用于分析产业链结构、关键环节、卡点、替代路径和供需约束。它调用 M4 供应链卡点 Prompt，并引用 M2 供应链卡脖子方法论与 M3 Evidence Card 规范。它不输出交易动作或价格预测。

## 2. Inputs（输入）

- `industry_or_product`：行业、产品或技术链条。
- `scope`：地区、时间范围、上下游边界。
- `target_claims`：待验证的供应链命题。
- `evidence_context`：已有 Evidence Card 或 Evidence Chain。
- `output_granularity`：环节级、公司级或材料级。

## 3. Outputs（输出）

- 供应链分层图谱描述。
- 关键卡点候选列表。
- 每个卡点的 Evidence Card 需求和证据链摘要。
- 替代路径、反方观点和不确定性。
- 合规免责声明。

## 4. Dependencies（依赖，包括引用的 Prompt/Methodology/Evidence）

- Prompt：`prompts/supply-chain/chokepoint-analysis.md`。
- Methodology：`docs/methodology/supply-chain-chokepoint.md`。
- Evidence：`docs/evidence/evidence-card-specification.md`、`docs/evidence/evidence-level-standard.md`、`schemas/evidence/evidence-card.schema.json`。

## 5. Invoked Prompt（调用的 Prompt，引用 M4 Prompt Library）

调用 `prompts/supply-chain/chokepoint-analysis.md`。Skill 只提供研究对象、时间范围、证据上下文和输出约束，不复制 Prompt 正文。

## 6. Invoked Methodology（调用的方法论，引用 M2）

引用 `docs/methodology/supply-chain-chokepoint.md`。分析维度、Required Evidence、Counter Evidence 和 Confidence 规则均以该文档为准，Skill 只执行编排。

## 7. Invoked Evidence（调用的 Evidence Engine 组件，引用 M3）

输出必须使用 M3 Evidence Card 字段：`supports` 绑定卡点命题，`refutes` 记录替代供应或供给改善证据，`missing_evidence` 记录未验证环节，`traceability` 保留来源路径。

## 8. Workflow（工作流程）

1. 明确产业链边界和分析层级。
2. 调用 M4 供应链 Prompt 生成卡点候选。
3. 按 M2 方法论识别供给集中、替代难度、扩产周期和认证壁垒。
4. 调用 Evidence Skill 或 Evidence Engine 生成 Evidence Card 需求。
5. 输出卡点排序、反方证据和不确定性。

## 9. Failure Handling（失效处理）

- 产业边界不清：返回补充范围要求。
- 上下游数据不足：标注 `missing_evidence`。
- 只存在传闻证据：输出 PARTIAL，不给确定结论。
- 用户要求交易动作：返回 `FAIL_COMPLIANCE`。

## 10. Review Checklist（审查清单）

- 是否调用 `prompts/supply-chain/chokepoint-analysis.md`。
- 是否引用 `docs/methodology/supply-chain-chokepoint.md`。
- 是否输出支持证据、反方证据和缺失证据。
- 是否避免把卡点分析写成投资结论。
- 是否包含免责声明。

