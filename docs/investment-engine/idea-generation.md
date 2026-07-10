# Investment Idea Generation

免责声明：本文档仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## Inputs

Idea Generation 接收主题、行业、公司、政策、供应链、新闻和财务线索。所有外部信息必须通过 Data Connectors 进入 Evidence Card，不能直接把未追溯文本写入最终结论。

在 Engine 中，Idea Generation 由 Runtime 调度的研究任务触发，Workspace 记录输入、产物和审计轨迹。

## Method

Engine 使用三层过滤：

- Theme Signal：需求扩张、供给约束、政策催化、竞争格局。
- Evidence Strength：证据等级、置信度、来源优先级、反方证据。
- Research Fit：是否能形成可验证命题、是否存在清晰证据缺口、是否能被 Review Agent 复核。

## Idea To Thesis

一个 idea 只有在具备至少两张支持证据卡、一条反方证据、一项缺失证据和可解释 Score 后，才能进入 Investment Thesis。否则只能作为观察项进入 Workspace Task Board。

## Compliance

Idea 不是投资建议。Idea Generation 不输出买卖方向、不输出目标价、不承诺收益，也不触发自动交易。所有结果只用于研究优先级排序和质量控制。
