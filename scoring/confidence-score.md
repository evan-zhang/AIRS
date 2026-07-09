# Confidence Score（置信度评分）

**归属 Milestone**：M6  
**版本**：v0.6.0  
**免责声明**：置信度评分用于表达研究结论可靠程度，不构成投资建议或确定性承诺。

## 1. 评分目的

Confidence Score 衡量结论置信度是否与证据等级、证据链完整度、反证压力、缺口透明度和方法论适配程度一致。

## 2. 评分维度

| 维度 | 权重 | 规则 |
|------|------|------|
| Evidence Confidence | 0.30 | Evidence Card confidence 加权平均 |
| Chain Completeness | 0.20 | 证据链是否完整 |
| Counter Evidence Pressure | 0.15 | 反方证据越强，置信度应越谨慎 |
| Missing Evidence Impact | 0.15 | 关键缺口是否降级 |
| Methodology Fit | 0.10 | 方法论是否适配 |
| Recency Fit | 0.10 | 证据时间是否匹配 |

## 3. 计算公式

```text
confidence_score = evidence_confidence * 0.3
                 + chain_completeness * 0.2
                 + counter_factor * 0.15
                 + missing_factor * 0.15
                 + methodology_fit * 0.1
                 + recency_fit * 0.1
```

所有因子映射为 0-100。核心证据缺失时最高不得超过 70。

## 4. 输入输出

输入：Evidence Chain、Methodology Score、反方证据、missing_evidence。  
输出：confidence_score、confidence_level、downgrade_reasons、uncertainty_notes。

## 5. 与 Evidence / Methodology 的关系

Confidence Score 直接承接 M3 对 Confidence 与 Evidence Level 的区分，并使用 M2 各方法论的 Confidence 降级条件。

## 6. 权重建议

Overall Score 默认权重 0.10；不确定性审查任务可提高到 0.20。

