# AIRS Prompt Review Checklist（Prompt 审查清单）

**归属 Milestone**：M4: Prompt DSL & Prompt Library  
**适用角色**：Review Agent / Verification Agent  
**免责声明**：本清单用于提示词质量审查，不构成投资建议，不提供交易指令或收益承诺。

## 1. 评分维度（100 分）

| 维度 | 分值 | 检查重点 |
|------|------|----------|
| 方法论一致性 | 20 | 是否引用并遵循对应 M2 方法论 |
| 证据一致性 | 20 | 是否使用 M3 Evidence Card / Evidence Chain |
| 可执行性 | 15 | System Prompt 是否完整、清晰、可直接执行 |
| 输入输出契约 | 15 | Input Schema 与 Output Schema 是否完整 |
| 反方与不确定性 | 10 | 是否强制输出反方观点、missing_evidence 和置信度 |
| 合规边界 | 15 | 是否禁止荐股、交易指令、目标价、收益承诺 |
| 可维护性 | 5 | 版本、状态、引用路径是否清晰 |

## 2. PASS 标准

- 总分不低于 85。
- 没有强制 FAIL 项。
- Prompt 可被对应 Skill 直接调用。
- 输出能够被 Report、Evaluation、Benchmark 复用。

## 3. PASS_WITH_LIMITATION 标准

- 总分 70-84。
- 没有严重合规风险。
- 仅在指定场景可使用，并必须记录限制。

## 4. FAIL 标准

出现任一情况即 FAIL：

- 缺少七个必需 section 之一。
- 未引用 M2 方法论。
- Evidence Requirements 未引用 M3 Evidence Card 或 Evidence Chain。
- 缺少免责声明。
- 允许或诱导买入、卖出、持有、目标价或收益承诺。
- 输出不包含反方观点或不确定性。

## 5. Review Agent 输出模板

```markdown
## Prompt Review

- Prompt：
- Version：
- Result：PASS / PASS_WITH_LIMITATION / FAIL
- Score：
- Methodology Alignment：
- Evidence Alignment：
- Compliance：
- Required Fixes：
- Known Limitations：
```

