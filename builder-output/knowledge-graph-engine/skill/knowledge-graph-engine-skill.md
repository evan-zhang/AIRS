# Knowledge Graph Engine Skill 草案

**Feature**：FEATURE-002  
**Skill 模板引用**：`templates/skill-template.md`  
**Skill Engine 引用**：`docs/skill-engine/skill-architecture.md`、`docs/skill-engine/skill-invocation.md`、`docs/skill-engine/skill-governance.md`  

## 1. Purpose

本 Skill 草案用于实现 Knowledge Graph Engine 的开发入口。它必须遵循 M5 Skill Engine，并引用既有 M2 Methodology、M3 Evidence、M4 Prompt 和 M6/M7 质量资产。

## 2. Inputs

- `feature_request`：结构化 Feature 请求。
- `research_context`：可选研究上下文。
- `evidence_refs`：M3 Evidence Card / Evidence Chain 引用。
- `constraints`：[
  "不得生成荐股内容、自动交易功能、交易指令、目标价或收益承诺。",
  "必须绑定 M3 Evidence Card，并兼容 M2 Methodology Layer。",
  "节点和关系类型必须受控，分析结果必须记录反方证据、缺失证据和不确定性。"
]

## 3. Outputs

- builder-output/knowledge-graph-engine/ 标准 Feature Package
- docs/knowledge-graph/ 知识图谱设计与工作流文档
- knowledge_graph/ 最小可运行 Python 实现
- schemas/knowledge-graph/knowledge-graph.schema.json
- templates/knowledge-graph/ 图谱与分析模板
- examples/knowledge-graph/ 两个生产示例
- scripts/validate_knowledge_graph.py

## 4. Dependencies

- docs/methodology/supply-chain-chokepoint.md
- docs/evidence/evidence-card-specification.md
- schemas/evidence/evidence-card.schema.json
- templates/skill-template.md
- templates/prompt-template.md
- templates/benchmark-template.md

## 5. Workflow

1. 校验输入范围与合规边界。
2. 选择或确认上游 Methodology、Evidence 与 Prompt 引用。
3. 调用 M4 Prompt 草案，不内置 Prompt 正文。
4. 绑定 M3 Evidence Card / Evidence Chain。
5. 输出结构化结果、缺失证据、反方观点、不确定性和免责声明。

## 6. Failure Handling

- `FAIL_INPUT_INCOMPLETE`：Feature 或研究上下文字段不足。
- `FAIL_DEPENDENCY_MISSING`：声明依赖不存在或未被验证。
- `FAIL_EVIDENCE_INSUFFICIENT`：证据不足或不可追溯。
- `FAIL_COMPLIANCE`：请求触及荐股、交易指令、目标价或收益承诺。

## 7. Review Checklist

- [ ] 已引用 `templates/skill-template.md`。
- [ ] 已引用 M5 Skill Engine。
- [ ] 未重复定义 M2-M7 规则。
- [ ] 包含反方观点、不确定性和免责声明要求。

## 8. 免责声明

本生成物仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

