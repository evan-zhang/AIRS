# Committee Report Learning Example

## Feedback Input

- Committee Decision Record 未充分解释少数意见如何影响报告修订。
- Report 没有把 Follow-up Tasks 映射到 Evidence 或 Score 改进。

## Pattern Mining

Learning Engine 将反馈归并为 `committee/decision_record_gap`，并识别记录结构影响后续 Review Agent 验证。

## Rule Generation

生成规则候选：Committee 通过或有条件通过时，Decision Record 必须列出少数意见、Follow-up Tasks、证据引用和报告修订要求。

## Optimization Suggestions

- Skill：Committee Skill 增加 Decision Record 完整性门禁。
- Prompt：报告生成 Prompt 引用 Committee Follow-up Tasks。
- Memory：只保存可审计摘要，不替代 Decision Record。

## 免责声明

本示例仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。
