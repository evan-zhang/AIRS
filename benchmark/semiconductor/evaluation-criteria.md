# Semiconductor Evaluation Criteria

**Benchmark ID**：BENCH-SEMICONDUCTOR-EVALUATION-CRITERIA  
**版本**：v0.7.0

**免责声明**：本评估标准仅用于 AIRS 半导体类 Benchmark 的质量门禁，不构成投资建议，不提供交易指令、价格预测或收益承诺。

## 1. M6 评分映射

| Score 维度 | 权重 | 半导体类通过要求 |
|------------|------|------------------|
| Evidence Score | 0.25 | Evidence ID、Evidence Level、Confidence、Weight、supports、refutes、missing_evidence 完整 |
| Methodology Score | 0.15 | 供应链拆解、生命周期和财务异常流程完整 |
| Prompt Score | 0.10 | 使用 M4 Prompt 格式和 Failure Cases |
| Report Score | 0.20 | 报告包含证据链、Scorecard、反方观点、不确定性和免责声明 |
| Risk Score | 0.15 | 覆盖出口管制、库存周期、客户认证和技术替代 |
| Confidence Score | 0.15 | 与证据等级、时间口径和缺失证据一致 |

## 2. Quality Gate

PASS 要求 Overall Score >= 80，并且 A/B 级证据覆盖关键命题。CONDITIONAL_PASS 允许存在单个数据缺口，但必须写入 Missing Evidence。FAIL 适用于缺少 Scorecard、Evidence Level、反方观点或免责声明。

## 3. 半导体特有检查

评估应检查 Agent 是否把“产能建设”“良率提升”“客户认证”“收入确认”分开处理。若只引用单一扩产新闻并得出确定结论，应降低 Evidence Score 和 Confidence Score。

## 4. 反证要求

必须至少包含库存回落、海外供应缓和、技术路线变化或客户导入慢于预期中的两项反方观点，并标注证据强度。

## 5. M7 一致性声明

本评估标准直接检查 M3 Evidence 字段，包括 Evidence ID、Evidence Level、Confidence、Weight、supports、refutes 和 missing_evidence，并将结果映射到 M6 Scorecard 和 Quality Gate。
