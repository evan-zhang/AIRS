# Evidence Review Checklist（证据审查清单）

**归属 Milestone**：M3 Evidence Engine  
**版本**：v0.3.0  
**最后更新**：2026-07-10

**免责声明**：本清单用于 AIRS 研究质量评估，不构成投资建议，不提供交易指令或收益承诺。

---

## 1. 使用方式

Review Agent 使用本清单审查 Evidence Card 与 Evidence Chain。审查结果应给出 PASS、CONDITIONAL PASS 或 FAIL，并说明必须修复的问题。

## 2. 评分 Rubric（100 分）

| 维度 | 分值 | 检查项 |
|------|------|--------|
| 字段完整性 | 15 | Evidence Card 是否包含 16 个必需字段；Evidence Chain 是否包含命题、证据、关系和缺口 |
| 来源可靠性 | 15 | Source、Source Type、URL、Publication Time 是否明确，等级是否合理 |
| 可追溯性 | 15 | Traceability 是否能让其他 Agent 复核来源、处理步骤和下游引用 |
| 命题相关性 | 15 | Supports / Refutes 是否绑定具体可验证命题 |
| 反方覆盖 | 15 | 是否记录反证、冲突证据或替代解释 |
| 缺口透明度 | 10 | Missing Evidence 是否具体，是否说明后续验证路径 |
| 时间与口径 | 10 | 时间范围、数据口径、更新需求是否明确 |
| 合规与免责声明 | 5 | 是否避免荐股、目标价、确定性收益表达，并包含免责声明 |

## 3. 等级判定

- **PASS（85-100）**：可进入 Evidence Chain，可支撑研究结论。
- **CONDITIONAL PASS（70-84）**：可作为辅助证据，但必须披露限制并降低置信度。
- **FAIL（0-69）**：不得支撑核心结论，需补证、降级或剔除。

## 4. 必须 FAIL 的情况

以下任一情况出现时，即使总分较高，也必须判定为 FAIL：

- 核心证据没有可追溯来源。
- 缺少 Evidence ID 或来源时间。
- 用 D/E 级证据单独支撑核心结论。
- 没有任何反方证据或缺口披露。
- 出现“建议买入”“目标价”“保证收益”等违规表达。
- Evidence Level 明显高估且未修正。

## 5. Review Agent 输出模板

```markdown
## Evidence Review Result

- Review Object:
- Score:
- Result: PASS / CONDITIONAL PASS / FAIL
- Key Strengths:
- Key Issues:
- Required Fixes:
- Level Adjustment:
- Confidence Adjustment:
- Missing Evidence To Add:
- Compliance Notes:
```

## 6. Code Agent 自检要点

Code Agent 在交付 Evidence Engine 时应确认：

- `docs/evidence/` 8 个文档存在且有实际内容。
- `schemas/evidence/` 3 个 JSON Schema 有效。
- `evidence-card.schema.json` 包含 16 个必需字段。
- 证据卡模板和证据链模板存在。
- 本 checklist 存在。
- M1/M2 自检和 M3 自检均 PASS。

