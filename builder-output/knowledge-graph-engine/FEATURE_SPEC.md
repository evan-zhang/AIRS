# FEATURE-002 Feature Spec - Knowledge Graph Engine

## 1. Feature 摘要

为 AIRS 研究流程提供实体、关系、Evidence 绑定、路径分析和供应链卡脖子分析的最小可运行知识图谱引擎。

## 2. Business Goal

把 M2 Methodology 与 M3 Evidence Engine 的研究结果结构化为可验证图谱，支持 Research、Review 与 Verification Agent 复用证据链、反方证据和不确定性。

## 3. Scope

### In Scope

- builder-output/knowledge-graph-engine/ 标准 Feature Package
- docs/knowledge-graph/ 知识图谱设计与工作流文档
- knowledge_graph/ 最小可运行 Python 实现
- schemas/knowledge-graph/knowledge-graph.schema.json
- templates/knowledge-graph/ 图谱与分析模板
- examples/knowledge-graph/ 两个生产示例
- scripts/validate_knowledge_graph.py

### Out of Scope

- 自动交易或下单执行。
- 个性化投资建议。
- 目标价、收益承诺或确定性价格预测。
- 重写 M2-M7 已有规范。

## 4. User Scenarios

- Research Agent 将 AI 算力供应链拆解为节点、关系和证据绑定，并输出路径分析与卡脖子分析。
- Research Agent 将创新药产业链拆解为研发、临床、生产、准入和商业化链路，并标注关键约束。
- Review Agent 按图谱 Schema 检查 Evidence 引用、反方证据、缺失证据和合规免责声明。

## 5. Dependencies

- docs/methodology/supply-chain-chokepoint.md
- docs/evidence/evidence-card-specification.md
- schemas/evidence/evidence-card.schema.json
- templates/skill-template.md
- templates/prompt-template.md
- templates/benchmark-template.md

## 6. Constraints

- 不得生成荐股内容、自动交易功能、交易指令、目标价或收益承诺。
- 必须绑定 M3 Evidence Card，并兼容 M2 Methodology Layer。
- 节点和关系类型必须受控，分析结果必须记录反方证据、缺失证据和不确定性。

## 7. Functional Requirements

- 生成物必须可被 Code Agent 读取和执行。
- Schema 必须是合法 JSON Schema。
- Tests 必须描述可复现的验收步骤。
- Benchmark 必须引用 M7 Benchmark 模板和 M6 质量门禁。
- Skill、Prompt、Benchmark 必须引用 AIRS 既有层，不复制底层规则。

## 8. Acceptance Criteria

- `python3 scripts/validate_builder.py` 返回 PASS。
- 回归验证脚本保持 PASS。
- Release Notes 记录 Feature 影响和限制。
- 所有生成物包含免责声明。

## 9. Risk Level

`MEDIUM`

## 10. Disclaimer

本生成物仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

