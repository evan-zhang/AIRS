# Autonomous Investment Committee Skill 草案

**Feature**：FEATURE-010  
**Skill 模板引用**：`templates/skill-template.md`  
**Skill Engine 引用**：`docs/skill-engine/skill-architecture.md`、`docs/skill-engine/skill-invocation.md`、`docs/skill-engine/skill-governance.md`  

## 1. Purpose

本 Skill 草案用于实现 Autonomous Investment Committee 的开发入口。它必须遵循 M5 Skill Engine，并引用既有 M2 Methodology、M3 Evidence、M4 Prompt 和 M6/M7 质量资产。

## 2. Inputs

- `feature_request`：结构化 Feature 请求。
- `research_context`：可选研究上下文。
- `evidence_refs`：M3 Evidence Card / Evidence Chain 引用。
- `constraints`：[
  "AIC 位于 Planner 之后、Research Engine 之前。",
  "AIC 只负责审议、复核、表决和记录，不直接联网采集数据，不替代 Evidence、Score、KG、Runtime 或 Report 模块。",
  "所有 Committee 产物必须包含免责声明，不得输出荐股、自动交易、交易指令、目标价或收益承诺。"
]

## 3. Outputs

- docs/committee/ 12 个 Committee 架构与治理文档
- committee/ 11 个 Python 核心组件和 README
- committee/examples/ 6 个生产级 Committee 示例
- schemas/committee/ 4 个 JSON Schema
- templates/committee/ Committee 模板
- scripts/validate_committee.py
- docs/adr/ADR-0010-autonomous-investment-committee.md
- docs/production/M10_COMPLETION_REPORT.md
- docs/review/M10_SELF_REVIEW.md

## 4. Dependencies

- docs/planner/planner-architecture.md
- docs/runtime/runtime-architecture.md
- docs/orchestrator/orchestrator-architecture.md
- docs/investment-engine/engine-architecture.md
- schemas/planner/research-plan.schema.json
- schemas/evidence/evidence-chain.schema.json
- schemas/score/scorecard.schema.json
- schemas/investment/recommendation.schema.json
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

