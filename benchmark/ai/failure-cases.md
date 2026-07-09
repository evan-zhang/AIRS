# AI Failure Cases

**Benchmark ID**：BENCH-AI-FAILURE-CASES  
**版本**：v0.7.0

**免责声明**：本失败样例仅用于 AIRS AI 类 Benchmark 质量控制，不构成投资建议，不提供交易指令、价格预测或收益承诺。

## 1. Evidence 失败

- 缺少 Evidence ID、Evidence Level、Confidence 或 Weight。
- 只引用新闻热度，不提供公司公告、产业数据或订单证据。
- 将 D/E 级证据作为核心结论主证据。
- 没有记录 Refutes 和 Missing Evidence。

## 2. Methodology 失败

- 没有执行供应链拆解，直接从 AI 主题推导结论。
- 没有区分训练、推理、服务器、网络、电力和散热。
- 主题扩散没有剔除伪相关公司或滞后收入。

## 3. M6 Scorecard 失败

- 缺少 Scorecard 或 Quality Gate。
- Score 维度缺失 Evidence Score 或 Confidence Score。
- Overall Score 与证据缺口不一致。
- 把评分表述为投资评级。

## 4. 报告与合规失败

- 缺少反方观点、不确定性或风险提示。
- 缺少“不构成投资建议”免责声明。
- 输出交易动作、收益承诺或确定性预测。

## 5. Gate 处理

触发任一强制失败条件时，Quality Gate 必须为 FAIL。若仅存在证据时效轻微不足但已记录 Missing Evidence，可为 CONDITIONAL_PASS。

## 6. M7 一致性声明

所有失败样例均按 M3 Evidence 字段和 M6 Scorecard 门禁判断，重点检查反方观点、不确定性和免责声明是否缺失。
