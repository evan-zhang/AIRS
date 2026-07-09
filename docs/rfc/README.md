# Request for Comments（RFC）

**归属 Milestone**：M2 Methodology Core  
**用途**：在正式实现前讨论 AIRS 的较大功能、接口、方法论扩展和评估机制。

## 1. RFC 目的

RFC 用于收集设计意见和约束，适合尚未定稿、影响范围较大或需要多 Agent 协作的变更。RFC 不等同于最终决策；一旦方案被采纳，应转化为 ADR、任务清单或具体实现。

## 2. 适用范围

- 新增大型 Methodology、Skill、Prompt 套件或 Benchmark 套件。
- 调整 Evidence、Score、Evaluation 或 Report Engine 的接口。
- 引入新的数据源、外部工具或跨 Agent 通信 Schema。
- 对合规边界、报告格式或质量标准进行重大调整。

## 3. 命名规范

RFC 文件使用递增编号和短横线命名：

```text
0001-methodology-dsl-extension.md
0002-benchmark-case-taxonomy.md
```

## 4. RFC 模板

```markdown
# RFC-000X: 提案标题

**状态**：Draft | In Review | Accepted | Rejected | Withdrawn  
**日期**：YYYY-MM-DD  
**作者/执行 Agent**：Code Agent / Research Agent / Review Agent / Verification Agent  

## Summary（摘要）
[用简短段落说明提案]

## Motivation（动机）
[说明为什么需要该提案]

## Proposal（方案）
[说明设计、接口、文件和工作流]

## Compatibility（兼容性）
[说明与 README、ARCHITECTURE、AGENTS、SKILL 和既有 Schema 的关系]

## Risks（风险）
[说明技术、数据、合规和维护风险]

## Review Questions（待评审问题）
[列出需要确认的问题]
```

## 5. 审查要求

RFC 必须说明兼容性和风险。涉及投资研究能力的 RFC 必须声明 AIRS 只提供研究框架，不提供荐股、自动交易或价格预测。

