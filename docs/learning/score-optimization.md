# Score Optimization

## 1. 目标

Score Optimization 用于校准研究质量评分，不用于形成投资评级。它根据 Evidence 质量、Outcome 偏差、反方证据、缺失证据和报告一致性提出权重调整建议。

## 2. 常见信号

- 低证据等级结论获得过高置信度。
- Outcome 复核显示原评分对不确定性惩罚不足。
- Committee 少数意见没有进入 Scorecard。
- Report 把 Memory 摘要当成证据，导致评分来源不清。

## 3. 输出

Score Proposal 包含 change_type、source_rule、summary、review_status 和 rollback_plan。所有权重变动必须有 Benchmark 支持，并保留调整前后对比。

## 4. 约束

Score Optimization 不输出买入、卖出、持有、目标价或收益预测，只服务研究质量控制。

## 免责声明

本文档仅用于 AIRS 工程开发、研究质量控制和持续改进，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

