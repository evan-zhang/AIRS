# ADR-0007：AI Research Workspace

## Status

Accepted

## Context

FEATURE-006 已提供 Research Agent Runtime，但用户入口、项目管理、会话管理、产物治理、快照、重放、导出和协作审计仍分散。AIRS 需要一个统一 Research Workspace，把 Runtime、Workflow、Agent、Evidence、Knowledge Graph、Scorecard、Report 和 Review 产物组织到同一工作空间中。

## Decision

新增 `workspace/` 作为 AI Research Workspace 最小可运行实现，新增 `docs/workspace/`、`schemas/workspace/`、`templates/workspace-dashboard-template.md`、`workspace/examples/` 和 `scripts/validate_workspace.py`。Workspace 是用户交互唯一入口，但 Agent 执行仍由 Runtime 调度。

## Consequences

- Project、Session、Task Board、Artifact、Timeline、Snapshot、Version、Replay、Export、Collaboration 和 Audit 具备统一 API。
- Evidence、Knowledge Graph、Scorecard 和 Report 以 Artifact refs 进入 Workspace，不复制业务规则。
- Review Agent 和 Verification Agent 可以通过 Snapshot、Replay Plan、Export Bundle 和 Audit Log 复核研究过程。
- 当前实现为内存型最小可运行版本，后续可接入持久化存储、权限系统和外部协作界面。

## Compliance

Workspace 不生成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。所有示例和模板保留免责声明。

免责声明：本文档和示例仅用于 AIRS 工程开发、投资研究流程编排与质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。
