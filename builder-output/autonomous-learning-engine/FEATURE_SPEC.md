# FEATURE-012 Feature Spec - Autonomous Learning Engine

## 1. Feature 摘要

建立 AIRS Autonomous Learning Engine，从历史研究、Committee、Memory、Report 与 Outcome 中提取反馈、挖掘模式、生成规则并提出 Prompt、Methodology、Skill 与 Score 优化建议。

## 2. Business Goal

让 AIRS 在不输出荐股、不自动交易、不预测价格的前提下，形成可审计、可回滚、可评审的研究质量闭环，持续提升证据充分性、反方观点强度、评分校准和报告一致性。

## 3. Scope

### In Scope

- docs/learning/ 11 个 Learning 架构、反馈、Outcome、模式、规则、优化和治理文档
- learning/ 12 个 Python 核心组件、README 和 6 个学习示例
- schemas/learning/ 4 个 JSON Schema
- scripts/validate_learning.py
- docs/adr/ADR-012-autonomous-learning-engine.md
- docs/production/FEATURE_012_COMPLETION_REPORT.md
- docs/review/FEATURE_012_SELF_REVIEW.md

### Out of Scope

- 自动交易或下单执行。
- 个性化投资建议。
- 目标价、收益承诺或确定性价格预测。
- 重写 M2-M7 已有规范。

## 4. User Scenarios

- Research Agent 完成报告后，Learning Engine 汇总 Report、Evidence、Score、Committee 与实际 Outcome 的偏差，生成改进建议。
- Review Agent 发现证据缺口、逻辑跳跃或反方观点薄弱时，Learning Engine 将问题沉淀为 Pattern 与 Rule Candidate。
- Verification Agent 运行 Benchmark 后，Learning Engine 分析失败样本，提出 Prompt、Methodology、Skill 和 Score 权重优化方案。

## 5. Dependencies

- docs/runtime/memory-manager.md
- docs/orchestrator/orchestrator-architecture.md
- docs/investment-engine/engine-architecture.md
- docs/committee/committee-architecture.md
- schemas/evidence/evidence-chain.schema.json
- schemas/score/scorecard.schema.json
- schemas/report/report.schema.json
- schemas/committee/committee-decision.schema.json

## 6. Constraints

- Learning Engine 只生成质量改进建议，不直接修改生产 Prompt、Methodology、Skill 或 Score 权重。
- 所有学习建议必须保留来源、证据、置信度、适用范围、回滚策略和人工评审状态。
- 所有产物必须包含免责声明，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

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

`HIGH`

## 10. Disclaimer

本生成物仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

