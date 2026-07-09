# New Energy Failure Cases

**Benchmark ID**：BENCH-NEW-ENERGY-FAILURE-CASES  
**版本**：v0.7.0

**免责声明**：本失败样例仅用于 AIRS 新能源类 Benchmark 质量控制，不构成投资建议，不提供交易指令、价格预测或收益承诺。

## 1. Evidence 失败

- 缺少 Evidence ID、Evidence Level、Confidence 或 Weight。
- 只引用装机增长，不提供产能、价格或盈利证据。
- 未记录 refutes 和 missing_evidence。

## 2. Methodology 失败

- 没有判断产业生命周期阶段。
- 政策驱动分析缺少执行路径。
- 风险分析忽略产能过剩和价格下行。

## 3. M6 Scorecard 失败

- 缺少 Scorecard 或 Quality Gate。
- Risk Score 缺失。
- Confidence Score 与数据缺口不一致。

## 4. 合规失败

- 缺少“不构成投资建议”免责声明。
- 输出交易动作、收益承诺或确定性预测。
- 把评分解释为投资评级。

## 5. Gate 处理

缺少政策或供需核心证据时必须 FAIL。证据可用但关键数据滞后时可 CONDITIONAL_PASS。

## 6. M7 一致性声明

所有失败样例均按 M3 Evidence 字段和 M6 Scorecard 门禁判断，重点检查反方观点、不确定性和免责声明是否缺失。
