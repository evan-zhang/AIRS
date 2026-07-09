# Evidence Review Standard（证据审查标准）

**归属 Milestone**：M3 Evidence Engine  
**版本**：v0.3.0  
**最后更新**：2026-07-10

**免责声明**：证据审查用于提高研究质量，不构成投资建议，不对任何投资结果作出保证。

---

## 1. 审查目标

Evidence Review 的目标不是寻找更多支持材料，而是判断证据是否足够、是否真实、是否相关、是否存在被忽略的反证。Review Agent 必须保持反方视角，避免确认偏误。

## 2. 审查维度

| 维度 | 问题 | 通过标准 |
|------|------|----------|
| 完整性 | 必需字段是否完整 | 16 个必需字段均存在 |
| 来源可靠性 | 来源是否可追溯 | 来源名称、类型、时间、URL 或路径明确 |
| 时间匹配度 | 证据是否适合研究时间范围 | 发布时间、数据期间和采集时间清晰 |
| 相关性 | 证据是否直接对应命题 | supports/refutes 是具体命题 |
| 独立性 | 是否多源独立验证 | 明确原始来源，避免转载伪多源 |
| 反证覆盖 | 是否记录反方证据 | refutes 或 missing_evidence 不为空 |
| 等级合理性 | Evidence Level 是否高估 | 等级符合来源和口径 |
| 可复现性 | 其他 Agent 能否复核 | Traceability 足够明确 |

## 3. 审查结论

Review Agent 应输出四种状态之一：

- `PASS`：可进入 Evidence Chain。
- `PASS_WITH_LIMITATION`：可使用，但必须在报告中说明限制。
- `NEEDS_REVISION`：需要补字段、补来源、补反证或修正等级。
- `REJECTED`：不得用于支撑结论。

## 4. 常见失败

1. 来源只写“媒体报道”，没有来源名称和链接。
2. 支持命题过宽，无法验证。
3. 把专家观点标为 A/B 级事实证据。
4. 未写 missing_evidence。
5. 同一来源多篇转载被计作多源。
6. 只记录支持证据，不记录反证。
7. 证据与结论之间存在跳跃，中间判断缺失。

## 5. 审查输出格式

```markdown
## Evidence Review

- Evidence ID:
- Review Status:
- Main Issues:
- Required Fixes:
- Level Adjustment:
- Confidence Adjustment:
- Missing Evidence:
- Can Support Core Conclusion: Yes/No
```

## 6. 审查门槛

核心结论使用的证据卡必须达到：

- Review Status 为 `PASS` 或 `PASS_WITH_LIMITATION`。
- Evidence Level 不低于 B，或说明为何低等级证据仍可作为辅助。
- Traceability 完整。
- 至少存在一个反证检查记录。

如果不满足，Report Layer 必须降低结论置信度，并在不确定性章节披露。

