# ADR-0014: APP-001 Equity Research App

## 状态

Accepted

## 日期

2026-07-10

## 背景

AIRS 已经具备 Planner、Committee、Runtime、Data Connector、Investment Engine、Knowledge Graph、Report Generator、Memory 和 Learning 等基础能力，但用户仍需要一个可以直接输入股票代码、公司名称或研究问题的应用入口。APP-001 是第一个应用层交付，用于验证 AIRS 全链路是否可以被组合成可运行的股票研究工作流。

免责声明：本 ADR 仅记录工程架构决策，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## 决策

在 `apps/equity_research/` 新增 APP-001，并采用轻量编排方式串联既有模块：

- `request_parser.py` 标准化用户输入。
- `company_resolver.py` 通过本地目录解析常见股票代码与公司名称，未命中时返回 `NEED_REVIEW`。
- `data_collector.py` 通过 FEATURE-013 Connector 获取数据，真实数据不可用时写入 Mock/SKIP 降级说明。
- `analyzer.py` 复用 Investment Engine，生成 Profile、Industry、Supply Chain、Financial、Valuation、Catalyst、Risk、Evidence Chain、Knowledge Graph 和 Score Card。
- `report_exporter.py` 复用 Report Generator，并输出 APP-001 要求的 15 段报告。
- `app.py` 作为统一入口，执行 Planner、Committee、Runtime、Connector、Analysis、二次 Committee、Report、Memory 和 Learning。

## 约束

- 所有投资相关输出必须包含免责声明。
- 所有 section 必须区分 Facts / Inference / Assumption / Opinion。
- Mock/SKIP 只能作为工程降级信号，不能冒充真实研究证据。
- Committee Decision 和 Score Card 只用于研究质量控制，不得解释为投资评级或交易建议。

## 后果

正向影响：

- AIRS 首次具备直接可运行的应用层入口。
- 15 段输出规范为后续 APP-002、APP-003 提供模板。
- 自检脚本可验证应用完整性、案例、Schema、文档和运行时输出。

代价与缺口：

- 公司目录仍是小型本地目录，覆盖范围有限。
- Yahoo Finance Connector 当前仍是 Mock 模式，真实财务数据需后续接入。
- APP-001 的分析深度受当前 Connector 与 Investment Engine 最小实现约束。

