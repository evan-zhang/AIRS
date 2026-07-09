# AI Evaluation Criteria

**Benchmark ID**：BENCH-AI-EVALUATION-CRITERIA  
**版本**：v0.7.0

**免责声明**：本评估标准仅用于 AIRS AI 类 Benchmark 的质量门禁，不构成投资建议，不提供交易指令、价格预测或收益承诺。

## 1. M6 评分映射

| Score 维度 | 权重 | AI 类通过要求 |
|------------|------|---------------|
| Evidence Score | 0.25 | M3 Evidence Card 完整，Evidence Level、Confidence、Weight、supports、refutes、missing_evidence 均存在 |
| Methodology Score | 0.15 | 遵循供应链拆解、卡点识别、主题扩散和反证生成 |
| Prompt Score | 0.10 | 保留 Prompt ID、输入约束、输出格式和 Failure Cases |
| Report Score | 0.20 | 报告包含核心观点、证据链、Scorecard、反方观点、不确定性、风险和免责声明 |
| Risk Score | 0.15 | 覆盖 CapEx 波动、技术路线、供应扩产、客户集中度 |
| Confidence Score | 0.15 | 置信度与证据等级和缺失证据一致 |

## 2. Quality Gate

- PASS：Overall Score >= 80，证据链覆盖需求、供给和反证，免责声明完整。
- CONDITIONAL_PASS：Overall Score 70-79，或证据覆盖存在轻微缺口但已标注。
- FAIL：缺少 Evidence ID、Evidence Level、Scorecard、反方观点或免责声明。

## 3. 关键检查项

AI 类输出必须区分“主题热度”“订单可见度”“收入确认”和“盈利弹性”。若只引用市场情绪或二手传闻，不得给高 Confidence。若把 M6 Scorecard 解释为投资评级，必须 FAIL。

## 4. 反方观点评分

反方观点至少包含两类：需求透支或扩产超预期。强反方需要 B 级以上证据；弱反方可以是情景推演，但必须标注为不确定性。

