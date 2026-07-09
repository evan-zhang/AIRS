# Innovative Drug Failure Cases

**Benchmark ID**：BENCH-INNOVATIVE-DRUG-FAILURE-CASES  
**版本**：v0.7.0

**免责声明**：本失败样例仅用于 AIRS 创新药类 Benchmark 质量控制，不构成投资建议，不提供交易指令、价格预测或收益承诺。

## 1. Evidence 失败

- 缺少 Evidence ID、Evidence Level、Confidence、Weight。
- 未说明临床阶段、终点和样本量。
- 忽略 refutes 和 missing_evidence。
- 用二手传闻替代临床注册或公司公告。

## 2. Methodology 失败

- 把临床进展直接等同于商业化成功。
- 估值分析缺少假设和敏感性。
- 风险分析未覆盖监管、支付和竞争。

## 3. M6 Scorecard 失败

- 缺少 Scorecard 或 Quality Gate。
- Risk Score 缺失。
- Confidence Score 与临床阶段不一致。

## 4. 合规失败

- 缺少“不构成投资建议”免责声明。
- 输出交易动作、收益承诺或确定性预测。
- 把评分解释为投资评级。

## 5. Gate 处理

临床核心证据缺失时必须 FAIL。商业化数据缺口已标注时可 CONDITIONAL_PASS。

## 6. M7 一致性声明

所有失败样例均按 M3 Evidence 字段和 M6 Scorecard 门禁判断，重点检查反方观点、不确定性和免责声明是否缺失。
