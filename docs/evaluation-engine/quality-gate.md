# Quality Gate（质量门禁）

**归属 Milestone**：M6 Score Engine & Evaluation Engine  
**版本**：v0.6.0  
**最后更新**：2026-07-10

**免责声明**：质量门禁只判断研究产物是否符合 AIRS 框架质量要求，不构成投资建议。

## 1. 门禁等级

| Gate | 分数 | 含义 | 动作 |
|------|------|------|------|
| PASS | 80-100 | 可进入正式报告或 Benchmark | Go |
| CONDITIONAL_PASS | 70-79 | 可修复后进入 | Loop |
| FAIL | 0-69 | 不得进入正式报告 | Loop 重做 |

## 2. 评分构成

| 项目 | 权重 |
|------|------|
| Evidence Gate | 25 |
| Methodology Gate | 15 |
| Score Gate | 15 |
| Prompt / Skill Gate | 15 |
| Report Gate | 15 |
| Compliance Gate | 15 |

## 3. 强制 FAIL

- 缺少免责声明。
- 存在直接投资建议、交易指令、目标价或收益承诺。
- 核心结论没有 Evidence Card。
- Evidence Level、Confidence 或 Weight 字段缺失。
- 没有反方观点。
- Scorecard 无综合评分或权重无法解释。

## 4. 条件通过

以下情况可给 CONDITIONAL_PASS：

- 证据充分但存在时效性缺口。
- 反方观点存在但强度不足。
- 权重已归一化但调整解释不充分。
- 报告结构完整但缺少部分复核记录。

## 5. 输出要求

Quality Gate 必须输出：

- gate_result。
- total_score。
- force_fail_triggered。
- conditional_items。
- required_fixes。
- can_publish。

