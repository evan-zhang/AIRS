# Autonomous Learning Engine Skill 草案

**Feature**：FEATURE-012  
**Skill 模板引用**：`templates/skill-template.md`  
**Skill Engine 引用**：`docs/skill-engine/skill-architecture.md`、`docs/skill-engine/skill-invocation.md`、`docs/skill-engine/skill-governance.md`  

## 1. Purpose

本 Skill 草案用于实现 Autonomous Learning Engine 的开发入口。它必须遵循 M5 Skill Engine，并引用既有 M2 Methodology、M3 Evidence、M4 Prompt 和 M6/M7 质量资产。

## 2. Inputs

- `feature_request`：结构化 Feature 请求。
- `research_context`：可选研究上下文。
- `evidence_refs`：M3 Evidence Card / Evidence Chain 引用。
- `constraints`：[
  "Learning Engine 只生成质量改进建议，不直接修改生产 Prompt、Methodology、Skill 或 Score 权重。",
  "所有学习建议必须保留来源、证据、置信度、适用范围、回滚策略和人工评审状态。",
  "所有产物必须包含免责声明，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。"
]

## 3. Outputs

- docs/learning/ 11 个 Learning 架构、反馈、Outcome、模式、规则、优化和治理文档
- learning/ 12 个 Python 核心组件、README 和 6 个学习示例
- schemas/learning/ 4 个 JSON Schema
- scripts/validate_learning.py
- docs/adr/ADR-012-autonomous-learning-engine.md
- docs/production/FEATURE_012_COMPLETION_REPORT.md
- docs/review/FEATURE_012_SELF_REVIEW.md

## 4. Dependencies

- docs/runtime/memory-manager.md
- docs/orchestrator/orchestrator-architecture.md
- docs/investment-engine/engine-architecture.md
- docs/committee/committee-architecture.md
- schemas/evidence/evidence-chain.schema.json
- schemas/score/scorecard.schema.json
- schemas/report/report.schema.json
- schemas/committee/committee-decision.schema.json

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

