# Skill Composition（Skill 组合规则）

## 1. 组合目标

Skill Composition 规定多个 Skill 如何串联、并行、回退和合并结果。组合规则避免重复调用、重复定义证据规则，也避免不同 Skill 输出互相覆盖。

## 2. 标准组合链路

标准研究链路如下：

```
Master Skill
  → Research Skill
  → Domain Skill（Supply Chain / Financial / News / Valuation / Risk）
  → Evidence Skill
  → Report Skill
  → Verification Skill
```

Master Skill 负责调度；Research Skill 负责研究计划；Domain Skill 负责专题分析；Evidence Skill 负责证据卡与证据链；Report Skill 负责整合输出；Verification Skill 负责结构、合规和引用检查。

## 3. 串行规则

当后一个 Skill 依赖前一个 Skill 的输出时必须串行。例如 Report Skill 必须等待 Evidence Skill 输出 Evidence Chain 摘要；Verification Skill 必须等待 Report Skill 输出完整报告。串行调用需要传递 `request_id`、`evidence_chain_ids` 和 `used_prompts`。

## 4. 并行规则

多个 Domain Skill 可以并行执行，但必须共享同一个研究范围和证据命题列表。例如 Supply Chain Skill 与 Financial Skill 可以同时分析产业链和财报异常，随后由 Evidence Skill 合并 Evidence Card。并行结果存在冲突时，不得强行取平均，应交给 Risk Skill 或 Review Agent 标注不确定性。

## 5. 回退规则

当主 Skill 失败时，允许回退：

- Supply Chain Skill 证据不足，可回退到 Evidence Skill 生成缺失证据清单。
- Valuation Skill 估值样本不足，可回退到 Risk Skill 标注估值不确定性。
- Report Skill 结构不完整，可回退到 Verification Skill 返回修复清单。

回退不能绕过 M4 Prompt，也不能跳过 M3 Evidence Card。

## 6. 合并规则

合并多个 Skill 输出时，必须保留来源：

- 每个结论绑定来源 Skill。
- 每个结论绑定 Evidence Card ID。
- 每个反方观点绑定 `refutes` 或 `missing_evidence`。
- 每个不确定性标注说明触发 Skill。
- 报告中不得把低置信度结论写成确定性判断。

## 7. 合规说明

**免责声明**：组合规则用于研究流程编排，不构成投资建议。多 Skill 一致并不等同于投资确定性，冲突或缺失证据必须显式保留。
