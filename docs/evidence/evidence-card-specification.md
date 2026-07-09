# Evidence Card Specification（证据卡规范）

**归属 Milestone**：M3 Evidence Engine  
**版本**：v0.3.0  
**最后更新**：2026-07-10

**免责声明**：证据卡只用于组织投资研究材料，不构成投资建议，不提供交易指令或收益承诺。

---

## 1. 定义

Evidence Card 是 AIRS 的最小证据单元。每张卡记录一个可追溯来源中的事实、数据、观点或披露，并明确它支持哪些命题、反驳哪些命题、还有哪些关键缺口。

证据卡不是报告段落，也不是结论本身。证据卡只回答：

- 来源是什么？
- 内容是什么？
- 可信到什么程度？
- 能支持或反驳什么？
- 下游使用时有哪些限制？

## 2. 必需字段

| 字段 | Schema 字段 | 必需 | 说明 |
|------|-------------|------|------|
| Evidence ID | `evidence_id` | 是 | 全局唯一 ID，建议格式 `EV-YYYYMMDD-XXXX` |
| Title | `title` | 是 | 简短标题 |
| Category | `category` | 是 | 财务、供应链、政策、行业、管理层、风险等 |
| Source | `source` | 是 | 来源名称 |
| Source Type | `source_type` | 是 | 官方公告、财报、监管文件、研报、新闻、专家观点等 |
| URL | `url` | 否 | 可访问链接或内部文档路径 |
| Publication Time | `publication_time` | 是 | 来源发布时间 |
| Collection Time | `collection_time` | 是 | Agent 采集时间 |
| Confidence | `confidence` | 是 | 证据可信度，0-1 或 LOW/MEDIUM/HIGH |
| Evidence Level | `evidence_level` | 是 | A/B/C/D/E |
| Supports | `supports` | 是 | 支持的命题、结论或中间判断 |
| Refutes | `refutes` | 是 | 反驳或削弱的命题 |
| Missing Evidence | `missing_evidence` | 是 | 仍缺少的关键证据 |
| Weight | `weight` | 是 | 在证据链中的研究权重，0-1 |
| Traceability | `traceability` | 是 | 采集、处理、验证、引用记录 |
| Version | `version` | 是 | 证据卡版本 |

## 3. 推荐扩展字段

- `summary`：证据摘要。
- `raw_excerpt`：短摘录或数据片段，避免粘贴超长原文。
- `entities`：涉及公司、产业、政策、产品或人物。
- `time_scope`：证据对应的数据期间。
- `review_status`：未审查、已通过、需复核、已弃用。
- `review_notes`：Review Agent 的审查意见。
- `related_evidence_ids`：关联证据 ID。

## 4. 字段填写规则

### 4.1 Supports

`supports` 必须写成可验证命题，而不是宽泛主题。例如：

- ✅ “2025 年 HBM 供给紧张可能制约 AI 加速卡交付。”
- ❌ “支持 AI 主题。”

### 4.2 Refutes

`refutes` 用于记录削弱主命题的证据。即使证据主要支持研究结论，也应说明它是否反驳某个替代解释。

### 4.3 Missing Evidence

`missing_evidence` 不允许留空。若没有已知缺口，填写“未发现关键缺口，并说明检查范围”。这能防止 Agent 假装证据完整。

### 4.4 Weight

`weight` 代表证据在当前证据链中的研究权重，不代表投资价值。权重必须考虑：

- 证据等级。
- 与命题的相关性。
- 来源独立性。
- 时效性。
- 是否可被反证削弱。

## 5. 最低可用标准

一张可进入 Evidence Chain 的证据卡必须满足：

1. 必需字段完整。
2. 来源可追溯。
3. 时间字段明确。
4. 至少绑定一个 supports 或 refutes 命题。
5. 明确 evidence_level 与 confidence。
6. 写明 missing_evidence。

## 6. 使用限制

- C 级和 D 级证据可以用于背景、线索和反方假设，但不得单独支撑核心结论。
- 观点类证据必须标注为观点，不得伪装成事实。
- 数据口径不清的证据必须降低 confidence。
- 超出时间范围的旧证据必须说明为何仍然适用。

