# Research Skill（研究入口）

## 1. Purpose（目的）

Research Skill 负责把用户研究意图转化为可执行研究计划，明确研究问题、研究范围、方法论选择、证据需求和下游 Skill 调用顺序。它是 Master Skill 与 Domain Skill 之间的计划层，不直接生成最终投资研究报告。

本 Skill 适用于热点主题、产业链、公司专题和事件影响研究。输出仅供研究流程使用，不构成投资建议。

## 2. Inputs（输入）

- `research_question`：用户提出的研究问题。
- `scope`：行业、公司、地区、时间范围。
- `research_depth`：简版、标准或深度。
- `preferred_methodology`：可选的 M2 方法论路径。
- `available_context`：已有 Evidence Chain、历史报告或用户资料。

## 3. Outputs（输出）

- 研究计划：研究命题、子问题和执行顺序。
- 方法论选择：一个或多个 M2 Methodology 路径。
- Prompt 调用计划：M4 Prompt 路径列表。
- Evidence 需求：Evidence Card 类型、关键字段和缺失证据预期。
- 失败或补充需求：无法启动时返回明确原因。

## 4. Dependencies（依赖，包括引用的 Prompt/Methodology/Evidence）

- Prompt：`prompts/hot-topic/theme-expansion.md`、`prompts/evidence/evidence-chain.md`。
- Methodology：`docs/methodology/theme-expansion.md`、`docs/methodology/evidence-chain.md`、必要时引用其他 M2 文档。
- Evidence：`docs/evidence/evidence-card-specification.md`、`schemas/evidence/evidence-chain.schema.json`。

## 5. Invoked Prompt（调用的 Prompt，引用 M4 Prompt Library）

Research Skill 使用：

- `prompts/hot-topic/theme-expansion.md`：拆解主题、扩散路径和研究命题。
- `prompts/evidence/evidence-chain.md`：把研究命题映射为 Evidence Chain 需求。

Skill 不复制上述 Prompt 的 System Prompt 或 User Template，只传入变量和上下文。

## 6. Invoked Methodology（调用的方法论，引用 M2）

默认引用：

- `docs/methodology/theme-expansion.md`
- `docs/methodology/evidence-chain.md`

如研究问题涉及供应链、财务、估值或风险，可追加引用对应 M2 方法论，但不重新定义方法论规则。

## 7. Invoked Evidence（调用的 Evidence Engine 组件，引用 M3）

Research Skill 只定义证据需求，不生成最终证据等级。证据需求必须对齐 M3 Evidence Card 字段，包括 `source_type`、`supports`、`refutes`、`missing_evidence`、`confidence` 和 `traceability`。

## 8. Workflow（工作流程）

1. 识别研究类型和研究边界。
2. 将大问题拆成 3-7 个可验证研究命题。
3. 为每个命题选择 M2 方法论。
4. 为每个命题指定 M4 Prompt 路径。
5. 为每个命题生成 Evidence Card 需求。
6. 输出下游 Skill 调用计划。

## 9. Failure Handling（失效处理）

- 问题过宽：返回需要缩小范围的字段。
- 研究对象不清：返回可接受的对象类型示例。
- 方法论无法匹配：返回 `FAIL_METHODOLOGY_MISMATCH`。
- 证据需求无法定义：返回 `FAIL_EVIDENCE_SCOPE_UNCLEAR`。

## 10. Review Checklist（审查清单）

- 研究问题是否被拆解为可验证命题。
- 是否引用 M4 Prompt，而非内置 Prompt。
- 是否引用至少一个 M2 方法论。
- Evidence 需求是否包含支持、反驳和缺失证据。
- 是否明确不构成投资建议。

