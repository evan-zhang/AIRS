# Risk Report 示例：光伏产业链周期风险

**Example ID**：EXAMPLE-RISK-001  
**版本**：v0.7.0  
**方法论引用**：`docs/methodology/risk.md`, `docs/methodology/industry-lifecycle.md`  
**Prompt 引用**：`prompts/risk/analysis.md`  
**Scorecard 引用**：`schemas/score/scorecard.schema.json`

**免责声明**：本示例仅用于 AIRS 风险报告格式演示，不构成投资建议，不提供交易指令、价格预测或收益承诺。

## 1. M4 Prompt 输入

- Prompt ID：`PROMPT-RISK-ANALYSIS`
- 研究问题：光伏产业链在产能扩张后面临哪些周期风险？
- 研究范围：硅料、硅片、电池片、组件、逆变器、海外贸易和终端装机。
- 输出要求：M3 Evidence Card、Evidence Chain、M6 Scorecard、Quality Gate、反方观点、不确定性和免责声明。

## 2. 核心观点

光伏产业链风险不只来自需求波动，也来自供给扩张、价格下行、库存周期、海外贸易政策和技术路线切换。风险报告应把风险触发条件、影响路径和证据缺口分开记录。

## 3. M3 Evidence Card

### Evidence Card 1

- Evidence ID：EV-20260710-PV-RI01
- Title：行业产能扩张和价格走势
- Category：risk
- Source Type：industry_report
- Evidence Level：B
- Confidence：MEDIUM
- Supports：产能扩张和价格下行支持周期风险命题。
- Refutes：需求增长可能部分吸收新增供给。
- Missing Evidence：缺少企业开工率和库存分环节数据。
- Weight：0.26

### Evidence Card 2

- Evidence ID：EV-20260710-PV-RI02
- Title：海外贸易政策变化
- Category：policy
- Source Type：government_policy
- Evidence Level：A
- Confidence：HIGH
- Supports：贸易政策变化影响出口链条。
- Refutes：企业海外产能布局可部分缓释风险。
- Missing Evidence：缺少分地区订单转移数据。
- Weight：0.22

## 4. Evidence Chain

EV-20260710-PV-RI01 说明价格和产能风险，EV-20260710-PV-RI02 说明海外政策风险。反证包括终端需求韧性和海外产能布局。Missing Evidence 包括库存、开工率、分地区订单。

## 5. M6 Scorecard

- Scorecard ID：SCORECARD-PV-RISK-001
- Methodology Refs：`risk`, `industry-lifecycle`
- Evidence Chain Refs：EV-20260710-PV-RI01, EV-20260710-PV-RI02
- Evidence Score：80
- Methodology Score：82
- Prompt Score：84
- Report Score：82
- Risk Score：86
- Confidence Score：74
- Overall Score：81
- Quality Gate：PASS
- Disclaimer：仅供研究参考，不构成投资建议

## 6. 反方观点

终端装机需求若超预期，可能缓解产能过剩；海外本地化产能可能降低贸易摩擦影响；技术迭代可能改善成本曲线，但也可能带来旧产能减值。

## 7. 不确定性与风险

不确定性包括价格指数口径、库存数据、海外政策执行、技术路线迭代和企业产能弹性。风险触发条件包括价格持续下行、库存高企、贸易壁垒增强和融资环境收紧。

## 8. 免责声明

本风险报告示例仅供 AIRS 流程演示，所有内容仅供研究参考，不构成投资建议。

