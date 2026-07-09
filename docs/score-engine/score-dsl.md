# Score DSL（评分描述语言）

**归属 Milestone**：M6 Score Engine & Evaluation Engine  
**版本**：v0.6.0  
**最后更新**：2026-07-10

**免责声明**：Score DSL 仅用于描述研究评分规则，不构成投资建议或投资评级。

## 1. 目的

Score DSL 用统一字段描述评分对象、维度、权重、公式、输入引用和输出约束，使 Score Engine 可以复核评分是否可计算、可解释、可追溯。

## 2. 顶层结构

```yaml
score_id: SCORE-YYYYMMDD-001
score_type: evidence | methodology | prompt | skill | report | risk | confidence | theme | overall
version: v0.6.0
methodology_refs:
  - docs/methodology/supply-chain-chokepoint.md
evidence_chain_refs:
  - ECHAIN-001
input_refs:
  prompt_output_id: PROMPT-RUN-001
  skill_run_id: SKILL-RUN-001
dimensions:
  - name: evidence_quality
    weight: 0.25
    formula: weighted_average(level_score, confidence, evidence_weight)
    evidence_refs: [EVID-001, EVID-002]
penalties:
  missing_evidence: 8
  counter_evidence: 5
overall_formula: sum(dimension_score * weight)
quality_gate: PASS
disclaimer_required: true
```

## 3. 必需字段

| 字段 | 类型 | 必需 | 说明 |
|------|------|------|------|
| score_id | string | 是 | 评分唯一 ID |
| score_type | enum | 是 | 评分类型 |
| methodology_refs | array | 是 | M2 方法论引用 |
| evidence_chain_refs | array | 是 | M3 Evidence Chain 引用 |
| dimensions | array | 是 | 评分维度 |
| weight | number | 是 | 维度权重，0-1 |
| formula | string | 是 | 可解释公式 |
| overall_formula | string | 是 | 综合评分公式 |
| disclaimer_required | boolean | 是 | 必须为 true |

## 4. 分数区间

- 90-100：优秀，可进入报告但仍需 Evaluation Gate。
- 80-89：良好，允许进入报告。
- 70-79：合格，必须披露主要缺口。
- 60-69：条件合格，进入 Loop 修复。
- 0-59：失败，不得进入正式报告。

## 5. 标准映射

Evidence Level 映射只引用 M3 标准：

| Evidence Level | level_score |
|----------------|-------------|
| A | 100 |
| B | 85 |
| C | 65 |
| D | 40 |
| E | 0 |

`confidence` 与 `weight` 使用 Evidence Card 原字段，不在 DSL 中重新定义含义。

## 6. 权重规则

每组 `dimensions.weight` 必须满足：

```text
0 < weight <= 1
abs(sum(weight) - 1.0) <= 0.001
```

如果输入权重不满足总和为 1，必须先记录调整原因，再按 `normalized_weight = weight / sum(weight)` 归一化。

## 7. 合规字段

Score DSL 必须包含：

- `disclaimer_required: true`
- `forbidden_outputs`: 买入、卖出、持有、目标价、收益承诺
- `rating_boundary`: 评分不是投资评级

