# General Expected Output

**Benchmark ID**：BENCH-GENERAL-EXPECTED-OUTPUT  
**版本**：v0.7.0

**免责声明**：本期望输出仅用于 AIRS 通用 Benchmark 回归测试，不构成投资建议，不提供交易指令、价格预测或收益承诺。

## 1. 输出结构

通用 Benchmark 的期望输出必须包含：

- Prompt ID 和 M4 Prompt 输入摘要。
- Methodology Refs。
- M3 Evidence Card，包含 Evidence ID、Evidence Level、Confidence、Weight。
- Evidence Chain，包含 supports、refutes、missing_evidence。
- M6 Scorecard，包含 Overall Score、Confidence Score、Quality Gate。
- 反方观点。
- 不确定性标注。
- 风险提示。
- 免责声明。

## 2. 示例片段

```markdown
### M6 Scorecard
- Scorecard ID: SCORECARD-GENERAL-001
- Evidence Score: 82
- Report Score: 84
- Confidence Score: 78
- Quality Gate: PASS
- Disclaimer: 仅供研究参考，不构成投资建议
```

## 3. Gate 期望

若输出能解释为什么证据不足并给出 Missing Evidence，可以获得 CONDITIONAL_PASS。若无 Evidence Card 或 Scorecard，应为 FAIL。

