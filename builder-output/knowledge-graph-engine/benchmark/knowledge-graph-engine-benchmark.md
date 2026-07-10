# FEATURE-002 Benchmark 草案 - Knowledge Graph Engine

**Benchmark 模板引用**：`templates/benchmark-template.md`  
**Benchmark Engine 引用**：`docs/benchmark/benchmark-architecture.md`、`docs/benchmark/benchmark-lifecycle.md`、`docs/benchmark/benchmark-governance.md`  

## 1. Benchmark Intent

验证 Knowledge Graph Engine 的输出是否符合 Feature Spec、M3 Evidence、M4 Prompt、M6 Score / Evaluation 与 M7 Benchmark 质量要求。

## 2. Input

- Research Agent 将 AI 算力供应链拆解为节点、关系和证据绑定，并输出路径分析与卡脖子分析。
- Research Agent 将创新药产业链拆解为研发、临床、生产、准入和商业化链路，并标注关键约束。
- Review Agent 按图谱 Schema 检查 Evidence 引用、反方证据、缺失证据和合规免责声明。

## 3. Expected Output

- builder-output/knowledge-graph-engine/ 标准 Feature Package
- docs/knowledge-graph/ 知识图谱设计与工作流文档
- knowledge_graph/ 最小可运行 Python 实现
- schemas/knowledge-graph/knowledge-graph.schema.json
- templates/knowledge-graph/ 图谱与分析模板
- examples/knowledge-graph/ 两个生产示例
- scripts/validate_knowledge_graph.py

## 4. Evaluation Criteria

- Evidence 引用完整。
- Prompt 输出结构符合 M4。
- Skill 编排符合 M5。
- 质量门禁引用 M6。
- Benchmark 格式引用 M7。
- 不输出投资建议、交易指令、目标价或收益承诺。

## 5. Failure Cases

- 缺少 Evidence Chain。
- 缺少反方观点。
- 缺少不确定性。
- 缺少免责声明。
- 重复定义 M2-M7 规则而不是引用。

## 6. 免责声明

本生成物仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

