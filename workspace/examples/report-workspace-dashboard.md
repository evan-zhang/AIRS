# 报告生成 Workspace Dashboard

## Project

- Research Question: 汇总证据、评分、反方观点和不确定性生成研究报告。
- Scope: structured-report。

## Sessions

- Runtime Workflow: report-workflow。

## Task Board

- Report Agent 生成报告草稿。
- Review Agent 复核 Evidence、Scorecard、反方观点和免责声明。

## Artifacts

- research_report: `schemas/report/report.schema.json`

## Timeline

Timeline 记录报告草稿创建、Artifact 发布、Snapshot 创建和 Review 节点，帮助 Review Agent 还原报告生成过程。

## Version

Version Manager 记录报告版本和 change_summary，禁止覆盖旧版本。

## Replay

最终 Snapshot 生成 Replay Plan，供 Verification Agent 做质量验证。

免责声明：本文档和示例仅用于 AIRS 工程开发、投资研究流程编排与质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。
