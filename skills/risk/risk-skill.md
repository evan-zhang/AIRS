# Risk Skill（风险分析）

## 1. Purpose（目的）

Risk Skill 用于识别研究结论中的数据风险、方法风险、产业风险、财务风险、政策风险、估值风险和认知偏差。它调用 M4 风险 Prompt，引用 M2 风险方法论，并把风险证据写入 M3 Evidence Chain。

## 2. Inputs（输入）

- `research_findings`：其他 Skill 输出的研究发现。
- `evidence_chain`：Evidence Card 与 Evidence Chain 摘要。
- `methodology_refs`：已使用 M2 方法论路径。
- `scope`：研究对象、时间和地区范围。
- `risk_focus`：可选风险重点。

## 3. Outputs（输出）

- 风险清单和风险等级。
- 反方观点和证据绑定。
- 缺失证据与高不确定性字段。
- 对报告措辞的限制建议。
- 合规免责声明。

## 4. Dependencies（依赖，包括引用的 Prompt/Methodology/Evidence）

- Prompt：`prompts/risk/analysis.md`、`prompts/evidence/counter-consensus.md`。
- Methodology：`docs/methodology/risk.md`、`docs/methodology/counter-consensus.md`。
- Evidence：`docs/evidence/evidence-review-standard.md`、`schemas/evidence/evidence-card.schema.json`。

## 5. Invoked Prompt（调用的 Prompt，引用 M4 Prompt Library）

调用：

- `prompts/risk/analysis.md`
- `prompts/evidence/counter-consensus.md`

Skill 不内置风险分析 Prompt，只引用 M4 生产版 Prompt。

## 6. Invoked Methodology（调用的方法论，引用 M2）

引用：

- `docs/methodology/risk.md`
- `docs/methodology/counter-consensus.md`

风险分类、Counter Evidence 和 Confidence 规则以 M2 文档为准。

## 7. Invoked Evidence（调用的 Evidence Engine 组件，引用 M3）

每个风险必须绑定支持证据或缺失证据。支持风险命题的材料写入 Evidence Card 的 `supports`，反方观点应写入 `refutes`，无法验证的风险写入 `missing_evidence`，并保留 `traceability`。

## 8. Workflow（工作流程）

1. 接收研究发现和证据链。
2. 调用风险 Prompt 识别主要风险。
3. 调用反共识 Prompt 生成反方观点。
4. 将风险和反方观点绑定 Evidence Card。
5. 输出风险矩阵和报告措辞约束。

## 9. Failure Handling（失效处理）

- 没有 Evidence Chain：返回 `FAIL_EVIDENCE_CHAIN_MISSING`。
- 反方证据不足：返回 PARTIAL 并列出补采方向。
- 研究结论过度确定：返回合规修正建议。
- 用户要求风险结论转化为交易动作：返回 `FAIL_COMPLIANCE`。

## 10. Review Checklist（审查清单）

- 是否调用 M4 风险与反共识 Prompt。
- 是否引用 M2 风险和反共识方法论。
- 是否把风险绑定 Evidence Card。
- 是否保留反方观点和缺失证据。
- 是否避免投资建议化表述。
