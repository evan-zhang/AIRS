# Innovative Drug Benchmark Template

**Benchmark ID**：BENCH-INNOVATIVE-DRUG-TEMPLATE  
**行业分类**：innovative-drug  
**方法论引用**：`docs/methodology/policy-driven.md`, `docs/methodology/risk.md`, `docs/methodology/valuation.md`  
**Prompt 引用**：`prompts/risk/analysis.md`, `prompts/valuation/analysis.md`  
**版本**：v0.7.0

**免责声明**：本 Benchmark 仅用于 AIRS 创新药研究质量测试，不构成投资建议，不提供交易指令、价格预测或收益承诺。

## 1. 测试场景

创新药用例测试 Agent 是否能区分临床阶段、适应症空间、竞争格局、医保准入、商业化能力和研发失败风险。研究不得把单个临床事件直接推导为确定结论。

## 2. M4 Prompt 输入

- Prompt ID：`PROMPT-RISK-ANALYSIS` 或 `PROMPT-VALUATION-ANALYSIS`
- 研究问题：某类创新药管线的临床进展和商业化风险如何评估？
- 输出要求：M3 Evidence Card、Evidence Chain、M6 Scorecard、Quality Gate、反方观点、不确定性和免责声明。

## 3. M3 Evidence 要求

| Evidence ID | Evidence Level | Confidence | Weight | Supports | Refutes | Missing Evidence |
|-------------|----------------|------------|--------|----------|---------|------------------|
| EV-20260710-ID01 | A | HIGH | 0.25 | 临床试验注册、公告或监管进展 | 终点数据尚未成熟 | 完整临床数据 |
| EV-20260710-ID02 | B | MEDIUM | 0.20 | 适应症空间和竞争格局 | 同靶点竞争加剧 | 商业化放量数据 |

## 4. M6 Scorecard 要求

Scorecard 必须覆盖 Evidence Score、Risk Score、Confidence Score 和 Report Score。Quality Gate PASS 要求临床证据、商业化证据和反方风险均被记录。

## 5. 反方观点与不确定性

反方观点应覆盖临床失败、监管延迟、医保降价、同靶点竞争和商业化不及预期。不确定性应包括样本量、终点选择、随访时间和真实世界数据缺口。

