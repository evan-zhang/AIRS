# FEATURE-004 Release Notes - Data Connector Framework

## 1. Summary

建立统一 Data Connector Framework，所有外部数据源必须通过 Connector 接入并输出可追溯结果。

## 2. Added

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

