# Project Management（项目管理）

## 1. 职责

Project Manager 管理研究项目的创建、状态、范围、引用和负责人。它把用户研究意图转化为可追踪 project_id，是 Workspace 内所有 Session、Artifact、Timeline 和 Audit 记录的上游锚点，但不直接生成研究结论。

## 2. Project 字段

Project 包含 project_id、name、research_question、scope、owner、status、refs、created_at、updated_at 和 disclaimer。

## 3. 状态

推荐状态包括 ACTIVE、PAUSED、REVIEWING、COMPLETED 和 ARCHIVED。状态变化必须写入 Audit Log。

## 4. 约束

- 研究问题必须清晰可复核。
- scope 应包含行业、公司、时间段或数据边界。
- refs 指向 Methodology、Evidence、Runtime、Knowledge Graph、Report 或 Review 文档。
- Project 不提供买入、卖出、持有、目标价或收益承诺。

## 5. Dashboard

Project Dashboard 至少展示 Project、Sessions、Task Board、Artifacts、Timeline 和 Disclaimer。

---

免责声明：本文档和示例仅用于 AIRS 工程开发、投资研究流程编排与质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。
