# Semiconductor Benchmark Template

**Benchmark ID**：BENCH-SEMICONDUCTOR-TEMPLATE  
**行业分类**：semiconductor  
**方法论引用**：`docs/methodology/supply-chain-chokepoint.md`, `docs/methodology/industry-lifecycle.md`, `docs/methodology/financial-anomaly.md`  
**Prompt 引用**：`prompts/supply-chain/chokepoint-analysis.md`, `prompts/financial/anomaly-analysis.md`  
**版本**：v0.7.0

**免责声明**：本 Benchmark 仅用于 AIRS 半导体研究质量测试，不构成投资建议，不提供交易指令、价格预测或收益承诺。

## 1. 测试场景

半导体类用例测试 Agent 是否能区分设计、制造、设备、材料、EDA、封测和库存周期。研究问题应要求同时处理国产替代、先进制程、成熟制程供需、客户认证周期和财务异常。

## 2. M4 Prompt 输入

- Prompt ID：`PROMPT-SUPPLY-CHAIN-CHOKEPOINT`
- 研究问题：半导体关键设备或材料是否构成产业链卡点？
- 输出要求：M3 Evidence Card、Evidence Chain、M6 Scorecard、Quality Gate、反方观点、不确定性、免责声明。

## 3. M3 Evidence 要求

| Evidence ID | Evidence Level | Confidence | Weight | Supports | Refutes | Missing Evidence |
|-------------|----------------|------------|--------|----------|---------|------------------|
| EV-20260710-SC01 | A | HIGH | 0.25 | 公司订单、认证或收入结构变化 | 单一客户拉动不可持续 | 客户验证进度 |
| EV-20260710-SC02 | B | MEDIUM | 0.20 | 设备材料国产化缺口 | 海外供应恢复 | 行业库存数据 |

## 4. M6 Scorecard 要求

Scorecard 必须解释 Evidence Score、Methodology Score、Risk Score 和 Confidence Score。Quality Gate PASS 要求证据覆盖供给限制、需求来源、替代可能性和财务口径。

## 5. 反方观点与不确定性

反方观点应覆盖库存周期回落、客户验证失败、技术路线替代和贸易政策变化。不确定性必须说明设备交付周期、收入确认、客户集中度和出口管制边界。

