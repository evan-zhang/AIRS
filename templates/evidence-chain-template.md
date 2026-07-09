# AIRS Evidence Chain Template（证据链模板）

**模板版本**：v0.3.0  
**适用 Schema**：`schemas/evidence/evidence-chain.schema.json`  
**免责声明**：本模板用于组织投资研究证据链，不构成投资建议，不提供交易指令、目标价或收益承诺。

---

## 1. 证据链元数据

- **Chain ID**：`EC-YYYYMMDD-XXXX`
- **Title**：[证据链标题]
- **Research Question**：[研究问题]
- **Methodology**：[使用的方法论]
- **Version**：[0.3.0]
- **Review Status**：[DRAFT / PASS / PASS_WITH_LIMITATION / NEEDS_REVISION / FAIL]
- **Overall Confidence**：[0.00-1.00]

## 2. 核心命题

| Claim ID | Claim Type | Statement |
|----------|------------|-----------|
| C-001 | core_conclusion | [核心结论] |
| C-002 | intermediate_judgement | [中间判断] |
| C-003 | counter_claim | [反方命题] |

## 3. 证据卡清单

| Evidence ID | Title | Level | Confidence | Weight | Review Status |
|-------------|-------|-------|------------|--------|---------------|
| EV-YYYYMMDD-0001 | [标题] | A/B/C/D/E | [0-1] | [0-1] | [状态] |

## 4. 证据关系

| From ID | Relation Type | To ID | Notes |
|---------|---------------|-------|-------|
| EV-YYYYMMDD-0001 | supports | C-001 | [说明] |
| EV-YYYYMMDD-0002 | refutes | C-001 | [说明] |
| EV-YYYYMMDD-0003 | qualifies | C-001 | [说明适用边界] |

关系类型可选：`supports`、`refutes`、`contextualizes`、`qualifies`、`conflicts_with`、`depends_on`、`updates`。

## 5. 推理路径

```text
[证据 A] + [证据 B]
    ↓
[中间判断]
    ↓
[核心结论]
    ↘
 [反方证据与限制条件]
```

## 6. 反方证据

| Evidence ID | Refuted Claim | Strength | Impact |
|-------------|---------------|----------|--------|
| EV-YYYYMMDD-0002 | C-001 | medium | [削弱但不推翻 / 推翻 / 限定范围] |

## 7. 缺失证据

- [缺口 1：对结论影响，后续验证方式]
- [缺口 2：对评分或置信度的影响]

## 8. 结论限制

- [限制 1：时间窗口、数据口径或来源限制]
- [限制 2：不得解释为投资建议或评级]

## 9. 下游映射

| 下游模块 | 使用方式 |
|----------|----------|
| Score Layer | [映射到哪些评分维度] |
| Evaluation Layer | [映射到哪些反方观点和不确定性] |
| Report Layer | [报告中引用位置] |
| Benchmark Layer | [标准答案或检查点] |

## 10. 审查结论

- **Can Support Core Conclusion**：[Yes/No]
- **Required Fixes**：[需修复项]
- **Confidence Adjustment**：[置信度调整理由]

