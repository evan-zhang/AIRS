# Investment Research Engine Skill 草案

**Feature**：FEATURE-008  
**Skill 模板引用**：`templates/skill-template.md`  
**Skill Engine 引用**：`docs/skill-engine/skill-architecture.md`、`docs/skill-engine/skill-invocation.md`、`docs/skill-engine/skill-governance.md`  

## 1. Purpose

本 Skill 草案用于实现 Investment Research Engine 的开发入口。它必须遵循 M5 Skill Engine，并引用既有 M2 Methodology、M3 Evidence、M4 Prompt 和 M6/M7 质量资产。

## 2. Inputs

- `feature_request`：结构化 Feature 请求。
- `research_context`：可选研究上下文。
- `evidence_refs`：M3 Evidence Card / Evidence Chain 引用。
- `constraints`：[
  "Engine 只编排既有底层服务，不绕过 Runtime、Workspace 或 Evidence 规则。",
  "Recommendation 必须区分 Facts、Inference、Assumption 和 Opinion。",
  "不得输出确定性投资建议、交易指令、目标价或收益承诺。"
]

## 3. Outputs

- docs/investment-engine/ Engine 架构、管线、创意生成和推荐标准文档
- investment_engine/ 最小可运行 Python 研究引擎
- investment_engine/examples/ 五个研究案例
- schemas/investment/ 投资研究请求、命题和推荐 Schema
- templates/investment/ 报告与命题模板
- scripts/validate_investment_engine.py
- ADR-0008-investment-research-engine.md
- FEATURE_008_COMPLETION_REPORT.md

## 4. Dependencies

- docs/runtime/runtime-architecture.md
- docs/orchestrator/
- docs/workspace/workspace-architecture.md
- docs/data-connectors/connector-interface.md
- docs/methodology/
- docs/evidence/
- docs/prompt-engine/
- schemas/evidence/evidence-card.schema.json
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

