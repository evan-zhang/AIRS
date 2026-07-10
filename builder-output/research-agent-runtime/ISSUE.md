# FEATURE-006 - Research Agent Runtime

## 1. 背景

建立统一 Agent Runtime，将 Orchestrator 的流程编排升级为可运行的多 Agent 执行框架。

## 2. 业务目标

让 AIRS Workflow 由 Runtime 统一调度，形成可追踪、可暂停、可恢复、可验证的多 Agent 研究执行底座。

## 3. 用户场景

- Code Agent 可以基于 Runtime Core 开发新的研究执行流。
- Research Agent 可以在 Runtime Session 中执行公司、行业、热点、供应链和报告生成任务。
- Review Agent 可以通过 Event Log、Context Snapshot 和 Final State 复核执行过程。

## 4. 依赖

- docs/skill-engine/skill-architecture.md
- docs/methodology/DSL.md
- docs/evidence/evidence-architecture.md
- schemas/README.md

## 5. 约束

- Workflow 必须由 Runtime 调度执行，不允许 Workflow 直接驱动业务模块。
- Runtime 只编排 Agent、Session、Task、Message、Event 和 State，不重复定义 M2-M7 规则。
- 所有投资相关内容必须包含免责声明。

## 6. 期望输出

- docs/runtime/ Runtime 架构文档
- runtime/ 最小可运行 Python Runtime
- runtime/examples/ 五个 Runtime 示例
- schemas/runtime/ Runtime Schema
- templates/runtime/ Runtime 模板
- scripts/validate_runtime.py
- FEATURE_006_COMPLETION_REPORT.md

## 7. 验收标准

- Feature Package 必须包含 Issue、ADR、Feature Spec、Skill、Prompt、Schema、Tests、Benchmark、PR Checklist、Release Notes。
- Skill 草案必须引用 `templates/skill-template.md` 与 M5 Skill Engine。
- Prompt 草案必须引用 `templates/prompt-template.md` 与 M4 Prompt Engine。
- Benchmark 草案必须引用 `templates/benchmark-template.md` 与 M7 Benchmark。
- 所有投资研究相关内容必须包含免责声明。

## 8. 风险等级

`MEDIUM`

## 9. 免责声明

本生成物仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

