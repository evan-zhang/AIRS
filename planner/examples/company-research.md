# Company Research Plan Example

免责声明：本文档仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## Goal Analysis

目标是为 AI 服务器供应链公司生成研究计划。Planner 先识别为 Company Research，再要求公司公告、行业报告和新闻证据进入 Evidence Plan。

## Scope

研究范围包含公司角色、供应链位置、财务异常、管理层质量、估值口径和风险复核。范围排除交易动作、确定性收益判断和未追溯来源的结论。

## Required Connectors/Methodologies/Skills/Runtime

Connectors：company_filings、market_news、industry_report。Methodologies：financial-anomaly、management-quality、valuation、risk。Skills：financial、valuation、risk、report。Runtime 必须由 Planner 生成，且 `raw_user_request_allowed=false`。

## Expected Evidence/KG

至少四张 Evidence Card，包含支持证据、反方证据、缺失证据和来源追溯。KG 需要表达公司、供应链节点、证据、风险和报告产物之间的关系。

## Execution Order

goal_analysis -> scope -> methodology_selection -> connector_plan -> evidence_plan -> skill_plan -> knowledge_graph_plan -> score_plan -> report_plan -> review_plan -> runtime_plan。

## Estimated Cost/Time

预计 83 分钟，成本单位约 25，最大并发 3。预算用于调度约束，不代表研究价值。

## Expected Deliverables

Research Plan、Runtime Plan、Workflow Spec、Evidence Plan、Knowledge Graph Plan、Scorecard Plan、Final Report Outline、Review Checklist。

## Confidence

计划置信度预计为中高。主要不确定性来自公告时效性、行业报告口径和反方证据覆盖。

## Risks

证据不足、公司披露不完整、行业对比口径不一致、Runtime 绕过 Planner 的集成风险。
