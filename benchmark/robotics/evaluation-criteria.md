# Robotics Evaluation Criteria

**Benchmark ID**：BENCH-ROBOTICS-EVALUATION-CRITERIA  
**版本**：v0.7.0

**免责声明**：本评估标准仅用于 AIRS 机器人类 Benchmark 的质量门禁，不构成投资建议，不提供交易指令、价格预测或收益承诺。

## 1. M6 评分映射

| Score 维度 | 权重 | 机器人类通过要求 |
|------------|------|------------------|
| Theme Score | 0.15 | 主题扩散路径清晰，伪相关剔除充分 |
| Evidence Score | 0.25 | Evidence Card 字段完整且覆盖订单、收入或验证 |
| Methodology Score | 0.15 | 遵循主题扩散和反共识方法论 |
| Report Score | 0.20 | 报告结构、Scorecard、反方观点、不确定性和免责声明完整 |
| Risk Score | 0.15 | 覆盖量产、成本、技术路线和客户风险 |
| Confidence Score | 0.10 | 与量产证据和财务贡献一致 |

## 2. Quality Gate

PASS 要求证据链能从主题扩散走到产业链环节和财务验证。只有主题叙述没有收入或订单证据时，应为 FAIL 或 CONDITIONAL_PASS。

## 3. 特有检查项

评估应检查 Agent 是否区分工业机器人和人形机器人，是否识别零部件价值量、国产替代和量产节奏。不能把样机展示视为商业化完成。

## 4. 反方观点评分

反方观点至少包括量产延后、成本下降不足或应用场景不足。若反方观点没有 Evidence Level 和 Confidence，应扣分。

## 5. M7 一致性声明

本评估标准直接检查 M3 Evidence 字段，包括 Evidence ID、Evidence Level、Confidence、Weight、supports、refutes 和 missing_evidence，并将结果映射到 M6 Scorecard 和 Quality Gate。
