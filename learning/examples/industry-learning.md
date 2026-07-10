# Industry Learning Example

## Feedback Input

- 行业研究在范围定义上出现漂移，子行业边界不清晰。
- Review Agent 要求 Methodology 增加适用范围和排除范围。

## Pattern Mining

Learning Engine 将反馈归并为 `methodology/scope_drift`，并通过 Outcome 记录发现评分解释需要体现范围不确定性。

## Rule Generation

生成规则候选：当 Methodology 出现 scope_drift 时，研究计划必须显式记录行业边界、时间范围、地理范围和排除项。

## Optimization Suggestions

- Methodology：补充 Scope Boundary 小节。
- Prompt：要求输出包含边界假设。
- Score：对范围不明确的结论降低置信度。

## 免责声明

本示例仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

