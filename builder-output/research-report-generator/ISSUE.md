# FEATURE-003 - Research Report Generator

## 1. 背景

生成统一结构的 AIRS 投资研究报告，自动汇总 Methodology、Evidence、Knowledge Graph、Prompt、Skill、Score 和 Evaluation 输出。

## 2. 业务目标

把 M1-M6 和 FEATURE-002 的研究资产组合为可审查、可追溯、可验证且合规的标准研究报告。

## 3. 用户场景

- 研究人员输入研究主题、Evidence Cards、Knowledge Graph 和 Scorecard 后生成标准报告。
- Review Agent 可以按统一章节检查证据引用、反方观点、不确定性和免责声明。
- Verification Agent 可以通过脚本验证报告结构、引用完整性和质量门禁。

## 4. 依赖

- M1 项目结构与生产治理
- M2 Methodology Layer
- M3 Evidence Engine
- FEATURE-002 Knowledge Graph Engine
- M4 Prompt Engine
- M5 Skill Engine
- M6 Score/Evaluation Engine

## 5. 约束

- 不得输出荐股、自动交易、交易指令、目标价或收益承诺。
- 所有报告必须包含免责声明。
- 报告核心结论必须引用 Evidence Card、KG Summary 和 Scorecard。
- 必须保留反方观点、缺失证据与不确定性。

## 6. 期望输出

- docs/report-generator/ 架构、流程和 Pipeline 文档
- report_generator/ Python 核心实现
- schemas/report/ 报告 Schema
- templates/report/ 12 核心章节报告模板
- examples/reports/ 两个生产示例
- scripts/validate_report_generator.py 专项验收脚本

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

