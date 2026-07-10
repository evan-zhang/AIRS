# Investment Research Pipeline

免责声明：本文档仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## Pipeline Steps

1. Investment Request：接收 `request_id`、`topic`、`scope`、`time_horizon` 和可选约束。
2. Runtime Plan：生成 Workflow，明确 Agent、依赖和 expected output。
3. Theme Discovery：引用主题扩展方法论和热点 Prompt，形成研究问题。
4. Evidence Chain：通过 Connector 结果转化为 Evidence Card，并标注 supports、refutes、missing evidence。
5. Knowledge Graph：把 Evidence、供应链节点、依赖边和卡点绑定成图谱。
6. Score Card：使用 Score Engine 输出质量评分和 Gate。
7. Recommendation Standard：对每条关键语句标注 Fact、Inference、Assumption 或 Opinion。
8. Final Research Report：按照模板输出研究报告，保留证据、反方观点、不确定性和免责声明。

## Runtime Boundary

Workflow 只描述任务顺序，执行必须由 Runtime 调度。Engine 不直接驱动外部数据源，不绕过 Workspace 保存研究资产，不绕过 Evidence 生成证据卡。

## Review Boundary

Review Agent 应检查四类语句覆盖情况、证据链完整性、反方观点强度、缺失证据、Score Gate 和最终报告合规表达。Verification Agent 应运行 `scripts/validate_investment_engine.py` 和既有回归脚本。

## Outputs

每次 Pipeline 运行必须输出 Investment Thesis、Knowledge Graph、Evidence Chain、Supply Chain Analysis、Chokepoint Analysis、Score Card、Risk Analysis、Catalyst Analysis、Recommendation 和 Final Research Report。
