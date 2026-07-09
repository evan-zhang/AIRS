# AI Benchmark Template

**Benchmark ID**：BENCH-AI-TEMPLATE  
**行业分类**：ai  
**方法论引用**：`docs/methodology/supply-chain-chokepoint.md`, `docs/methodology/theme-expansion.md`, `docs/methodology/risk.md`  
**Prompt 引用**：`prompts/supply-chain/chokepoint-analysis.md`, `prompts/hot-topic/theme-expansion.md`  
**版本**：v0.7.0

**免责声明**：本 Benchmark 仅用于 AIRS 对 AI 产业研究能力的质量测试，不构成投资建议，不提供交易指令、价格预测或收益承诺。

## 1. 测试场景

AI 类用例重点测试 Agent 对算力、AI 服务器、GPU 供给、网络设备、液冷、电力和云厂商资本开支的研究能力。标准输入应要求 Agent 拆解供应链卡点、识别主题扩散路径，并说明数据滞后和资本开支周期的不确定性。

## 2. M4 Prompt 输入

- Prompt ID：`PROMPT-SUPPLY-CHAIN-CHOKEPOINT` 或 `PROMPT-THEME-EXPANSION`
- 研究问题：AI 服务器需求变化是否会形成可验证的供应链瓶颈？
- 研究范围：算力芯片、HBM、服务器 ODM、高速互联、液冷和数据中心电力。
- 输出要求：必须包含 M3 Evidence Card、Evidence Chain、M6 Scorecard、Quality Gate、反方观点、不确定性和免责声明。

## 3. M3 Evidence 要求

| Evidence ID | Evidence Level | Confidence | Weight | Supports | Refutes | Missing Evidence |
|-------------|----------------|------------|--------|----------|---------|------------------|
| EV-20260710-AI01 | A | HIGH | 0.25 | 云厂商 CapEx 或订单变化 | 需求仅为短期库存拉动 | 下游真实利用率 |
| EV-20260710-AI02 | B | MEDIUM | 0.20 | HBM、先进封装或网络设备瓶颈 | 供应扩产超预期 | 供应商产能指引 |

## 4. M6 Scorecard 要求

Scorecard 必须覆盖 Evidence Score、Methodology Score、Prompt Score、Report Score、Risk Score 和 Confidence Score。Quality Gate 只有在证据链包含供需两端和至少一个反证时才可为 PASS。

## 5. 反方观点与不确定性

必需反方观点：云厂商资本开支可能提前透支需求；模型推理效率提升可能削弱硬件增量；供应链扩产可能缓解短缺。不确定性必须标注数据口径、订单可见度和技术路线变化。

