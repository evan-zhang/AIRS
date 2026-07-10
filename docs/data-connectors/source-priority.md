# Data Source Priority（数据源优先级）

**Feature**：FEATURE-004 Data Connector Framework  
**版本**：v0.1.0  
**最后更新**：2026-07-10

免责声明：本文档和代码仅用于 AIRS 工程开发、研究质量控制和数据接入治理，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## 1. 优先级顺序

AIRS Connector Framework 使用以下数据源优先级：

1. Official：政府、统计机构、标准制定机构等官方来源。
2. Regulatory：SEC、交易所监管披露、监管公告和法定申报。
3. Company：公司公告、财报、官网投资者关系材料。
4. Exchange：交易所行情、上市资料、公告系统。
5. Trusted Third-party：经过治理登记的专业数据库或研究数据供应商。
6. Public News：公开新闻媒体。
7. Community：社区、论坛、个人博客或非正式来源。

## 2. 使用规则

优先级只决定证据采集和冲突处理时的排序，不等同于投资价值或结论强度。高优先级来源仍可能存在滞后、口径差异或披露不完整；低优先级来源可以作为线索，但不得单独支撑核心结论。

## 3. 冲突处理

当多个 Connector 输出冲突时，Research Agent 应优先检查：

- 是否是同一事实的不同时间版本。
- 是否存在口径差异。
- 是否存在币种、会计准则、统计范围差异。
- 是否有监管或公司源能够验证。
- 是否需要写入 Evidence Card 的 `refutes` 或 `missing_evidence`。

## 4. 与 Evidence Level 的关系

Source Priority 不重复定义 M3 Evidence Level。它只提供数据源选择顺序；Evidence Level 仍由 Evidence Engine 根据来源、可验证性、独立性、时效性和命题相关性判断。

## 5. 当前官方 Connector 映射

- SEC / EDGAR：Regulatory。
- Yahoo Finance：Trusted Third-party。
- Alpha Vantage：Trusted Third-party。
- News：Public News。
- GitHub：Community 或 Company，取决于仓库归属。
- RSS：按 feed 发布者映射，默认 Public News。

## Traceability 对齐

Connector 输出必须保留 Source、URL、Timestamp、Version、Trace ID 和 Traceability，并传递给 Evidence Card 的追溯字段。
