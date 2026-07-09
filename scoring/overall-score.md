# Overall Score（综合评分）

**归属 Milestone**：M6  
**版本**：v0.6.0  
**免责声明**：综合评分仅用于 AIRS 研究质量和结构化分析，不构成投资建议，不构成投资评级或交易依据。

## 1. 评分目的

Overall Score 聚合 Theme、Evidence、Methodology、Prompt、Skill、Report、Risk 和 Confidence 等维度，形成统一 Scorecard。

## 2. 评分维度

| 维度 | 默认权重 |
|------|----------|
| Evidence Score | 0.25 |
| Methodology Score | 0.15 |
| Prompt Score | 0.10 |
| Skill Score | 0.10 |
| Report Score | 0.15 |
| Risk Score | 0.10 |
| Confidence Score | 0.10 |
| Theme Score | 0.05 |

## 3. 计算公式

```text
overall_score = sum(score_i * normalized_weight_i)
```

若某维度不适用，必须说明原因并归一化；Evidence Score、Confidence Score 和合规检查不得缺失。

## 4. 输入输出

输入：8 个维度评分、权重配置、扣分项、Quality Gate 结果。  
输出：overall_score、overall_grade、dimension_breakdown、gate_result、publication_readiness。

## 5. 与 Evidence / Methodology 的关系

综合评分以 Evidence Score 为基础，用 Methodology Score 检查研究路径是否正确。所有维度必须能追溯到 M2-M5 的对应对象。

## 6. 权重建议

默认权重来自 `docs/score-engine/weight-system.md`。任何覆盖权重必须记录调整原因、调整前后值和对最终等级的影响。
