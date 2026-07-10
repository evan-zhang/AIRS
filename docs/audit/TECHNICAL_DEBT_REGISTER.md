# AIRS Technical Debt Register

审计日期：2026-07-10

## TD-001: Orchestrator Boundary Debt

严重级别：Blocker

状态：Partially fixed in QA-SPRINT-2

涉及文件：`docs/orchestrator/*`、`planner/engine.py`、`planner/runtime.py`、`runtime/core.py`、`common/contract.py`

问题描述：Orchestrator 是架构文档中的关键层，但运行代码没有对应模块。Planner 和 Runtime 直接承担了编排与任务转换。

影响：架构承诺与实现不一致；未来补 Orchestrator 时会引发职责迁移。

根因：文档先行，最小实现直接连通 Planner 和 Runtime。

建议方案：Stable 前选择明确降级或实现薄 Orchestrator Facade。

是否应在 v1.0 发布前修复：是。

QA-SPRINT-2 处理：新增 `orchestrator/core.py` 薄 Facade，并将 APP-001 Runtime handoff 改为 `run_planned_workflow()`。剩余工作是后续将更多测试和文档入口统一到 Orchestrator。

## TD-002: Validation Signal Debt

严重级别：High

状态：Partially fixed in QA-SPRINT-2

涉及文件：`scripts/validate_*.py`、`tests/production-e2e/*`、`tests/integration/*`

问题描述：验证偏向文件、文档、import 和演示运行，业务语义断言不足。

影响：测试通过不能证明真实链路成立。

根因：Feature 交付验收脚本累计，没有统一发布门禁。

建议方案：新增 contract validation 和 business-path validation；旧脚本保留为 artifact checks。

是否应在 v1.0 发布前修复：是。

QA-SPRINT-2 处理：新增 `scripts/validate_architecture_stabilization.py`，覆盖 Orchestrator、APP-Core contract、mock evidence policy 和 API bind security。

## TD-003: Real Data Readiness Debt

严重级别：High

状态：Partially fixed in QA-SPRINT-2

涉及文件：`data_connectors/*`、`apps/equity_research/data_collector.py`、`tests/integration/test_*_real.py`

问题描述：默认 Mock，部分真实源失败 fallback/skip。真实数据可用性不是硬门禁。

影响：产品可演示但不可证明真实研究可用。

根因：离线回归优先。

建议方案：Stable 前至少一个端到端 real-mode case 必须通过；输出 fallback 明细。

是否应在 v1.0 发布前修复：是。

QA-SPRINT-2 处理：Connector traceability 增加 mode，APP-001 输出 `data_lineage`，Mock/SKIP 不可标记为 Fact。剩余工作是配置并验证不可 SKIP 的 real-mode release case。

## TD-004: App-Core Boundary Debt

严重级别：High

状态：Partially fixed in QA-SPRINT-2

涉及文件：`apps/equity_research/*`、`investment_engine/pipeline.py`、`knowledge_graph/*`、`schemas/evidence/*`、`schemas/score/*`

问题描述：APP-001 调用 Core，但本地构造 Evidence/KG/Score。

影响：Core 能力复用不充分，App 可能成为第二套研究引擎。

根因：快速产品化演示时直接拼装输出对象。

建议方案：先接统一 validators，再逐步抽 builder。

是否应在 v1.0 发布前修复：是，至少接 validator。

QA-SPRINT-2 处理：新增 `common/contract_validation.py`，APP-001 输出必须通过 Evidence/KG/Score/Report 引用闭合校验。

## TD-005: Score Engine Runtime Debt

严重级别：High

涉及文件：`scoring/*`、`schemas/score/*`、`investment_engine/pipeline.py`、`apps/equity_research/analyzer.py`

问题描述：评分方法和 Schema 存在，运行时评分逻辑分散。

影响：质量门禁语义不稳定。

根因：Score Engine 未形成独立 runtime module。

建议方案：短期统一质量门禁字段语义；中期抽 `ScorecardBuilder`。

是否应在 v1.0 发布前修复：部分。

## TD-006: API Production Hardening Debt

严重级别：High

状态：Partially fixed in QA-SPRINT-2

涉及文件：`api/server.py`、`docker/*`、`docs/deployment/*`

问题描述：API 无鉴权、CORS `*`、无请求限制，不适合公网。

影响：公网测试有安全和成本风险。

根因：当前目标是本地演示。

建议方案：公网部署前必须增加 API key、CORS allowlist、request size limit、rate limit、环境隔离。

是否应在 v1.0 发布前修复：是，如果 Stable 包含公网测试。

QA-SPRINT-2 处理：默认 localhost，非本地绑定必须设置 `AIRS_API_KEY`，新增 CORS allowlist、请求体限制和错误脱敏。剩余工作是速率限制和生产部署 profile。

## TD-007: Artifact Source-of-Truth Debt

严重级别：Medium

涉及文件：`schemas/*`、`templates/*`、`prompts/*`、`skills/*`、`docs/*`

问题描述：同一概念在 Schema、Template、Prompt、Skill、Docs 中多处表达，缺少 authoritative registry。

影响：长期维护会出现字段漂移。

根因：多条产品线并行沉淀。

建议方案：新增 source-of-truth manifest；不必先做自动生成。

是否应在 v1.0 发布前修复：是，文档级修复。

## TD-008: Workspace / Memory / Learning Lifecycle Debt

严重级别：Medium

涉及文件：`workspace/*`、`runtime/memory_manager.py`、`learning/*`

问题描述：Memory 概念分散，Workspace、Runtime、Learning 的持久化边界不清。

影响：复盘、学习、数据隔离和多用户部署风险。

根因：各 Feature 各自实现局部闭环。

建议方案：定义三层 Memory 生命周期，暂不必全面重写。

是否应在 v1.0 发布前修复：部分。

## TD-009: Degradation Status Debt

严重级别：Medium

涉及文件：`apps/equity_research/report_exporter.py`、`apps/equity_research/app.py`、`api/routes/research.py`

问题描述：降级、SKIP、质量门禁失败没有统一映射到顶层任务状态。

影响：用户可能误读“完成”为“高质量完成”。

根因：演示优先，容错输出优先于失败传播。

建议方案：统一 `completed`、`completed_with_degradation`、`failed_quality_gate`。

是否应在 v1.0 发布前修复：是。

## TD-010: Directory Semantics Debt

严重级别：Low

涉及文件：`src/`、`builder/`、`builder-output/`、`examples/`、`demo/output/`

问题描述：源码、脚手架、生成物、示例输出混在同一仓库层级。

影响：贡献者认知成本高。

根因：研发资产累积。

建议方案：先文档标注，不立即删除。

是否应在 v1.0 发布前修复：否。
