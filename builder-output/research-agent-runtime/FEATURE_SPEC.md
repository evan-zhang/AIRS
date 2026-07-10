# FEATURE-006 Feature Spec - Research Agent Runtime

## 1. Feature 摘要

建立统一 Agent Runtime，将 Orchestrator 的流程编排升级为可运行的多 Agent 执行框架。

## 2. Business Goal

让 AIRS Workflow 由 Runtime 统一调度，形成可追踪、可暂停、可恢复、可验证的多 Agent 研究执行底座。

## 3. Scope

### In Scope

- docs/runtime/ Runtime 架构文档
- runtime/ 最小可运行 Python Runtime
- runtime/examples/ 五个 Runtime 示例
- schemas/runtime/ Runtime Schema
- templates/runtime/ Runtime 模板
- scripts/validate_runtime.py
- FEATURE_006_COMPLETION_REPORT.md

### Out of Scope

- 自动交易或下单执行。
- 个性化投资建议。
- 目标价、收益承诺或确定性价格预测。
- 重写 M2-M7 已有规范。

## 4. User Scenarios

- Code Agent 可以基于 Runtime Core 开发新的研究执行流。
- Research Agent 可以在 Runtime Session 中执行公司、行业、热点、供应链和报告生成任务。
- Review Agent 可以通过 Event Log、Context Snapshot 和 Final State 复核执行过程。

## 5. Dependencies

- docs/skill-engine/skill-architecture.md
- docs/methodology/DSL.md
- docs/evidence/evidence-architecture.md
- schemas/README.md

## 6. Constraints

- Workflow 必须由 Runtime 调度执行，不允许 Workflow 直接驱动业务模块。
- Runtime 只编排 Agent、Session、Task、Message、Event 和 State，不重复定义 M2-M7 规则。
- 所有投资相关内容必须包含免责声明。

## 7. Functional Requirements

- 生成物必须可被 Code Agent 读取和执行。
- Schema 必须是合法 JSON Schema。
- Tests 必须描述可复现的验收步骤。
- Benchmark 必须引用 M7 Benchmark 模板和 M6 质量门禁。
- Skill、Prompt、Benchmark 必须引用 AIRS 既有层，不复制底层规则。

## 8. Acceptance Criteria

- `python3 scripts/validate_builder.py` 返回 PASS。
- 回归验证脚本保持 PASS。
- Release Notes 记录 Feature 影响和限制。
- 所有生成物包含免责声明。

## 9. Risk Level

`MEDIUM`

## 10. Disclaimer

本生成物仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

