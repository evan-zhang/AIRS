# AIRS Orchestrator Architecture

免责声明：本文档仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## Role

Orchestrator 是 Planner 和 Runtime 之间的正式边界。Planner 负责生成 Research Plan 和 Runtime Workflow，Orchestrator 负责校验 Planner 输出、确认任务依赖闭合，并把合规 Workflow 交给 Runtime。Runtime 负责 Agent 调度、状态、事件和资源。

QA Sprint 2 决策：当前 Stable 主干采用薄 Orchestrator Facade，不新增业务编排逻辑，不替代 Planner 或 Runtime。

## Boundary

- Planner 描述研究目标、任务图、资源、预算、风险和 Runtime Workflow。
- Orchestrator 校验 Workflow 形状、任务唯一性、依赖存在性和 contract version。
- Runtime 执行 Workflow。
- Workspace 保存项目、会话、任务、产物、快照和审计。
- Skill、Prompt、Evidence、Knowledge Graph、Score 和 Report 按引用进入流程。

禁止事项：

- App 层不得直接实例化 `RuntimeCore`。
- Orchestrator 不直接调用 Connector、Evidence、KG、Score、Report 或业务 App。
- Runtime 不直接接收用户原始研究请求。

## Implementation

- Runtime boundary: `orchestrator/core.py`
- Shared contract: `common/contract.py`
- Contract validation: `common/contract_validation.py`
- APP-001 handoff: `apps/equity_research/app.py`

## FEATURE-008 Usage

Investment Research Engine 在 `pipeline.py` 中生成 Runtime Plan，并通过 `infrastructure_refs.orchestrator` 保留 Orchestrator 引用。Review Agent 和 Verification Agent 可以据此复核 Engine 是否遵守统一调度边界。
