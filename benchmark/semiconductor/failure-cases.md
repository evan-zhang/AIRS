# Semiconductor Failure Cases

**Benchmark ID**：BENCH-SEMICONDUCTOR-FAILURE-CASES  
**版本**：v0.7.0

**免责声明**：本失败样例仅用于 AIRS 半导体类 Benchmark 质量控制，不构成投资建议，不提供交易指令、价格预测或收益承诺。

## 1. Evidence 失败

- 缺少 Evidence ID、Evidence Level、Confidence 或 Weight。
- 用行业口号替代公司公告、订单、认证和财务证据。
- 忽略 refutes 和 missing_evidence。
- 将不可验证传闻作为核心证据。

## 2. Methodology 失败

- 没有区分设计、制造、设备、材料和封测环节。
- 没有识别库存周期与需求周期的差异。
- 对财务异常只描述数字变化，不解释业务口径。

## 3. M6 Scorecard 失败

- 缺少 Scorecard 或 Quality Gate。
- Evidence Score 与证据质量不一致。
- Confidence Score 在缺少客户认证时仍给高分。

## 4. 合规失败

- 缺少“不构成投资建议”免责声明。
- 输出交易动作、收益承诺或确定性预测。
- 把 Scorecard 用作投资评级。

## 5. Gate 处理

任何合规失败均为 FAIL。证据时效不足但已标注不确定性时，可视严重程度为 CONDITIONAL_PASS。

## 6. M7 一致性声明

所有失败样例均按 M3 Evidence 字段和 M6 Scorecard 门禁判断，重点检查反方观点、不确定性和免责声明是否缺失。
