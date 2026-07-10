# APP-001 用户指南

免责声明：APP-001 生成内容仅供 AIRS 投资研究流程验证和研究参考，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## 适用场景

- 想快速生成某家上市公司的研究工作底稿。
- 想验证某个研究问题需要哪些证据、方法论、KG 和评分。
- 想比较两家公司在行业、供应链、风险或催化因素上的研究框架。
- 想把真实 Connector 不可用时的缺口显式记录下来。

APP-001 不适合用于实时交易、个性化投资建议或价格预测。

## 命令行使用

```bash
python -m apps.equity_research.app "分析 NVDA 的 AI 芯片供应链卡点和估值风险"
python -m apps.equity_research.app "分析 0867.HK 康哲药业的财务和风险" --markdown docs/tmp/cms.md
```

## Python 使用

```python
from apps.equity_research import run_equity_research

result = run_equity_research({
    "symbol": "TSM",
    "market": "US",
    "research_question": "分析 TSMC 在先进制程供应链中的行业位置和风险",
    "time_range": "最近12个月",
    "focus_areas": ["industry", "supply_chain", "financial", "risk"],
    "peer_companies": ["NVDA", "ASML"],
})

markdown = result["report"]["markdown"]
```

## 如何阅读输出

APP-001 的报告不是单一模型直接生成的文本，而是 Planner 先生成研究计划，Committee 进行范围审议，Runtime 执行任务图，Connector 采集或降级数据，Evidence Chain 组织证据，Knowledge Graph 记录公司、行业、风险和报告节点，Score Card 给出研究质量门禁，最后再由 Report Generator 汇总输出。

每个 section 有四类陈述：

- Facts：来自解析、Connector、AIRS 模块或追溯字段的事实记录。
- Inference：基于事实和方法论得到的推断，必须受证据置信度约束。
- Assumption：当前流程必须承认的假设、缺失证据或降级前提。
- Opinion：研究者或委员会层面的判断语气，不得转化为交易动作。

如果看到 `SKIP` 或 `Mock 降级`，表示真实数据不可用或未配置。该内容只能作为工程流程证据，不能作为真实投资研究结论。

## 质量门禁

- `PASS`：证据结构、追溯字段和报告格式满足当前门禁。
- `CONDITIONAL_PASS`：可输出研究底稿，但存在真实数据或复核缺口。
- `FAIL`：证据不足或格式不达标，应补充数据后重跑。

默认情况下 APP-001 会因为真实数据源未配置而输出 `CONDITIONAL_PASS`，这是合规降级，不是失败伪装。
