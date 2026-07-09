# Valuation Report 示例：创新药管线估值研究

**Example ID**：EXAMPLE-VALUATION-001  
**版本**：v0.7.0  
**方法论引用**：`docs/methodology/valuation.md`, `docs/methodology/risk.md`  
**Prompt 引用**：`prompts/valuation/analysis.md`  
**Scorecard 引用**：`schemas/score/scorecard.schema.json`

**免责声明**：本示例仅用于 AIRS 估值研究流程演示，不构成投资建议，不提供交易指令、价格预测或收益承诺。

## 1. M4 Prompt 输入

- Prompt ID：`PROMPT-VALUATION-ANALYSIS`
- 研究问题：某创新药管线应如何进行研究性估值框架分析？
- 研究范围：临床阶段、适应症空间、竞争格局、商业化假设和风险折现。
- 输出要求：M3 Evidence Card、Evidence Chain、M6 Scorecard、Quality Gate、反方观点、不确定性和免责声明。

## 2. 核心观点

估值研究应输出假设框架和敏感性，不应输出确定价格结论。创新药管线价值高度依赖临床成功概率、适应症空间、竞争格局、定价支付和商业化能力。

## 3. M3 Evidence Card

### Evidence Card 1

- Evidence ID：EV-20260710-ID-VA01
- Title：临床试验注册和阶段信息
- Category：valuation
- Source Type：regulatory_filing
- Evidence Level：A
- Confidence：HIGH
- Supports：临床阶段支持估值模型的成功概率假设。
- Refutes：临床终点未读出，限制确定性。
- Missing Evidence：缺少完整有效性和安全性数据。
- Weight：0.30

### Evidence Card 2

- Evidence ID：EV-20260710-ID-VA02
- Title：同靶点竞争格局
- Category：industry
- Source Type：industry_report
- Evidence Level：B
- Confidence：MEDIUM
- Supports：竞争格局支持市场份额假设。
- Refutes：同类产品拥挤可能压缩商业化空间。
- Missing Evidence：缺少真实世界疗效和支付数据。
- Weight：0.22

## 4. Evidence Chain

EV-20260710-ID-VA01 支持临床阶段和成功概率假设，EV-20260710-ID-VA02 支持竞争与市场份额假设。反证集中在临床终点、支付环境和同靶点竞争。Missing Evidence 说明估值只能作为框架性研究。

## 5. M6 Scorecard

- Scorecard ID：SCORECARD-DRUG-VALUATION-001
- Methodology Refs：`valuation`, `risk`
- Evidence Chain Refs：EV-20260710-ID-VA01, EV-20260710-ID-VA02
- Evidence Score：78
- Methodology Score：82
- Prompt Score：84
- Report Score：80
- Risk Score：76
- Confidence Score：68
- Overall Score：77
- Quality Gate：CONDITIONAL_PASS
- Disclaimer：仅供研究参考，不构成投资建议

## 6. 反方观点

临床失败或安全性问题可能使估值框架失效；同靶点竞争可能降低商业化份额；医保和支付环境可能压缩假设空间；商业化团队能力不足可能导致收入兑现慢于预期。

## 7. 不确定性与风险

主要不确定性来自临床数据、随访时间、支付环境、竞争格局和模型参数。示例不输出确定价格结论，仅展示估值分析结构。

## 8. 免责声明

本估值报告示例仅供 AIRS 方法演示，不构成投资建议，不作为投资决策依据。

