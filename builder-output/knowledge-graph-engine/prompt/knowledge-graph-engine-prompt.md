# Knowledge Graph Engine Prompt 草案

**Feature**：FEATURE-002  
**Prompt 模板引用**：`templates/prompt-template.md`  
**Prompt Engine 引用**：`docs/prompt-engine/prompt-architecture.md`、`docs/prompt-engine/prompt-dsl.md`、`docs/prompt-engine/prompt-governance.md`  

## 1. Prompt Purpose

本 Prompt 草案用于支持 Knowledge Graph Engine 的研究流程输入输出约束。它必须遵循 M4 Prompt Engine，并引用 M2 Methodology 与 M3 Evidence Engine。

## 2. System Prompt Draft

你是 AIRS 研究流程中的 Prompt 执行组件。请围绕 Feature `FEATURE-002` 的目标处理输入，必须引用上游方法论和证据链，不得输出投资建议、交易指令、目标价或收益承诺。

## 3. User Template

```text
Feature ID：FEATURE-002
Feature Name：Knowledge Graph Engine
研究问题：为 AIRS 研究流程提供实体、关系、Evidence 绑定、路径分析和供应链卡脖子分析的最小可运行知识图谱引擎。
业务目标：把 M2 Methodology 与 M3 Evidence Engine 的研究结果结构化为可验证图谱，支持 Research、Review 与 Verification Agent 复用证据链、反方证据和不确定性。
用户场景：[
  "Research Agent 将 AI 算力供应链拆解为节点、关系和证据绑定，并输出路径分析与卡脖子分析。",
  "Research Agent 将创新药产业链拆解为研发、临床、生产、准入和商业化链路，并标注关键约束。",
  "Review Agent 按图谱 Schema 检查 Evidence 引用、反方证据、缺失证据和合规免责声明。"
]
依赖：[
  "docs/methodology/supply-chain-chokepoint.md",
  "docs/evidence/evidence-card-specification.md",
  "schemas/evidence/evidence-card.schema.json",
  "templates/skill-template.md",
  "templates/prompt-template.md",
  "templates/benchmark-template.md"
]
约束：[
  "不得生成荐股内容、自动交易功能、交易指令、目标价或收益承诺。",
  "必须绑定 M3 Evidence Card，并兼容 M2 Methodology Layer。",
  "节点和关系类型必须受控，分析结果必须记录反方证据、缺失证据和不确定性。"
]
输出要求：[
  "builder-output/knowledge-graph-engine/ 标准 Feature Package",
  "docs/knowledge-graph/ 知识图谱设计与工作流文档",
  "knowledge_graph/ 最小可运行 Python 实现",
  "schemas/knowledge-graph/knowledge-graph.schema.json",
  "templates/knowledge-graph/ 图谱与分析模板",
  "examples/knowledge-graph/ 两个生产示例",
  "scripts/validate_knowledge_graph.py"
]
```

## 4. Input Schema

```json
{
  "feature_id": "string",
  "research_question": "string",
  "evidence_cards": "array",
  "methodology_refs": "array",
  "output_requirements": "array"
}
```

## 5. Output Schema

```json
{
  "summary": "string",
  "evidence_chain": {},
  "counter_arguments": [],
  "uncertainties": [],
  "failure_status": "string",
  "disclaimer": "string"
}
```

## 6. Review Checklist

- [ ] 已引用 `templates/prompt-template.md`。
- [ ] 已引用 M4 Prompt Engine。
- [ ] 已引用 M3 Evidence 要求。
- [ ] 输出包含反方观点、不确定性和免责声明。

## 7. 免责声明

本生成物仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

