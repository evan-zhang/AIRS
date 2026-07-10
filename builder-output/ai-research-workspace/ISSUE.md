# FEATURE-007 - AI Research Workspace

## 1. 背景

建立统一 Research Workspace，作为 Runtime、Workflow、Agent、Evidence、Knowledge Graph、Report 和用户交互的唯一入口。

## 2. 业务目标

让 AIRS 的研究过程以项目、会话、任务、证据、产物、快照和审计记录统一管理，提升可追踪、可复核和可恢复能力。

## 3. 用户场景

- 用户通过 Workspace 创建研究项目并启动 Runtime 会话。
- Research Agent 在 Workspace 中登记任务、证据引用、图谱引用和报告产物。
- Review Agent 通过 Timeline、Snapshot、Audit Log 和 Artifact Registry 复核研究过程。
- Verification Agent 使用 Workspace Export 重放关键研究流程并检查合规边界。

## 4. 依赖

- docs/runtime/runtime-architecture.md
- runtime/core.py
- schemas/runtime/runtime.schema.json
- schemas/evidence/evidence-card.schema.json
- schemas/knowledge-graph/knowledge-graph.schema.json
- templates/report/research-report-template.md

## 5. 约束

- Workspace 是统一入口，但不绕过 Runtime 调度 Agent。
- Workspace 只保存引用、状态、产物、快照和审计记录，不生成投资建议。
- 所有投资研究相关内容必须包含免责声明。

## 6. 期望输出

- docs/workspace/ Workspace 架构与治理文档
- workspace/ 最小可运行 Python Workspace
- workspace/examples/ 五个 Workspace 示例和 Dashboard
- schemas/workspace/ Workspace Schema
- scripts/validate_workspace.py
- ADR-0007-ai-research-workspace.md
- M7_COMPLETION_REPORT.md

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

