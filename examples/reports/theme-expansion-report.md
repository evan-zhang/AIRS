# Theme Expansion Report 示例：人形机器人主题扩散

**Example ID**：EXAMPLE-THEME-EXPANSION-001  
**版本**：v0.7.0  
**方法论引用**：`docs/methodology/theme-expansion.md`, `docs/methodology/counter-consensus.md`  
**Prompt 引用**：`prompts/hot-topic/theme-expansion.md`  
**Scorecard 引用**：`schemas/score/scorecard.schema.json`

**免责声明**：本示例仅用于 AIRS 主题扩散研究格式演示，不构成投资建议，不提供交易指令、价格预测或收益承诺。

## 1. M4 Prompt 输入

- Prompt ID：`PROMPT-THEME-EXPANSION`
- 研究问题：人形机器人主题如何从整机厂扩散到核心零部件和自动化服务环节？
- 研究范围：减速器、丝杠、传感器、控制器、执行器、代工和工业应用。
- 输出要求：M3 Evidence Card、Evidence Chain、Theme Score、M6 Scorecard、Quality Gate、反方观点、不确定性和免责声明。

## 2. 核心观点

主题扩散应先识别“技术相关性”，再验证“订单或收入相关性”。人形机器人主题可以扩散到部分核心零部件，但样机展示、客户验证和规模收入之间存在明显阶段差异。

## 3. M3 Evidence Card

### Evidence Card 1

- Evidence ID：EV-20260710-RB-TE01
- Title：核心零部件企业披露机器人业务收入
- Category：financial
- Source Type：company_filing
- Evidence Level：A
- Confidence：HIGH
- Supports：财报披露支持机器人业务具有收入相关性。
- Refutes：收入占比可能较低，主题贡献有限。
- Missing Evidence：缺少客户分布和订单持续性。
- Weight：0.30

### Evidence Card 2

- Evidence ID：EV-20260710-RB-TE02
- Title：人形机器人样机与供应链验证进展
- Category：industry
- Source Type：industry_report
- Evidence Level：B
- Confidence：MEDIUM
- Supports：验证进展支持主题向零部件扩散。
- Refutes：样机验证不等于量产交付。
- Missing Evidence：缺少批量交付和毛利数据。
- Weight：0.22

## 4. Evidence Chain

EV-20260710-RB-TE01 证明部分公司已有业务相关性，EV-20260710-RB-TE02 证明主题扩散路径存在，但 Missing Evidence 指向量产、客户、成本和毛利。反证要求保留“伪相关”和“收入滞后”风险。

## 5. M6 Scorecard

- Scorecard ID：SCORECARD-ROBOTICS-THEME-001
- Methodology Refs：`theme-expansion`, `counter-consensus`
- Evidence Chain Refs：EV-20260710-RB-TE01, EV-20260710-RB-TE02
- Theme Score：78
- Evidence Score：76
- Methodology Score：82
- Prompt Score：84
- Report Score：80
- Risk Score：74
- Confidence Score：70
- Overall Score：77
- Quality Gate：CONDITIONAL_PASS
- Disclaimer：仅供研究参考，不构成投资建议

## 6. 反方观点

人形机器人商业化节奏可能慢于主题传播；零部件企业即使技术相关，也未必形成规模收入；成本下降不足可能压制终端需求；客户集中度可能导致订单波动。

## 7. 不确定性与风险

主要不确定性来自量产时间、成本曲线、客户验证、收入确认和应用场景。Quality Gate 为 CONDITIONAL_PASS，是因为示例证据尚未充分证明规模交付。

## 8. 免责声明

本示例仅用于 AIRS 主题扩散流程演示，所有内容仅供研究参考，不构成投资建议。

