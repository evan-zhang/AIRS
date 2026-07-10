# AIRS 项目路线图

## 总览

AIRS 项目分为 M1-M8 共 8 个里程碑，逐步从架构基础到生产级系统。

**当前状态**：✅ M1-M8 全部完成，当前版本为 `v1.0.0 Production Release`。

```
M1: Architecture Foundation  → M2: Methodology Core  → M3: Evidence Engine  → M4: Prompt Engine 
         ↓                                ↓                        ↓                    ↓
      已完成                          已完成                  已完成              已完成
         ↓                                ↓                        ↓                    ↓
M5: Skill Engine            → M6: Score & Evaluation → M7: Benchmark       → M8: Production
         ↓                                ↓                        ↓                    ↓
       已完成                         已完成                  已完成              已完成
```

---

## M1: Architecture Foundation

**目标**：建立生产级、可持续开发的工程基础。

**交付物**：
- ✅ 完整项目目录结构
- ✅ 顶层文档（README, ROADMAP, ARCHITECTURE, AGENTS, SKILL, CONTRIBUTING）
- ✅ 各模块目录 README
- ✅ 基础模板文件
- ✅ 自检脚本
- ✅ M1 完成报告

**验收标准**：
- 目录结构与 REQUIRED_REPOSITORY_STRUCTURE.md 一致
- 所有顶层文件有实际内容
- 目录 README 能指导后续开发
- 自检脚本可运行
- M1_COMPLETION_REPORT.md 完整

**状态**：✅ 已完成

---

## M2: Methodology Core

**目标**：完成核心研究方法论 Prompt 与 Schema。

**交付物**：
- 供应链卡脖子分析 Prompt
- 主题扩散分析 Prompt
- 产业生命周期分析 Prompt
- 政策与监管驱动分析 Prompt
- 财报异常语言分析 Prompt
- 新闻事件影响分析 Prompt
- 各方法论对应的 Schema
- 方法论集成文档

**验收标准**：
- 每个方法论有完整的 Prompt 和 Schema
- Prompt 可被 Agent 执行
- Schema 可验证输出格式
- 有使用示例

**状态**：✅ 已完成

---

## M3: Evidence Engine

**目标**：实现证据链系统，支撑所有研究结论。

**交付物**：
- 证据卡 Schema
- 证据采集 Prompt
- 证据验证 Prompt
- 证据关联规则
- 证据质量评分
- 证据图谱 Schema

**验收标准**：
- 证据可被采集、验证、关联
- 证据质量可评分
- 证据链可追踪
- 有 50+ 证据示例

**状态**：✅ 已完成

---

## M4: Prompt Engine

**目标**：建立 Prompt DSL 与生产级 Prompt Library。

**交付物**：
- Prompt Engine 文档
- Prompt DSL
- Prompt Schema
- 11 个生产版 Prompt
- Prompt Review Checklist
- Prompt 自检脚本

**验收标准**：
- Prompt 可被 Agent 执行
- Prompt 引用 M2 方法论和 M3 Evidence
- Prompt 包含 Failure Cases 与 Review Checklist
- 所有 Prompt 包含免责声明

**状态**：✅ 已完成

---

## M5: Skill Engine

**目标**：建立 Skill Engine 与生产版 Skill 编排规范。

**交付物**：
- Skill Engine 文档
- 10 个生产版 Skill
- Skill Schema
- Skill Registry Schema
- Skill 模板
- Skill 自检脚本

**验收标准**：
- Skill 引用 M4 Prompt、M2 Methodology 和 M3 Evidence
- Skill 不内置 Prompt 正文
- Skill 有输入、输出、依赖、失败处理和 Review Checklist
- 所有 Skill 保留免责声明

**状态**：✅ 已完成

---

## M6: Evaluation Engine

**目标**：实现评估系统，对 AI Agent 投研能力进行评估。

**交付物**：
- Loop/Go 评估机制
- 评估 Rubric
- 评估 Prompt
- 评估 Schema
- 评估报告
- 评估基准

**验收标准**：
- 可对 Agent 进行 Loop/Go 评估
- 评估结果可量化
- 评估可复现
- 有评估报告示例

**状态**：✅ 已完成

---

## M7: Benchmark

**目标**：建立完整的测试基准，验证系统有效性。

**交付物**：
- 300+ 测试用例
- 覆盖所有方法论
- 覆盖所有行业
- 测试用例文档
- 测试结果记录
- 测试覆盖率报告

**验收标准**：
- 300+ 测试用例
- 覆盖 AI、半导体、创新药、机器人、新能源等
- 每个用例有标准答案
- 测试可自动执行

**状态**：✅ 已完成

---

## M8: Production

**目标**：生产级交付，系统可用、可维护、可扩展。

**交付物**：
- 完整文档体系
- 完整示例库
- 完整测试覆盖
- 部署指南
- 维护指南
- 性能优化
- 安全加固
- 用户手册

**验收标准**：
- 250+ Markdown 文件
- 120+ Prompt
- 15+ Skill
- 300+ Benchmark
- 100+ Example
- 所有测试通过
- 文档完整

**状态**：✅ 已完成

---

## 里程碑依赖关系

```
M1: 架构基础
    ↓ 必须先完成
M2: 方法论核心
    ↓ 依赖 M1
M3-M5: 证据/评分/报告引擎（可并行开发）
    ↓ 依赖 M2
M6: 评估引擎
    ↓ 依赖 M3-M5
M7: Benchmark
    ↓ 依赖 M6
M8: 生产交付
    ↓ 依赖全部
```

## 版本规划

| 版本 | 里程碑 | 目标时间 | 状态 |
|------|--------|----------|------|
| v0.1.0 | M1 | Week 1 | ✅ 已完成 |
| v0.2.0 | M2 | Week 2-3 | ✅ 已完成 |
| v0.3.0 | M3 | Week 4-5 | ✅ 已完成 |
| v0.4.0 | M4 | Week 6-7 | ✅ 已完成 |
| v0.5.0 | M5 | Week 8-9 | ✅ 已完成 |
| v0.6.0 | M6 | Week 10-11 | ✅ 已完成 |
| v0.7.0 | M7 | Week 12-15 | ✅ 已完成 |
| v1.0.0 | M8 | Week 16-20 | ✅ 已完成 |

## V1.x 路线

V1.x 重点从“生产级规范库”推进到“可执行运行时”：

- V1.1：Prompt 渲染器与 Prompt 输出 JSON 校验。
- V1.2：Skill Registry 数据文件与 Skill 调度器。
- V1.3：Scorecard runner 与 Evaluation Gate runner。
- V1.4：Benchmark runner 与历史回归结果库。
- V1.5：扩展到 100+ Example 和更完整的失败样例。

## V2 路线

V2 重点建设完整平台化能力：

- 真实数据源接入与数据源治理。
- Knowledge Graph 与 Evidence Graph 存储。
- 多 Agent 编排运行时。
- 300+ 可执行 Benchmark。
- 自动化回归报告与质量趋势分析。
- 更严格的安全、权限和审计体系。

## 风险与挑战

| 风险 | 影响 | 缓解措施 |
|------|------|----------|
| 数据质量风险 | 高 | 建立数据验证机制，多源交叉验证 |
| Prompt 复杂度风险 | 中 | 拆分 Prompt，建立 Prompt DSL |
| Agent 协作风险 | 中 | 完善 AGENTS.md，明确协作流程 |
| Benchmark 构建成本 | 高 | 逐步构建，优先核心场景 |
| 性能风险 | 低 | M8 阶段专项优化 |

---

**最后更新**：2026-07-10
**当前阶段**：v1.0.0 Production Release
