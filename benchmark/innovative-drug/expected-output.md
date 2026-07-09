# Innovative Drug Expected Output

**Benchmark ID**：BENCH-INNOVATIVE-DRUG-EXPECTED-OUTPUT  
**版本**：v0.7.0

**免责声明**：本期望输出仅用于 AIRS 创新药类 Benchmark 回归测试，不构成投资建议，不提供交易指令、价格预测或收益承诺。

## 1. 输出结构

期望输出必须包含：

- Prompt ID 和 M4 Prompt 输入摘要。
- 方法论引用：风险、政策驱动或估值。
- M3 Evidence Card：临床、监管、竞争或商业化证据。
- Evidence Chain：说明 supports、refutes、missing_evidence。
- M6 Scorecard：Risk Score、Evidence Score、Confidence Score、Quality Gate。
- 反方观点：临床失败、监管延迟、竞争加剧、支付端压力。
- 不确定性：样本量、终点选择、随访时间、真实世界数据。
- 免责声明。

## 2. 示例片段

```markdown
### M3 Evidence Card
- Evidence ID: EV-20260710-ID01
- Evidence Level: A
- Confidence: MEDIUM
- Weight: 0.25
- Supports: 临床进展支持管线有效性命题
- Refutes: 完整终点未读出削弱确定性
- Missing Evidence: 长期随访和商业化数据
```

## 3. Gate 期望

若临床证据充分但商业化证据缺失，Quality Gate 应为 CONDITIONAL_PASS。只有证据链、Scorecard、反方观点、不确定性和免责声明完整时才可 PASS。

