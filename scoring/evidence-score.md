# Evidence Score（证据评分）

**归属 Milestone**：M6  
**版本**：v0.6.0  
**免责声明**：证据评分仅用于研究质量控制，不构成投资建议或投资评级。

## 1. 评分目的

Evidence Score 是 AIRS 所有评分的基础项，用于衡量 Evidence Card 与 Evidence Chain 的来源等级、可信度、权重、完整性、反方覆盖和缺口透明度。

## 2. 评分维度

| 维度 | 权重 | 规则 |
|------|------|------|
| Evidence Level | 0.30 | A=100, B=85, C=65, D=40, E=0 |
| Confidence | 0.20 | 直接使用 Evidence Card `confidence` 映射为 0-100 |
| Evidence Weight | 0.15 | 使用 Evidence Card `weight` 做加权贡献 |
| Chain Completeness | 0.15 | 证据是否覆盖核心命题 |
| Counter Evidence | 0.10 | 是否有 `refutes` 和反方证据 |
| Missing Evidence Transparency | 0.10 | 缺失证据是否披露并降级 |

## 3. 计算公式

```text
card_quality = level_score * 0.5 + confidence * 100 * 0.3 + evidence_weight * 100 * 0.2
evidence_score = weighted_average(card_quality, evidence_weight) * chain_factor - missing_penalty
```

`chain_factor` 在 0.70-1.00 之间；核心结论无 A/B 级证据时最高不得超过 75。

## 4. 输入输出

输入：Evidence Card、Evidence Chain、supports、refutes、missing_evidence、traceability。  
输出：evidence_score、card_scores、chain_factor、missing_penalty、confidence_adjustment。

## 5. 与 Evidence / Methodology 的关系

本评分直接对接 M3 Evidence Level / Confidence / Weight，不重新定义证据等级。Required Evidence 与 Counter Evidence 来自 M2 方法论。

## 6. 权重建议

Evidence Score 在 Overall Score 中默认权重 0.25。任何正式研究报告缺失 Evidence Score 时必须 FAIL。

