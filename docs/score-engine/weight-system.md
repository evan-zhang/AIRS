# Weight System（权重体系）

**归属 Milestone**：M6 Score Engine & Evaluation Engine  
**版本**：v0.6.0  
**最后更新**：2026-07-10

**免责声明**：权重体系用于研究评分解释，不构成投资建议或投资评级。

## 1. 目标

Weight System 定义 AIRS 评分权重的默认值、覆盖规则、归一化规则和审计要求。权重只表达研究框架中的相对重要性，不表达资产配置比例或交易建议。

## 2. 权重层级

| 层级 | 来源 | 说明 |
|------|------|------|
| Global Default | M6 Score Engine | 所有评分通用默认权重 |
| Methodology Default | M2 Future Score Mapping | 某个方法论的建议权重 |
| Task Override | 研究任务约束 | 由用户或 Benchmark 指定 |
| Review Adjustment | Review Agent | 因证据缺口或反证压力调整 |

优先级：`Review Adjustment > Task Override > Methodology Default > Global Default`。

## 3. 默认综合权重

| 维度 | 默认权重 | 说明 |
|------|----------|------|
| Evidence Score | 0.25 | 证据质量是所有评分基础 |
| Methodology Score | 0.15 | 方法论匹配与执行完整度 |
| Prompt Score | 0.10 | Prompt 输出结构和合规 |
| Skill Score | 0.10 | Skill 调用与失败处理 |
| Report Score | 0.15 | 报告结构、反方观点和披露 |
| Risk Score | 0.10 | 风险识别与披露 |
| Confidence Score | 0.10 | 置信度与不确定性 |
| Theme Score | 0.05 | 主题或研究对象相关度 |

总和为 1.00。

## 4. 归一化公式

```text
normalized_weight_i = raw_weight_i / sum(raw_weight)
```

当某个维度不可用时，不得直接删除；必须记录缺失原因，并在 Evaluation Gate 中判断是否允许归一化。核心维度 Evidence Score 缺失时必须 FAIL。

## 5. 扣分权重

| 扣分项 | 默认影响 | 说明 |
|--------|----------|------|
| missing_evidence | 5-20 | 按关键证据缺口严重度扣分 |
| unsupported_claim | 10-30 | 结论未绑定证据 |
| weak_counter_evidence | 5-15 | 反方观点无实质证据 |
| compliance_missing | 强制 FAIL | 缺少免责声明或出现交易建议 |
| stale_evidence | 3-12 | 证据时间不匹配 |

## 6. 审计规则

每次权重调整必须记录：

- 调整前权重。
- 调整后权重。
- 调整原因。
- 调整 Agent。
- 是否影响综合评分等级。

