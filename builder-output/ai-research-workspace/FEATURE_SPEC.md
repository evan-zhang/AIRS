# FEATURE-007 Feature Spec - AI Research Workspace

## 1. Feature 摘要

建立统一 Research Workspace，作为 Runtime、Workflow、Agent、Evidence、Knowledge Graph、Report 和用户交互的唯一入口。

## 2. Business Goal

让 AIRS 的研究过程以项目、会话、任务、证据、产物、快照和审计记录统一管理，提升可追踪、可复核和可恢复能力。

## 3. Scope

### In Scope

- docs/workspace/ Workspace 架构与治理文档
- workspace/ 最小可运行 Python Workspace
- workspace/examples/ 五个 Workspace 示例和 Dashboard
- schemas/workspace/ Workspace Schema
- scripts/validate_workspace.py
- ADR-0007-ai-research-workspace.md
- M7_COMPLETION_REPORT.md

### Out of Scope

- 自动交易或下单执行。
- 个性化投资建议。
- 目标价、收益承诺或确定性价格预测。
- 重写 M2-M7 已有规范。

## 4. User Scenarios

- 用户通过 Workspace 创建研究项目并启动 Runtime 会话。
- Research Agent 在 Workspace 中登记任务、证据引用、图谱引用和报告产物。
- Review Agent 通过 Timeline、Snapshot、Audit Log 和 Artifact Registry 复核研究过程。
- Verification Agent 使用 Workspace Export 重放关键研究流程并检查合规边界。

## 5. Dependencies

- docs/runtime/runtime-architecture.md
- runtime/core.py
- schemas/runtime/runtime.schema.json
- schemas/evidence/evidence-card.schema.json
- schemas/knowledge-graph/knowledge-graph.schema.json
- templates/report/research-report-template.md

## 6. Constraints

- Workspace 是统一入口，但不绕过 Runtime 调度 Agent。
- Workspace 只保存引用、状态、产物、快照和审计记录，不生成投资建议。
- 所有投资研究相关内容必须包含免责声明。

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

