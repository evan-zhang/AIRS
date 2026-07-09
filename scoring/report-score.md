# Report Score（报告质量评分）

**归属 Milestone**：M6  
**版本**：v0.6.0  
**免责声明**：报告评分用于研究报告质量控制，不构成投资建议。

## 1. 评分目的

Report Score 衡量研究报告是否包含核心观点、证据链、评分、反方观点、不确定性、风险提示和免责声明。

## 2. 评分维度

| 维度 | 权重 | 规则 |
|------|------|------|
| 结构完整性 | 0.15 | 是否包含标准章节 |
| 结论可追溯 | 0.20 | 核心结论是否绑定 Evidence Card |
| 评分解释 | 0.15 | Scorecard 是否解释清楚 |
| 反方观点 | 0.15 | 是否有实质反方 |
| 不确定性 | 0.10 | confidence 与缺口是否披露 |
| 风险披露 | 0.10 | 风险是否分类说明 |
| 合规免责声明 | 0.15 | 是否明确不构成投资建议 |

## 3. 计算公式

```text
report_score = sum(section_score_i * weight_i)
```

免责声明缺失时强制 FAIL；核心观点无证据时最高不得超过 50。

## 4. 输入输出

输入：报告草稿、Scorecard、Evidence Chain、Evaluation result。  
输出：report_score、section_findings、publication_readiness、required_fixes。

## 5. 与 Evidence / Methodology 的关系

报告质量必须回到 M2 方法论选择和 M3 Evidence Chain，不允许使用无来源概括性判断。

## 6. 权重建议

Overall Score 默认权重 0.15；报告生成任务可提高到 0.30。

