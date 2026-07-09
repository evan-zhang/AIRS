# News Skill（新闻事件分析）

## 1. Purpose（目的）

News Skill 用于分析新闻、公告、政策事件或市场叙事对研究命题的影响。当前 M4 未单独提供 news Prompt，因此本 Skill 通过 `prompts/hot-topic/theme-expansion.md` 与 `prompts/evidence/evidence-chain.md` 执行事件拆解和证据链构建。

## 2. Inputs（输入）

- `event_or_topic`：新闻事件、公告、政策或主题。
- `time_window`：事件发生和影响观察窗口。
- `affected_entities`：行业、公司或供应链环节。
- `source_materials`：新闻链接、公告摘要或政策文本摘要。
- `research_claims`：待验证命题。

## 3. Outputs（输出）

- 事件事实摘要。
- 影响路径和受影响对象。
- 支持证据、反方证据和缺失证据。
- 事件不确定性和时效性风险。
- 下游 Skill 调用建议。

## 4. Dependencies（依赖，包括引用的 Prompt/Methodology/Evidence）

- Prompt：`prompts/hot-topic/theme-expansion.md`、`prompts/evidence/evidence-chain.md`。
- Methodology：`docs/methodology/theme-expansion.md`、`docs/methodology/policy-driven.md`、`docs/methodology/evidence-chain.md`。
- Evidence：`docs/evidence/evidence-validation-workflow.md`、`schemas/evidence/evidence-card.schema.json`。

## 5. Invoked Prompt（调用的 Prompt，引用 M4 Prompt Library）

调用：

- `prompts/hot-topic/theme-expansion.md`：识别事件扩散路径。
- `prompts/evidence/evidence-chain.md`：将新闻材料转为 Evidence Chain。

不在 Skill 内编写新闻分析 Prompt。

## 6. Invoked Methodology（调用的方法论，引用 M2）

引用：

- `docs/methodology/theme-expansion.md`
- `docs/methodology/policy-driven.md`
- `docs/methodology/evidence-chain.md`

政策或监管事件优先使用 Policy Driven Analysis。

## 7. Invoked Evidence（调用的 Evidence Engine 组件，引用 M3）

新闻证据必须按 Evidence Card 保存来源、发布时间、采集时间、source_type 和 `traceability`。事件命题成立的事实写入 `supports`，相反报道、澄清公告或口径冲突写入 `refutes`；缺少官方材料时必须写入 `missing_evidence`。

## 8. Workflow（工作流程）

1. 识别事件事实和时间线。
2. 调用主题扩散 Prompt 生成影响路径。
3. 调用 Evidence Chain Prompt 绑定证据。
4. 标注消息来源等级、反方报道和缺失官方证据。
5. 输出事件研究摘要和下游分析建议。

## 9. Failure Handling（失效处理）

- 新闻来源不明：返回 `FAIL_SOURCE_MISSING`。
- 只有单一媒体来源：返回 PARTIAL。
- 事件尚未发生或无法验证：标注高不确定性。
- 用户要求短期价格判断：返回 `FAIL_COMPLIANCE`。

## 10. Review Checklist（审查清单）

- 是否使用 M4 现有 Prompt 组合。
- 是否引用 M2 主题扩散、政策驱动或证据链方法论。
- 是否按 M3 记录新闻来源和时间。
- 是否区分事实、推断和不确定性。
- 是否包含免责声明。
