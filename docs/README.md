# AIRS 文档目录

本目录包含 AIRS 项目的详细文档。

---

## 目录结构

```
docs/
├── overview/           # 项目概览
├── architecture/       # 系统架构详细设计
├── methodology/        # 研究方法论详解
├── research-engine/    # 研究引擎文档
├── evidence-engine/    # 证据引擎文档
├── score-engine/       # 评分引擎文档
├── report-engine/      # 报告引擎文档
├── evaluation-engine/  # 评估引擎文档
├── knowledge-graph/    # 知识图谱文档
├── data-sources/       # 数据源文档
├── production/         # 生产交付文档
└── governance/         # 治理与规范文档
```

---

## 子目录说明

### overview/

项目概览文档，包括：
- 项目背景
- 设计理念
- 适用场景
- 核心概念

**归属 Milestone**：M1

---

### architecture/

系统架构详细设计，包括：
- 8 层架构设计
- 层间接口
- 数据流
- 扩展方式

**归属 Milestone**：M1

---

### methodology/

研究方法论详解，包括：
- 供应链卡脖子分析
- 主题扩散分析
- 产业生命周期分析
- 政策与监管驱动分析
- 财报异常语言分析
- 新闻事件影响分析
- 反共识验证

**归属 Milestone**：M2

---

### research-engine/

研究引擎文档，包括：
- 研究任务调度
- 研究技能管理
- 研究质量保证

**归属 Milestone**：M3

---

### evidence-engine/

证据引擎文档，包括：
- 证据采集
- 证据验证
- 证据关联
- 证据质量评分

**归属 Milestone**：M3

---

### score-engine/

评分引擎文档，包括：
- 评分模型设计
- 评分权重体系
- 评分计算规则
- 评分解释机制

**归属 Milestone**：M4

---

### report-engine/

报告引擎文档，包括：
- 报告模板设计
- 报告生成流程
- 报告质量检查
- 反方观点生成

**归属 Milestone**：M5

---

### evaluation-engine/

评估引擎文档，包括：
- Loop/Go 评估机制
- 评估 Rubric
- 评估报告生成
- 评估基准

**归属 Milestone**：M6

---

### knowledge-graph/

知识图谱文档，包括：
- 产业知识图谱
- 供应链图谱
- 公司关系图谱

**归属 Milestone**：M7

---

### data-sources/

数据源文档，包括：
- 财报数据源
- 行业数据源
- 新闻数据源
- 政策数据源
- 市场数据源

**归属 Milestone**：M7

---

### production/

生产交付文档，包括：
- M1 完成报告
- M2-M8 完成报告
- 部署指南
- 维护指南

**归属 Milestone**：M1-M8

---

### governance/

治理与规范文档，包括：
- 开发规范
- 质量标准
- 免责声明
- 合规要求

**归属 Milestone**：M1

---

## 命名规范

### 文件命名

- 使用小写字母和连字符
- ✅ `supply-chain-analysis.md`
- ❌ `SupplyChainAnalysis.md`

### 目录命名

- 使用小写字母和连字符
- ✅ `research-engine/`
- ❌ `ResearchEngine/`

---

## 文档格式

### Markdown 规范

1. **标题**：使用 `#` 表示标题，不超过 3 级
2. **列表**：使用 `-` 作为无序列表符号
3. **代码块**：使用 ` ``` ` 包裹，指定语言
4. **表格**：使用 Markdown 表格格式
5. **引用**：使用 `>` 表示引用

### 文档结构

每个文档应包含：

```markdown
# 文档标题

## 简介
[文档简介]

## 目的
[文档目的]

## 范围
[文档范围]

## 内容
[文档主体内容]

## 后续扩展
[后续扩展计划]

---

**归属 Milestone**：M[X]
**最后更新**：YYYY-MM-DD
```

---

## 扩展方式

### 新增文档

1. 在对应子目录创建文档
2. 遵循命名规范
3. 遵循格式规范
4. 包含必要的元数据

### 新增子目录

1. 在 `docs/` 创建新目录
2. 在本 README 添加说明
3. 创建目录 README
4. 添加初始文档

---

## 文档质量标准

### 内容质量

- 有明确目的和范围
- 有实际内容，非空壳
- 有清晰的结构
- 有使用示例（如适用）

### 技术质量

- 符合项目架构
- 准确无误
- 可维护
- 可扩展

### 格式质量

- 符合 Markdown 规范
- 符合命名规范
- 包含元数据

---

## 后续扩展

### M2 扩展计划

- 完善 methodology/ 文档
- 添加更多示例

### M3-M8 扩展计划

- 逐步完善各引擎文档
- 添加更多技术细节
- 完善示例和最佳实践

---

**最后更新**：2026-07-10
**归属 Milestone**：M1: Architecture Foundation
