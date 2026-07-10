# FEATURE-009 - Autonomous Research Planner

## 1. 背景

建立 AIRS 最上层 Autonomous Research Planner，把用户研究目标拆解为可执行 Research Plan，并生成 Runtime、Workflow、Methodology、Connector、Skill、KG、Evidence、Score、Report 的完整执行链路。

## 2. 业务目标

确保任何 Runtime 都不能直接接收用户请求，必须先经过 Planner 完成目标解析、范围约束、依赖规划、资源预算、置信度评估和执行计划生成。

## 3. 用户场景

- Research Agent 接收公司、行业、主题、供应链、卡点、政策、组合或对比研究目标后，Planner 先生成结构化 Research Plan。
- Runtime 只接收 Planner 输出的 Runtime Plan、Workflow Spec 和 Task Graph，不接收原始用户输入。
- Review Agent 和 Verification Agent 根据 Planner 产物复核目标拆解、证据链预期、成本预算、风险和合规边界。

## 4. 依赖

- docs/orchestrator/orchestrator-architecture.md
- docs/runtime/runtime-architecture.md
- docs/investment-engine/engine-architecture.md
- schemas/runtime/runtime.schema.json
- schemas/investment/investment-request.schema.json
- schemas/evidence/evidence-chain.schema.json
- schemas/knowledge-graph/knowledge-graph.schema.json
- schemas/score/scorecard.schema.json
- templates/report/research-report-template.md

## 5. 约束

- Planner 是 AIRS 最上层入口，Runtime 不允许直接接收用户请求。
- Planner 只生成研究计划和执行链路，不执行外部数据采集，不生成荐股、交易指令、目标价或收益承诺。
- 所有计划必须保留 Evidence、KG、Score、Report、Review 和 Verification 引用。

## 6. 期望输出

- docs/planner/ 12 个 Planner 架构与组件文档
- planner/ 12 个 Python 组件和 README
- planner/examples/ 8 个研究目标示例及 Markdown 文档
- schemas/planner/ 4 个 JSON Schema
- templates/planner/ Planner 模板
- scripts/validate_planner.py
- docs/adr/ADR-0009-autonomous-research-planner.md
- docs/production/FEATURE_009_COMPLETION_REPORT.md
- docs/review/FEATURE_009_SELF_REVIEW.md

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

