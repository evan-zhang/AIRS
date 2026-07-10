# Plan Optimizer

免责声明：本文档仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## 职责

Plan Optimizer 对 Research Plan 做最后整理：去重 Connector、标记可并行任务、补充风险、确认不可绕过的门禁。

## 优化内容

- Deduplicate：去重 Connector 与 Skill 引用。
- Parallelize：识别 Connector Plan、Evidence Plan、KG Plan 等可并行阶段。
- Gate：确认 Planner、Evidence、Review 不可绕过。
- Risk：根据置信度和预算补充已知风险。

## 不做的事

Plan Optimizer 不改变研究结论、不删除反方证据要求、不把低置信计划改写成高置信计划。它只让计划更清晰、更可执行、更容易验证。

## 审计

优化结果写入 `optimization` 字段，供 Review Agent 和 Verification Agent 对比原始计划与优化计划。

## 与 Planner / Runtime 的关系

Plan Optimizer 是 Planner 输出前的最后一步。它可以标记可并行任务，但不能提前启动 Runtime。只有 Planning Engine 汇总优化结果、写入 Planner Gate 并生成 `planner_generated=true` 的 Runtime Plan 后，Runtime 才能进入调度阶段。

## 风险处理

当 Confidence Planner 给出较低置信度，Plan Optimizer 只能增加风险提示、补充复核要求或建议收窄 Scope，不能把计划强行改写为高置信。优化动作必须可审计，避免 Review Agent 无法判断计划为什么发生变化。
