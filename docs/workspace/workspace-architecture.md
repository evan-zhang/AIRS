# Workspace Architecture（架构总览）

## 1. 定位

AI Research Workspace 是 AIRS V1.x 的统一研究工作空间，位于用户交互层和 Runtime 之间。它是 Project、Session、Task、Timeline、Artifact、Memory、Snapshot、Version、Replay、Collaboration 和 Audit 的统一入口，同时保持 Runtime 调度边界：Workspace 创建研究上下文，Runtime 执行 Agent 工作流。

## 2. 核心原则

- Workspace 是用户交互唯一入口。
- Runtime 仍是 Agent、Task、Message、Event 和 State 的唯一执行底座。
- Workspace 不直接调用 Methodology、Evidence、Knowledge Graph、Score、Evaluation 或 Report 业务模块，只保存引用。
- Evidence、Knowledge Graph、Report、Scorecard 和 Export 都必须以 Artifact 登记，并保留 refs。
- 所有状态变化进入 Audit Log，关键节点进入 Research Timeline。

## 3. 分层结构

```text
User
  -> AI Research Workspace
  -> Project / Session / Task Board
  -> Runtime Plan Reference
  -> Artifact Registry / Timeline / Snapshot
  -> Review / Replay / Export
```

## 4. 与 Runtime 的关系

Workspace 可以创建 project_id、session_id、workflow_id 和 runtime_id，并记录 Runtime 输出的 event_log、context_snapshot 和 final_state 引用。Workspace 不绕过 Task Dispatcher，不让 Workflow 直接驱动业务模块。

## 5. 输出对象

Workspace 输出 Workspace Dashboard、Project Registry、Session Registry、Task Board、Artifact Registry、Timeline、Snapshot、Version History、Replay Plan、Export Bundle 和 Audit Log。

---

免责声明：本文档和示例仅用于 AIRS 工程开发、投资研究流程编排与质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。
