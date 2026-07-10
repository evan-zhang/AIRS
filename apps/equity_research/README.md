# APP-001 Equity Research App 使用说明

APP-001 是 AIRS 的首个可直接运行的股票研究应用。它接收股票代码、公司名称或研究问题，按 AIRS 全链路生成结构化研究结果：Request Parser、Company Resolver、Planner、Committee、Runtime、Connector、Investment Engine、Evidence、Knowledge Graph、Score、Report、Memory 与 Learning。

免责声明：APP-001 仅用于投资研究流程编排、证据追溯和研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## 快速使用

```bash
python -m apps.equity_research.app "分析 NVDA 的财务、估值、供应链和风险"
python -m apps.equity_research.app "比较 NVIDIA 和 TSMC 在 AI 算力供应链中的位置" --markdown /tmp/nvda-tsmc.md
```

也可以在 Python 中调用：

```python
from apps.equity_research import run_equity_research

result = run_equity_research({
    "symbol": "NVDA",
    "market": "US",
    "research_question": "分析 NVIDIA 的财务、估值、供应链和风险",
    "focus_areas": ["financial", "valuation", "supply_chain", "risk"],
})
print(result["report"]["markdown"])
```

## 输入字段

- `symbol`：股票代码，如 `NVDA`、`TSM`、`2330.TW`、`0867.HK`。
- `company_name`：公司名称；代码缺失时用于 Resolver 本地目录匹配。
- `market`：市场，支持 `US`、`HK`、`TW`、`CN`。
- `research_question`：研究问题，建议包含研究范围。
- `time_range`：时间范围，默认最近 12 个月。
- `focus_areas`：研究重点，支持 `profile`、`industry`、`supply_chain`、`financial`、`valuation`、`catalyst`、`risk`。
- `peer_companies`：对比公司代码或名称列表。
- `risk_preference`：`conservative`、`balanced`、`aggressive`，只影响研究风险提示语气，不生成交易建议。

## 输出

输出包含 15 个 section：

1. Executive Summary
2. Company Profile
3. Industry Position
4. Supply Chain / Chokepoint
5. Financial Analysis
6. Valuation
7. Catalysts
8. Risks
9. Counter View
10. Evidence Chain
11. Knowledge Graph
12. Score Card
13. Committee Decision
14. Final Report
15. Appendix (Sources / Traceability)

每个 section 都必须严格拆分 `Facts`、`Inference`、`Assumption`、`Opinion`。真实 Connector 不可用时输出 `SKIP` 或降级说明，不允许用 Mock 数据冒充真实研究证据。

## 降级规则

- Connector 返回 `mode=mock`：保留追溯字段，并在 `degradation_notes` 中说明。
- Connector 抛错或不可用：写入 `SKIP`，并保留失败原因。
- 公司无法识别：`resolver_status=NEED_REVIEW`，后续公司特定结论降级。
- Evidence 不足：Score Card 输出 `CONDITIONAL_PASS` 或 `FAIL`，Committee 二次审议。

