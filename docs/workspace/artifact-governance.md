# Artifact Governance（产物治理）

## 1. 职责

Artifact Manager 统一登记 Evidence Bundle、Knowledge Graph、Scorecard、Report、Review Note、Runtime Export 和 Workspace Export。Artifact 是可复核研究产物的索引，不替代原始证据。

## 2. 必需字段

Artifact 包含 artifact_id、project_id、session_id、artifact_type、title、uri、refs、metadata、status、created_at 和 disclaimer。

## 3. 类型

推荐类型包括 evidence_bundle、knowledge_graph、scorecard、research_report、review_report、runtime_export、workspace_export 和 replay_plan。

## 4. 版本

Version Manager 对 Artifact 追加版本记录。版本必须说明 change_summary 和 refs，禁止覆盖旧版本。

## 5. 合规

Report 和 Review Artifact 必须保留反方观点、不确定性、证据引用和免责声明。任何交易指令、目标价或收益承诺都应被 Quality Gate 拒绝。

---

免责声明：本文档和示例仅用于 AIRS 工程开发、投资研究流程编排与质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。
