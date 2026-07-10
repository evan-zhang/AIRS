# FEATURE-010 - Autonomous Investment Committee

## 1. 背景

建立 AIRS Autonomous Investment Committee，作为 Planner 之后、Research Engine 之前的多角色审议门禁，对研究计划和投资结论进行交叉验证、反方质疑、证据复核、共识构建和最终表决。

## 2. 业务目标

确保任何投资研究结论在进入 Research Engine 深度执行或最终报告前，必须经过 Committee 多角色讨论、证据挑战、反方观点和投票记录，形成可审计的决策链。

## 3. 用户场景

- Planner 生成 Research Plan 后，AIC 先审查研究范围、方法论、证据预期和风险预算，再决定是否允许进入 Research Engine。
- Research Agent 产生阶段性结论时，AIC 组织 Bull、Bear、Financial、Industry、Risk、Portfolio、Evidence Reviewer 和 Devil's Advocate 交叉质询。
- Review Agent 和 Verification Agent 根据 AIC 的 Vote、Minority Report 和 Decision Record 复核质量门禁。

## 4. 依赖

- docs/planner/planner-architecture.md
- docs/runtime/runtime-architecture.md
- docs/orchestrator/orchestrator-architecture.md
- docs/investment-engine/engine-architecture.md
- schemas/planner/research-plan.schema.json
- schemas/evidence/evidence-chain.schema.json
- schemas/score/scorecard.schema.json
- schemas/investment/recommendation.schema.json
- templates/report/research-report-template.md

## 5. 约束

- AIC 位于 Planner 之后、Research Engine 之前。
- AIC 只负责审议、复核、表决和记录，不直接联网采集数据，不替代 Evidence、Score、KG、Runtime 或 Report 模块。
- 所有 Committee 产物必须包含免责声明，不得输出荐股、自动交易、交易指令、目标价或收益承诺。

## 6. 期望输出

- docs/committee/ 12 个 Committee 架构与治理文档
- committee/ 11 个 Python 核心组件和 README
- committee/examples/ 6 个生产级 Committee 示例
- schemas/committee/ 4 个 JSON Schema
- templates/committee/ Committee 模板
- scripts/validate_committee.py
- docs/adr/ADR-0010-autonomous-investment-committee.md
- docs/production/M10_COMPLETION_REPORT.md
- docs/review/M10_SELF_REVIEW.md

## 7. 验收标准

- Feature Package 必须包含 Issue、ADR、Feature Spec、Skill、Prompt、Schema、Tests、Benchmark、PR Checklist、Release Notes。
- Skill 草案必须引用 `templates/skill-template.md` 与 M5 Skill Engine。
- Prompt 草案必须引用 `templates/prompt-template.md` 与 M4 Prompt Engine。
- Benchmark 草案必须引用 `templates/benchmark-template.md` 与 M7 Benchmark。
- 所有投资研究相关内容必须包含免责声明。

## 8. 风险等级

`HIGH`

## 9. 免责声明

本生成物仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

