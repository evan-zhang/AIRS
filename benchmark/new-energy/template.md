# New Energy Benchmark Template

**Benchmark ID**：BENCH-NEW-ENERGY-TEMPLATE  
**行业分类**：new-energy  
**方法论引用**：`docs/methodology/industry-lifecycle.md`, `docs/methodology/policy-driven.md`, `docs/methodology/risk.md`  
**Prompt 引用**：`prompts/risk/analysis.md`, `prompts/industry/lifecycle-analysis.md`  
**版本**：v0.7.0

**免责声明**：本 Benchmark 仅用于 AIRS 新能源研究质量测试，不构成投资建议，不提供交易指令、价格预测或收益承诺。

## 1. 测试场景

新能源类用例测试 Agent 是否能处理电池材料、储能、光伏、风电、充电网络和电网消纳。研究必须区分政策驱动、供需周期、成本曲线和产能过剩风险。

## 2. M4 Prompt 输入

- Prompt ID：`PROMPT-RISK-ANALYSIS`
- 研究问题：某新能源细分环节处于产业生命周期的哪个阶段，主要风险是什么？
- 输出要求：M3 Evidence Card、Evidence Chain、M6 Scorecard、Quality Gate、反方观点、不确定性和免责声明。

## 3. M3 Evidence 要求

| Evidence ID | Evidence Level | Confidence | Weight | Supports | Refutes | Missing Evidence |
|-------------|----------------|------------|--------|----------|---------|------------------|
| EV-20260710-NE01 | A | HIGH | 0.25 | 政策或装机数据支持需求 | 补贴退坡削弱需求 | 地区消纳数据 |
| EV-20260710-NE02 | B | MEDIUM | 0.20 | 成本下降支持渗透率提升 | 产能过剩压制盈利 | 企业开工率 |

## 4. M6 Scorecard 要求

Scorecard 必须覆盖 Methodology Score、Evidence Score、Risk Score、Confidence Score。Quality Gate PASS 要求供需、政策、成本和风险证据均有记录。

## 5. 反方观点与不确定性

反方观点应包括产能过剩、价格下行、政策调整、海外贸易限制和电网消纳约束。不确定性必须标注数据口径、政策执行和周期位置。

