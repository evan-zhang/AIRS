# Theme Score（主题评分）

**归属 Milestone**：M6  
**版本**：v0.6.0  
**免责声明**：主题评分仅用于研究主题强度和相关度分析，不构成投资建议或投资评级。

## 1. 评分目的

Theme Score 衡量研究主题与研究对象之间的相关性、传导强度、持续性和拥挤度，承接 `docs/methodology/theme-expansion.md` 的 Future Score Mapping。

## 2. 评分维度

| 维度 | 权重 | 规则 |
|------|------|------|
| 主题强度 | 0.25 | 政策、产业、资本开支或需求变化是否明确 |
| 业务相关度 | 0.25 | 研究对象是否直接暴露于主题 |
| 传导距离 | 0.15 | 从主题到业绩或风险的链条长度 |
| 持续性 | 0.15 | 主题是否有多期证据支持 |
| 拥挤度与反证 | 0.10 | 是否存在叙事过热或反方证据 |
| 证据质量 | 0.10 | Evidence Score 输入 |

## 3. 计算公式

```text
theme_score = sum(dimension_score_i * weight_i) - crowding_penalty - missing_evidence_penalty
```

每个维度 0-100。`crowding_penalty` 取 0-10，`missing_evidence_penalty` 取 0-15。

## 4. 输入输出

输入：研究主题、研究对象、Theme Expansion 方法论引用、Evidence Chain、反方证据。  
输出：theme_score、dimension_scores、evidence_refs、penalties、confidence_score。

## 5. 与 Evidence / Methodology 的关系

Theme Score 使用 M2 主题扩散方法论定义的传导链，不重复定义扩散理论；证据等级、confidence、weight 直接来自 M3 Evidence Card。

## 6. 权重建议

Theme Score 在 Overall Score 中默认权重为 0.05；主题研究任务可提高到 0.15，但必须记录调整原因。

