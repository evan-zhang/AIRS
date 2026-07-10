# FEATURE-KG-001 Feature Spec - Knowledge Graph Engine

## 1. Feature 摘要

Knowledge Graph Engine 为 AIRS 研究流程提供实体、关系、证据和命题的结构化表达。它面向后续运行时实现，当前 Package 只定义开发规格、Schema、Skill、Prompt、测试与 Benchmark。

## 2. Scope

### In Scope

- 定义图谱节点：company、industry、product、supply_chain_node、policy、event、evidence、claim、risk。
- 定义图谱边：supports、refutes、depends_on、belongs_to、affected_by、competes_with、has_risk。
- 定义 Evidence Card 与节点/边的绑定方式。
- 输出缺失证据、反方证据、不确定性和质量门禁字段。

### Out of Scope

- 图数据库选型。
- 实时数据抓取。
- 自动投资结论。
- 价格预测、交易建议或收益承诺。

## 3. Functional Requirements

- FR-1：每个节点必须有稳定 `node_id`、`node_type`、`label`、`source_refs` 和 `confidence`。
- FR-2：每条边必须有 `edge_id`、`from_node`、`to_node`、`relation_type`、`evidence_refs` 和 `directionality`。
- FR-3：图谱输出必须保留 `counter_evidence_refs` 与 `missing_evidence`。
- FR-4：Prompt 输出必须引用 M4 Prompt Engine，不内置新的 Prompt DSL。
- FR-5：Skill 编排必须引用 M5 Skill Engine，不重复定义 Skill 调度规则。
- FR-6：Benchmark 必须引用 M7 Benchmark 模板，验证证据链完整性。

## 4. Acceptance Criteria

- 10 个 Builder artifact 全部存在。
- `schema/knowledge-graph.schema.json` 是合法 JSON Schema。
- 测试计划覆盖正常图谱、缺失证据、反方证据和合规失败。
- Benchmark 包含 Gold Standard、Evaluation Criteria 和 Failure Cases。

## 5. 免责声明

本规格仅用于 AIRS 工程开发与投资研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

