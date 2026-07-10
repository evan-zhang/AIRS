# FEATURE-009 Release Notes - Autonomous Research Planner

## 1. Summary

建立 AIRS 最上层 Autonomous Research Planner，把用户研究目标拆解为可执行 Research Plan，并生成 Runtime、Workflow、Methodology、Connector、Skill、KG、Evidence、Score、Report 的完整执行链路。

## 2. Added

- docs/planner/ 12 个 Planner 架构与组件文档
- planner/ 12 个 Python 组件和 README
- planner/examples/ 8 个研究目标示例及 Markdown 文档
- schemas/planner/ 4 个 JSON Schema
- templates/planner/ Planner 模板
- scripts/validate_planner.py
- docs/adr/ADR-0009-autonomous-research-planner.md
- docs/production/FEATURE_009_COMPLETION_REPORT.md
- docs/review/FEATURE_009_SELF_REVIEW.md

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

