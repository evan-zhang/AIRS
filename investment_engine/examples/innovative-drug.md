# 创新药 Investment Research Engine Case

免责声明：本案例仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## Investment Thesis

创新药 的研究价值来自需求驱动、供应链瓶颈和风险反证之间的动态平衡。

## Knowledge Graph

Graph: kg-innovative-drug；节点覆盖临床管线、适应症扩展、创新药；边关系覆盖 depends_on 和 supports。

## Evidence Chain

Evidence cards: ev-01, ev-02, ev-03, ev-counter-01, ev-counter-02。包含支持证据、反方证据和缺失证据。

## Supply Chain Analysis

供应链关注临床管线、适应症扩展、医保谈判、出海授权，以及 BioPipeline A、ClinicalCRO B、LicenseOut C 的研究角色。

## Chokepoint Analysis

关键卡点包括临床管线和适应症扩展，需用临床进度、支付环境、商业化和监管证据复核。

## Score Card

质量门禁为 CONDITIONAL_PASS，仅表示研究质量可继续复核。

## Risk Analysis

主要风险包括需求兑现风险、竞争和利润率风险、政策或监管变化风险。

## Catalyst Analysis

催化剂包括临床数据披露、监管更新、授权合作或商业化进展。

## Final Research Report

本案例通过 `investment_engine/examples/innovative_drug.py` 可执行生成完整结构化结果，Recommendation 覆盖 Fact、Inference、Assumption 和 Opinion。
