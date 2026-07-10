# AIRS Orchestrator Architecture

免责声明：本文档仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## Role

Orchestrator 是 Runtime 上层的研究流程描述层。它定义阶段、依赖、输入输出和质量门禁，但不直接调用外部数据源、不直接生成 Evidence Card、不绕过 Runtime 执行 Agent。

## Boundary

- Orchestrator 描述 Workflow。
- Runtime 执行 Workflow。
- Workspace 保存项目、会话、任务、产物、快照和审计。
- Skill、Prompt、Evidence、Knowledge Graph、Score 和 Report 按引用进入流程。

## FEATURE-008 Usage

Investment Research Engine 在 `pipeline.py` 中生成 Runtime Plan，并通过 `infrastructure_refs.orchestrator` 保留 Orchestrator 引用。Review Agent 和 Verification Agent 可以据此复核 Engine 是否遵守统一调度边界。
