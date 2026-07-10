# AIRS 使用说明书

**AIRS — AI Investment Research System**
**让 AI 做研究增强，而不是替人盲目下投资结论**

---

## ⚠️ 免责声明

AIRS 是一套面向 AI Agent 的投资研究方法论框架，**不是荐股工具，不是自动交易系统，不承诺收益**。所有输出仅用于研究质量控制和学习参考，最终投资决策由人工负责。

---

## 目录

1. [项目概览](#1-项目概览)
2. [系统架构](#2-系统架构)
3. [快速开始](#3-快速开始)
4. [核心模块说明](#4-核心模块说明)
5. [完整研究流程](#5-完整研究流程)
6. [Feature 开发流程](#6-feature-开发流程)
7. [测试与验证](#7-测试与验证)
8. [目录结构参考](#8-目录结构参考)
9. [常见问题](#9-常见问题)

---

## 1. 项目概览

### 什么是 AIRS

AIRS 是一套完整的 AI 投资研究系统框架，覆盖从研究意图拆解到最终报告生成的全链路。它不是单一工具，而是一套分层架构：

- **基础设施层**：Architecture、Methodology、Evidence、Prompt、Skill、Score、Evaluation、Benchmark
- **引擎层**：Builder、Knowledge Graph、Report Generator、Data Connectors、Orchestrator、Runtime、Workspace
- **能力层**：Investment Research Engine、Planner、Committee、Memory、Learning

### 项目规模

| 维度 | 数量 |
|------|------|
| 总文件数 | 751 |
| Markdown 文档 | 447 |
| Python 代码 | 11,236 行 |
| JSON Schema | 47 |
| 验证脚本 | 23 |
| 完成里程碑 | M1-M8 + FEATURE-001~012 |
| Git 版本 | v1.0.0-rc1 |
| GitHub 仓库 | <https://github.com/evan-zhang/AIRS> |

---

## 2. 系统架构

```
用户研究目标
    │
    ▼
┌─────────────────┐
│   Planner        │  意图拆解 → Research Plan
│  (FEATURE-009)   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Committee      │  多角色辩论 → 证据复核 → 表决
│  (FEATURE-010)   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Orchestrator     │  Workflow 编排
│  (FEATURE-005)   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Runtime        │  多 Agent 调度执行
│  (FEATURE-006)   │
└────────┬────────┘
         │
    ┌────┼────┬────┬────┬────┬────┐
    ▼    ▼    ▼    ▼    ▼    ▼    ▼
 Connector  Methodology  Evidence  Knowledge Graph  Skill  Prompt  Score
 (F-004)    (M2)         (M3)      (F-002)          (M5)   (M4)    (M6)
    │           │           │           │             │      │      │
    └───────────┴───────────┴───────────┴─────────────┴──────┴──────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │ Report Generator │  统一报告生成
                    │  (FEATURE-003)   │
                    └────────┬────────┘
                             │
                    ┌────────┴────────┐
                    │   Workspace      │  项目管理、会话、快照
                    │  (FEATURE-007)   │
                    └────────┬────────┘
                             │
                    ┌────────┴────────┐
                    │   Memory         │  知识沉淀
                    │  (FEATURE-011)   │
                    └────────┬────────┘
                             │
                    ┌────────┴────────┐
                    │   Learning       │  闭环优化
                    │  (FEATURE-012)   │
                    └─────────────────┘
```

### 分层说明

**第一层：基础设施（M1-M8）**

| 里程碑 | 模块 | 说明 |
|--------|------|------|
| M1 | Architecture Foundation | 目录结构、顶层文档、自检脚本 |
| M2 | Methodology Core | 10 套研究方法论（供应链、估值、风险等） |
| M3 | Evidence Engine | 证据卡规范、证据链、证据生命周期 |
| M4 | Prompt DSL & Library | 11 个生产级 Prompt + DSL 规范 |
| M5 | Skill Engine | 10 个生产级 Skill + 调用协议 |
| M6 | Score & Evaluation | 9 维评分 + 质量门禁 + 回归策略 |
| M7 | Benchmark & Examples | 6 类 × 5 项 Benchmark + 6 个生产示例 |
| M8 | Production Release | 生产文档、治理、发布流程 |

**第二层：引擎层（FEATURE-001~007）**

| Feature | 模块 | 说明 |
|---------|------|------|
| F-001 | Builder | Feature 请求 → 完整开发包自动生成 |
| F-002 | Knowledge Graph | 图谱模型、路径分析、卡脖子分析 |
| F-003 | Report Generator | 12 段统一报告模板 + 引用链 |
| F-004 | Data Connectors | 6 个官方 Connector + 统一接口 |
| F-005 | Orchestrator | Workflow 编排（串行/并行/条件/重试） |
| F-006 | Runtime | 16 组件 Agent 运行时 |
| F-007 | Workspace | 项目、会话、快照、回放、导入导出 |

**第三层：能力层（FEATURE-008~012）**

| Feature | 模块 | 说明 |
|---------|------|------|
| F-008 | Investment Engine | 11 个研究组件 + 5 个完整案例 |
| F-009 | Planner | 目标拆解 → 执行计划 |
| F-010 | Committee | 多角色辩论 + 表决 + 少数报告 |
| F-011 | Memory | 长期记忆 + 语义检索 + 知识复用 |
| F-012 | Learning | 反馈闭环 + 模式挖掘 + 持续优化 |

---

## 3. 快速开始

### 环境要求

- Python 3.10+
- Git
- macOS / Linux

### 安装

```bash
git clone https://github.com/evan-zhang/AIRS.git
cd AIRS
```

### 验证安装

```bash
# 运行全部 23 个验证脚本
python3 scripts/validate_m1.py
python3 scripts/validate_m2.py
python3 scripts/validate_evidence.py
python3 scripts/validate_prompt.py
python3 scripts/validate_skill.py
python3 scripts/validate_score.py
python3 scripts/validate_evaluation.py
python3 scripts/validate_benchmark.py
python3 scripts/validate_examples.py
python3 scripts/validate_release.py
python3 scripts/validate_builder.py
python3 scripts/validate_knowledge_graph.py
python3 scripts/validate_report_generator.py
python3 scripts/validate_connectors.py
python3 scripts/validate_orchestrator.py
python3 scripts/validate_runtime.py
python3 scripts/validate_planner.py
python3 scripts/validate_committee.py
python3 scripts/validate_memory.py
python3 scripts/validate_learning.py
python3 scripts/validate_workspace.py
python3 scripts/validate_investment_engine.py
python3 scripts/validate_e2e.py
```

全部输出 PASS 即安装成功。

---

## 4. 核心模块说明

### 4.1 Planner（研究规划器）

**位置**：`planner/`
**作用**：接收用户研究目标，自动拆解为可执行 Research Plan

**支持 8 类研究目标**：
- Company Research（公司研究）
- Industry Research（行业研究）
- Theme Research（主题研究）
- Supply Chain Research（供应链研究）
- Chokepoint Research（卡脖子研究）
- Policy Research（政策研究）
- Portfolio Research（组合研究）
- Comparative Research（对比研究）

**使用示例**：

```python
from planner.engine import PlanningEngine

engine = PlanningEngine()
plan = engine.create_plan(
    goal="分析 AI 算力产业链的供应链卡脖子环节",
    goal_type="chokepoint_research"
)

# Plan 包含：
# - Goal Analysis
# - Required Connectors / Methodologies / Skills
# - Execution Order
# - Estimated Cost / Time
# - Expected Deliverables
# - Confidence / Risks
```

### 4.2 Committee（投资委员会）

**位置**：`committee/`
**作用**：多角色辩论、证据复核、投票表决

**角色**：
- Bull Analyst（看多分析师）
- Bear Analyst（看空分析师）
- Industry Expert（行业专家）
- Financial Analyst（财务分析师）
- Risk Officer（风险官）
- Portfolio Manager（组合经理）
- Devil's Advocate（魔鬼代言人）
- Evidence Reviewer（证据审查员）
- Moderator（主持人）

**输出**：
- 辩论记录
- 证据复核结果
- 投票结果
- 最终建议（区分事实/推断/假设/观点）
- 少数派报告
- 后续研究任务

### 4.3 Orchestrator（编排器）

**位置**：`orchestrator/`
**作用**：将 Plan 编排为可执行 Workflow

**支持的工作流模式**：
- Sequential（串行）
- Parallel（并行）
- Conditional（条件分支）
- Retry（重试）
- Human Review Node（人工审查节点）

### 4.4 Runtime（运行时）

**位置**：`runtime/`
**作用**：调度 Agent 执行 Workflow

**支持的 Agent 类型**：
- Sync Agent（同步）
- Async Agent（异步）
- Parallel Agent（并行）
- Long-running Agent（长时间运行）
- Human-in-the-loop Agent（人工介入）

### 4.5 Data Connectors（数据连接器）

**位置**：`data_connectors/`
**作用**：统一数据接入，所有模块通过 Connector 获取外部数据

**内置 6 个 Connector（Mock）**：
- SEC / EDGAR
- Yahoo Finance
- Alpha Vantage
- News
- GitHub
- RSS

**数据源优先级**：
Official > Regulatory > Company > Exchange > Trusted Third-party > Public News > Community

### 4.6 Knowledge Graph（知识图谱）

**位置**：`knowledge_graph/`
**作用**：产业图谱建模、路径分析、卡脖子识别

**功能**：
- Graph Model（节点/关系建模）
- Builder（图谱构建器）
- Validator（图谱验证）
- Path Analyzer（路径分析）
- Chokepoint Analyzer（卡脖子分析）

### 4.7 Evidence Engine（证据引擎）

**位置**：`docs/evidence/` + `schemas/evidence/`
**作用**：统一证据卡规范、证据链、证据等级

**Evidence Card 必须包含 16 个字段**：
Evidence ID、Title、Category、Source、Source Type、URL、Publication Time、Collection Time、Confidence、Evidence Level、Supports、Refutes、Missing Evidence、Weight、Traceability、Version

### 4.8 Report Generator（报告生成器）

**位置**：`report_generator/`
**作用**：生成统一格式研究报告

**12 段报告结构**：
Executive Summary → Investment Thesis → Industry Overview → Knowledge Graph Analysis → Supply Chain Analysis → Evidence Summary → Financial Analysis → Valuation → Risks → Counter View → Conclusion → Appendix

### 4.9 Memory（研究记忆）

**位置**：`memory/`
**作用**：长期知识沉淀、语义检索、经验复用

**支持**：
- Long-term / Short-term Memory
- Semantic Retrieval（语义检索）
- Similar Case Search（相似案例搜索）
- Experience Replay（经验回放）
- Memory Consolidation（记忆合并）
- Memory Expiration（记忆过期）

### 4.10 Learning（学习引擎）

**位置**：`learning/`
**作用**：从历史研究中持续学习，优化 Prompt / Methodology / Skill / Score

**闭环**：
Feedback → Outcome Tracking → Pattern Mining → Rule Generation → Optimization Proposal → 人工审核 → 应用

### 4.11 Builder（Feature 开发包生成器）

**位置**：`builder/`
**作用**：输入 Feature 请求 YAML，自动生成完整开发包

**生成物**：
Issue、ADR、Feature Spec、Skill、Prompt、Schema、Tests、Benchmark、PR Checklist、Release Notes

```bash
# 使用示例
python3 builder/main.py --request builder/requests/feature-request-xxx.yaml
# 输出到 builder-output/xxx/
```

---

## 5. 完整研究流程

一个完整的研究任务从用户提出目标到最终报告生成，经过以下步骤：

```
Step 1: 用户提出研究目标
        "分析 AI 算力产业链的供应链卡脖子环节"

Step 2: Planner 拆解
        → 确定研究类型：Chokepoint Research
        → 生成 Research Plan（含 Connector、Methodology、Skill 清单）
        → 估算成本和时间

Step 3: Committee 审议
        → 多角色讨论研究范围的合理性
        → 证据要求确认
        → 表决是否批准执行

Step 4: Orchestrator 编排
        → 将 Plan 转为 Workflow
        → 确定执行顺序和依赖关系

Step 5: Runtime 执行
        → 调度 Agent 执行各步骤
        → 通过 Connector 获取数据
        → 应用 Methodology 分析
        → 生成 Evidence Card
        → 构建 Knowledge Graph
        → 路径分析和卡脖子识别
        → 评分

Step 6: Committee 二次审议
        → 审查 Evidence 充分性
        → 反方质疑
        → 最终表决

Step 7: Report Generator 生成报告
        → 12 段统一格式
        → 自动引用 Evidence、KG、Score
        → 严格区分 Facts / Inference / Assumption / Opinion

Step 8: Memory 沉淀
        → 研究结果写入 Memory
        → 可被未来研究检索复用

Step 9: Learning 反馈
        → 记录研究质量反馈
        → 挖掘改进模式
        → 生成优化建议（需人工审核）
```

---

## 6. Feature 开发流程

AIRS 采用 Feature-driven 开发模式，不再使用 Milestone。

### 标准流程

```bash
# 1. 同步主分支
git checkout main && git pull origin main

# 2. 创建 Feature 分支
git checkout -b feature/feature-xxx-name

# 3. 使用 Builder 生成开发包
python3 builder/main.py --request builder/requests/feature-request-xxx.yaml

# 4. 开发实现
# ... 编写代码和文档 ...

# 5. 编写自检脚本
# scripts/validate_xxx.py

# 6. 运行全量回归
# 依次运行所有 validate_*.py

# 7. 提交并推送
git add -A
git commit -m "feat: FEATURE-xxx Name"
git push origin feature/feature-xxx-name

# 8. 创建 PR
gh pr create --base main --head feature/feature-xxx-name

# 9. 审核通过后合并
gh pr merge N --merge --delete-branch

# 10. 合并后回归
git checkout main && git pull origin main
python3 scripts/production_check.py
```

### Git 分支规范

- 主分支：`main`
- Feature 分支：`feature/feature-NNN-name`
- 测试分支：`test/xxx`
- 禁止直接在 main 开发

### 提交信息规范

采用 Conventional Commits：
- `feat:` 新功能
- `fix:` 修复
- `docs:` 文档
- `chore:` 杂项
- `test:` 测试

---

## 7. 测试与验证

### 验证脚本

AIRS 有 23 个 `validate_*.py` 脚本，覆盖所有模块：

| 脚本 | 验证目标 |
|------|----------|
| validate_m1.py | M1 架构基础 |
| validate_m2.py | M2 方法论 |
| validate_evidence.py | M3 证据引擎 |
| validate_prompt.py | M4 Prompt |
| validate_skill.py | M5 Skill |
| validate_score.py | M6 Score |
| validate_evaluation.py | M6 Evaluation |
| validate_benchmark.py | M7 Benchmark |
| validate_examples.py | M7 Examples |
| validate_release.py | M8 Release |
| validate_builder.py | F-001 Builder |
| validate_knowledge_graph.py | F-002 KG |
| validate_report_generator.py | F-003 Report |
| validate_connectors.py | F-004 Connectors |
| validate_orchestrator.py | F-005 Orchestrator |
| validate_runtime.py | F-006 Runtime |
| validate_workspace.py | F-007 Workspace |
| validate_investment_engine.py | F-008 Engine |
| validate_planner.py | F-009 Planner |
| validate_committee.py | F-010 Committee |
| validate_memory.py | F-011 Memory |
| validate_learning.py | F-012 Learning |
| validate_e2e.py | E2E 测试 |

### E2E 测试

```bash
# 运行端到端测试
python3 scripts/run_production_tests.py
```

覆盖 8 个完整场景 + 3 个故障注入测试。

### 质量门禁

- 所有 validate_* 必须 PASS
- E2E 测试必须 PASS
- 故障注入测试必须 PASS
- 代码必须有免责声明
- 不允许伪造数据

---

## 8. 目录结构参考

```
AIRS/
├── README.md                 # 项目说明
├── ARCHITECTURE.md           # 架构文档
├── AGENTS.md                 # Agent 规范
├── SKILL.md                  # Skill 说明
├── ROADMAP.md                # 路线图
├── CONTRIBUTING.md           # 贡献指南
├── CHANGELOG.md              # 变更日志
├── LICENSE                   # MIT License
│
├── docs/                     # 全部文档
│   ├── methodology/          # 10 套方法论
│   ├── evidence/             # 证据引擎文档
│   ├── prompt-engine/        # Prompt 引擎文档
│   ├── skill-engine/         # Skill 引擎文档
│   ├── score-engine/         # 评分引擎文档
│   ├── evaluation-engine/    # 评估引擎文档
│   ├── benchmark/            # Benchmark 文档
│   ├── builder/              # Builder 文档
│   ├── knowledge-graph/      # 知识图谱文档
│   ├── report-generator/     # 报告生成器文档
│   ├── data-connectors/      # 数据连接器文档
│   ├── orchestrator/         # 编排器文档
│   ├── runtime/              # 运行时文档
│   ├── workspace/            # 工作空间文档
│   ├── investment-engine/    # 投资引擎文档
│   ├── planner/              # 规划器文档
│   ├── committee/            # 委员会文档
│   ├── memory/               # 记忆系统文档
│   ├── learning/             # 学习引擎文档
│   ├── production/           # 完成报告
│   ├── review/               # 自审报告
│   ├── testing/              # 测试报告
│   ├── adr/                  # 架构决策记录
│   └── rfc/                  # RFC
│
├── planner/                  # 规划器实现
├── committee/                # 委员会实现
├── orchestrator/             # 编排器实现
├── runtime/                  # 运行时实现
├── investment_engine/        # 投资引擎实现
├── knowledge_graph/          # 知识图谱实现
├── report_generator/        # 报告生成器实现
├── data_connectors/          # 数据连接器实现
├── workspace/                # 工作空间实现
├── memory/                   # 记忆系统实现
├── learning/                 # 学习引擎实现
├── builder/                  # Builder 实现
├── common/                   # 共享契约
│
├── prompts/                  # 11 个生产级 Prompt
├── skills/                   # 10 个生产级 Skill
├── scoring/                  # 9 维评分
├── evaluation/               # 评估工具
├── benchmark/                # 6 类 Benchmark
├── examples/                 # 生产示例
├── templates/                # 全部模板
├── schemas/                  # 47 个 JSON Schema
│
├── scripts/                  # 23 个验证脚本
├── tests/                    # E2E + 故障测试
└── builder-output/           # Builder 生成的 Feature 包
```

---

## 9. 常见问题

### Q: AIRS 能直接用来做投资决策吗？

**不能。** AIRS 是研究辅助框架，所有输出必须经过人工审核。投资决策由人负责。

### Q: Connector 是真实的 API 调用吗？

当前 6 个 Connector 是 Mock 实现，返回示例数据。接入真实 API 需要在 `data_connectors/connectors/` 中替换 fetch 逻辑。

### Q: 如何新增一个研究方法论？

1. 阅读 `docs/methodology/DSL.md` 和 `templates/methodology-template.md`
2. 按 16 个 section 模板编写新方法论
3. 运行 `python3 scripts/validate_m2.py` 验证
4. 提交 PR

### Q: 如何开发一个新 Feature？

1. 使用 Builder 生成开发包：`python3 builder/main.py`
2. 按 Feature 分支流程开发（见第 6 节）
3. 编写 `validate_xxx.py`
4. 全量回归通过后创建 PR

### Q: Planner → Runtime 的契约是什么？

通过 `common/contract.py` 中的 `resolve_agent_id()` 函数。Planner 输出 `agent_role`，Contract 将其映射为 Runtime 可消费的 `agent_id`。

### Q: 报告中的 Facts / Inference / Assumption / Opinion 如何区分？

- **Facts（事实）**：可验证的客观数据（财报数字、政策原文）
- **Inference（推断）**：基于事实的逻辑推导（趋势 extrapolation）
- **Assumption（假设）**：无法直接验证的前提条件（市场假设）
- **Opinion（观点）**：分析员的主观判断（估值观点）

详见 `docs/investment-engine/recommendation-standards.md`。

### Q: 如何运行 E2E 测试？

```bash
python3 scripts/run_production_tests.py
```

测试结果输出到 `docs/testing/artifacts/`。

### Q: Memory 如何检索？

```python
from memory.retrieval import RetrievalEngine

engine = RetrievalEngine()
results = engine.search(
    query="AI 算力供应链",
    memory_type="research",
    limit=5
)
```

### Q: Learning 会自动修改 Prompt 吗？

**不会。** Learning 只生成 `pending_review` 状态的优化建议，必须经过人工审核后才能应用。

---

## 附录

- **GitHub 仓库**：<https://github.com/evan-zhang/AIRS>
- **版本**：v1.0.0-rc1
- **License**：MIT
- **文档语言**：中文
- **代码语言**：Python 3.10+
- **最新更新**：2026-07-10

---

*AIRS 让 AI 做研究增强，而不是替人盲目下投资结论。*
