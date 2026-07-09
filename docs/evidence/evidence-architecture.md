# Evidence Architecture（证据架构总览）

**归属 Milestone**：M3 Evidence Engine  
**适用层级**：Methodology Layer → Evidence Layer → Score Layer → Evaluation Layer → Report Layer  
**版本**：v0.3.0  
**最后更新**：2026-07-10

**免责声明**：本文档用于定义 AIRS 投资研究框架中的证据组织方式，不构成投资建议，不提供买入、卖出、持有或价格预测指令。

---

## 1. 目标

Evidence Engine 的目标是为 AIRS 提供统一、可验证、可追溯的证据底座。后续所有 Methodology、Prompt、Skill、Score、Report 和 Benchmark 都必须通过 Evidence Card 或 Evidence Chain 引用证据，禁止用无来源的“市场认为”“综合判断”“行业普遍预期”支撑核心结论。

Evidence Engine 解决四个问题：

1. 证据是否真实存在，来源是否可追溯。
2. 证据是否足以支持或反驳某个研究命题。
3. 多条证据之间是否能组成完整推理链。
4. 证据缺口、反方证据和不确定性是否被显式披露。

## 2. 分层结构

```
Research Question
    ↓
Methodology Required Evidence / Counter Evidence
    ↓
Evidence Collection
    ↓
Evidence Card
    ↓
Evidence Review
    ↓
Evidence Chain
    ↓
Score / Evaluation / Report
```

### 2.1 Evidence Collection

Research Agent 根据方法论中的 Required Evidence 和 Counter Evidence 列表采集材料。采集结果必须转为 Evidence Card，不允许直接把原始材料塞进报告。

### 2.2 Evidence Card

Evidence Card 是最小证据单元，描述一个来源、一段事实、一个观点或一个可验证数据点。证据卡必须包含来源、时间、等级、支持命题、反驳命题、缺口、权重和追溯信息。

### 2.3 Evidence Review

Review Agent 按来源可靠性、时间匹配度、可验证性、独立性、相关性和反方覆盖度审查证据卡。未通过审查的证据不得支撑高置信度结论。

### 2.4 Evidence Chain

Evidence Chain 把多张证据卡组织为推理路径，说明“证据 → 中间判断 → 结论”的关系，并标注支持、反驳、冲突、背景、因果、相关或时间先后关系。

## 3. 核心对象

| 对象 | 作用 | 下游使用 |
|------|------|----------|
| Evidence Card | 记录单条证据 | Score、Evaluation、Report、Benchmark |
| Evidence Chain | 组织证据关系 | Report、Review、Verification |
| Evidence Level | 给出证据等级 | Confidence、Score |
| Evidence Review | 审查质量和缺口 | Evaluation、Benchmark |
| Traceability | 保留来源和处理记录 | 审计、复现、更新 |

## 4. 与 M2 Methodology 的接口

M2 的每个方法论都包含 Required Evidence 与 Counter Evidence。M3 将这两个字段落地为 Evidence Card 的 `supports`、`refutes` 与 `missing_evidence`：

- Required Evidence → 必须收集的支持性或背景性证据。
- Counter Evidence → 必须收集的反证、替代解释或冲突证据。
- Confidence → 由证据等级、链条完整性、反证压力和缺口透明度共同决定。

如果某个方法论要求“至少一个官方或原始来源证据”，Evidence Engine 必须检查是否存在 A 级或 B 级 Evidence Card。

## 5. Agent 职责

### Research Agent

- 从研究问题和方法论中拆解证据需求。
- 采集原始材料并生成 Evidence Card。
- 明确证据支持什么、反驳什么、缺少什么。

### Review Agent

- 审查证据卡完整性。
- 检查证据等级是否被高估。
- 检查证据链是否存在断点、循环论证或单源伪多源。

### Verification Agent

- 运行 Schema 与脚本验证。
- 检查报告是否引用了 Evidence Card。
- 检查 Benchmark 案例是否包含标准证据链。

### Code Agent

- 维护 Evidence Schema、模板、校验脚本和文档。
- 保证 M3 交付物与 M1/M2 保持一致。

## 6. 质量原则

1. **来源优先**：结论必须回到来源，不得只回到二次摘要。
2. **时间匹配**：证据时间必须与研究问题时间范围一致。
3. **反证并行**：支持性证据和反证必须同时进入审查。
4. **缺口透明**：无法取得的关键证据必须写入 Missing Evidence。
5. **等级约束**：低等级证据不得单独支撑高置信度结论。
6. **可复现**：另一个 Agent 应能根据证据卡找到来源并复核。

## 7. 禁止事项

- 禁止用未经标注的传闻、二手摘要或主观判断替代证据卡。
- 禁止把同一原始来源被多家媒体转载误判为多源验证。
- 禁止只采集支持观点的证据而忽略明显反证。
- 禁止把 Evidence Level 或 Weight 解释为投资评级。
- 禁止输出任何直接投资建议或价格预测。

