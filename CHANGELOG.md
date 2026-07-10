# AIRS 变更日志

## [FEATURE-010] Autonomous Investment Committee - 2026-07-10

### Added

- 新增 `builder/requests/feature-request-autonomous-investment-committee.yaml` 并生成 `builder-output/autonomous-investment-committee/` Feature Package。
- 新增 `docs/committee/` 12 份 AIC 架构、生命周期、角色、辩论、证据挑战、反方、共识、投票、少数报告、记录、治理和评审工作流文档。
- 新增 `committee/` 最小可运行 Python AIC，覆盖 Coordinator、Role Registry、Analysts、Experts、Reviewer、Moderator、Voting Engine、Consensus Engine 和 Recorder。
- 新增 `committee/examples/` 6 个生产级 Committee 示例：AI 算力、创新药、半导体、机器人、新能源、港股个股。
- 新增 `schemas/committee/`、`templates/committee/` 和 `scripts/validate_committee.py`。
- 新增 `docs/adr/ADR-0010-autonomous-investment-committee.md`、`docs/production/M10_COMPLETION_REPORT.md` 和 `docs/review/M10_SELF_REVIEW.md`。

### Compliance

- AIC 明确位于 Planner 之后、Research Engine 之前。
- AIC 只执行审议、质询、证据复核、投票和记录，不重复定义 M1-M9 能力。
- 所有 AIC 产物仅用于研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## [FEATURE-009] Autonomous Research Planner - 2026-07-10

### Added

- 新增 `builder/requests/feature-request-autonomous-research-planner.yaml` 并生成 `builder-output/autonomous-research-planner/` Feature Package。
- 新增 `docs/planner/` 12 份 Planner 架构与组件文档，明确 Planner 是 AIRS 最上层入口。
- 新增 `planner/` 最小可运行 Python Planner，覆盖 Goal Parser、Intent Analyzer、Scope Builder、Planning Engine、Dependency、Workflow、Runtime、Resource、Budget、Confidence 和 Optimizer。
- 新增 `planner/examples/` 8 个研究目标示例：Company、Industry、Theme、Supply Chain、Chokepoint、Policy、Portfolio、Comparative Research。
- 新增 `schemas/planner/`、`templates/planner/` 和 `scripts/validate_planner.py`。
- 新增 `docs/adr/ADR-0009-autonomous-research-planner.md`、`docs/production/FEATURE_009_COMPLETION_REPORT.md` 和 `docs/review/FEATURE_009_SELF_REVIEW.md`。

### Compliance

- Runtime 不允许直接接收用户请求，必须接收 Planner 生成的 Runtime Plan。
- Planner 仅生成研究计划、执行链路、预算、置信度和风险，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## [FEATURE-008] Investment Research Engine - 2026-07-10

### Added

- 新增 `builder/requests/feature-request-investment-research-engine.yaml` 并生成 `builder-output/investment-research-engine/` Feature Package。
- 新增 `docs/investment-engine/`，覆盖 Engine 架构、研究管线、创意生成和 Recommendation 标准。
- 新增 `docs/orchestrator/orchestrator-architecture.md`，明确 Orchestrator 与 Runtime、Workspace、Evidence 的边界。
- 新增 `investment_engine/` 最小可运行 Python Engine，统一输出 Investment Thesis、Knowledge Graph、Evidence Chain、Supply Chain Analysis、Chokepoint Analysis、Score Card、Risk Analysis、Catalyst Analysis 和 Final Research Report。
- 新增 `investment_engine/examples/` 五个案例：AI 算力、创新药、半导体、机器人、新能源。
- 新增 `schemas/investment/`、`templates/investment/` 和 `scripts/validate_investment_engine.py`。
- 新增 `docs/adr/ADR-0008-investment-research-engine.md`、`docs/production/FEATURE_008_COMPLETION_REPORT.md` 和 `docs/review/FEATURE_008_SELF_REVIEW.md`。

### Compliance

- Recommendation 强制区分 Fact、Inference、Assumption 和 Opinion。
- Engine 仅用于研究流程编排和质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## [FEATURE-007] AI Research Workspace - 2026-07-10

### Added

- 新增 `docs/workspace/` 5 份 Workspace 架构、生命周期、项目管理、会话管理和产物治理文档。
- 新增 `workspace/` 最小可运行 Python Workspace，覆盖 Project、Session、Timeline、Artifact、Task Board、Memory、Snapshot、Version、Replay、Export、Collaboration 和 Audit。
- 新增 5 个 Workspace 示例和 Markdown Dashboard，覆盖公司、行业、热点主题、供应链和报告生成。
- 新增 `schemas/workspace/`、`templates/workspace-dashboard-template.md` 和 `scripts/validate_workspace.py`。
- 使用 AIRS Builder 生成 `builder-output/ai-research-workspace/` Feature Package。
- 新增 FEATURE-007 ADR、Completion Report 和 Self Review。

### Compliance

- Workspace 是用户交互和研究资产管理唯一入口，但 Agent 执行仍由 Runtime 调度。
- Workspace 只保存引用、状态、产物、快照、导出和审计记录，不构成投资建议。

## [FEATURE-006] Research Agent Runtime - 2026-07-10

### Added

- 新增 `docs/runtime/` 10 份 Runtime 架构、生命周期、注册表、调度、消息、事件、状态、内存、资源和监控文档。
- 新增 `runtime/` 最小可运行 Python Runtime，覆盖 Core、Agent Registry、Lifecycle、Context、Session、Dispatcher、Message Bus、Event Bus、State、Memory、Resource、Retry、Timeout、Cancellation 和 Monitor。
- 新增 5 个 Runtime 示例，覆盖公司研究、行业研究、热点主题、供应链和报告生成。
- 新增 `schemas/runtime/`、`templates/runtime/` 和 `scripts/validate_runtime.py`。
- 新增 FEATURE-006 ADR、Completion Report 和 Self Review。

### Compliance

- 所有 Workflow 必须由 Runtime 调度执行，不允许 Workflow 直接驱动业务模块。
- Runtime 仅用于 AIRS 工程开发、研究流程编排和质量控制，不构成投资建议。

## [FEATURE-004] Data Connector Framework - 2026-07-10

### Added

- 新增 `docs/data-connectors/`，定义 Connector 架构、生命周期、接口、数据源优先级和治理规则。
- 新增 `data_connectors/` 最小可运行 Python 框架，包含 Registry、Base Interface、Auth、Rate Limit、Cache、Retry、Normalizer、Priority 和 Health Check。
- 新增 6 个官方 Mock Connector：SEC EDGAR、Yahoo Finance、Alpha Vantage、News、GitHub、RSS。
- 新增 `schemas/connectors/`、`templates/connectors/` 和 `scripts/validate_connectors.py`。
- 新增 FEATURE-004 ADR、Completion Report 和 Self Review。

### Compliance

- Connector 输出统一保留 Source、URL、Timestamp、Version、Trace ID 和 Traceability。
- Methodology、Skill、Report、Knowledge Graph 不直接访问外部数据源，只通过 Connector 接入。
- 本 Feature 仅用于 AIRS 工程开发与研究质量控制，不构成投资建议。


本文档记录 AIRS 项目的所有重要变更。

格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)，
本项目遵循 [语义化版本](https://semver.org/lang/zh-CN/)。

---

## [Unreleased]

### Added - FEATURE-002: Knowledge Graph Engine
- 新增 `docs/knowledge-graph/` 知识图谱架构与工作流文档。
- 新增 `knowledge_graph/` 最小可运行内存图谱实现，覆盖 Graph Model、Builder、Validator、Path Analyzer 和 Chokepoint Analyzer。
- 新增 `schemas/knowledge-graph/knowledge-graph.schema.json`，定义节点、关系、Evidence 绑定、路径分析和卡脖子分析输出。
- 新增 `templates/knowledge-graph/` 图谱输出模板和卡脖子分析模板。
- 新增两个生产示例：`examples/knowledge-graph/ai-compute-supply-chain.json` 与 `examples/knowledge-graph/innovative-drug-industry-chain.json`。
- 新增 `scripts/validate_knowledge_graph.py` 自检脚本。
- 新增 `docs/production/FEATURE_002_COMPLETION_REPORT.md` 与 `docs/review/FEATURE_002_SELF_REVIEW.md`。

### Validation - FEATURE-002
- `validate_knowledge_graph.py` PASS。
- M1-M8 与 FEATURE-001 Builder 回归脚本保持 PASS。

### Compliance - FEATURE-002
- Knowledge Graph Engine 只用于工程开发、研究结构化表达和质量控制，不构成投资建议。
- 图谱示例绑定 M3 Evidence Card、保留反方证据和缺失证据，并避免荐股、自动交易、交易指令、目标价或收益承诺。

### Added - FEATURE-001: AIRS Builder
- 新增 `docs/builder/` Builder 架构、生命周期、治理和生成流程文档。
- 新增 `builder/` 本地 Feature Package 生成器入口、模板 registry 和 generators 目录说明。
- 新增 `schemas/builder/` 下 Feature Request、Feature Package 和 Generated Artifact 三个 Schema。
- 新增 `templates/builder/` 下 11 个 Builder 生成模板。
- 新增 `scripts/validate_builder.py` 自检脚本。
- 新增两个生产级 Feature Package 示例：`builder-output/knowledge-graph-engine/` 与 `builder-output/news-connector/`。
- 新增 `docs/adr/ADR-0003-feature-builder.md`、`docs/production/FEATURE_001_COMPLETION_REPORT.md` 和 `docs/review/FEATURE_001_SELF_REVIEW.md`。

### Validation - FEATURE-001
- `validate_m1.py` PASS。
- `validate_m2.py` PASS。
- `validate_evidence.py` PASS。
- `validate_prompt.py` PASS。
- `validate_skill.py` PASS。
- `validate_score.py` PASS。
- `validate_evaluation.py` PASS。
- `validate_benchmark.py` PASS。
- `validate_examples.py` PASS。
- `validate_release.py` PASS。
- `validate_builder.py` PASS。

### Compliance - FEATURE-001
- AIRS Builder 只用于工程开发包生成和研究质量控制，不构成投资建议。
- Builder 模板引用 M4 Prompt、M5 Skill 与 M7 Benchmark 既有模板，不重复定义 M2-M7 规则。

### Planned
- V1.x: Runtime、Benchmark Runner、Scorecard Runner、更多生产示例和回归数据集。

---

## [1.0.0] - 2026-07-10

### Added - M8: Production Release
- 新增 `docs/production/production-guide.md` 生产指南。
- 新增 `docs/production/deployment-guide.md` 部署指南。
- 新增 `docs/production/upgrade-guide.md` 升级指南。
- 新增 `docs/production/maintenance-guide.md` 维护指南。
- 新增 `docs/production/governance-guide.md` 治理指南。
- 新增 `docs/production/release-checklist.md` 发布清单。
- 新增 `docs/production/release-notes.md` V1.0 发布说明。
- 新增 `docs/production/production-acceptance-checklist.md` 生产验收清单。
- 新增 `docs/production/final-quality-gate.md` 最终质量门禁。
- 新增 `docs/production/regression-test-process.md` 回归测试流程。
- 新增 `docs/governance/semantic-versioning.md` 语义化版本规范。
- 新增 `docs/governance/release-workflow.md` 发布流程。
- 新增 `.github/ISSUE_TEMPLATE/bug_report.md` 和 `.github/ISSUE_TEMPLATE/feature_request.md`。
- 新增 `.github/pull_request_template.md`、`.github/CODEOWNERS`、`.github/SECURITY.md`、`.github/SUPPORT.md`。
- 新增 `scripts/validate_release.py` 和 `scripts/production_check.py`。
- 新增 `docs/production/M8_COMPLETION_REPORT.md`、`docs/production/PROJECT_HEALTH_REPORT.md`、`docs/production/FINAL_REVIEW.md`。
- 新增 `docs/adr/0002-m8-production-top-level-updates.md`，记录 M8 对顶层文件的受控生产更新。

### Changed - M8
- 更新 `README.md`，补充 V1.0 Production 状态、完整功能列表和最终免责声明。
- 更新 `CONTRIBUTING.md`，补充 V1.0 贡献流程、版本规范和发布流程引用。
- 更新 `ROADMAP.md`，标注 M1-M8 全部完成，并补充 V1.x / V2 路线。
- 确认 `LICENSE` 保持 MIT License 和投资研究免责声明，无需修改。

### Validation - M8
- `validate_m1.py` PASS。
- `validate_m2.py` PASS。
- `validate_evidence.py` PASS。
- `validate_prompt.py` PASS。
- `validate_skill.py` PASS。
- `validate_score.py` PASS。
- `validate_evaluation.py` PASS。
- `validate_benchmark.py` PASS。
- `validate_examples.py` PASS。
- `validate_release.py` PASS。
- `production_check.py` FINAL RESULT PASS。

### Compliance
- V1.0 Production Release 仍然只用于投资研究流程、质量控制和教育研究，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

### Added - M7: Benchmark & Production Examples
- 新增 `docs/benchmark/` 4 个 Benchmark 架构、生命周期、分类和治理文档。
- 新增 `docs/examples/` 2 个示例规范和回归数据集说明文档。
- 新增 6 类 x 5 项 Benchmark 分类种子，共 30 个 Markdown 文件。
- 新增 6 个生产示例，覆盖供应链、主题扩散、证据报告、估值、风险和完整研究报告。
- 新增 `schemas/benchmark/` 下 3 个 JSON Schema。
- 新增 `templates/benchmark-template.md` 与 `templates/example-template.md`。
- 新增 `scripts/validate_benchmark.py` 与 `scripts/validate_examples.py`。
- 新增 `docs/production/M7_COMPLETION_REPORT.md` 与 `docs/review/M7_SELF_REVIEW.md`。
- 新增 `docs/adr/0001-m7-benchmark-template-disclaimer.md` 记录 M7 对 M1 Benchmark Case 模板的受控增强。

### Changed - M7
- 更新 `schemas/README.md`，补充 Benchmark Schema 说明。
- 增强 `templates/benchmark-case-template.md`，补充免责声明以满足 M7 合规回归要求；不改变 M1 模板结构和语义。

### Completed
- M8: Production Release 已完成。

---

## [0.1.0] - 2026-07-10

### Added - M1: Architecture Foundation

#### 顶层文档
- README.md：项目简介、适用场景、项目结构、快速开始、免责声明
- ROADMAP.md：M1-M8 里程碑规划、交付物、验收标准
- ARCHITECTURE.md：8 层系统架构设计
- AGENTS.md：4 种 Agent 协作规范
- SKILL.md：Master Skill 激活条件、工作流程、输入输出要求
- CONTRIBUTING.md：贡献指南、提交规范、质量标准
- LICENSE：MIT License
- CHANGELOG.md：版本变更记录

#### 目录结构
- docs/：11 个子目录（overview, architecture, methodology, research-engine, evidence-engine, score-engine, report-engine, evaluation-engine, knowledge-graph, data-sources, production, governance）
- skills/：13 个子目录（master, hot-topic, industry, supply-chain, chokepoint, financial, news, evidence, committee, valuation, risk, report, verification）
- prompts/：12 个子目录（_dsl, hot-topic, industry, supply-chain, chokepoint, financial, news, evidence, committee, valuation, risk, report）
- schemas/：6 个子目录（common, research, evidence, score, report, evaluation）
- scoring/：含 rubrics/ 子目录
- evaluation/：含 rubrics/ 子目录
- benchmark/：6 个子目录（ai, semiconductor, innovative-drug, robotics, new-energy, general）
- examples/：4 个子目录（reports, evidence, scores, workflows）
- templates/：5 个模板文件
- scripts/：2 个自检脚本
- .github/：GitHub 配置

#### 目录 README
- docs/README.md：文档目录说明
- skills/README.md：Skill 模块说明
- prompts/README.md：Prompt 库说明
- schemas/README.md：Schema 定义说明
- scoring/README.md：评分引擎说明
- evaluation/README.md：评估引擎说明
- benchmark/README.md：测试基准说明
- examples/README.md：示例库说明
- templates/README.md：模板文件说明
- scripts/README.md：自检脚本说明

#### 模板文件
- templates/report-template.md：研究报告模板
- templates/evidence-card-template.md：证据卡模板
- templates/score-card-template.md：评分卡模板
- templates/benchmark-case-template.md：基准测试用例模板
- templates/skill-template.md：Skill 开发模板

#### 自检脚本
- scripts/check_structure.py：目录结构完整性检查
- scripts/validate_m1.py：M1 验收标准检查

#### 文档体系
- 完整的 8 层架构设计文档
- Agent 协作与开发规范
- Master Skill 总控框架
- 贡献指南与质量标准

### Changed
- N/A（初始版本）

### Deprecated
- N/A（初始版本）

### Removed
- N/A（初始版本）

### Fixed
- N/A（初始版本）

### Security
- N/A（初始版本）

---

## 版本说明

### 版本编号规则

- 主版本号（Major）：不兼容的 API 变更
- 次版本号（Minor）：向后兼容的功能性新增
- 修订号（Patch）：向后兼容的问题修正

### Milestone 对应版本

| Milestone | 版本 |
|-----------|------|
| M1 | v0.1.0 |
| M2 | v0.2.0 |
| M3 | v0.3.0 |
| M4 | v0.4.0 |
| M5 | v0.5.0 |
| M6 | v0.6.0 |
| M7 | v0.7.0 |
| M8 | v1.0.0 |

---

**最后更新**：2026-07-10
**当前版本**：v1.0.0
