# New Energy Expected Output

**Benchmark ID**：BENCH-NEW-ENERGY-EXPECTED-OUTPUT  
**版本**：v0.7.0

**免责声明**：本期望输出仅用于 AIRS 新能源类 Benchmark 回归测试，不构成投资建议，不提供交易指令、价格预测或收益承诺。

## 1. 输出结构

期望输出必须包含：

- M4 Prompt ID、研究问题和输出约束。
- 方法论引用：产业生命周期、政策驱动或风险。
- M3 Evidence Card：政策、装机、价格、产能或消纳证据。
- Evidence Chain：说明 supports、refutes、missing_evidence。
- M6 Scorecard：Evidence Score、Risk Score、Confidence Score、Quality Gate。
- 反方观点：产能、价格、政策、贸易、消纳。
- 不确定性：数据口径、地区差异、政策执行、库存。
- 免责声明。

## 2. 示例片段

```markdown
### Evidence Chain
- EV-20260710-NE01 supports: 官方装机数据支持需求增长命题。
- EV-20260710-NE02 refutes: 价格下行和产能扩张削弱盈利改善命题。
- Missing Evidence: 企业开工率和库存周期数据不足。
```

## 3. Gate 期望

若需求证据充分但盈利和价格证据不足，Quality Gate 应为 CONDITIONAL_PASS。只有证据链、Scorecard、反方观点、不确定性和免责声明完整时才可 PASS。

## 4. M7 一致性声明

期望输出必须逐项列出 M3 Evidence 字段，包括 Evidence ID、Evidence Level、Confidence、Weight，并纳入 M6 Scorecard 与 Quality Gate。
