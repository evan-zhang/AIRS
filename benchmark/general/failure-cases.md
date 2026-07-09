# General Failure Cases

**Benchmark ID**：BENCH-GENERAL-FAILURE-CASES  
**版本**：v0.7.0

**免责声明**：本失败样例仅用于 AIRS 通用 Benchmark 质量控制，不构成投资建议，不提供交易指令、价格预测或收益承诺。

## 1. Evidence 失败

- 缺少 Evidence ID、Evidence Level、Confidence 或 Weight。
- 证据没有 supports、refutes 或 missing_evidence。
- 证据来源不可追踪。

## 2. Prompt 与 Methodology 失败

- 缺少 Prompt ID。
- 未引用 M2 Methodology。
- 输出没有遵循 M4 Prompt 格式。

## 3. M6 Scorecard 失败

- 缺少 Scorecard 或 Quality Gate。
- Overall Score 无解释。
- Confidence Score 与证据缺口不一致。

## 4. 报告失败

- 缺少核心观点、证据链、反方观点、不确定性或风险提示。
- 缺少“不构成投资建议”免责声明。
- 输出交易动作、收益承诺或确定性预测。

## 5. Gate 处理

任何合规缺失均为 FAIL。结构完整但证据轻微不足且已标注 Missing Evidence 时可为 CONDITIONAL_PASS。

## 6. M7 一致性声明

所有失败样例均按 M3 Evidence 字段和 M6 Scorecard 门禁判断，重点检查反方观点、不确定性和免责声明是否缺失。
