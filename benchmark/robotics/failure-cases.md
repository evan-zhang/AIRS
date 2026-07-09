# Robotics Failure Cases

**Benchmark ID**：BENCH-ROBOTICS-FAILURE-CASES  
**版本**：v0.7.0

**免责声明**：本失败样例仅用于 AIRS 机器人类 Benchmark 质量控制，不构成投资建议，不提供交易指令、价格预测或收益承诺。

## 1. Evidence 失败

- 缺少 Evidence ID、Evidence Level、Confidence 或 Weight。
- 只引用主题热度，不提供订单、收入、验证或客户证据。
- 未记录 refutes 和 missing_evidence。

## 2. Methodology 失败

- 把样机展示等同于规模商业化。
- 主题扩散没有剔除伪相关。
- 反共识缺失或只写空泛风险。

## 3. M6 Scorecard 失败

- 缺少 Scorecard 或 Quality Gate。
- Theme Score 与 Evidence Score 混淆。
- Confidence Score 与量产证据不一致。

## 4. 合规失败

- 缺少“不构成投资建议”免责声明。
- 输出交易动作、收益承诺或确定性预测。
- 把评分解释为投资评级。

## 5. Gate 处理

缺少财务或量产证据时不得 PASS。若已充分披露 Missing Evidence，可为 CONDITIONAL_PASS。

## 6. M7 一致性声明

所有失败样例均按 M3 Evidence 字段和 M6 Scorecard 门禁判断，重点检查反方观点、不确定性和免责声明是否缺失。
