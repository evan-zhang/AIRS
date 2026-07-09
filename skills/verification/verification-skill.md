# Verification Skill（验证检查）

## 1. Purpose（目的）

Verification Skill 用于检查 Skill Engine 输出是否满足结构、依赖、一致性和合规要求。它面向系统验证与测试，不生成投资研究结论。

本 Skill 的验证结论仅用于工程质量控制，不构成投资建议。

## 2. Inputs（输入）

- `artifact_paths`：需要检查的 Skill、报告、Schema 或 Completion Report 路径。
- `execution_trace`：Skill 调用记录。
- `required_checks`：结构、Prompt、Methodology、Evidence、合规、自检结果。
- `baseline`：M1-M4 验收状态和 M5 要求。

## 3. Outputs（输出）

- PASS / FAIL 验证结论。
- 缺失文件、缺失 section 或引用不一致清单。
- Prompt、Methodology、Evidence 引用检查结果。
- 合规问题和修复建议。
- 自检脚本执行摘要。

## 4. Dependencies（依赖，包括引用的 Prompt/Methodology/Evidence）

- Prompt：`prompts/evidence/evidence-chain.md`、`prompts/report/generation.md` 用于验证证据链和报告结构。
- Methodology：`docs/methodology/evidence-chain.md`、`docs/methodology/risk.md`。
- Evidence：`docs/evidence/evidence-review-standard.md`、`docs/evidence/evidence-validation-workflow.md`、`schemas/evidence/evidence-card.schema.json`。
- Scripts：`scripts/validate_m1.py`、`scripts/validate_m2.py`、`scripts/validate_evidence.py`、`scripts/validate_prompt.py`、`scripts/validate_skill.py`。

## 5. Invoked Prompt（调用的 Prompt，引用 M4 Prompt Library）

Verification Skill 可引用 `prompts/evidence/evidence-chain.md` 检查证据链完整性，引用 `prompts/report/generation.md` 检查报告结构是否承接 M4 输出约束。它不内置验证 Prompt。

## 6. Invoked Methodology（调用的方法论，引用 M2）

引用 `docs/methodology/evidence-chain.md` 和 `docs/methodology/risk.md`，用于判断证据链、反方观点、不确定性和风险披露是否完整。

## 7. Invoked Evidence（调用的 Evidence Engine 组件，引用 M3）

验证时检查 Evidence Card 是否含 `supports`、`refutes`、`missing_evidence`、`traceability`，Evidence Chain 是否保留整体置信度与缺失证据，不重新定义证据等级。

## 8. Workflow（工作流程）

1. 读取待验证路径和执行记录。
2. 检查文件存在、section 完整、JSON Schema 合法。
3. 检查 Prompt、Methodology、Evidence 引用是否真实存在。
4. 检查是否存在内置 Prompt 或重复定义规则。
5. 执行自检脚本并输出 PASS/FAIL。

## 9. Failure Handling（失效处理）

- 文件缺失：返回 `FAIL_FILE_MISSING`。
- 引用不存在：返回 `FAIL_REFERENCE_INVALID`。
- Schema 非法：返回 `FAIL_SCHEMA_INVALID`。
- 合规缺失：返回 `FAIL_COMPLIANCE`。
- 自检脚本失败：返回失败脚本名称和修复方向。

## 10. Review Checklist（审查清单）

- 是否覆盖 M5 所有交付物。
- 是否逐项验证 M4 Prompt、M2 Methodology 和 M3 Evidence。
- 是否检查十个 Skill section。
- 是否运行全部自检脚本。
- 是否记录已知缺口和 M6 建议。
