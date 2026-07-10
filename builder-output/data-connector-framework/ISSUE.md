# FEATURE-004 - Data Connector Framework

## 1. 背景

建立统一 Data Connector Framework，所有外部数据源必须通过 Connector 接入并输出可追溯结果。

## 2. 业务目标

为 AIRS Research、Evidence、Knowledge Graph 和 Report 提供统一、可治理、可审计的数据接入边界。

## 3. 用户场景

- Code Agent 读取 Feature Package 后可以直接开发。
- Review Agent 可以按 ADR、Spec、Tests 和 Benchmark 审查。

## 4. 依赖

- templates/skill-template.md
- templates/prompt-template.md
- templates/benchmark-template.md
- docs/evidence/evidence-card-specification.md

## 5. 约束

- 不得重复定义 M2-M7 规则，只能引用。
- 所有投资相关内容必须包含免责声明。

## 6. 期望输出

- ISSUE.md
- ADR.md
- FEATURE_SPEC.md
- Skill 草案
- Prompt 草案
- Schema 草案
- Tests
- Benchmark
- PR Checklist
- Release Notes

## 7. 验收标准

- Feature Package 必须包含 Issue、ADR、Feature Spec、Skill、Prompt、Schema、Tests、Benchmark、PR Checklist、Release Notes。
- Skill 草案必须引用 `templates/skill-template.md` 与 M5 Skill Engine。
- Prompt 草案必须引用 `templates/prompt-template.md` 与 M4 Prompt Engine。
- Benchmark 草案必须引用 `templates/benchmark-template.md` 与 M7 Benchmark。
- 所有投资研究相关内容必须包含免责声明。

## 8. 风险等级

`HIGH`

## 9. 免责声明

本生成物仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

