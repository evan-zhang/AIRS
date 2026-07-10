# FEATURE-008 Release Notes - Investment Research Engine

## 1. Summary

构建统一 Investment Research Engine，调度 Runtime、Skill、Prompt、Evidence、Knowledge Graph、Score、Report 和 Workspace，形成可执行投资研究全流程。

## 2. Added

- docs/investment-engine/ Engine 架构、管线、创意生成和推荐标准文档
- investment_engine/ 最小可运行 Python 研究引擎
- investment_engine/examples/ 五个研究案例
- schemas/investment/ 投资研究请求、命题和推荐 Schema
- templates/investment/ 报告与命题模板
- scripts/validate_investment_engine.py
- ADR-0008-investment-research-engine.md
- FEATURE_008_COMPLETION_REPORT.md

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

