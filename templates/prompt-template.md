# [Prompt Name]（[中文名称]）

**Prompt ID**：[prompt.category.name]  
**版本**：v0.4.0  
**归属 Milestone**：M4: Prompt DSL & Prompt Library  
**方法论引用**：`docs/methodology/[methodology].md`  
**证据规范引用**：`docs/evidence/evidence-card-specification.md`、`docs/evidence/evidence-validation-workflow.md`  
**免责声明**：本 Prompt 仅用于投资研究，不构成投资建议，不提供买卖指令、目标价或收益承诺。

## 1. System Prompt（系统提示词）

[写入可直接执行的完整中文系统提示词。必须说明角色、任务、方法论引用、证据要求、输出边界、反方观点、不确定性和免责声明。]

## 2. User Template（用户输入模板）

```text
研究问题：{{research_question}}
研究对象：{{target}}
时间范围：{{time_range}}
地理或市场范围：{{market_scope}}
可用证据：{{evidence_cards}}
输出要求：{{output_requirements}}
```

## 3. Input Schema（输入数据结构）

```json
{
  "research_question": "string",
  "target": "string",
  "time_range": "string",
  "market_scope": "string",
  "evidence_cards": "array",
  "output_requirements": "object"
}
```

## 4. Output Schema（输出数据结构）

```json
{
  "summary": "string",
  "methodology_ref": "string",
  "claims": [],
  "evidence_chain": {},
  "counter_arguments": [],
  "uncertainties": [],
  "failure_status": "string",
  "disclaimer": "string"
}
```

## 5. Evidence Requirements（证据要求）

[说明必须使用 M3 Evidence Card / Evidence Chain 字段，包括 supports、refutes、missing_evidence、traceability、evidence_level、confidence。不要重写证据等级定义，只引用 M3 规范。]

## 6. Failure Cases（失效场景）

- [必填输入缺失]
- [证据不足或不可追溯]
- [反方观点不足]
- [方法论不适配]
- [输出触及荐股、交易或价格预测]

## 7. Review Checklist（审查清单）

- [ ] 已引用正确 M2 方法论。
- [ ] 已使用 M3 Evidence Card / Evidence Chain。
- [ ] System Prompt 可直接执行。
- [ ] 输出包含反方观点、不确定性和免责声明。
- [ ] 未输出投资建议、交易指令、目标价或收益承诺。

---

**审查状态**：DRAFT  
**最后更新**：YYYY-MM-DD

