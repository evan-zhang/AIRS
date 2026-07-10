# Research Report Generator Pipeline 说明

**Feature**：FEATURE-003 Research Report Generator  
**版本**：v0.1.0  

**免责声明**：本文档仅用于 AIRS 工程开发、Pipeline 验证和研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## 1. Payload Schema 摘要

Pipeline payload 至少包含：

```json
{
  "report_id": "REPORT-20260710-AI-COMPUTE",
  "title": "AI 算力产业研究报告",
  "research_question": "AI 算力产业链中哪些环节需要重点验证？",
  "methodology_refs": ["supply-chain-chokepoint", "counter-consensus"],
  "evidence_cards": {},
  "knowledge_graph": {},
  "scorecard": {}
}
```

`schemas/report/report.schema.json` 给出结构化报告 artifact 的约束。Markdown 模板位于 `templates/report/research-report-template.md`。

## 2. 输入一致性规则

- `methodology_refs` 不能为空，并且应与 Knowledge Graph、Scorecard 的方法论引用保持一致。
- `evidence_cards` 至少包含两个 Evidence Card。
- Knowledge Graph 中的 Evidence Card 必须存在于报告 Evidence Card 集合。
- Scorecard 的 `evidence_chain_refs` 必须存在于报告 Evidence Card 集合。
- Scorecard 的免责声明必须为 `仅供研究参考，不构成投资建议`。
- Report 层免责声明必须包含 `不构成投资建议`。

## 3. 输出一致性规则

- Markdown 报告必须包含 12 个核心章节。
- 核心观点章节必须同时引用 Evidence、KG 和 Scorecard。
- Evidence 引用表必须列出证据等级、来源类型、权重、支持命题和反方限制。
- KG Summary 必须列出 KG ID、节点数量、关系数量、路径数量和 Top Chokepoint。
- Score Summary 必须列出 Scorecard ID、Overall Score、Confidence Score 和 Quality Gate。
- 反方观点、不确定性、风险提示和免责声明不得为空。

## 4. 与 M1-M6/FEATURE-002 的兼容方式

Pipeline 使用引用而不是复制规则：

- M2 Methodology：在报告中展示引用，不重新定义方法论。
- M3 Evidence：只读取 Evidence Card 字段并生成引用表。
- FEATURE-002 Knowledge Graph：只读取图谱摘要、路径和卡点结果。
- M4 Prompt：通过 `prompt_ref` 记录生成 Prompt。
- M5 Skill：通过 `skill_ref` 记录报告 Skill。
- M6 Score/Evaluation：只展示 Scorecard 与 Quality Gate，不调整分数。

## 5. 当前边界

当前实现是本地内存 Pipeline，不接入外部数据库，不执行联网检索，不执行自然语言大模型生成。示例报告用于工程验收和结构演示，不能作为投资决策依据。

