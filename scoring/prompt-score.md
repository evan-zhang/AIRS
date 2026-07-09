# Prompt Score（Prompt 质量评分）

**归属 Milestone**：M6  
**版本**：v0.6.0  
**免责声明**：Prompt 评分用于提示词质量控制，不构成投资建议。

## 1. 评分目的

Prompt Score 衡量 M4 Prompt 是否结构完整、引用正确、输出可验证、失败处理清晰且合规。

## 2. 评分维度

| 维度 | 权重 | 规则 |
|------|------|------|
| 结构完整性 | 0.20 | 七段式 Prompt 是否完整 |
| M2 引用 | 0.15 | 是否引用方法论 |
| M3 引用 | 0.15 | 是否引用 Evidence Card / Chain |
| 输入输出 Schema | 0.20 | Schema 是否明确 |
| Failure Cases | 0.10 | 失败状态是否可识别 |
| Review Checklist | 0.10 | 是否可复核 |
| 合规边界 | 0.10 | 是否有免责声明和禁止项 |

## 3. 计算公式

```text
prompt_score = sum(section_score_i * weight_i)
```

出现买卖建议、目标价或收益承诺时强制为 0 并触发 Evaluation FAIL。

## 4. 输入输出

输入：Prompt 文档、Prompt 输出、prompt.schema.json、prompt-output.schema.json。  
输出：prompt_score、schema_findings、compliance_findings、fix_required。

## 5. 与 Evidence / Methodology 的关系

Prompt Score 不评判投资结论，只评判 Prompt 是否正确装配 M2 与 M3，并产生可被 Skill、Score、Evaluation 使用的输出。

## 6. 权重建议

Overall Score 默认权重 0.10；Prompt 专项评审可提高到 0.30。

