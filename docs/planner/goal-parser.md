# Goal Parser

免责声明：本文档仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## 职责

Goal Parser 将用户研究目标转为 `Research Goal`。它不判断研究结论，不选择执行 Agent，只负责把原始目标变成可审计输入。

## 输入

- 原始目标文本，例如“分析 AI 服务器供应链卡点”。
- 可选结构化字段：`goal_id`、`goal_type`、`subject`、`time_horizon`、`constraints`、`success_criteria`。

## 输出

标准输出包含：

- `goal_id`
- `raw_goal`
- `goal_type`
- `subject`
- `time_horizon`
- `constraints`
- `success_criteria`
- `disclaimer`

## 分类规则

Goal Parser 使用保守关键词识别目标类型。识别不到时默认进入 `theme`，由 Intent Analyzer 再做二次确认。这个默认值可以保证 Planner 不因自然语言模糊而跳过计划阶段。

## 失败处理

空目标直接失败；缺少 `goal_id` 或 `raw_goal` 的结构化输入失败。失败结果应返回给 Planner，而不是传给 Runtime。
