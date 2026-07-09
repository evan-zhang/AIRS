# Innovative Drug Evaluation Criteria

**Benchmark ID**：BENCH-INNOVATIVE-DRUG-EVALUATION-CRITERIA  
**版本**：v0.7.0

**免责声明**：本评估标准仅用于 AIRS 创新药类 Benchmark 的质量门禁，不构成投资建议，不提供交易指令、价格预测或收益承诺。

## 1. M6 评分映射

| Score 维度 | 权重 | 创新药类通过要求 |
|------------|------|------------------|
| Evidence Score | 0.25 | 临床、监管、商业化证据卡完整 |
| Methodology Score | 0.15 | 遵循政策驱动、风险或估值方法论 |
| Prompt Score | 0.10 | M4 Prompt 输入输出字段完整 |
| Report Score | 0.20 | 报告包含证据链、Scorecard、反方观点、不确定性和免责声明 |
| Risk Score | 0.20 | 临床、监管、竞争、支付和商业化风险充分 |
| Confidence Score | 0.10 | 与临床阶段和证据完整性一致 |

## 2. Quality Gate

PASS 要求临床数据、监管路径、竞争格局和商业化约束都有证据支撑。若临床终点未读出但报告已明确 Missing Evidence，可为 CONDITIONAL_PASS。缺少 Evidence Level、Scorecard 或免责声明时为 FAIL。

## 3. 特有检查项

评估必须检查 Agent 是否区分 Phase I/II/III、上市申请、医保谈判、真实世界数据和商业化放量。若用研发管线数量直接推导结论，应扣减 Methodology Score。

## 4. 反方观点评分

强反方观点应包括临床失败或同类竞争加剧，且至少有 B 级证据。仅口头提示“风险较大”不满足反方观点要求。

## 5. M7 一致性声明

本评估标准直接检查 M3 Evidence 字段，包括 Evidence ID、Evidence Level、Confidence、Weight、supports、refutes 和 missing_evidence，并将结果映射到 M6 Scorecard 和 Quality Gate。
