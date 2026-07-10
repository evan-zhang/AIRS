# Autonomous Investment Committee Prompt 草案

**Feature**：FEATURE-010  
**Prompt 模板引用**：`templates/prompt-template.md`  
**Prompt Engine 引用**：`docs/prompt-engine/prompt-architecture.md`、`docs/prompt-engine/prompt-dsl.md`、`docs/prompt-engine/prompt-governance.md`  

## 1. Prompt Purpose

本 Prompt 草案用于支持 Autonomous Investment Committee 的研究流程输入输出约束。它必须遵循 M4 Prompt Engine，并引用 M2 Methodology 与 M3 Evidence Engine。

## 2. System Prompt Draft

你是 AIRS 研究流程中的 Prompt 执行组件。请围绕 Feature `FEATURE-010` 的目标处理输入，必须引用上游方法论和证据链，不得输出投资建议、交易指令、目标价或收益承诺。

## 3. User Template

```text
Feature ID：FEATURE-010
Feature Name：Autonomous Investment Committee
研究问题：建立 AIRS Autonomous Investment Committee，作为 Planner 之后、Research Engine 之前的多角色审议门禁，对研究计划和投资结论进行交叉验证、反方质疑、证据复核、共识构建和最终表决。
业务目标：确保任何投资研究结论在进入 Research Engine 深度执行或最终报告前，必须经过 Committee 多角色讨论、证据挑战、反方观点和投票记录，形成可审计的决策链。
用户场景：[
  "Planner 生成 Research Plan 后，AIC 先审查研究范围、方法论、证据预期和风险预算，再决定是否允许进入 Research Engine。",
  "Research Agent 产生阶段性结论时，AIC 组织 Bull、Bear、Financial、Industry、Risk、Portfolio、Evidence Reviewer 和 Devil's Advocate 交叉质询。",
  "Review Agent 和 Verification Agent 根据 AIC 的 Vote、Minority Report 和 Decision Record 复核质量门禁。"
]
依赖：[
  "docs/planner/planner-architecture.md",
  "docs/runtime/runtime-architecture.md",
  "docs/orchestrator/orchestrator-architecture.md",
  "docs/investment-engine/engine-architecture.md",
  "schemas/planner/research-plan.schema.json",
  "schemas/evidence/evidence-chain.schema.json",
  "schemas/score/scorecard.schema.json",
  "schemas/investment/recommendation.schema.json",
  "templates/report/research-report-template.md"
]
约束：[
  "AIC 位于 Planner 之后、Research Engine 之前。",
  "AIC 只负责审议、复核、表决和记录，不直接联网采集数据，不替代 Evidence、Score、KG、Runtime 或 Report 模块。",
  "所有 Committee 产物必须包含免责声明，不得输出荐股、自动交易、交易指令、目标价或收益承诺。"
]
输出要求：[
  "docs/committee/ 12 个 Committee 架构与治理文档",
  "committee/ 11 个 Python 核心组件和 README",
  "committee/examples/ 6 个生产级 Committee 示例",
  "schemas/committee/ 4 个 JSON Schema",
  "templates/committee/ Committee 模板",
  "scripts/validate_committee.py",
  "docs/adr/ADR-0010-autonomous-investment-committee.md",
  "docs/production/M10_COMPLETION_REPORT.md",
  "docs/review/M10_SELF_REVIEW.md"
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

