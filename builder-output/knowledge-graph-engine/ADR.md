# ADR - Knowledge Graph Engine Feature Package

**状态**：Proposed  
**日期**：2026-07-10  
**Feature**：FEATURE-KG-001  

## 背景

AIRS V1.0 已具备方法论、证据、Prompt、Skill、Score、Evaluation 和 Benchmark 规范，但研究对象之间的结构关系仍主要散落在报告文本和 Evidence Chain 中。Knowledge Graph Engine 作为 Feature Package，先定义可交付的工程边界，再由 Code Agent 后续实现。

## 决策

采用 Builder 生成的独立 Feature Package 承载 Knowledge Graph Engine。图谱层只表达实体关系和证据追溯，不重新定义证据等级、评分公式或方法论流程。

## 备选方案

- 直接修改 Evidence Engine：会扩大 M3 已验收内容变更范围，不适合作为首选。
- 在 Report Layer 中嵌入关系表：难以被 Skill 和 Benchmark 复用。
- 新增独立 Feature Package：能保持 M1-M8 稳定，并提供后续实现入口。

## 影响

- Code Agent 可基于 `schema/knowledge-graph.schema.json` 实现图谱结构。
- Review Agent 可检查节点、边、Evidence ID、反方证据是否完整。
- Verification Agent 可通过 Benchmark 验证输出质量。

## 风险

- 图谱结构可能被误用为投资因果结论，因此必须保留置信度、不确定性和反方边。
- 如果后续实现运行时，需要新增 ADR 说明存储、查询和可视化方案。

## 免责声明

本 ADR 仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

