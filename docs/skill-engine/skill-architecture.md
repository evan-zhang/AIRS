# Skill Architecture（Skill 架构总览）

## 1. 目标

Skill Engine 是 AIRS 的统一执行层，位于 M4 Prompt Engine、M2 Methodology Layer 与 M3 Evidence Engine 之上。它负责把用户研究意图拆解为可执行 Skill 调用，并保证每个 Skill 只做编排、约束和结果整合，不在 Skill 内部复制 Prompt、方法论或证据规则。

Skill Engine 的核心目标包括：

- 统一 Skill 文档结构、输入输出和调用协议。
- 强制每个 Skill 显式引用 M4 Prompt Library。
- 强制每个 Skill 显式引用 M2 方法论文档。
- 强制每个 Skill 使用 M3 Evidence Card / Evidence Chain 规范。
- 为后续 M6-M8 的评估、Benchmark 和生产化提供可验证接口。

## 2. 分层位置

```
User Intent
  ↓
Master Skill
  ↓
Research / Domain Skill
  ↓
M4 Prompt Engine
  ↓
M2 Methodology + M3 Evidence Engine
  ↓
Report / Verification Skill
```

Master Skill 不直接生成研究结论，而是选择 Research Skill、Evidence Skill、Risk Skill、Report Skill 等组件。Domain Skill 不内置 Prompt，只把研究对象、边界、Evidence Chain ID 和输出要求传给 M4 Prompt。

## 3. 核心组件

- **Skill Document**：位于 `skills/*/*-skill.md`，包含 Purpose、Inputs、Outputs、Dependencies、Invoked Prompt、Invoked Methodology、Invoked Evidence、Workflow、Failure Handling、Review Checklist。
- **Skill Registry**：记录 Skill ID、版本、能力、依赖 Prompt、方法论、证据组件和治理状态。
- **Invocation Protocol**：规定调用请求、上下文、证据链、失败状态和输出结构。
- **Composition Rule**：规定多 Skill 串联、并行、回退和冲突处理方式。
- **Governance Rule**：规定合规边界、版本审计和 Review Agent 评审要求。

## 4. 依赖边界

Skill Engine 必须遵守依赖单向流动：

- Skill 可以引用 Prompt，但不能复制 Prompt 正文。
- Skill 可以引用 Methodology，但不能重新定义方法论理论、评分规则或证据门槛。
- Skill 可以引用 Evidence Engine，但不能重新定义 Evidence Level、Evidence Card 字段或 Evidence Chain 关系。
- Skill 输出必须携带使用过的 Prompt 路径、方法论路径、Evidence Chain ID 和免责声明状态。

## 5. 执行原则

Skill Engine 以“可追溯、可复核、可失败”为原则。可追溯意味着每个结论都能回到 Prompt、方法论和 Evidence Card；可复核意味着 Review Agent 可以基于同一注册表重放调用；可失败意味着当输入不足、证据不足或 Prompt 输出不合格时，Skill 必须返回失败状态，而不是生成看似完整但无法验证的研究结论。

## 6. 合规边界

Skill Engine 只支持投资研究流程，不构成投资建议。所有 Skill 必须拒绝交易指令、收益承诺、价格预测和个性化投资建议。输出如涉及公司、行业或资产，必须标注“仅供研究参考，不构成投资建议，投资有风险”。

