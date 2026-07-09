# Prompt Governance（Prompt 治理）

**归属 Milestone**：M4: Prompt DSL & Prompt Library  
**适用层级**：Prompt Engine → Agent 协作流程  
**免责声明**：本文档用于 AIRS Prompt 治理，不构成投资建议，不提供买卖指令或收益承诺。

## 1. 治理目标

Prompt Governance 确保 AIRS 中的 Prompt 可执行、可复核、可追溯、可合规。治理重点不是让 Prompt 产生更强结论，而是让 Prompt 产生证据充分、反方完整、不确定性清晰、边界明确的研究输出。

## 2. 角色职责

| 角色 | 职责 |
|------|------|
| Code Agent | 创建和维护 Prompt、Schema、验证脚本 |
| Research Agent | 按 Prompt 执行研究，不绕过证据要求 |
| Review Agent | 审查 Prompt 与输出质量 |
| Verification Agent | 运行验证脚本和 Benchmark |

## 3. 合规底线

所有 Prompt 必须强制输出免责声明，并禁止：

- 荐股、交易指令、目标价预测。
- 将研究评分解释为投资评级。
- 用单一低等级证据支撑核心结论。
- 忽略反方观点或缺失证据。
- 在证据不足时编造数据。

## 4. 质量门槛

生产版 Prompt 至少满足：

1. 七个必需 section 全部完整。
2. System Prompt 可直接复制执行。
3. Input Schema 与 Output Schema 清晰。
4. Evidence Requirements 引用 M3 Evidence Card。
5. Review Checklist 能被 Review Agent 逐项打勾。

## 5. 例外处理

当输入不足、来源不可访问、证据冲突或方法论不适配时，Prompt 必须要求 Agent 输出“无法形成结论”的原因、已完成检查范围、缺失 Evidence Card 和后续验证建议。

## 6. 审计要求

每次 Prompt 发布应能回答：

- 这个 Prompt 服务哪个 M2 方法论？
- 它要求哪些 Evidence Card 字段？
- 它怎样处理反方证据和 missing_evidence？
- 它是否会诱导投资建议？
- 它是否通过 M4 自检脚本？

