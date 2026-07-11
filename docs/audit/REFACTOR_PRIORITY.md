# AIRS Refactor Priority

审计日期：2026-07-10

## Release Gate

当前不建议发布 `v1.0.0 Stable`。建议先发布 `v1.0.0-rc2` 或 `Developer Preview`，并按以下顺序修复。

## P0: Stable 前必须完成

### P0-1: Orchestrator Decision

对应问题：AUDIT-001、TD-001

动作：

1. 明确当前 Stable 架构是 Planner -> Runtime，还是补薄 Orchestrator Facade。
2. 如果不补代码，必须修改文档与 release notes，不能继续承诺 Orchestrator 是可执行层。
3. `common/contract.py` 的职责保留为跨 Planner/Runtime 契约，不扩展业务逻辑。

验收：

- 架构图、README、docs/orchestrator 与代码入口一致。
- 不再出现“Orchestrator 执行编排”但无入口的说法。

### P0-2: Business Path Validation

对应问题：AUDIT-004、TD-002

动作：

1. 增加 contract/business validation，不替代旧 validate。
2. 验证 Planner 输出 task 能被 Runtime 执行。
3. 验证 APP-001 输出 Evidence/KG/Score/Report 的引用闭合。
4. 验证 Report quality gate failure 会传播到顶层状态。

验收：

- 至少一条本地不可 SKIP 的端到端业务语义测试。
- 失败时能指出是 contract、data、report 还是 quality gate 问题。

### P0-3: Real Data Readiness Gate

对应问题：AUDIT-003、TD-003

动作：

1. 定义 real-mode release case。
2. 输出 `real_sources`、`mock_sources`、`skipped_sources`、`fallback_sources`。
3. 如果真实行情/财务不可用，则 release notes 明确排除该能力。

验收：

- 至少一个真实公共源成功，不允许全部 fallback。
- Mock 不能被计入真实证据。

### P0-4: App-Core Contract Validation

对应问题：AUDIT-002、AUDIT-006、TD-004、TD-005

动作：

1. APP-001 结果接统一 Evidence/KG/Score schema validator。
2. 明确 App-local analyzer 是 adapter，不是替代 Core。
3. Scorecard 字段语义统一。

验收：

- APP-001 的 Evidence refs、KG refs、Score refs、Report refs 闭合。
- App 输出不通过 validator 时必须失败或标记 `failed_quality_gate`。

### P0-5: Public Deployment Guardrail

对应问题：AUDIT-008、TD-006

动作：

1. 公网部署前增加 API key。
2. 限制 CORS。
3. 增加 request size limit 和 rate limit。
4. 区分 local/demo/prod profile。

验收：

- 默认公网不可裸跑。
- docs/deployment 明确生产最低安全配置。

## P1: Stable 后第一轮

### P1-1: Extract ScorecardBuilder

把 Investment Engine 和 APP-001 的评分逻辑收敛到一个 builder 或 service。

### P1-2: Artifact Source-of-Truth Manifest

为 Schema、Template、Prompt、Skill 建立 manifest，标注 source、generated、example、deprecated。

### P1-3: Memory Lifecycle Model

定义 Runtime Memory、Workspace Memory、Learning Memory 的读写边界和持久化策略。

### P1-4: Template Index Cleanup

明确 core report template、app report template、builder scaffold 的关系。

## P2: 可延期维护项

1. 清理 `src/`。
2. 清理或迁移 `builder-output/`。
3. 合并旧 validate 脚本。
4. 归档历史 examples。
5. 将 docs 中的 Feature completion report 与当前 Stable scope 对齐。

## Recommended Module Actions

删除：暂不删除。

合并：

- APP-001 score 与 Investment Engine score。
- APP-001 KG 构造与 `knowledge_graph` validator/builder。
- 重复 report templates 的索引和命名。

保留：

- Planner 和 Runtime：保留为当前最小主干。
- `common/contract.py`：保留，但限制在契约映射职责。
- Data Connectors：保留 mock/real 双模式，但发布时严格标注状态。
- Report Generator：保留，是当前边界相对清晰的模块。
- Committee：保留，但作为 review gate，不应替代 evidence validation。

## Next QA Sequence

1. `common/contract.py` contract QA。
2. Planner -> Runtime execution QA。
3. APP-001 output closure QA。
4. Connector real-mode QA。
5. Report quality gate QA。
6. API local security QA。
7. Original 25 validate scripts regression QA。
