# Connector Governance（连接器治理）

**Feature**：FEATURE-004 Data Connector Framework  
**版本**：v0.1.0  
**最后更新**：2026-07-10

免责声明：本文档和代码仅用于 AIRS 工程开发、研究质量控制和数据接入治理，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## 1. 治理目标

Connector Governance 保证外部数据接入可审计、可替换、可回归。治理对象包括 Connector 注册、认证配置、限流、缓存、错误处理、Schema 演进、健康检查和停用流程。

## 2. 准入标准

新增 Connector 必须满足：

- 提供 Config、Input Schema、Output Schema。
- 输出包含 Source、URL、Timestamp、Version、Trace ID 和 Traceability。
- 明确 Source Priority 和 Source Type。
- 有错误处理、重试策略、缓存策略和健康检查。
- 有最小测试用例和验证脚本覆盖。
- 文档说明使用限制、合规要求和免责声明。

## 3. 版本治理

Connector Version 用于标记接口和归一化逻辑版本。若外部 API 字段变化、归一化字段变化或缓存键变化，必须升级版本并在 CHANGELOG 记录。下游 Evidence Card 应保留 Connector Result 的版本，便于审计。

## 4. 安全治理

API Key、Token 和 Cookie 不得写入文档、示例、报告或 Git。认证上下文只在运行时使用。Mock Connector 不需要真实凭证。

## 5. 运行治理

- 限流：默认按 Connector ID 隔离。
- 缓存：默认记录 TTL、创建时间和命中状态。
- 重试：只对可重试错误生效。
- 健康检查：至少返回状态、延迟、最后成功时间和错误信息。
- 停用：当来源不可靠、违反合规或长期失败时，Registry 可将状态标记为 disabled。

## 6. 审查清单

Review Agent 审查 Connector 时应检查：输出追溯字段是否完整、是否绕过 Evidence Card、是否重复定义 M2/M3/M6 规则、是否存在投资建议表达、是否记录失败和缓存状态。
