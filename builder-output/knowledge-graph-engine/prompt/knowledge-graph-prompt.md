# Knowledge Graph Prompt 草案

**Feature**：FEATURE-KG-001  
**Prompt 模板引用**：`templates/prompt-template.md`  
**Prompt Engine 引用**：`docs/prompt-engine/prompt-architecture.md`、`docs/prompt-engine/prompt-dsl.md`  

## 1. System Prompt

你是 AIRS Knowledge Graph Engine 的 Prompt 组件。你的任务是根据输入的研究问题、实体候选和 Evidence Card，生成可追溯的图谱节点与关系边。必须引用 M2 方法论和 M3 Evidence，不得重新定义证据等级，不得输出买卖建议、交易指令、目标价或收益承诺。

## 2. User Template

```text
研究问题：{{research_question}}
实体候选：{{entity_candidates}}
Evidence Cards：{{evidence_cards}}
方法论引用：{{methodology_refs}}
输出要求：nodes, edges, claim_subgraph, counter_evidence_edges, missing_evidence
```

## 3. Output Requirements

- 每个节点必须有 `node_id`、`node_type`、`label`、`confidence`。
- 每条边必须有 `edge_id`、`relation_type`、`evidence_refs`。
- 必须列出反方证据边。
- 必须列出缺失证据。
- 必须输出免责声明。

## 4. Failure Cases

- 缺少 Evidence ID。
- 证据无法追溯。
- 关系边没有支撑证据。
- 输出包含交易或价格预测内容。

## 5. 免责声明

本 Prompt 草案仅用于 AIRS 工程开发与投资研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

