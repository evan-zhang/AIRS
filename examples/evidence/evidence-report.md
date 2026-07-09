# Evidence Report 示例：新能源储能证据链

**Example ID**：EXAMPLE-EVIDENCE-001  
**版本**：v0.7.0  
**方法论引用**：`docs/methodology/evidence-chain.md`, `docs/methodology/policy-driven.md`  
**Prompt 引用**：`prompts/evidence/evidence-chain.md`  
**Scorecard 引用**：`schemas/score/scorecard.schema.json`

**免责声明**：本示例仅用于 AIRS Evidence Card 与 Evidence Chain 演示，不构成投资建议，不提供交易指令、价格预测或收益承诺。

## 1. M4 Prompt 输入

- Prompt ID：`PROMPT-EVIDENCE-CHAIN`
- 研究问题：储能需求增长命题是否有可审计证据链支持？
- 研究范围：政策、装机、招标、成本和电网消纳。
- 输出要求：M3 Evidence Card、Evidence Chain、M6 Scorecard、Quality Gate、反方观点、不确定性和免责声明。

## 2. M3 Evidence Card

### Evidence Card 1

- Evidence ID：EV-20260710-NE-EV01
- Title：官方储能装机统计
- Category：policy
- Source Type：official_statistics
- Evidence Level：A
- Confidence：HIGH
- Supports：装机统计支持储能需求增长命题。
- Refutes：装机增长不一定代表盈利改善。
- Missing Evidence：缺少项目利用小时和收益率数据。
- Weight：0.30

### Evidence Card 2

- Evidence ID：EV-20260710-NE-EV02
- Title：储能系统价格下降
- Category：market
- Source Type：industry_report
- Evidence Level：B
- Confidence：MEDIUM
- Supports：成本下降支持储能渗透率提升。
- Refutes：价格下降可能压缩供应链盈利。
- Missing Evidence：缺少企业毛利率分环节数据。
- Weight：0.22

### Evidence Card 3

- Evidence ID：EV-20260710-NE-EV03
- Title：地方电网消纳约束
- Category：risk
- Source Type：news
- Evidence Level：C
- Confidence：MEDIUM
- Supports：消纳约束解释地区差异。
- Refutes：部分地区需求可能低于装机规划。
- Missing Evidence：缺少统一口径消纳数据。
- Weight：0.14

## 3. Evidence Chain

证据链命题：储能需求增长有政策和装机支持，但盈利质量仍受价格、消纳和利用小时影响。EV-20260710-NE-EV01 是主证据，EV-20260710-NE-EV02 解释成本驱动，EV-20260710-NE-EV03 提供风险反证。Missing Evidence 包括项目收益率、利用小时和企业毛利率。

## 4. M6 Scorecard

- Scorecard ID：SCORECARD-ENERGY-EVIDENCE-001
- Methodology Refs：`evidence-chain`, `policy-driven`
- Evidence Chain Refs：EV-20260710-NE-EV01, EV-20260710-NE-EV02, EV-20260710-NE-EV03
- Evidence Score：84
- Methodology Score：80
- Prompt Score：82
- Report Score：78
- Risk Score：76
- Confidence Score：74
- Overall Score：79
- Quality Gate：CONDITIONAL_PASS
- Disclaimer：仅供研究参考，不构成投资建议

## 5. 反方观点

装机增长可能由政策驱动，未必转化为高质量收益；系统价格下降可能带来渗透率提升，也可能压缩利润；地区消纳约束可能导致项目利用率差异。

## 6. 不确定性与风险

不确定性包括统计口径、项目质量、利用小时、收益模式和地区差异。由于盈利证据不足，本示例 Gate 为 CONDITIONAL_PASS。

## 7. 免责声明

本证据报告示例仅用于 AIRS Evidence Engine 演示，所有内容仅供研究参考，不构成投资建议。

