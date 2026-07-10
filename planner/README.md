# Autonomous Research Planner

免责声明：本文档仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

`planner/` 是 FEATURE-009 的最小可运行实现。它位于 AIRS 最上层，负责把用户研究目标转换为结构化 Research Plan。Runtime 只能接收 Planner 生成的 Runtime Plan、Workflow Spec 和 Task Graph，不能直接接收原始用户请求。

## 组件

- `goal_parser.py`：解析原始研究目标。
- `intent_analyzer.py`：识别公司、行业、主题、供应链、卡点、政策、组合和对比研究意图。
- `scope_builder.py`：生成研究范围、边界和成功标准。
- `dependency.py`：生成组件依赖图和关键路径。
- `workflow.py`：生成 Orchestrator Workflow。
- `runtime.py`：生成带 Planner Gate 的 Runtime Plan。
- `resource.py`：估算 Connector、Methodology、Skill 和 Workspace 资源。
- `budget.py`：估算时间、成本和并发预算。
- `confidence.py`：估算计划置信度和不确定性。
- `optimizer.py`：去重资源、识别可并行任务和风险。
- `engine.py`：统一入口 `AutonomousResearchPlanner.plan()`。

## 输出

每个 Research Plan 都包含 Goal Analysis、Scope、Required Connectors、Methodologies、Skills、Runtime、Expected Evidence/KG、Execution Order、Estimated Cost/Time、Expected Deliverables、Confidence 和 Risks。
