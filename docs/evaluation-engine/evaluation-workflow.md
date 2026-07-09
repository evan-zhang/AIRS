# Evaluation Workflow（评估工作流）

**归属 Milestone**：M6 Score Engine & Evaluation Engine  
**版本**：v0.6.0  
**最后更新**：2026-07-10

**免责声明**：本文档定义质量评估流程，不构成投资建议或投资评级。

## 1. 标准流程

```text
Collect Inputs
  ↓
Schema Check
  ↓
Evidence Check
  ↓
Score Check
  ↓
Counter-view Check
  ↓
Compliance Check
  ↓
Quality Gate
  ↓
Loop / Go Decision
```

## 2. 检查步骤

### 2.1 Schema Check

验证 Score、Scorecard 和 Evaluation JSON 是否符合 `schemas/score/` 中的 Schema。

### 2.2 Evidence Check

检查 Evidence Card、Evidence Chain、Evidence Level、Confidence、Weight、supports、refutes、missing_evidence 是否存在，并与 M3 规范一致。

### 2.3 Score Check

检查评分维度、公式、权重和综合评分是否可计算。权重总和必须为 1.00 或有归一化记录。

### 2.4 Counter-view Check

检查反方观点是否覆盖数据、逻辑、场景和时间至少两类；强反方观点必须有 B 级以上证据。

### 2.5 Compliance Check

检查是否存在荐股、交易指令、目标价、收益承诺，检查免责声明是否存在。

## 3. Loop / Go 决策

| 结果 | 条件 | 动作 |
|------|------|------|
| PASS | 总分 >= 80 且无强制失败 | Go |
| CONDITIONAL_PASS | 70-79 或有轻微缺口 | Loop 修复后可 Go |
| FAIL | < 70 或触发强制失败 | Loop 重做 |

## 4. 输出格式

Evaluation 输出必须包含：

- evaluation_id。
- evaluated_artifact。
- score_summary。
- gate_result。
- failed_checks。
- fix_required。
- reviewer_notes。
- disclaimer_status。

