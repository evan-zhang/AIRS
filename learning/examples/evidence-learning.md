# Evidence Learning Example

## Feedback Input

- Evidence Card 中部分来源缺少 trace_id、版本或采集时间。
- Report 引用证据时未说明证据等级变化。

## Pattern Mining

Learning Engine 将反馈归并为 `evidence/source_traceability_gap`，并标注其影响 Report、Score 和 Review 的可复核性。

## Rule Generation

生成规则候选：Evidence Card 缺少 source、url、timestamp、version 或 traceability 时不得进入最终报告。

## Optimization Suggestions

- Prompt：要求输出证据字段完整性检查。
- Skill：Evidence Skill 增加缺失字段失败处理。
- Score：对缺少 traceability 的证据降低权重。

## 免责声明

本示例仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

