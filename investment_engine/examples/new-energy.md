# 新能源 Investment Research Engine Case

免责声明：本案例仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## Investment Thesis

新能源 的研究价值来自需求驱动、供应链瓶颈和风险反证之间的动态平衡。

## Knowledge Graph

Graph: kg-new-energy；节点覆盖储能、电网消纳、新能源；边关系覆盖 depends_on 和 supports。

## Evidence Chain

Evidence cards: ev-01, ev-02, ev-03, ev-counter-01, ev-counter-02。包含支持证据、反方证据和缺失证据。

## Supply Chain Analysis

供应链关注储能、电网消纳、锂电材料、光伏逆变器，以及 StorageSystem A、Inverter B、BatteryMaterial C 的研究角色。

## Chokepoint Analysis

关键卡点包括储能和电网消纳，需用装机、并网、价格和政策证据复核。

## Score Card

质量门禁为 CONDITIONAL_PASS，仅表示研究质量可继续复核。

## Risk Analysis

主要风险包括需求兑现风险、竞争和利润率风险、政策或监管变化风险。

## Catalyst Analysis

催化剂包括招标披露、政策更新、并网改善和成本变化。

## Final Research Report

本案例通过 `investment_engine/examples/new_energy.py` 可执行生成完整结构化结果，Recommendation 覆盖 Fact、Inference、Assumption 和 Opinion。
