# Supply Chain Report 示例：AI 服务器供应链卡点

**Example ID**：EXAMPLE-SUPPLY-CHAIN-001  
**版本**：v0.7.0  
**方法论引用**：`docs/methodology/supply-chain-chokepoint.md`  
**Prompt 引用**：`prompts/supply-chain/chokepoint-analysis.md`  
**Scorecard 引用**：`schemas/score/scorecard.schema.json`

**免责声明**：本示例仅用于 AIRS 生产级报告格式演示，不构成投资建议，不提供交易指令、价格预测或收益承诺。

## 1. M4 Prompt 输入

- Prompt ID：`PROMPT-SUPPLY-CHAIN-CHOKEPOINT`
- 研究问题：AI 服务器需求增长是否会在 HBM、先进封装和高速互联环节形成供应链卡点？
- 研究范围：AI 加速卡、HBM、CoWoS/先进封装、高速交换芯片、液冷和服务器 ODM。
- 输出要求：按 M4 Prompt 输出 Evidence Card、Evidence Chain、M6 Scorecard、反方观点、不确定性、风险提示和免责声明。

## 2. 核心观点

基于示例证据链，AI 服务器供应链的瓶颈不应被简化为单一芯片供给问题。HBM、先进封装、高速互联和数据中心配套能力都可能影响交付节奏，但结论强度取决于订单可见度、产能爬坡和下游利用率。

本示例的结论是研究性判断：在证据完整时可识别“需要重点跟踪的卡点”，但不能推导为任何投资动作。

## 3. M3 Evidence Card

### Evidence Card 1

- Evidence ID：EV-20260710-AI-SC01
- Title：云厂商资本开支和 AI 服务器订单指引
- Category：supply_chain
- Source Type：company_filing
- Evidence Level：A
- Confidence：HIGH
- Supports：云厂商资本开支提升支持 AI 服务器需求扩张命题。
- Refutes：资本开支可能包含非 AI 基础设施，削弱纯 AI 需求判断。
- Missing Evidence：缺少最终服务器利用率和订单取消率。
- Weight：0.28

### Evidence Card 2

- Evidence ID：EV-20260710-AI-SC02
- Title：HBM 与先进封装产能爬坡进展
- Category：supply_chain
- Source Type：industry_report
- Evidence Level：B
- Confidence：MEDIUM
- Supports：HBM 与先进封装供给紧张支持卡点命题。
- Refutes：供应商扩产可能缓解未来供需紧张。
- Missing Evidence：缺少逐季度可验证产能和良率数据。
- Weight：0.24

### Evidence Card 3

- Evidence ID：EV-20260710-AI-SC03
- Title：高速互联与液冷配套需求
- Category：industry
- Source Type：news
- Evidence Level：C
- Confidence：MEDIUM
- Supports：高速互联和液冷成为高密度数据中心配套约束。
- Refutes：不同数据中心架构对液冷需求差异较大。
- Missing Evidence：缺少项目级部署数据。
- Weight：0.16

## 4. Evidence Chain

EV-20260710-AI-SC01 支持需求端扩张，EV-20260710-AI-SC02 支持关键供给瓶颈，EV-20260710-AI-SC03 补充配套基础设施约束。反向证据包括扩产超预期、推理效率提升和资本开支结构变化。Missing Evidence 集中在真实利用率、订单持续性和产能良率。

## 5. M6 Scorecard

- Scorecard ID：SCORECARD-AI-SUPPLY-CHAIN-001
- Methodology Refs：`supply-chain-chokepoint`
- Evidence Chain Refs：EV-20260710-AI-SC01, EV-20260710-AI-SC02, EV-20260710-AI-SC03
- Evidence Score：82
- Methodology Score：84
- Prompt Score：86
- Report Score：83
- Risk Score：78
- Confidence Score：76
- Overall Score：81
- Quality Gate：PASS
- Disclaimer：仅供研究参考，不构成投资建议

## 6. 反方观点

第一，云厂商资本开支可能提前反映长期需求，短期订单不一定持续。第二，HBM 和先进封装扩产若快于预期，供应瓶颈可能弱化。第三，模型架构和推理效率提升可能改变服务器配置需求。

## 7. 不确定性与风险

不确定性包括订单口径、收入确认周期、供应商良率、数据中心利用率和客户集中度。风险包括需求透支、供应扩产、技术路线变化和宏观资本开支收缩。

## 8. 免责声明

本示例仅用于 AIRS 框架演示，所有评分和结论仅供研究参考，不构成投资建议，不作为投资决策依据。

