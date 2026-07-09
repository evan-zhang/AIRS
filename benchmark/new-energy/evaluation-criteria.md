# New Energy Evaluation Criteria

**Benchmark ID**：BENCH-NEW-ENERGY-EVALUATION-CRITERIA  
**版本**：v0.7.0

**免责声明**：本评估标准仅用于 AIRS 新能源类 Benchmark 的质量门禁，不构成投资建议，不提供交易指令、价格预测或收益承诺。

## 1. M6 评分映射

| Score 维度 | 权重 | 新能源类通过要求 |
|------------|------|------------------|
| Evidence Score | 0.25 | 政策、供需、价格和风险证据卡完整 |
| Methodology Score | 0.15 | 遵循生命周期、政策驱动或风险方法论 |
| Prompt Score | 0.10 | M4 Prompt 格式完整 |
| Report Score | 0.20 | 报告包含 Scorecard、反方观点、不确定性和免责声明 |
| Risk Score | 0.20 | 覆盖产能、价格、政策、贸易和消纳 |
| Confidence Score | 0.10 | 与数据时效、口径和缺口一致 |

## 2. Quality Gate

PASS 要求 Overall Score >= 80 且供需、政策、价格证据均完整。若缺少开工率、库存或消纳数据，应为 CONDITIONAL_PASS。缺少 Evidence Level、Scorecard 或免责声明时为 FAIL。

## 3. 特有检查项

评估必须检查 Agent 是否区分装机量、出货量、收入确认和盈利能力。若只用政策方向推断确定结论，应降低 Methodology Score 和 Confidence Score。

## 4. 反方观点评分

反方观点至少包含产能过剩和价格下行，也应考虑贸易政策或电网消纳。没有 Evidence Card 支撑的反方观点不得计为强反方。

## 5. M7 一致性声明

本评估标准直接检查 M3 Evidence 字段，包括 Evidence ID、Evidence Level、Confidence、Weight、supports、refutes 和 missing_evidence，并将结果映射到 M6 Scorecard 和 Quality Gate。
