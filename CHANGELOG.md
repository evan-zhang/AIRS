# AIRS 变更日志

本文档记录 AIRS 项目的所有重要变更。

格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)，
本项目遵循 [语义化版本](https://semver.org/lang/zh-CN/)。

---

## [Unreleased]

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

### 计划中
- M8: Production

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
**当前版本**：v0.1.0
