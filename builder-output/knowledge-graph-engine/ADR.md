# ADR - FEATURE-002 Knowledge Graph Engine

**状态**：Proposed  
**日期**：2026-07-10  
**Feature**：FEATURE-002  

## 1. 背景

为 AIRS 研究流程提供实体、关系、Evidence 绑定、路径分析和供应链卡脖子分析的最小可运行知识图谱引擎。

## 2. 决策

为该 Feature 生成独立 Feature Package，并将开发入口、架构决策、规格、Skill、Prompt、Schema、测试、Benchmark、PR Checklist 和 Release Notes 放在 `builder-output/knowledge-graph-engine/`。

## 3. 依赖引用

- docs/methodology/supply-chain-chokepoint.md
- docs/evidence/evidence-card-specification.md
- schemas/evidence/evidence-card.schema.json
- templates/skill-template.md
- templates/prompt-template.md
- templates/benchmark-template.md

## 4. 约束

- 不得生成荐股内容、自动交易功能、交易指令、目标价或收益承诺。
- 必须绑定 M3 Evidence Card，并兼容 M2 Methodology Layer。
- 节点和关系类型必须受控，分析结果必须记录反方证据、缺失证据和不确定性。

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

