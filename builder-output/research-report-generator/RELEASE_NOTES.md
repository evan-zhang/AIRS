# FEATURE-003 Release Notes - Research Report Generator

## 1. Summary

生成统一结构的 AIRS 投资研究报告，自动汇总 Methodology、Evidence、Knowledge Graph、Prompt、Skill、Score 和 Evaluation 输出。

## 2. Added

- docs/report-generator/ 架构、流程和 Pipeline 文档
- report_generator/ Python 核心实现
- schemas/report/ 报告 Schema
- templates/report/ 12 核心章节报告模板
- examples/reports/ 两个生产示例
- scripts/validate_report_generator.py 专项验收脚本

## 3. Changed

- 默认不修改 AIRS M1-M8 已验收内容。
- 如后续实现需要修改历史内容，必须新增 ADR 并更新仓库 CHANGELOG。

## 4. Validation

- `scripts/validate_builder.py`
- M1-M8 回归验证脚本。

## 5. Known Limits

- Builder 生成物仍需 Code Agent 和 Review Agent 审查。
- Builder 不接入真实行情，不执行投资研究，不生成投资结论。

## 6. 免责声明

本生成物仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

