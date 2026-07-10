# Portfolio Research Plan Example

免责声明：本文档仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## Goal Analysis

目标是分析 AI 主题组合暴露和风险复核计划，Planner 将其识别为 Portfolio Research。

## Scope

范围包含主题暴露、风险渠道、压力情景、证据缺口和报告输出。范围排除仓位动作和个性化投资建议。

## Required Connectors/Methodologies/Skills/Runtime

Connectors：portfolio_snapshot、company_filings、market_news。Methodologies：risk、valuation、counter-consensus。Skills：risk、valuation、verification、report。Runtime 只执行 Planner 生成的任务。

## Expected Evidence/KG

Evidence Plan 需要组合快照引用、公司披露、市场新闻和反方证据。KG 连接持仓暴露、主题、风险和证据。

## Execution Order

goal_analysis -> scope -> methodology_selection -> connector_plan -> evidence_plan -> skill_plan -> knowledge_graph_plan -> score_plan -> report_plan -> review_plan -> runtime_plan。

## Estimated Cost/Time

预计 81 分钟，成本单位约 23，最大并发 3。

## Expected Deliverables

组合研究计划、风险矩阵、压力情景、证据计划、报告提纲和复核清单。

## Confidence

置信度依赖组合数据完整性和主题映射质量。

## Risks

组合快照过期、主题映射误差、风险相关性估计不足、输出被误用为仓位动作。
