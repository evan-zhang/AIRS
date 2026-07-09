# Prompt Versioning（Prompt 版本管理）

**归属 Milestone**：M4: Prompt DSL & Prompt Library  
**适用层级**：Prompt Engine  
**免责声明**：本文档只定义 Prompt 版本管理规则，不构成投资建议，不提供交易指令、目标价或收益承诺。

## 1. 版本格式

Prompt 使用语义化版本：`major.minor.patch`。

- `major`：Input Schema、Output Schema 或方法论引用发生破坏性变化。
- `minor`：新增输出字段、补充审查项、扩展可选变量，保持兼容。
- `patch`：修正文案、错别字、示例、非结构性说明。

M4 初始 Prompt 版本为 `0.4.0`。

## 2. 版本元数据

每个 Prompt 文档末尾应保留：

- 归属 Milestone。
- Prompt 版本。
- 最后更新日期。
- 方法论引用。
- 证据规范引用。
- 审查状态。

## 3. 兼容性规则

如果 Prompt 增加必填输入变量，必须升 `major`。如果只增加可选变量，可升 `minor`。如果调整 System Prompt 但不改变输入输出契约，可升 `patch` 或 `minor`，由 Review Agent 根据影响范围判断。

## 4. 追溯要求

研究报告中应记录使用的 Prompt ID 与版本。若报告结论被复核，应能回溯到：

1. Prompt 文档版本。
2. M2 方法论版本或文件路径。
3. M3 Evidence Card / Evidence Chain 版本。
4. 生成报告的时间和执行 Agent。

## 5. 禁止行为

- 禁止无版本号的生产 Prompt。
- 禁止修改已被报告引用的 Prompt 后不记录版本变化。
- 禁止让 Skill 固定调用“最新 Prompt”而不记录实际版本。

## 6. 发布记录要求

每次发布 Prompt 时，Completion Report 或变更记录中至少说明 Prompt ID、旧版本、新版本、变更类型、受影响 Skill、受影响 Benchmark 和自检结果。若 Prompt 的证据要求随 M3 Evidence Engine 更新而调整，应说明是引用路径变化、字段使用变化，还是输出结构变化。

## 7. 回滚规则

当新版本 Prompt 造成输出结构不兼容、合规风险或证据链断裂时，可以回滚到最近一个 APPROVED 版本。回滚不是删除历史版本，而是在调用配置中恢复旧版本，并记录回滚原因、触发条件和后续修复计划。

## 8. 与报告追溯的关系

Report Layer 生成报告时必须保留 Prompt ID 和版本。后续复核报告时，Review Agent 应确认报告所用 Prompt 与当时的 M2/M3 规范兼容；如果 Prompt 已废弃，只能说明历史报告基于旧版本生成，不能静默用新版本重新解释旧结论。
