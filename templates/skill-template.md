# AIRS Skill 模板

## Skill 元数据

- **Skill ID**：`airs.skill.[name].v1`
- **Skill 名称**：[中文名 / English Name]
- **Skill 版本**：v1.0.0
- **状态**：Draft / Review / Active
- **归属 Milestone**：M5 Skill Engine
- **免责声明**：仅供研究参考，不构成投资建议。投资有风险，决策需谨慎。

## 1. Purpose（目的）

[说明 Skill 负责解决的研究流程问题、适用范围和不适用范围。明确 Skill 只做编排和执行，不内置 Prompt，不替代 M2 方法论或 M3 Evidence Engine。]

## 2. Inputs（输入）

- `research_question`：[研究问题]
- `scope`：[行业、公司、时间、地区等边界]
- `context_refs`：[Prompt、Methodology、Evidence Chain 等上下文引用]
- `constraints`：[输出格式、数据源偏好、语言等约束]

## 3. Outputs（输出）

- [结构化研究发现或执行计划]
- [使用的 Prompt、Methodology、Evidence 引用清单]
- [Evidence Card / Evidence Chain 摘要]
- [失败状态、缺失证据、不确定性和免责声明]

## 4. Dependencies（依赖，包括引用的 Prompt/Methodology/Evidence）

- **Prompt**：`prompts/[category]/[prompt].md`
- **Methodology**：`docs/methodology/[methodology].md`
- **Evidence**：`docs/evidence/evidence-card-specification.md`、`schemas/evidence/evidence-card.schema.json`
- **Skill Engine**：`docs/skill-engine/skill-invocation.md`

## 5. Invoked Prompt（调用的 Prompt，引用 M4 Prompt Library）

[列出实际调用的 M4 Prompt 路径。禁止复制 System Prompt、User Template 或其他 Prompt 正文。Skill 只能传入变量和上下文。]

## 6. Invoked Methodology（调用的方法论，引用 M2）

[列出实际引用的 M2 方法论文档路径。禁止重新定义 Theory、Workflow、Required Evidence、Counter Evidence 或 Confidence 规则。]

## 7. Invoked Evidence（调用的 Evidence Engine 组件，引用 M3）

[列出使用的 M3 Evidence Engine 文档和 Schema。必须说明 Evidence Card 字段如何用于 supports、refutes、missing_evidence、traceability 和 confidence。]

## 8. Workflow（工作流程）

1. [校验输入和研究范围]
2. [选择或确认 Prompt / Methodology / Evidence 引用]
3. [调用 M4 Prompt Engine]
4. [绑定 M3 Evidence Card / Evidence Chain]
5. [输出结果、失败状态和免责声明]

## 9. Failure Handling（失效处理）

- `FAIL_INPUT_INCOMPLETE`：[输入不完整时如何返回]
- `FAIL_PROMPT_UNAVAILABLE`：[Prompt 不存在或不可用时如何返回]
- `FAIL_METHODOLOGY_MISMATCH`：[方法论不匹配时如何返回]
- `FAIL_EVIDENCE_INSUFFICIENT`：[证据不足时如何返回]
- `FAIL_COMPLIANCE`：[用户要求交易动作、价格预测或收益承诺时如何返回]

## 10. Review Checklist（审查清单）

- 是否引用真实存在的 M4 Prompt。
- 是否引用真实存在的 M2 Methodology。
- 是否使用 M3 Evidence Card / Evidence Chain。
- 是否避免内置 Prompt 和重复定义规则。
- 是否包含反方观点、缺失证据、不确定性和免责声明。

