# Counter Argument

免责声明：本文档仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## 目标

Counter Argument 是 AIC 的强制环节，用于避免确认偏误、叙事过度拟合和单一路径外推。它复用 AIRS 既有反共识方法论，不在 Committee 内重新定义研究框架。

## 反方类型

- 数据反方：不同数据源或时间窗口给出不同结论。
- 逻辑反方：因果链中存在跳跃、遗漏变量或循环论证。
- 场景反方：政策、供需、技术路线、竞争格局变化导致结论失效。
- 时间反方：短期景气和长期竞争力方向不同。

## 处理方式

Devil's Advocate 的反方观点不能被简单删除。Moderator 必须把反方观点映射为降级条件、后续任务或 Minority Report。若反方证据强于支持证据，投票应转为 `CONDITIONAL_APPROVE` 或 `REJECT`。

Counter Argument 审查 Planner 给出的研究假设，并影响 Research Engine 的执行范围和后续补证任务。
