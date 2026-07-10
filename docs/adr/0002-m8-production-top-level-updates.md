# ADR 0002: M8 Production 顶层文件受控更新

**状态**：Accepted  
**日期**：2026-07-10  
**相关里程碑**：M8 Production Release

## Context

M1-M7 已经通过验收并提交。M8 明确要求完善 README、CONTRIBUTING、CHANGELOG、ROADMAP 和 LICENSE，以支持 V1.0 Production Release。由于 README、CONTRIBUTING、CHANGELOG、ROADMAP、LICENSE 属于顶层核心文件，任何生产化修改都需要记录原因和影响。

## Decision

M8 对顶层文件采取受控增量更新：

- README：补充 V1.0 Production 状态、完整功能列表和最终免责声明。
- CONTRIBUTING：补充 V1.0 贡献流程、版本规范和发布流程引用。
- CHANGELOG：新增 v1.0.0 release 记录。
- ROADMAP：标注 M1-M8 完成，并补充 V1.x / V2 路线。
- LICENSE：确认 MIT License 与投资研究免责声明已经满足 V1.0 要求，不修改。

## Consequences

这些更新不会改变 M1-M7 已 PASS 的核心能力语义，只修正顶层状态与最终发布治理信息，使项目文档与 V1.0 Production Release 保持一致。

## Compliance Boundary

所有更新必须继续保留“不构成投资建议”边界，不新增荐股、自动交易、目标价或收益承诺能力声明。

## 免责声明

本 ADR 仅说明 AIRS 工程治理决策，不构成投资建议，不提供交易指令或收益承诺。
