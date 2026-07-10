# Company Learning Example

## Feedback Input

- 公司研究报告在 Evidence 引用表中缺少部分来源解释。
- Committee 要求把推断和事实区分得更清楚。

## Pattern Mining

Learning Engine 将两条反馈归并为 `report/evidence_gap` 模式，并结合 Outcome 偏差识别出 `score/outcome_variance`。

## Rule Generation

生成规则候选：当 Report 出现 evidence_gap 且频次达到阈值时，必须增加证据复核、反方观点和不确定性标注。

## Optimization Suggestions

- Prompt：补充 Evidence 引用检查项。
- Score：降低低证据置信度结论的权重。
- Report：把 Memory 摘要降级为上下文，不作为证据。

## 免责声明

本示例仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

