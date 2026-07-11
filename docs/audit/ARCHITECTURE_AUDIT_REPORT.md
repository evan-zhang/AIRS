# AIRS Architecture Audit Report

审计日期：2026-07-10
审计对象：AIRS 当前 Git Repository（main）
审计角色：CTO Review Agent
审计约束：不新增功能，不修改生产代码，不提交 PR，不以测试 PASS 作为设计正确的充分条件。
状态说明：本文件记录 QA Sprint 2 开始前的审计基线；修复状态见 `docs/qa/ARCHITECTURE_STABILIZATION_REPORT.md` 和 `docs/audit/TECHNICAL_DEBT_REGISTER.md`。

## Executive Verdict

当前 AIRS 不建议标记为 `v1.0.0 Stable`。

可以发布为 `v1.0.0-rc`、`developer preview` 或 `architecture prototype`，但 Stable 发布前必须修复真实链路、契约一致性和验证有效性问题。当前系统的主要价值是“研究系统骨架、文档、示例和本地可运行演示”，不是“生产可依赖的公网研究平台”。

最大风险不是单点 bug，而是 Core、App、测试、文档之间存在多处“看起来串起来，实际业务语义没有真正闭合”的链路。

## Scope

本次审计覆盖：

- Planner -> Orchestrator -> Runtime
- Connector -> Evidence -> Knowledge Graph
- Methodology -> Prompt -> Skill
- Score -> Committee -> Report
- Workspace -> Memory -> Learning
- Core -> Apps -> API -> CLI -> Web
- `common/contract.py` 等跨模块契约
- `schemas/`、`templates/`、`prompts/`、`skills/`、`scripts/validate_*`
- APP-001 Equity Research App 是否复用 Core

## Critical Findings

### AUDIT-001: Orchestrator 是文档概念，不是可执行模块

严重级别：Blocker

QA Sprint 2 状态：Partially fixed。已新增薄 Orchestrator Facade，并将 APP-001 Runtime handoff 改为 Orchestrator 入口。

涉及文件：

- `docs/orchestrator/orchestrator-architecture.md`
- `planner/engine.py`
- `planner/runtime.py`
- `runtime/core.py`
- `common/contract.py`

问题描述：

架构链路宣称为 Planner -> Orchestrator -> Runtime，但仓库中没有顶层 `orchestrator/` Python 模块。Planner 直接生成 `required_runtime`，Runtime 直接消费 workflow/task spec，`common/contract.py` 直接承担 Planner task 到 Runtime agent 的映射。Orchestrator 目前主要存在于文档引用中。

影响：

- 架构图和实现不一致。
- 未来如果真的补 Orchestrator，会与 `planner/runtime.py`、`runtime/core.py` 和 `common/contract.py` 的职责重叠。
- 当前 “Planner -> Orchestrator -> Runtime” 不能作为 Stable 的真实运行承诺。

根因：

Feature-driven 增量开发时，文档层先定义了 Orchestrator，但实现层把编排逻辑内联进 Planner 和 Runtime。

建议方案：

- v1.0 前二选一：要么明确降级为 Planner -> Runtime，并把 Orchestrator 标为 future architecture；要么补一个薄 Orchestrator Facade，统一持有 workflow validation、task normalization、contract negotiation。
- 不建议大规模重写。先把 Orchestrator 边界定义为“只做编排契约和验证，不做业务分析”。

是否应在 v1.0 发布前修复：是。

### AUDIT-002: APP-001 调用 Core，但重复构造 Evidence / KG / Score

严重级别：High

QA Sprint 2 状态：Partially fixed。已新增 Core contract validation，APP-001 输出必须通过 Evidence/KG/Score/Report 引用闭合校验。

涉及文件：

- `apps/equity_research/app.py`
- `apps/equity_research/analyzer.py`
- `apps/equity_research/data_collector.py`
- `investment_engine/pipeline.py`
- `knowledge_graph/builder.py`
- `report_generator/pipeline.py`
- `schemas/evidence/evidence-card.schema.json`
- `schemas/knowledge-graph/knowledge-graph.schema.json`
- `schemas/score/scorecard.schema.json`

问题描述：

APP-001 确实调用了 `planner.plan_research`、`RuntimeCore().run_workflow`、`committee.run_committee`、`investment_engine.run_research` 和 `learning.ContinuousImprovementEngine`。但是 APP-001 的 `EquityResearchAnalyzer` 又自行构造 `evidence_chain`、`knowledge_graph`、`score_card`，而不是通过统一的 Evidence Engine、Knowledge Graph Builder 或 Score Engine。

影响：

- APP-001 的输出可能符合演示，但不能证明 Core 的 Evidence/KG/Score 能力被真实复用。
- Schema 漂移风险高：App 内字段、Investment Engine 内字段、Schema 文件之间可能逐渐不一致。
- Core 与 App 职责混乱：App 既是编排层，也是半个研究引擎和半个评分引擎。

根因：

为了快速完成产品化演示，App 层直接拼接核心结构，绕开了部分 Core 模块。

建议方案：

- Stable 前至少把 APP-001 标记为 “Core-assisted app”，不能宣称为完整 Core-driven app。
- 后续将 `EquityResearchAnalyzer._build_knowledge_graph` 替换为 `knowledge_graph` 模块调用，将 `_build_score_card` 替换为统一 Score Engine 或明确保留为 App-local score adapter。
- 增加一条验证：APP-001 结果必须由 Core KG/Score validator 校验，而不仅是字段存在。

是否应在 v1.0 发布前修复：是，至少要完成边界声明和验证补强；完整抽离可延期。

### AUDIT-003: Connector 默认 Mock，真实链路通过不等于真实数据成立

严重级别：High

QA Sprint 2 状态：Partially fixed。已新增 connector lineage 和 mock/skip evidence policy；不可 SKIP 的 real-mode release gate 仍待下一轮。

涉及文件：

- `data_connectors/env_config.py`
- `data_connectors/connectors/yahoo_finance.py`
- `data_connectors/connectors/alpha_vantage.py`
- `data_connectors/connectors/news.py`
- `data_connectors/connectors/sec_edgar.py`
- `data_connectors/connectors/rss.py`
- `apps/equity_research/data_collector.py`
- `tests/integration/test_*_real.py`

问题描述：

Connector 支持 real/mock 双模式，但默认 `AIRS_CONNECTOR_MODE=mock`。Yahoo Finance 和 Alpha Vantage 当前仍是 Mock；部分真实源失败时会 fallback 到 Mock 或测试 SKIP。APP-001 正确记录了 Mock/SKIP 降级，但产品层仍容易给人“研究链路已真实可用”的错觉。

影响：

- 生产测试可能拿到结构完整但事实不可用的研究结果。
- 外部测试者可能误以为行情、财务、新闻和监管数据都已真实接入。
- “测试通过”主要证明容错和结构，不证明数据质量。

根因：

为了离线回归和无凭证环境可运行，默认采用 Mock；但验证体系没有把 “真实源可用率” 作为发布门禁。

建议方案：

- Stable 前增加 release gate：至少一个端到端 case 必须在 real mode 下跑通，并输出真实源清单、fallback 清单、SKIP 清单。
- API/Web 默认页面必须显式展示 Mock/SKIP 状态。
- 将 Yahoo/Alpha Vantage 的 Mock 状态列入 Stable blocking risk，或从 Stable 声明中剔除行情/估值能力。

是否应在 v1.0 发布前修复：是。

### AUDIT-004: validate_* 更像交付物检查，不足以证明业务链路

严重级别：High

QA Sprint 2 状态：Partially fixed。已新增 `scripts/validate_architecture_stabilization.py` 覆盖核心行为断言。

涉及文件：

- `scripts/validate_*.py`
- `tests/production-e2e/e2e_harness.py`
- `tests/integration/test_connector_to_evidence.py`
- `scripts/validate_productization.py`

问题描述：

仓库有 25 个 `validate_*` 脚本，但大量检查集中在文件存在、文档存在、import 成功、示例可运行。脚本中几乎没有 `assert`、没有 JSON Schema 严格校验，也没有对真实业务语义做强断言。部分 e2e 允许 Mock/SKIP，真实外部源失败时测试可 SKIP。

影响：

- 25+ PASS 容易造成错误信心。
- 真实链路断裂、Schema 漂移、App 绕开 Core 等问题可能仍然通过。
- 发布质量门禁不够硬。

根因：

验证脚本承袭 Feature 验收方式，目标是证明交付物存在和最小运行，而不是证明生产业务语义成立。

建议方案：

- Stable 前建立三层验证：artifact validation、contract validation、business-path validation。
- 每条核心链路至少一条不可 SKIP 的本地语义测试。
- 对 `common/contract.py`、APP-001、ReportPipeline 增加 schema-driven validation。

是否应在 v1.0 发布前修复：是。

### AUDIT-005: Schema / Template / Prompt / Skill 缺少单一契约源

严重级别：High

涉及文件：

- `schemas/**`
- `templates/**`
- `prompts/**`
- `skills/**`
- `docs/methodology/**`
- `docs/prompt-engine/**`
- `docs/skill-engine/**`

问题描述：

同一业务对象在多处表达：JSON Schema、Markdown template、Prompt DSL、Skill 文档、Builder template、Product docs。当前没有 manifest 或 registry 明确说明哪个是 source of truth，哪个是生成物，哪个只是示例。

影响：

- Schema 与模板字段可能逐步漂移。
- Prompt/Skill 的版本与 App/Report 输出无法稳定追踪。
- Builder 模板与运行时模板容易重复演进。

根因：

平台同时建设了 Core、Builder、Prompt、Skill、Docs，缺少统一 artifact registry。

建议方案：

- Stable 前至少新增一份审计级 manifest 或在 docs 中声明 source of truth，不必先开发工具。
- 后续再考虑生成式校验：schema -> template required fields -> validate scripts。

是否应在 v1.0 发布前修复：是，文档级声明即可；自动化可延期。

### AUDIT-006: Score Engine 物理上主要是文档，运行时评分散落在 App 和 Investment Engine

严重级别：High

涉及文件：

- `scoring/*.md`
- `schemas/score/scorecard.schema.json`
- `investment_engine/pipeline.py`
- `apps/equity_research/analyzer.py`
- `committee/coordinator.py`
- `report_generator/pipeline.py`

问题描述：

仓库有 `scoring/` 文档和 `schemas/score`，但没有对应 `score_engine/` Python 模块。实际 scorecard 分别在 `InvestmentResearchPipeline._build_scorecard` 和 `EquityResearchAnalyzer._build_score_card` 中构造。

影响：

- Committee 与 Report 依赖 Scorecard，但 Score 不是独立可复用服务。
- App 和 Engine 两套评分逻辑可能产生不同含义的 `overall_score`、`quality_gate`。
- 未来扩展行业/资产类别时，评分规则会被复制。

根因：

M6/Score 先以文档与 schema 形式落地，运行实现被调用方局部实现。

建议方案：

- Stable 前在报告中明确 Score Engine 是 “schema + methodology + local calculators”，不是独立 Core module。
- 发布后第一优先级抽出 `score_engine` 或统一 `ScorecardBuilder`。

是否应在 v1.0 发布前修复：是，至少修正文档与发布措辞；代码抽取可延期。

### AUDIT-007: Workspace / Memory / Learning 边界不清晰

严重级别：Medium

涉及文件：

- `workspace/manager.py`
- `workspace/memory.py`
- `runtime/memory_manager.py`
- `learning/engine.py`
- `learning/manager.py`
- `apps/equity_research/app.py`

问题描述：

Memory 同时出现在 Workspace Memory 和 Runtime Memory Manager；APP-001 直接使用 `runtime.memory_manager.MemoryManager`，Learning 又有独立的 improvement engine。三者的关系没有统一边界：Workspace 负责项目上下文，Runtime Memory 负责执行上下文，Learning 负责反馈沉淀，但接口上没有明确隔离或同步协议。

影响：

- 研究结果沉淀到哪个 Memory 不清晰。
- 复盘、Replay、Learning 之间可能无法复原同一条真实研究链。
- 多用户/公网部署时，数据隔离风险会放大。

根因：

Memory/Workspace/Learning 分多个 Feature 开发，尚未收敛成持久化和生命周期模型。

建议方案：

- Stable 前声明单用户本地工作区假设。
- 后续定义 Memory Boundary：Runtime Memory 是 event-local，Workspace Memory 是 project-local，Learning Memory 是 cross-project pattern。

是否应在 v1.0 发布前修复：部分。公网/Stable 前必须有边界声明；完整实现可延期。

### AUDIT-008: API / CLI / Web 是薄壳，但 API 当前不适合公网

严重级别：High

QA Sprint 2 状态：Partially fixed。API 已默认绑定 localhost，非本地绑定必须配置 API key，并增加请求体限制、CORS allowlist 和错误脱敏。

涉及文件：

- `api/server.py`
- `api/routes/research.py`
- `api/routes/workspace.py`
- `cli/commands/run.py`
- `web/*.html`
- `docker/docker-compose.yml`

问题描述：

API 使用标准库 HTTP server，默认 `0.0.0.0:8765`，CORS `*`，无鉴权、无 rate limit、无 request size limit、无 persistent workspace isolation。CLI 调 APP，API 调 APP，Web 是静态控制台。作为本地演示合理，作为公网服务不合理。

影响：

- 任何公网部署都会暴露无鉴权研究接口。
- 未来接真实 API key 或付费模型后会有成本和安全风险。
- Web/API 无法承担生产验证环境。

根因：

Release-001 产品化目标偏 “可运行 demo”，尚未进入 production hardening。

建议方案：

- Stable 前不允许公网裸部署。
- 若要公网测试，先加 API key、CORS allowlist、request limit、deployment profile。

是否应在 v1.0 发布前修复：是，如果 v1.0 Stable 意味着公网可测；若仅本地 Stable，可文档限制。

### AUDIT-009: Report Generator 有较好的校验，但上游输入质量仍可伪通过

严重级别：Medium

涉及文件：

- `report_generator/pipeline.py`
- `apps/equity_research/report_exporter.py`
- `templates/report/research-report-template.md`
- `schemas/report/report.schema.json`

问题描述：

ReportPipeline 对 Evidence/KG/Score 引用关系有一定检查，这是当前较强的边界之一。但 APP-001 的报告导出层可以捕获 Report Generator 失败并输出 SKIP 文本，最终仍返回一个报告结构。

影响：

- Report Generator fail 可能被降级为文本，而不是阻塞业务质量门禁。
- 用户看到“研究任务完成”，但报告可能只是降级说明。

根因：

App 为了演示可用性，把报告失败设计为降级而不是失败。

建议方案：

- Stable 前区分 `status=completed_with_degradation` 和 `status=failed_quality_gate`。
- 报告质量门禁失败不能被普通 SKIP 文本吞掉。

是否应在 v1.0 发布前修复：是。

### AUDIT-010: `src/` 与 Builder 资产存在定位不清

严重级别：Low

涉及文件：

- `src/`
- `builder/`
- `templates/builder/**`
- `builder-output/`

问题描述：

仓库同时存在顶层 Core 模块、空/弱存在感 `src/`、Builder 模板与 Builder 输出目录。当前主运行链不依赖 `src/`，Builder 更像开发资产而非产品运行依赖。

影响：

- 新贡献者难以判断入口。
- Builder 产物和运行时代码边界不清时，后续可能把生成资产误当生产资产。

根因：

早期平台化和产品化资产并行沉淀，没有做目录语义收敛。

建议方案：

- Stable 前在 README 或 docs 中明确 `src/` 当前非生产入口。
- 不建议立即删除，先确认历史引用。

是否应在 v1.0 发布前修复：否，可延期。

## Release Decision

不允许发布 `v1.0.0 Stable`。

允许发布：

- `v1.0.0-rc2`
- `v1.0.0 Developer Preview`
- `v1.0.0 Local Demo`

前提是 release notes 明确声明：默认数据源可能为 Mock，公网部署不受支持，Orchestrator/Score Engine 部分为架构契约和最小实现，APP-001 是 Core-assisted demo app。

## Must Fix Before v1.0 Stable

1. 明确或实现 Orchestrator 边界，不能继续让架构图承诺一个不存在的可执行层。
2. 建立至少一条 real-mode 端到端验证链路，并输出 Mock/SKIP/fallback 明细。
3. 将 APP-001 的 Evidence/KG/Score 输出接入统一 Core validator。
4. 补强 validate 脚本：从交付物存在检查升级为契约和业务语义检查。
5. 明确 Schema/Template/Prompt/Skill 的 source of truth。
6. 公网部署前增加 API 鉴权、CORS 限制、请求限制和环境隔离。
7. 区分 completed、completed_with_degradation、failed_quality_gate。

## Can Defer

1. 把 App-local score 完全抽成独立 `score_engine`。
2. 把 Orchestrator 扩展成复杂调度服务。
3. 清理 `src/`、Builder 输出和历史示例。
4. 完整持久化 Workspace/Memory/Learning。
5. 把所有 Schema 校验自动生成到 CI。

## Module Actions

建议删除：暂不建议立即删除任何模块。`src/`、`builder-output/`、示例 artifacts 应先做引用审计。

建议合并：APP-001 内部 KG/Score builder 与 Core KG/Score validator；Investment Engine 和 APP-001 的 scorecard calculator。

建议保留：Planner、Runtime、Data Connectors、Report Generator、Committee、Workspace、Learning，但需要明确每个模块的稳定边界。

## Next QA Order

1. Contract QA：`common/contract.py`、Planner runtime plan、Runtime task normalization。
2. APP-001 QA：证明 App 输出经过 Core Evidence/KG/Score validators。
3. Real Data QA：至少一个 SEC/RSS/GitHub/News real-mode case，不允许全部 fallback。
4. Report QA：ReportPipeline failure 必须传递为 quality gate failure。
5. API QA：本地 API 安全边界、错误码、请求限制。
6. Regression QA：再跑原 25 个 validate 脚本，作为回归而不是发布门禁。
