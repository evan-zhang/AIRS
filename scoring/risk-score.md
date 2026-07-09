# Risk Score（风险评分）

**归属 Milestone**：M6  
**版本**：v0.6.0  
**免责声明**：风险评分用于风险识别和披露质量控制，不构成投资建议，不构成风险承诺。

## 1. 评分目的

Risk Score 衡量研究是否识别主要风险、评估影响程度、发生可能性、证据质量、可监测性和缓释因素，承接 `docs/methodology/risk.md`。

## 2. 评分维度

| 维度 | 权重 | 规则 |
|------|------|------|
| 影响程度 | 0.20 | 风险对结论影响是否量化 |
| 发生可能性 | 0.15 | 是否有证据支持概率判断 |
| 证据质量 | 0.15 | Evidence Score 输入 |
| 可监测性 | 0.15 | 是否有跟踪指标 |
| 缓释强度 | 0.10 | 是否说明缓释因素 |
| 结论相关性 | 0.15 | 风险是否直接影响核心命题 |
| 披露完整度 | 0.10 | 是否写入报告 |

## 3. 计算公式

```text
risk_score = sum(risk_dimension_score_i * weight_i)
```

高风险不等于低研究质量；若风险被充分识别和披露，Risk Score 可以较高。

## 4. 输入输出

输入：风险清单、Evidence Chain、反方证据、报告风险章节。  
输出：risk_score、top_risks、monitoring_indicators、disclosure_findings。

## 5. 与 Evidence / Methodology 的关系

风险分类和证据要求来自 M2 风险方法论；证据质量来自 M3，不重复定义证据等级。

## 6. 权重建议

Overall Score 默认权重 0.10；风险专项研究可提高到 0.25。
