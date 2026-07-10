# FEATURE-008 - Investment Research Engine

## 1. 背景

构建统一 Investment Research Engine，调度 Runtime、Skill、Prompt、Evidence、Knowledge Graph、Score、Report 和 Workspace，形成可执行投资研究全流程。

## 2. 业务目标

把 M1-M7 与 M8 基础设施串联成可复核、可验证、可审计的研究引擎，支持主题、公司、行业、供应链、风险、催化剂和报告生成。

## 3. 用户场景

- Research Agent 接收研究意图后，由 Engine 统一生成研究计划、证据链、图谱、评分卡和报告。
- Review Agent 使用 Facts、Inference、Assumption、Opinion 标注检查研究结论来源类型。
- Verification Agent 运行 Engine 示例和自检脚本，确认不输出确定性投资建议或收益承诺。

## 4. 依赖

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

## 5. 约束

- Engine 只编排既有底层服务，不绕过 Runtime、Workspace 或 Evidence 规则。
- Recommendation 必须区分 Facts、Inference、Assumption 和 Opinion。
- 不得输出确定性投资建议、交易指令、目标价或收益承诺。

## 6. 期望输出

- docs/investment-engine/ Engine 架构、管线、创意生成和推荐标准文档
- investment_engine/ 最小可运行 Python 研究引擎
- investment_engine/examples/ 五个研究案例
- schemas/investment/ 投资研究请求、命题和推荐 Schema
- templates/investment/ 报告与命题模板
- scripts/validate_investment_engine.py
- ADR-0008-investment-research-engine.md
- FEATURE_008_COMPLETION_REPORT.md

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

