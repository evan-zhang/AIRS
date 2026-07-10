# ADR - News Connector Feature Package

**状态**：Proposed  
**日期**：2026-07-10  
**Feature**：FEATURE-NEWS-001  

## 背景

AIRS 已包含 News Skill 和新闻事件影响分析能力的基础引用，但还缺少面向外部新闻接入的 Feature Package。News Connector 先定义事件结构、Prompt、Skill、Schema、测试和 Benchmark，避免直接在已有 M1-M8 资产中扩散修改。

## 决策

采用独立 Builder Package 定义 News Connector。Connector 只负责把新闻输入标准化为 AIRS 可消费的事件证据，不执行交易判断，不替代 Evidence Validation。

## 备选方案

- 直接扩展 `skills/news/news-skill.md`：可能影响 M5 已验收内容。
- 仅增加 Prompt：无法覆盖 Schema、测试和发布材料。
- 使用 Builder Package：能保持新增能力可审查、可回归。

## 影响

- 为后续新闻数据源接入提供工程入口。
- 强化新闻事件与 Evidence Card 的绑定。
- 保留事实、解读、推断之间的边界，降低过度归因风险。

## 风险

- 新闻来源可能存在延迟、偏见或二次传播失真。
- 事件影响分析容易被误读为投资建议，必须强制输出免责声明和不确定性。

## 免责声明

本 ADR 仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

