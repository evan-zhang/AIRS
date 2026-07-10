# AIRS Investment Research Engine

`investment_engine/` 是 FEATURE-008 的最小可运行研究引擎。它把 Runtime、Workspace、Data Connectors、Methodology、Skill、Prompt、Evidence、Knowledge Graph、Score 和 Report 的引用统一编排为一条可审计研究管线。

## 使用

```python
from investment_engine import run_research

result = run_research({
    "request_id": "ai-compute",
    "topic": "AI 算力",
    "scope": "AI 算力产业链卡点研究",
    "time_horizon": "6-12 months",
})
```

## 输出

引擎输出 Investment Thesis、Knowledge Graph、Evidence Chain、Supply Chain Analysis、Chokepoint Analysis、Score Card、Risk Analysis、Catalyst Analysis、Recommendation 和 Final Research Report。

## 合规边界

免责声明：本目录仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。Recommendation 必须区分 Fact、Inference、Assumption 和 Opinion。
