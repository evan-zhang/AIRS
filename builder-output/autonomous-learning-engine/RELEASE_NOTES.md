# FEATURE-012 Release Notes - Autonomous Learning Engine

## 1. Summary

建立 AIRS Autonomous Learning Engine，从历史研究、Committee、Memory、Report 与 Outcome 中提取反馈、挖掘模式、生成规则并提出 Prompt、Methodology、Skill 与 Score 优化建议。

## 2. Added

- docs/learning/ 11 个 Learning 架构、反馈、Outcome、模式、规则、优化和治理文档
- learning/ 12 个 Python 核心组件、README 和 6 个学习示例
- schemas/learning/ 4 个 JSON Schema
- scripts/validate_learning.py
- docs/adr/ADR-012-autonomous-learning-engine.md
- docs/production/FEATURE_012_COMPLETION_REPORT.md
- docs/review/FEATURE_012_SELF_REVIEW.md

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

