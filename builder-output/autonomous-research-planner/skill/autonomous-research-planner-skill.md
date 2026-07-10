# Autonomous Research Planner Skill 草案

**Feature**：FEATURE-009  
**Skill 模板引用**：`templates/skill-template.md`  
**Skill Engine 引用**：`docs/skill-engine/skill-architecture.md`、`docs/skill-engine/skill-invocation.md`、`docs/skill-engine/skill-governance.md`  

## 1. Purpose

本 Skill 草案用于实现 Autonomous Research Planner 的开发入口。它必须遵循 M5 Skill Engine，并引用既有 M2 Methodology、M3 Evidence、M4 Prompt 和 M6/M7 质量资产。

## 2. Inputs

- `feature_request`：结构化 Feature 请求。
- `research_context`：可选研究上下文。
- `evidence_refs`：M3 Evidence Card / Evidence Chain 引用。
- `constraints`：[
  "Planner 是 AIRS 最上层入口，Runtime 不允许直接接收用户请求。",
  "Planner 只生成研究计划和执行链路，不执行外部数据采集，不生成荐股、交易指令、目标价或收益承诺。",
  "所有计划必须保留 Evidence、KG、Score、Report、Review 和 Verification 引用。"
]

## 3. Outputs

- docs/planner/ 12 个 Planner 架构与组件文档
- planner/ 12 个 Python 组件和 README
- planner/examples/ 8 个研究目标示例及 Markdown 文档
- schemas/planner/ 4 个 JSON Schema
- templates/planner/ Planner 模板
- scripts/validate_planner.py
- docs/adr/ADR-0009-autonomous-research-planner.md
- docs/production/FEATURE_009_COMPLETION_REPORT.md
- docs/review/FEATURE_009_SELF_REVIEW.md

## 4. Dependencies

- docs/orchestrator/orchestrator-architecture.md
- docs/runtime/runtime-architecture.md
- docs/investment-engine/engine-architecture.md
- schemas/runtime/runtime.schema.json
- schemas/investment/investment-request.schema.json
- schemas/evidence/evidence-chain.schema.json
- schemas/knowledge-graph/knowledge-graph.schema.json
- schemas/score/scorecard.schema.json
- templates/report/research-report-template.md

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

