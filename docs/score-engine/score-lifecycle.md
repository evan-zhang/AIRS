# Score Lifecycle（评分生命周期）

**归属 Milestone**：M6 Score Engine & Evaluation Engine  
**版本**：v0.6.0  
**最后更新**：2026-07-10

**免责声明**：评分生命周期用于研究质量治理，不构成投资建议、投资评级或收益判断。

## 1. 状态流转

```text
DRAFT → COMPUTED → REVIEWED → GATED → FROZEN
   ↓        ↓          ↓         ↓
REJECTED ← NEEDS_FIX ← LOOP ← CONDITIONAL
```

## 2. 状态定义

| 状态 | 含义 | 进入条件 | 退出条件 |
|------|------|----------|----------|
| DRAFT | 评分输入已创建 | 有研究问题和方法论引用 | 输入字段完整 |
| COMPUTED | 分数已计算 | 维度、权重和公式有效 | Review Agent 复核 |
| REVIEWED | 已人工或自动复核 | 无结构性错误 | Evaluation Gate |
| GATED | 已通过质量门禁 | PASS 或 CONDITIONAL_PASS | 报告冻结 |
| FROZEN | 固化为报告引用版本 | 报告引用该评分 | 新证据触发新版本 |
| NEEDS_FIX | 需要修复 | 条件通过或小错误 | Loop 修复 |
| REJECTED | 不合格 | 强制失败条件 | 重新采证或重算 |

## 3. 版本规则

- 修改公式、维度或权重：major，例如 `v1.0.0`。
- 修改证据输入或缺口影响：minor，例如 `v0.7.0`。
- 修正错别字、说明文字：patch，例如 `v0.6.1`。

## 4. 更新触发器

- 新增 A/B 级核心证据。
- Evidence Level、Confidence 或 Weight 被复核调整。
- M2 方法论 Future Score Mapping 更新。
- M4 Prompt 输出结构变化。
- M5 Skill 调用 trace 显示失败处理未覆盖。
- Evaluation Engine 回归测试失败。

## 5. 冻结规则

报告引用的 Scorecard 必须处于 `FROZEN` 或 `GATED` 状态。冻结版本不得就地修改；任何重算必须生成新 `score_id` 或新版本号，并在报告中说明差异。

## 6. 审计要求

每个 Scorecard 必须记录：

- 输入 Evidence Chain ID。
- 评分公式版本。
- 权重版本。
- 计算 Agent 和复核 Agent。
- Evaluation Gate 结果。
- 免责声明状态。

