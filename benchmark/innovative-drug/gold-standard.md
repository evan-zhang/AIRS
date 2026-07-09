# Innovative Drug Gold Standard

**Benchmark ID**：BENCH-INNOVATIVE-DRUG-GOLD-STANDARD  
**版本**：v0.7.0

**免责声明**：本 Gold Standard 仅用于创新药 Benchmark 标准答案边界，不构成投资建议，不提供交易指令、价格预测或收益承诺。

## 1. 标准答案边界

合格答案应把临床、监管、商业化和竞争格局分开评估。创新药研究必须保留失败概率和数据不确定性，不能用单一临床公告替代完整证据链。

## 2. 必需 M3 Evidence

Evidence Card 至少覆盖：

- 临床试验注册或公司公告，Evidence Level 通常为 A。
- 同类药物竞争格局或适应症规模，Evidence Level 可为 B。
- 医保、监管或商业化数据，Evidence Level 依据来源确定。

字段必须包括 Evidence ID、Evidence Level、Confidence、Weight、supports、refutes、missing_evidence。若缺少完整终点数据，Confidence 不得过高。

## 3. 期望研究结论

可接受结论包括：

- 临床进展只能说明研究命题的部分证据，不能替代商业化判断。
- 估值分析应输出敏感性和假设，不输出价格预测。
- 风险分析必须覆盖临床、监管、商业化、竞争和支付端。
- Quality Gate 与证据完整性一致。

## 4. M6 Scorecard 标准

Scorecard 必须包含 Risk Score 和 Confidence Score。若反方观点缺少临床失败或竞争格局，Risk Score 应明显扣分。若缺少免责声明，Quality Gate 必须 FAIL。

## 5. 不合格边界

无 Evidence Card、无临床阶段说明、忽略同靶点竞争、没有 Missing Evidence、缺少 Scorecard 或免责声明，均为 FAIL。

