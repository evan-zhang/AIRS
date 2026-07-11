# AIRS Duplication Report

审计日期：2026-07-10

## DUP-001: Duplicate Evidence / KG / Score Construction

严重级别：High

涉及文件：

- `apps/equity_research/analyzer.py`
- `apps/equity_research/data_collector.py`
- `investment_engine/pipeline.py`
- `knowledge_graph/builder.py`
- `schemas/evidence/*.json`
- `schemas/knowledge-graph/*.json`
- `schemas/score/*.json`

问题描述：

APP-001 和 Investment Engine 都本地构造 Evidence Chain、Knowledge Graph 和 Scorecard。Schema 存在，但构造逻辑没有统一入口。

影响：

- 同名概念多套实现。
- App 输出可能绕开 Core KG/Score 能力。
- 未来新增研究 App 时容易复制第三套。

根因：

为完成端到端演示，业务对象由调用方直接拼装。

建议方案：

- 短期：增加 Core validators，要求 App/Engine 输出通过同一验证。
- 中期：抽出 `EvidenceChainBuilder`、`KnowledgeGraphBuilder`、`ScorecardBuilder`。

是否应在 v1.0 发布前修复：是，至少完成统一验证。

## DUP-002: Score Methodology 与 Runtime Scorecard Calculator 分离

严重级别：High

涉及文件：

- `scoring/*.md`
- `schemas/score/scorecard.schema.json`
- `investment_engine/pipeline.py`
- `apps/equity_research/analyzer.py`

问题描述：

评分方法在 `scoring/`，评分 Schema 在 `schemas/score/`，实际评分计算散落在 App 和 Investment Engine。

影响：

- `overall_score`、`confidence_score`、`quality_gate` 的语义可能不一致。
- Committee 和 Report 依赖 Scorecard，但不知道评分来源。

根因：

Score Engine 以文档和 Schema 形式交付，缺少运行时代码中心。

建议方案：

- Stable 前声明 Score 当前是 methodology + schema + local implementation。
- 发布后抽象统一 `ScorecardBuilder`。

是否应在 v1.0 发布前修复：部分修复。

## DUP-003: Prompt / Skill / Template DSL 重叠

严重级别：Medium

涉及文件：

- `prompts/_dsl/prompt.schema.json`
- `prompts/_dsl/prompt-dsl.md`
- `templates/builder/prompt-template.md`
- `templates/skill-template.md`
- `skills/*/*-skill.md`
- `docs/prompt-engine/*`
- `docs/skill-engine/*`

问题描述：

Prompt DSL、Builder prompt template、Skill markdown template、Skill docs 分别定义了结构和字段，但没有 source-of-truth 说明。

影响：

- Prompt 与 Skill 的版本追踪难。
- Builder 生成物可能与运行时模板不同步。

根因：

Prompt Engine、Skill Engine、Builder 资产并行沉淀。

建议方案：

- 增加 artifact source-of-truth 清单。
- Builder template 标为 scaffold，不作为运行时 contract。

是否应在 v1.0 发布前修复：是，文档级即可。

## DUP-004: Report Templates 命名重复

严重级别：Medium

涉及文件：

- `templates/report-template.md`
- `templates/report/research-report-template.md`
- `templates/apps/equity-research/equity-research-report-template.md`
- `apps/equity_research/report_exporter.py`

问题描述：

报告模板存在通用模板、Report Engine 模板、App 专用模板。命名上都接近 “report template”，职责边界不清。

影响：

- 修改模板时难以判断影响范围。
- App 报告输出可能与 Report Generator 输出不一致。

根因：

Core report 与 App report 分别演进，缺少模板索引。

建议方案：

- 保留三类模板，但明确：core template、app template、builder scaffold。
- App 专用模板必须声明其兼容 Core ReportPipeline 的字段。

是否应在 v1.0 发布前修复：是，轻量修复。

## DUP-005: Validation Scripts Overlap

严重级别：Medium

涉及文件：

- `scripts/validate_m*.py`
- `scripts/validate_score.py`
- `scripts/validate_evidence.py`
- `scripts/validate_productization.py`
- `scripts/validate_release.py`
- `scripts/validate_e2e.py`

问题描述：

Milestone validate、Feature validate、Release validate、Productization validate 重复检查文件、文档、示例和 import。缺少统一的 validation taxonomy。

影响：

- PASS 数量多但信号弱。
- 新问题可能被多个脚本同时漏掉。

根因：

每个 Feature 独立添加验收脚本，缺少后期合并。

建议方案：

- 不建议马上合并所有脚本。
- 先增加 `validate_contracts.py` 和 `validate_business_paths.py`，再逐步将旧脚本降级为 artifact checks。

是否应在 v1.0 发布前修复：是，至少新增强门禁。

## DUP-006: Examples and Generated Artifacts Mixed With Source

严重级别：Low

涉及文件：

- `apps/equity_research/examples/*`
- `committee/examples/*`
- `investment_engine/examples/*`
- `learning/examples/*`
- `runtime/examples/*`
- `workspace/examples/*`
- `builder-output/`
- `demo/output/`

问题描述：

多个模块都有 examples，部分为 source examples，部分为 generated artifacts，部分为 demo output。

影响：

- 仓库体积和认知负担增加。
- 回归测试可能误读生成物为规范。

根因：

工程演示和产品示例都保留在仓库中。

建议方案：

- 保留 examples，但增加 README 说明 source/example/generated 的区别。
- `demo/output/` 不应纳入 Git。

是否应在 v1.0 发布前修复：否，可延期。
