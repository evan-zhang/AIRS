# Master Skill（总调度）

## 1. Purpose（目的）

Master Skill 是 Skill Engine 的统一入口，负责接收研究意图、选择合适的生产版 Skill、传递统一调用上下文，并确保所有下游 Skill 调用 M4 Prompt Engine、M2 Methodology 和 M3 Evidence Engine。它不直接生成投资结论，不内置 Prompt，不替代证据审查。

本 Skill 适用于产业、公司、事件、供应链、财务、估值、风险和报告生成等投资研究流程。任何输出均仅供研究参考，不构成投资建议。

## 2. Inputs（输入）

- `research_question`：清晰的研究问题。
- `scope`：行业、公司、地区、时间范围和研究边界。
- `task_type`：供应链、热点、财务、新闻、估值、风险、报告或验证。
- `constraints`：数据源偏好、报告详细程度、语言和时限。
- `context_refs`：可选的 Evidence Chain ID、历史报告 ID 或用户补充材料。

若输入缺少研究对象或时间范围，Master Skill 必须先返回补充需求，不得生成完整研究结论。

## 3. Outputs（输出）

- Skill 调度计划：包含待调用 Skill、顺序、并行关系和回退策略。
- 依赖清单：包含 Prompt、Methodology、Evidence Engine 引用。
- 执行状态：PASS、PARTIAL 或 FAIL。
- 下游调用上下文：统一的 `request_id`、研究范围、证据需求和合规要求。
- 免责声明：说明 AIRS 不构成投资建议。

## 4. Dependencies（依赖，包括引用的 Prompt/Methodology/Evidence）

- Prompt Engine：`prompts/report/generation.md`、`prompts/evidence/evidence-chain.md` 用于最终报告和证据链整合。
- Methodology：按任务选择 `docs/methodology/*.md`，至少引用一个 M2 方法论。
- Evidence Engine：`docs/evidence/evidence-card-specification.md`、`docs/evidence/evidence-validation-workflow.md`、`schemas/evidence/evidence-card.schema.json`。
- Skill Engine：`docs/skill-engine/skill-invocation.md`、`docs/skill-engine/skill-composition.md`。

## 5. Invoked Prompt（调用的 Prompt，引用 M4 Prompt Library）

Master Skill 只引用 M4 Prompt 路径，不复制 Prompt 正文：

- `prompts/evidence/evidence-chain.md`：用于将多 Skill 发现汇总为 Evidence Chain。
- `prompts/report/generation.md`：用于最终结构化报告生成。
- 根据研究类型选择 `prompts/supply-chain/chokepoint-analysis.md`、`prompts/hot-topic/theme-expansion.md`、`prompts/financial/anomaly-analysis.md`、`prompts/valuation/analysis.md` 或 `prompts/risk/analysis.md`。

## 6. Invoked Methodology（调用的方法论，引用 M2）

Master Skill 使用 M2 方法论做路由依据：

- `docs/methodology/supply-chain-chokepoint.md`
- `docs/methodology/theme-expansion.md`
- `docs/methodology/evidence-chain.md`
- `docs/methodology/financial-anomaly.md`
- `docs/methodology/valuation.md`
- `docs/methodology/risk.md`

它只选择和引用方法论，不重写 Theory、Required Evidence 或 Confidence 规则。

## 7. Invoked Evidence（调用的 Evidence Engine 组件，引用 M3）

Master Skill 要求下游输出符合 M3：

- Evidence Card 字段：`supports`、`refutes`、`missing_evidence`、`traceability`、`confidence`、`evidence_level`。
- Evidence Chain：绑定研究命题、证据卡、反方证据和缺失证据。
- Evidence Validation Workflow：证据不足时返回失败或 PARTIAL。

## 8. Workflow（工作流程）

1. 解析研究问题和范围，生成 `request_id`。
2. 按任务类型匹配生产版 Skill 和 M2 方法论。
3. 为每个 Skill 注入 M4 Prompt 路径和 M3 Evidence 要求。
4. 并行或串行调用 Domain Skill。
5. 调用 Evidence Skill 汇总 Evidence Card 与 Evidence Chain。
6. 调用 Report Skill 生成结构化报告。
7. 调用 Verification Skill 检查引用、结构、合规和失败状态。

## 9. Failure Handling（失效处理）

- 输入不完整：返回 `FAIL_INPUT_INCOMPLETE` 和需要补充的字段。
- 未找到合适 Skill：返回 `FAIL_SKILL_UNAVAILABLE`。
- Prompt 缺失：返回 `FAIL_PROMPT_UNAVAILABLE`。
- 证据不足：返回 `PARTIAL` 并列出 `missing_evidence`。
- 合规风险：返回 `FAIL_COMPLIANCE`，拒绝交易指令或收益承诺。

## 10. Review Checklist（审查清单）

- 是否选择了真实存在的 M4 Prompt。
- 是否引用了真实存在的 M2 Methodology。
- 是否要求下游使用 M3 Evidence Card 和 Evidence Chain。
- 是否避免内置 Prompt 和重复定义规则。
- 是否保留反方观点、缺失证据、不确定性和免责声明。

