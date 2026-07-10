# FEATURE-KG-001 - Knowledge Graph Engine

## 背景

Knowledge Graph Engine 用于把 AIRS 研究过程中的公司、行业、产品、供应链节点、政策事件、证据卡和研究命题组织成可追溯的关系网络。它不替代 M2 方法论和 M3 Evidence Engine，而是在工程层提供结构化关系建模入口，帮助 Research Agent 与 Review Agent 检查证据链是否存在断点、循环引用或孤立节点。

## 业务目标

- 将 Evidence Card 与研究对象之间的关系显式化。
- 支持供应链卡点、主题扩散、政策驱动、估值和风险分析等方法论的关系查询。
- 为后续 Knowledge Graph runtime 或可视化能力提供 Feature Package。

## 用户场景

- Code Agent 需要实现图谱数据结构时，可直接读取本 Package。
- Research Agent 需要说明某个结论由哪些实体和证据支撑。
- Review Agent 需要检查证据链是否跨层引用完整。
- Verification Agent 需要通过 Benchmark 验证图谱输出不丢失反方证据。

## 依赖

- M2 Methodology：`docs/methodology/evidence-chain.md`、`docs/methodology/supply-chain-chokepoint.md`、`docs/methodology/policy-driven.md`
- M3 Evidence：`docs/evidence/evidence-card-specification.md`、`schemas/evidence/evidence-card.schema.json`
- M4 Prompt：`templates/prompt-template.md`
- M5 Skill：`templates/skill-template.md`
- M6 Score / Evaluation：`schemas/score/scorecard.schema.json`、`evaluation/quality-gate.md`
- M7 Benchmark：`templates/benchmark-template.md`

## 期望输出

- 图谱节点与边 Schema 草案。
- Knowledge Graph Skill 草案。
- Knowledge Graph Prompt 草案。
- 测试计划与 Benchmark。
- PR Checklist 与 Release Notes。

## 验收标准

- 包含 10 个标准 Builder artifact。
- Schema 文件可以被 JSON 解析。
- Skill、Prompt、Benchmark 均引用 M5、M4、M7 既有模板。
- 输出包含反方证据、缺失证据和不确定性字段。

## 免责声明

本示例仅用于 AIRS 工程开发与投资研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

