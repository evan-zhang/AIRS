# ADR - FEATURE-003 Research Report Generator

**状态**：Proposed  
**日期**：2026-07-10  
**Feature**：FEATURE-003  

## 1. 背景

生成统一结构的 AIRS 投资研究报告，自动汇总 Methodology、Evidence、Knowledge Graph、Prompt、Skill、Score 和 Evaluation 输出。

## 2. 决策

为该 Feature 生成独立 Feature Package，并将开发入口、架构决策、规格、Skill、Prompt、Schema、测试、Benchmark、PR Checklist 和 Release Notes 放在 `builder-output/research-report-generator/`。

## 3. 依赖引用

- M1 项目结构与生产治理
- M2 Methodology Layer
- M3 Evidence Engine
- FEATURE-002 Knowledge Graph Engine
- M4 Prompt Engine
- M5 Skill Engine
- M6 Score/Evaluation Engine

## 4. 约束

- 不得输出荐股、自动交易、交易指令、目标价或收益承诺。
- 所有报告必须包含免责声明。
- 报告核心结论必须引用 Evidence Card、KG Summary 和 Scorecard。
- 必须保留反方观点、缺失证据与不确定性。

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

