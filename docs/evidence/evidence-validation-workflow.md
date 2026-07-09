# Evidence Validation Workflow（证据验证工作流）

**归属 Milestone**：M3 Evidence Engine  
**版本**：v0.3.0  
**最后更新**：2026-07-10

**免责声明**：证据验证工作流仅用于研究过程控制，不构成投资建议，不提供交易决策。

---

## 1. 标准流程

```
1. 定义研究命题
2. 从方法论抽取 Required Evidence / Counter Evidence
3. 采集原始材料
4. 生成 Evidence Card
5. 执行字段完整性检查
6. 执行来源与时间检查
7. 执行反证与缺口检查
8. 生成 Evidence Chain
9. 输出审查结果给 Score / Evaluation / Report
```

## 2. 详细步骤

### 2.1 定义研究命题

Research Agent 先把研究问题拆成可验证命题。例如“某环节是供应链卡点”应拆成供给约束、替代难度、需求影响、扩产周期和反方缓释因素。

### 2.2 抽取证据需求

从 M2 方法论文档读取 Required Evidence 和 Counter Evidence，形成证据需求清单。每个需求都应有 ID，方便绑定证据卡。

### 2.3 采集材料

优先采集 A/B 级来源。若只能取得 C/D 级来源，必须同时写入 missing_evidence，说明缺少哪些原始材料。

### 2.4 生成证据卡

每条材料生成一张或多张 Evidence Card。若一个来源包含多个独立事实，允许拆分多张卡，但 Traceability 必须指向同一来源。

### 2.5 自动校验

Verification Agent 或脚本检查：

- Schema 是否通过。
- 16 个必需字段是否存在。
- 时间格式是否可识别。
- Evidence Level 是否在允许枚举内。
- Weight 和 Confidence 是否在合理范围内。

### 2.6 人工或 Agent 审查

Review Agent 按 Evidence Review Standard 输出审查结论。被标为 `NEEDS_REVISION` 或 `REJECTED` 的证据不得直接进入核心证据链。

### 2.7 证据链构建

通过审查的证据卡按命题组织成 Evidence Chain，并标注关系。每个核心结论必须能回溯到至少一条链。

## 3. PASS / FAIL 标准

### PASS

- 所有核心证据卡字段完整。
- 至少一个 A/B 级证据支撑核心结论。
- 反证已检查并记录。
- 缺口已披露。
- Evidence Chain 能解释推理路径。

### FAIL

- 核心结论没有证据卡。
- 证据来源不可追溯。
- 缺少反证审查。
- 用 D/E 级证据支撑高置信度结论。
- 报告输出投资建议、目标价或确定性收益表达。

## 4. Loop/Go 应用

Code Agent 和 Research Agent 应按 Loop 模式处理验证失败：

```python
while evidence_validation_result == "FAIL":
    identify_missing_fields()
    collect_or_mark_missing_evidence()
    adjust_level_and_confidence()
    rebuild_evidence_chain()
    rerun_validation()
```

## 5. 输出给下游

- Score Layer 接收 Evidence Level、Weight、Confidence。
- Evaluation Layer 接收 Refutes、Missing Evidence、Review Notes。
- Report Layer 接收 Evidence Chain、核心证据摘要和免责声明。
- Benchmark Layer 接收标准证据链和失败案例。

