# AIRS Production Acceptance Checklist（生产验收清单）

**版本**：v1.0.0  
**适用范围**：AIRS V1.0 最终验收

## 1. 结构验收

- [x] M1-M7 已有 Completion Report。
- [x] M8 Completion Report 已创建。
- [x] `docs/production/` 包含 M8 要求的生产文档。
- [x] `docs/governance/` 包含版本规范和发布流程。
- [x] `.github/` 包含协作、安全和支持文件。
- [x] `scripts/validate_release.py` 和 `scripts/production_check.py` 存在。

## 2. 内容验收

- [x] README 准确描述 V1.0 Production 状态。
- [x] ROADMAP 准确描述 M1-M8 完成状态。
- [x] CHANGELOG 记录 v1.0.0 发布。
- [x] 生产文档面向运维和治理人员可执行。
- [x] FINAL_REVIEW 如实记录技术债和风险。

## 3. 质量验收

- [x] 所有 validate 脚本可独立执行。
- [x] 聚合生产检查可执行并汇总结果。
- [x] 验收脚本覆盖生产文档、GitHub 文件、治理文档和最终报告。
- [x] 发布流程明确分支、Tag、CI/CD 和回滚规则。

## 4. 安全验收

- [x] SECURITY.md 定义报告安全问题的方式。
- [x] SUPPORT.md 定义支持范围和不支持范围。
- [x] 无自动交易能力声明。
- [x] 无荐股、收益承诺或目标价承诺。
- [x] 所有投资相关生产文档包含免责声明。

## 5. 治理验收

- [x] 版本规范明确 Major / Minor / Patch。
- [x] Release Workflow 明确 Issue、PR、Review、Tag、Release Notes。
- [x] 修改顶层核心文件已有 ADR 记录。
- [x] 维护、升级和回归流程可执行。

## 6. 验收结论规则

生产验收只有两种结论：

- PASS：所有关键项通过，`scripts/production_check.py` PASS。
- FAIL：任一关键项失败，或出现合规阻断项。

## 7. 免责声明

生产验收清单仅用于判断 AIRS 工程和治理交付是否满足 V1.0 要求，不构成投资建议，不提供任何证券交易建议、目标价或收益承诺。
