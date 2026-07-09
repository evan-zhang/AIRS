# Methodology Score（方法论评分）

**归属 Milestone**：M6  
**版本**：v0.6.0  
**免责声明**：方法论评分用于检查研究方法执行质量，不构成投资建议。

## 1. 评分目的

Methodology Score 衡量研究是否选择了合适 M2 方法论，并按 Purpose、Inputs、Workflow、Required Evidence、Counter Evidence、Confidence 和 Future Score Mapping 执行。

## 2. 评分维度

| 维度 | 权重 | 规则 |
|------|------|------|
| 方法论匹配 | 0.25 | 研究问题与适用场景是否匹配 |
| 输入完整性 | 0.15 | 必需输入是否齐全 |
| Workflow 执行 | 0.20 | 是否按步骤产生中间结果 |
| Required Evidence 覆盖 | 0.15 | 是否采集必需证据 |
| Counter Evidence 覆盖 | 0.10 | 是否执行反证检查 |
| Confidence 降级 | 0.10 | 是否按缺口调整置信度 |
| Future Mapping 一致性 | 0.05 | 是否按 M2 映射进入评分 |

## 3. 计算公式

```text
methodology_score = sum(check_score_i * weight_i)
```

每项 `check_score_i` 为 0、50、100：未满足、部分满足、满足。

## 4. 输入输出

输入：方法论引用、研究意图、执行 trace、Evidence Chain。  
输出：methodology_score、failed_sections、required_fixes、confidence_impact。

## 5. 与 Evidence / Methodology 的关系

本评分引用 M2 方法论文档，不复制 Theory 或 Workflow；证据覆盖判断通过 M3 Evidence Card 的 supports、refutes、missing_evidence 完成。

## 6. 权重建议

Overall Score 默认权重 0.15；方法论探索类任务可提高到 0.25。

