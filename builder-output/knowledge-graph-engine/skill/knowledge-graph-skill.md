# Knowledge Graph Skill 草案

**Feature**：FEATURE-KG-001  
**Skill 模板引用**：`templates/skill-template.md`  
**Skill Engine 引用**：`docs/skill-engine/skill-architecture.md`、`docs/skill-engine/skill-invocation.md`、`docs/skill-engine/skill-governance.md`  

## 1. Purpose

Knowledge Graph Skill 负责把研究对象、证据卡、命题和风险转换为图谱结构。它只做编排，不重新定义 M2 方法论、M3 Evidence 规则或 M6 评分体系。

## 2. Inputs

- `research_question`：研究问题。
- `entity_candidates`：公司、行业、产品、政策、事件等实体候选。
- `evidence_cards`：符合 M3 Evidence Card 的证据集合。
- `claim_candidates`：待验证研究命题。
- `methodology_refs`：M2 方法论引用。

## 3. Outputs

- `nodes`：标准化节点。
- `edges`：带 Evidence ID 的关系边。
- `claim_subgraph`：围绕核心命题的子图。
- `counter_evidence_edges`：反方证据边。
- `missing_evidence`：缺失证据清单。
- `disclaimer`：合规免责声明。

## 4. Workflow

1. 校验输入是否包含 Evidence ID、Evidence Level、Confidence 和 Traceability。
2. 将实体候选归一化为节点。
3. 将 Evidence Card 的 supports/refutes 映射为关系边。
4. 识别没有证据支撑的孤立命题并写入 `missing_evidence`。
5. 输出图谱、反方证据、不确定性和免责声明。

## 5. Failure Handling

- `FAIL_EVIDENCE_MISSING`：没有可追溯 Evidence Card。
- `FAIL_ENTITY_AMBIGUOUS`：实体无法消歧。
- `FAIL_CLAIM_UNSUPPORTED`：核心命题缺少证据边。
- `FAIL_COMPLIANCE`：请求要求交易结论或价格预测。

## 6. Review Checklist

- [ ] 引用 M5 Skill 模板。
- [ ] 引用 M3 Evidence Card。
- [ ] 输出包含反方证据与缺失证据。
- [ ] 未输出投资建议或交易指令。

## 7. 免责声明

本 Skill 草案仅用于 AIRS 工程开发与投资研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

