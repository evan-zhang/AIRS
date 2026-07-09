# Quality Gate（质量门禁定义）

**归属 Milestone**：M6  
**免责声明**：质量门禁仅用于研究质量控制，不构成投资建议。

## 1. Gate 结果

| 结果 | 条件 | 动作 |
|------|------|------|
| PASS | 总分 >= 80 且无强制失败 | 允许进入正式报告 |
| CONDITIONAL_PASS | 70-79 且无强制失败 | Loop 修复后复核 |
| FAIL | < 70 或触发强制失败 | 不得进入正式报告 |

## 2. 分项检查

| 分项 | 最低要求 |
|------|----------|
| Evidence | 核心结论至少 1 张 A/B 级证据 |
| Methodology | 研究问题与 M2 方法论匹配 |
| Score | 权重可解释，综合分可复算 |
| Prompt | 输出结构可被 Schema 验证 |
| Skill | 调用链可追溯 |
| Report | 有反方观点、不确定性和风险披露 |
| Compliance | 有免责声明，无交易建议 |

## 3. 输出字段

Quality Gate 输出字段：gate_result、total_score、force_fail_triggered、failed_checks、required_fixes、can_publish。

