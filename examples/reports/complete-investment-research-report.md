# Complete Investment Research Report 示例：AI 服务器产业链综合研究

**Example ID**：EXAMPLE-COMPLETE-RESEARCH-001  
**版本**：v0.7.0  
**方法论引用**：`docs/methodology/supply-chain-chokepoint.md`, `docs/methodology/theme-expansion.md`, `docs/methodology/risk.md`, `docs/methodology/counter-consensus.md`  
**Prompt 引用**：`prompts/supply-chain/chokepoint-analysis.md`, `prompts/report/generation.md`  
**Scorecard 引用**：`schemas/score/scorecard.schema.json`

**免责声明**：本完整研究报告示例仅用于 AIRS 生产级输出演示，不构成投资建议，不提供交易指令、价格预测或收益承诺。

## 报告元数据

- Prompt ID：`PROMPT-REPORT-GENERATION`
- 研究对象：AI 服务器产业链
- 研究方法：供应链卡脖子、主题扩散、风险分析、反共识分析
- 报告版本：v0.7.0

## 1. M4 Prompt 输入

研究问题：AI 服务器产业链中哪些环节存在可验证卡点，哪些风险会削弱研究结论？

输入约束：

- 必须使用 M3 Evidence Card。
- 必须输出 M6 Scorecard 和 Quality Gate。
- 必须包含反方观点、不确定性和免责声明。
- 不得输出交易动作、价格预测或收益承诺。

## 2. 核心观点

AI 服务器产业链的研究重点应放在需求持续性、关键供给约束、配套基础设施和反方风险之间的平衡。示例证据支持“HBM、先进封装和高速互联是需要跟踪的关键环节”，但真实利用率、订单持续性和扩产节奏仍构成重要不确定性。

## 3. M3 Evidence Card

### Evidence Card 1

- Evidence ID：EV-20260710-AI-CR01
- Title：云厂商 AI 基础设施资本开支披露
- Category：financial
- Source Type：company_filing
- Evidence Level：A
- Confidence：HIGH
- Supports：资本开支披露支持需求端扩张命题。
- Refutes：资本开支项目结构可能不完全对应 AI 服务器。
- Missing Evidence：缺少下游利用率与订单取消率。
- Weight：0.28

### Evidence Card 2

- Evidence ID：EV-20260710-AI-CR02
- Title：HBM 和先进封装供需研究
- Category：supply_chain
- Source Type：industry_report
- Evidence Level：B
- Confidence：MEDIUM
- Supports：供需紧张支持卡点命题。
- Refutes：扩产计划可能缓解未来紧张。
- Missing Evidence：缺少逐季度产能、良率和客户锁单数据。
- Weight：0.24

### Evidence Card 3

- Evidence ID：EV-20260710-AI-CR03
- Title：高速互联与数据中心电力约束
- Category：risk
- Source Type：news
- Evidence Level：C
- Confidence：MEDIUM
- Supports：配套基础设施约束影响交付节奏。
- Refutes：不同地区数据中心条件差异较大。
- Missing Evidence：缺少项目级电力容量和交付数据。
- Weight：0.14

### Evidence Card 4

- Evidence ID：EV-20260710-AI-CR04
- Title：模型效率提升与需求弹性反证
- Category：counter_evidence
- Source Type：expert_opinion
- Evidence Level：D
- Confidence：LOW
- Supports：效率提升可能降低单位算力需求。
- Refutes：推理应用增长可能抵消效率提升。
- Missing Evidence：缺少可量化工作负载变化数据。
- Weight：0.08

## 4. Evidence Chain

EV-20260710-AI-CR01 建立需求端基础，EV-20260710-AI-CR02 建立供给端卡点，EV-20260710-AI-CR03 说明交付配套风险，EV-20260710-AI-CR04 提供反方视角。证据链支持“存在需持续跟踪的卡点”，但不支持确定性投资结论。

## 5. M6 Scorecard

- Scorecard ID：SCORECARD-AI-COMPLETE-001
- Methodology Refs：`supply-chain-chokepoint`, `theme-expansion`, `risk`, `counter-consensus`
- Evidence Chain Refs：EV-20260710-AI-CR01, EV-20260710-AI-CR02, EV-20260710-AI-CR03, EV-20260710-AI-CR04
- Theme Score：80
- Evidence Score：83
- Methodology Score：85
- Prompt Score：86
- Skill Score：82
- Report Score：84
- Risk Score：80
- Confidence Score：76
- Overall Score：82
- Overall Grade：B
- Quality Gate：PASS
- Disclaimer：仅供研究参考，不构成投资建议

## 6. 反方观点

第一，云厂商 CapEx 可能包含通用基础设施，不能全部映射为 AI 服务器需求。第二，HBM 和先进封装扩产可能在未来缓解供给紧张。第三，模型效率提升和软件优化可能改变硬件需求结构。第四，数据中心电力和冷却约束具有地区差异，不能简单外推。

## 7. 不确定性标注

- 数据不确定性：订单、库存、利用率和良率口径不完全一致。
- 模型不确定性：供应链卡点评分依赖权重假设。
- 时间不确定性：扩产和需求确认存在季度级滞后。
- 结论不确定性：当前结论适合作为研究跟踪框架，不适合作为投资决策依据。

## 8. 风险提示

主要风险包括需求透支、供给扩张、技术路线变化、客户集中度、资本开支收缩和基础设施约束。任何单一证据变化都可能改变 Scorecard 和 Quality Gate。

## 9. 研究局限性

示例未接入实时数据库，证据为生产格式演示；缺少真实订单、项目交付、客户集中度和利用率数据；D 级专家观点仅作为反方辅助证据。

## 10. 免责声明

本完整研究报告示例由 AIRS 框架生成，用于展示 Prompt、Evidence Card、Scorecard 和报告结构。所有内容仅供研究参考，不构成投资建议，不作为投资决策依据。

