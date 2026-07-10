# Workspace Lifecycle（生命周期）

## 1. 生命周期阶段

Workspace 生命周期覆盖 CREATED、PROJECT_ACTIVE、SESSION_OPEN、RESEARCH_RUNNING、REVIEWING、SNAPSHOTTED、EXPORTED 和 ARCHIVED。

## 2. 创建

Workspace 创建时生成 workspace_id，并初始化 Project Manager、Session Manager、Artifact Manager、Task Board、Memory、Snapshot、Version、Replay、Collaboration 和 Audit Log。

## 3. 项目阶段

Project 保存研究问题、范围、负责人、状态、引用和免责声明。Project 不保存无来源投资结论，所有结论性内容必须指向 Evidence、Scorecard、Report 或 Review Artifact。

## 4. 会话阶段

Session 包装一次 Runtime 工作流执行，保存 runtime_id、workflow_id、intent、refs 和状态。Runtime 执行产生的事件和最终状态以引用或快照方式进入 Workspace。

## 5. 复核与快照

Review Agent 可读取 Timeline、Artifact Registry、Snapshot 和 Audit Log。Snapshot 用于暂停、恢复、重放和验证，不允许被改写。

## 6. 导出与归档

Export Bundle 包含 projects、sessions、tasks、artifacts、timeline、snapshots 和 audit_log。归档项目必须保留免责声明和审计链。

---

免责声明：本文档和示例仅用于 AIRS 工程开发、投资研究流程编排与质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。
