# FEATURE-002 Release Notes - Knowledge Graph Engine

## 1. Summary

为 AIRS 研究流程提供实体、关系、Evidence 绑定、路径分析和供应链卡脖子分析的最小可运行知识图谱引擎。

## 2. Added

- builder-output/knowledge-graph-engine/ 标准 Feature Package
- docs/knowledge-graph/ 知识图谱设计与工作流文档
- knowledge_graph/ 最小可运行 Python 实现
- schemas/knowledge-graph/knowledge-graph.schema.json
- templates/knowledge-graph/ 图谱与分析模板
- examples/knowledge-graph/ 两个生产示例
- scripts/validate_knowledge_graph.py

## 3. Changed

- 默认不修改 AIRS M1-M8 已验收内容。
- 如后续实现需要修改历史内容，必须新增 ADR 并更新仓库 CHANGELOG。

## 4. Validation

- `scripts/validate_builder.py`
- M1-M8 回归验证脚本。

## 5. Known Limits

- Builder 生成物仍需 Code Agent 和 Review Agent 审查。
- Builder 不接入真实行情，不执行投资研究，不生成投资结论。

## 6. 免责声明

本生成物仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

