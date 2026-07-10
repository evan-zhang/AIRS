# ADR - FEATURE-008 Investment Research Engine

**状态**：Proposed  
**日期**：2026-07-10  
**Feature**：FEATURE-008  

## 1. 背景

构建统一 Investment Research Engine，调度 Runtime、Skill、Prompt、Evidence、Knowledge Graph、Score、Report 和 Workspace，形成可执行投资研究全流程。

## 2. 决策

为该 Feature 生成独立 Feature Package，并将开发入口、架构决策、规格、Skill、Prompt、Schema、测试、Benchmark、PR Checklist 和 Release Notes 放在 `builder-output/investment-research-engine/`。

## 3. 依赖引用

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

## 4. 约束

- Engine 只编排既有底层服务，不绕过 Runtime、Workspace 或 Evidence 规则。
- Recommendation 必须区分 Facts、Inference、Assumption 和 Opinion。
- 不得输出确定性投资建议、交易指令、目标价或收益承诺。

## 5. 影响

- Code Agent 可以从 Package 直接进入开发。
- Review Agent 可以围绕 ADR、Spec、Tests 和 Benchmark 审查。
- Verification Agent 可以使用测试与 Benchmark 判断是否满足 Feature 目标。
- Builder 不改变 M2-M7 的既有规则，只生成引用这些规则的开发材料。

## 6. 后果

正向后果：

- Feature 开发输入标准化。
- 回归与发布材料前置。
- 合规边界在生成阶段显式化。

潜在代价：

- 模板需要随 AIRS 上游规范演进而维护。
- 生成包仍需人工审查，不应被视为自动通过。

## 7. 免责声明

本生成物仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

