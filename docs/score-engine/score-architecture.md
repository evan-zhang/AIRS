# Score Architecture（评分架构总览）

**归属 Milestone**：M6 Score Engine & Evaluation Engine  
**版本**：v0.6.0  
**最后更新**：2026-07-10

**免责声明**：Score Engine 仅用于 AIRS 投资研究质量控制和研究对象结构化分析，不构成投资建议，不提供买入、卖出、持有、目标价或收益承诺。

## 1. 目标

Score Engine 为 AIRS 提供统一、可解释、可复核的评分层。它承接 M2 Methodology 的 Future Score Mapping、M3 Evidence Level / Confidence / Weight、M4 Prompt 输出和 M5 Skill 执行结果，并输出标准化 Score 与 Scorecard。

Score Engine 不重新定义方法论、证据等级、Prompt 结构或 Skill 调用规则，只负责把这些上游对象转化为统一评分。

## 2. 架构位置

```text
M2 Methodology
    ↓
M3 Evidence Card / Evidence Chain
    ↓
M4 Prompt Output
    ↓
M5 Skill Output
    ↓
Score Engine
    ↓
Evaluation Engine / Report / Benchmark
```

## 3. 核心对象

| 对象 | 职责 | 产物 |
|------|------|------|
| Score DSL | 描述评分维度、公式、权重和门槛 | `docs/score-engine/score-dsl.md` |
| Score Dimension | 计算单个维度得分 | `scoring/*-score.md` |
| Weight System | 管理默认权重、覆盖权重和归一化 | `docs/score-engine/weight-system.md` |
| Scorecard | 汇总维度、证据、解释和置信度 | `schemas/score/scorecard.schema.json` |
| Score Lifecycle | 管理草稿、复核、冻结、更新 | `docs/score-engine/score-lifecycle.md` |

## 4. 标准评分流

1. 读取研究问题、方法论引用、Evidence Chain、Prompt 输出和 Skill trace。
2. 校验输入是否具备 Evidence Card ID、Evidence Level、confidence、weight、supports、refutes 和 missing_evidence。
3. 按评分维度计算 0-100 原始分。
4. 按权重归一化计算综合分。
5. 计算评分置信度，记录扣分来源和不确定性。
6. 输出 Scorecard，并交给 Evaluation Engine 做质量门禁。

## 5. 标准公式

```text
dimension_score = clamp(base_score + evidence_adjustment - penalty, 0, 100)
weighted_score = dimension_score * normalized_weight
overall_score = sum(weighted_score)
confidence_score = evidence_confidence * chain_completeness * counter_evidence_factor
```

其中 `clamp` 表示限制在 0-100，`normalized_weight` 的总和必须等于 1.00。

## 6. 与上游的关系

- 与 M2：使用每个方法论的 Future Score Mapping 作为维度候选，不复制 Theory、Workflow 或 Required Evidence。
- 与 M3：Evidence Score 必须直接使用 Evidence Level、Confidence、Weight、Refutes、Missing Evidence。
- 与 M4：Prompt Score 只检查 Prompt 结构、引用、输出完整性和合规边界，不重写 Prompt。
- 与 M5：Skill Score 只检查 Skill 是否正确引用 Prompt、Methodology、Evidence 与失败处理。

## 7. 输出约束

所有 Score 输出必须包含：

- score_id、score_type、methodology_refs、evidence_chain_refs。
- dimensions、weights、overall_score、confidence_score。
- penalties、missing_evidence_impact、counter_evidence_impact。
- disclaimer_status，必须为 `PRESENT`。

## 8. 禁止事项

- 禁止把评分解释为投资评级。
- 禁止根据评分输出买入、卖出、持有或目标价。
- 禁止在 Score Engine 中重复定义 Evidence Level。
- 禁止跳过反方证据和缺失证据影响。

