# ADR - FEATURE-007 AI Research Workspace

**状态**：Proposed  
**日期**：2026-07-10  
**Feature**：FEATURE-007  

## 1. 背景

建立统一 Research Workspace，作为 Runtime、Workflow、Agent、Evidence、Knowledge Graph、Report 和用户交互的唯一入口。

## 2. 决策

为该 Feature 生成独立 Feature Package，并将开发入口、架构决策、规格、Skill、Prompt、Schema、测试、Benchmark、PR Checklist 和 Release Notes 放在 `builder-output/ai-research-workspace/`。

## 3. 依赖引用

- docs/runtime/runtime-architecture.md
- runtime/core.py
- schemas/runtime/runtime.schema.json
- schemas/evidence/evidence-card.schema.json
- schemas/knowledge-graph/knowledge-graph.schema.json
- templates/report/research-report-template.md

## 4. 约束

- Workspace 是统一入口，但不绕过 Runtime 调度 Agent。
- Workspace 只保存引用、状态、产物、快照和审计记录，不生成投资建议。
- 所有投资研究相关内容必须包含免责声明。

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

