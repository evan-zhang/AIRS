# ADR-0004: Data Connector Framework

**状态**：Accepted  
**日期**：2026-07-10  
**Feature**：FEATURE-004 Data Connector Framework

## 免责声明

本文档仅用于 AIRS 工程开发、生产治理和研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## 背景

AIRS 已完成 Methodology、Evidence、Knowledge Graph 和 Report Generator 等核心规范，但外部数据接入仍需要统一边界。如果 Methodology、Skill、Knowledge Graph 或 Report 直接访问外部 API，会导致认证、限流、缓存、重试、字段归一化和追溯信息散落在多个层中，影响审计和回归。

## 决策

引入 Data Connector Framework。所有外部数据源必须通过 Connector 接入。Connector 负责 Register、Authenticate、Fetch、Normalize、Validate、Cache 和 Publish，并输出统一 Connector Result。

Connector Result 必须包含：

- Source
- URL
- Timestamp
- Version
- Trace ID
- Traceability

本 Feature 提供六个官方 Mock Connector：SEC / EDGAR、Yahoo Finance、Alpha Vantage、News、GitHub、RSS。Mock Connector 不联网，不访问真实交易接口，仅用于接口稳定性、自检和回归。

## 不做的事情

- 不修改 M2 Methodology 设计。
- 不修改 M3 Evidence Card 设计。
- 不修改 FEATURE-002 Knowledge Graph 设计。
- 不修改 FEATURE-003 Report Generator 设计。
- 不实现自动交易、下单、荐股或价格预测。

## 后果

正面影响：

- 外部数据接入有统一治理边界。
- 认证、限流、缓存、重试和健康检查可以复用。
- 下游 Evidence Card 能稳定继承 Source / URL / Timestamp / Version / Traceability。
- Review Agent 和 Verification Agent 可以通过统一脚本检查 Connector 完整性。

代价：

- 新数据源必须先开发 Connector，不能直接在业务层抓取。
- 真实 API 接入前需要补充凭证管理、网络错误处理和供应商条款审查。

## 验证

使用 `python3 scripts/validate_connectors.py` 验证文档、核心组件、六个 Connector、Schema、模板、Builder Package、Completion Report、自评报告和运行时输出。
