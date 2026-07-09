# AIRS - AI Investment Research System

> **AI Investment Research System (AIRS)** 是一套面向 AI Agent 的投资研究方法论框架（研究框架），包含 Skill、Prompt、Schema、Benchmark、Evaluation、Report 等模块。

## 项目简介

AIRS 不是荐股工具，不是自动交易系统，也不是预测股价的工具。AIRS 是一套面向 AI Agent 的投资研究方法论框架（研究框架），用于构建高质量的 AI 投资研究 Agent。

### 核心设计理念

1. **证据驱动**：所有结论必须有证据链
2. **反方思考**：所有报告必须包含反方观点
3. **不确定性标注**：所有推断必须标注假设和不确定性
4. **可解释性**：所有评分必须可解释
5. **可测试性**：所有模块必须可测试
6. **可持续开发**：所有开发任务必须可被 Code Agent 持续执行和验证

### 适用场景

✅ **AIRS 适用于**：
- 投资研究方法论验证
- AI Agent 投研能力评估
- 产业链分析研究
- 供应链卡点研究
- 财报异常分析
- 新闻事件影响分析
- 多 Agent 投资委员会模拟
- 反共识验证研究
- 投研 Benchmark 构建

❌ **AIRS 不适用于**：
- 个人投资建议
- 自动化交易执行
- 实时行情监控
- 预测具体股价涨跌
- 量化回测系统
- 投机策略开发

## 项目结构

```
AIRS/
├── README.md                 # 项目说明
├── ROADMAP.md              # M1-M8 里程碑规划
├── ARCHITECTURE.md         # 系统架构说明
├── AGENTS.md               # Agent 协作规范
├── SKILL.md                # Master Skill 入口
├── CONTRIBUTING.md         # 贡献规范
├── LICENSE                 # MIT License
├── CHANGELOG.md            # 版本变更记录
├── docs/                   # 详细文档
├── skills/                 # Skill 模块
├── prompts/                # Prompt 库
├── schemas/                # 数据 Schema
├── scoring/                # 评分引擎
├── evaluation/             # 评估引擎
├── benchmark/              # 测试基准
├── examples/               # 示例库
├── templates/              # 模板文件
├── scripts/                # 自检脚本
└── .github/                # GitHub 配置
```

## 快速开始

### 了解 AIRS

1. 阅读 [ARCHITECTURE.md](./ARCHITECTURE.md) 了解系统架构
2. 阅读 [AGENTS.md](./AGENTS.md) 了解 Agent 协作方式
3. 阅读 [SKILL.md](./SKILL.md) 了解 Master Skill 工作流程
4. 查看 [ROADMAP.md](./ROADMAP.md) 了解项目规划

### 为 Code Agent 准备

如果你是 Code Agent（OpenClaw、Codex、Claude Code、Cursor、Gemini CLI 等），可以：

1. 按照 [CONTRIBUTING.md](./CONTRIBUTING.md) 开始开发
2. 运行 `python scripts/check_structure.py` 检查项目结构
3. 运行 `python scripts/validate_m1.py` 验证 M1 完成情况

### 研究者使用

如果你是投资研究者，可以：

1. 查看 [docs/methodology/](./docs/methodology/) 了解研究方法论
2. 查看 [examples/reports/](./examples/reports/) 参考研究报告示例
3. 查看 [benchmark/](./benchmark/) 了解测试基准

## 当前版本状态

### v0.1.0 (M1: Architecture Foundation) - 当前进版

**已完成**：
- ✅ 完整项目目录结构
- ✅ 顶层文档架构
- ✅ Agent 协作规范
- ✅ Master Skill 框架
- ✅ M1-M8 Roadmap
- ✅ 基础模板与自检脚本

**进行中**：
- 🔄 具体研究方法论 Prompt (M2-M4)
- 🔄 证据引擎实现 (M5)
- 🔄 评分引擎实现 (M6)
- 🔄 报告引擎实现 (M7)
- 🔄 Benchmark 完善 (M8)

**未开始**：
- ⏳ 真实数据接入
- ⏳ 完整业务逻辑
- ⏳ 生产环境部署

## 免责声明

**重要提示：本免责声明适用于所有使用 AIRS 的用户和开发者**

1. AIRS 是一个投资研究方法论框架（研究框架），**不构成投资建议**。
2. AIRS 不提供荐股服务，不执行交易操作，不预测股价涨跌。
3. AIRS 生成的内容仅供研究参考，不作为投资决策依据。
4. 投资有风险，决策需谨慎。投资者应结合自身情况独立判断。
5. 使用 AIRS 产生的任何后果，由使用者自行承担。
6. AIRS 的开发者不对任何投资损失负责。

**AIRS 不是投资顾问，不提供个性化投资建议。所有投资决策应由投资者自行负责。**

## 长期目标

AIRS V2.0 Production 的长期目标包括：

- 250+ Markdown 文件
- 120+ 专业 Prompt
- 15+ Skill
- 300+ Benchmark
- 100+ Example
- 20+ Methodology
- 完整 Evidence Engine
- 完整 Score Engine
- 完整 Evaluation Engine
- 完整 Report Engine
- 完整 Knowledge Graph 规范
- 完整 Loop/Go 开发体系

## 联系方式

- 项目路径：`/Users/evan/.openclaw/gateways/life/state/workspace-life/projects/AIRS`
- 开发模式：Loop/Go 持续开发
- 验收方式：自检脚本 + 人工复核

---

**AIRS - 让 AI 做研究增强，而不是替人盲目下投资结论**
