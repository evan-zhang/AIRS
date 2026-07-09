# Evidence Skill（证据管理）

## 1. Purpose（目的）

Evidence Skill 负责把研究命题、材料和下游 Skill 发现转化为 Evidence Card 与 Evidence Chain。它是 M3 Evidence Engine 的执行入口，不重新定义证据等级、证据字段或验证规则。

## 2. Inputs（输入）

- `claims`：待验证命题列表。
- `raw_materials`：财报、公告、新闻、研究报告或用户资料摘要。
- `methodology_refs`：相关 M2 方法论路径。
- `prompt_refs`：相关 M4 Prompt 路径。
- `existing_evidence_chain_ids`：可选的既有证据链。

## 3. Outputs（输出）

- Evidence Card 列表。
- Evidence Chain 摘要。
- `supports`、`refutes`、`missing_evidence` 映射。
- 证据质量与置信度摘要。
- 证据不足或冲突时的失败状态。

## 4. Dependencies（依赖，包括引用的 Prompt/Methodology/Evidence）

- Prompt：`prompts/evidence/evidence-chain.md`、`prompts/evidence/counter-consensus.md`。
- Methodology：`docs/methodology/evidence-chain.md`、`docs/methodology/counter-consensus.md`。
- Evidence：`docs/evidence/evidence-card-specification.md`、`docs/evidence/evidence-validation-workflow.md`、`schemas/evidence/evidence-card.schema.json`、`schemas/evidence/evidence-chain.schema.json`。

## 5. Invoked Prompt（调用的 Prompt，引用 M4 Prompt Library）

调用：

- `prompts/evidence/evidence-chain.md`：构建 Evidence Chain。
- `prompts/evidence/counter-consensus.md`：生成反方证据需求。

不复制 Prompt 内容，只传入命题、材料和输出 Schema 约束。

## 6. Invoked Methodology（调用的方法论，引用 M2）

引用：

- `docs/methodology/evidence-chain.md`
- `docs/methodology/counter-consensus.md`

证据链结构和反方证据强度以 M2 文档为准。

## 7. Invoked Evidence（调用的 Evidence Engine 组件，引用 M3）

Evidence Skill 直接使用 M3 Evidence Card / Evidence Chain：

- Evidence Card 必含 `evidence_id`、`source`、`confidence`、`evidence_level`、`supports`、`refutes`、`missing_evidence`、`traceability`。
- Evidence Chain 必须绑定命题、证据关系和整体置信度。

## 8. Workflow（工作流程）

1. 接收研究命题并分配 claim_id。
2. 将原始材料抽取为候选 Evidence Card。
3. 按 M3 验证流程检查来源、时间、口径和可追溯性。
4. 构建 supports/refutes/missing_evidence 关系。
5. 输出 Evidence Chain，并标注未满足证据。

## 9. Failure Handling（失效处理）

- 材料无来源：返回 `FAIL_SOURCE_MISSING`。
- 证据无法支持命题：放入 `missing_evidence`。
- 证据相互冲突：标注冲突关系并降低置信度。
- 输出缺少必需字段：返回 `FAIL_SCHEMA_INVALID`。

## 10. Review Checklist（审查清单）

- Evidence Card 是否包含 M3 必需字段。
- Evidence Chain 是否绑定研究命题。
- 是否保留反方证据和缺失证据。
- 是否没有重新定义 Evidence Level。
- 是否包含不构成投资建议的免责声明。

