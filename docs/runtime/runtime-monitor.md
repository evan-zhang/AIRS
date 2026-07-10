# Runtime Monitor（监控）

## 1. 职责

Runtime Monitor 汇总执行健康度、任务进度、事件密度、失败原因、资源使用和合规状态，为 Code Agent、Review Agent 与 Verification Agent 提供运行报告。

## 2. 指标

核心指标包括 total_tasks、completed_tasks、failed_tasks、cancelled_tasks、retry_count、timeout_count、message_count、event_count、human_waiting_count 和 disclaimer_coverage。

## 3. Dashboard

Monitor 可输出 Markdown Dashboard，包含 Runtime Plan、Agent Graph、Execution Timeline、Event Log、Context Snapshot 和 Final State 摘要。

## 4. 合规检查

Monitor 检查是否存在 Workflow 直接驱动业务模块、缺少免责声明、缺少 Evidence 引用或输出交易指令等问题。

---

免责声明：本文档和示例仅用于 AIRS 工程开发、投资研究流程编排与质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。
