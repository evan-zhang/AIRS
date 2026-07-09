# Report Skill（报告生成）

## 1. Purpose（目的）

Report Skill 用于把研究计划、Domain Skill 输出、Evidence Chain、风险分析和反方观点整合成结构化研究报告。它调用 M4 报告生成 Prompt，引用 M2 Evidence Chain 方法论，并强制使用 M3 Evidence Card / Evidence Chain。

## 2. Inputs（输入）

- `research_plan`：Research Skill 输出的计划。
- `findings`：Domain Skill 输出。
- `evidence_chain`：Evidence Skill 输出。
- `risk_review`：Risk Skill 输出。
- `format_requirements`：报告长度、语言、章节要求。

## 3. Outputs（输出）

- 结构化 Markdown 研究报告。
- 使用的 Prompt、Methodology 和 Evidence 引用清单。
- 结论、证据链、评分或质量摘要。
- 反方观点、不确定性、风险提示和免责声明。
- 报告自检状态。

## 4. Dependencies（依赖，包括引用的 Prompt/Methodology/Evidence）

- Prompt：`prompts/report/generation.md`。
- Methodology：`docs/methodology/evidence-chain.md`，并继承上游 Skill 使用的方法论。
- Evidence：`schemas/evidence/evidence-chain.schema.json`、`docs/evidence/evidence-review-standard.md`。
- Template：`templates/report-template.md`。

## 5. Invoked Prompt（调用的 Prompt，引用 M4 Prompt Library）

调用 `prompts/report/generation.md`。Report Skill 不复制报告 Prompt，只将上游结果、Evidence Chain 和报告格式要求传入。

## 6. Invoked Methodology（调用的方法论，引用 M2）

主要引用 `docs/methodology/evidence-chain.md`，并在报告元数据中保留上游使用的 `docs/methodology/supply-chain-chokepoint.md`、`docs/methodology/financial-anomaly.md`、`docs/methodology/valuation.md` 或 `docs/methodology/risk.md`。

## 7. Invoked Evidence（调用的 Evidence Engine 组件，引用 M3）

报告中的每个核心结论必须绑定 Evidence Chain，并保留 Evidence Card 的 `supports`、`refutes`、`missing_evidence` 和 `traceability`。报告不得删除证据不足标注。

## 8. Workflow（工作流程）

1. 校验上游结果是否包含 Evidence Chain。
2. 调用报告生成 Prompt。
3. 按模板组织核心观点、方法、证据链、反方观点、风险和免责声明。
4. 将所有引用路径写入报告元数据。
5. 交给 Verification Skill 做最终检查。

## 9. Failure Handling（失效处理）

- 缺少 Evidence Chain：返回 `FAIL_EVIDENCE_CHAIN_MISSING`。
- 缺少免责声明：返回 `FAIL_COMPLIANCE`。
- 上游发现冲突：标注冲突并返回 PARTIAL。
- 报告章节不完整：返回修复清单。

## 10. Review Checklist（审查清单）

- 是否调用 `prompts/report/generation.md`。
- 是否保留所有 Prompt、Methodology、Evidence 引用。
- 是否包含反方观点、缺失证据和不确定性。
- 是否包含免责声明。
- 是否避免交易指令、收益承诺和价格预测。
