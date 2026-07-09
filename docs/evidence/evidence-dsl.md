# Evidence DSL（证据描述语言）

**归属 Milestone**：M3 Evidence Engine  
**版本**：v0.3.0  
**最后更新**：2026-07-10

**免责声明**：Evidence DSL 用于结构化研究证据，不构成投资建议，不提供交易动作建议。

---

## 1. 目标

Evidence DSL 是给 Agent 使用的轻量结构化描述。它既能映射到 JSON Schema，也能被 Markdown 模板表达。DSL 的目标是让 Prompt、Skill 和 Benchmark 使用同一套证据字段，避免不同模块各自发明证据格式。

## 2. 顶层结构

```yaml
evidence:
  evidence_id: EV-20260710-0001
  title: 证据标题
  category: supply_chain
  source:
    name: 来源名称
    source_type: company_filing
    url: https://example.com
    publication_time: "2026-07-10T00:00:00+08:00"
  collection_time: "2026-07-10T10:00:00+08:00"
  confidence: 0.82
  evidence_level: A
  supports:
    - claim_id: C-001
      statement: 支持的命题
      strength: strong
  refutes:
    - claim_id: C-002
      statement: 被削弱的命题
      strength: medium
  missing_evidence:
    - 仍缺少的证据
  weight: 0.75
  traceability:
    collected_by: Research Agent
    reviewed_by: Review Agent
    transformations:
      - 摘要抽取
  version: 0.3.0
```

## 3. 枚举规范

### 3.1 Category

建议枚举：

- `financial`
- `supply_chain`
- `industry`
- `policy`
- `management`
- `valuation`
- `risk`
- `market`
- `counter_evidence`
- `background`

### 3.2 Source Type

建议枚举：

- `company_filing`：公司财报、公告、招股书。
- `regulatory_filing`：监管披露。
- `government_policy`：政策文件。
- `official_statistics`：官方统计数据。
- `industry_report`：行业协会或研究机构报告。
- `broker_research`：券商研究报告。
- `news`：新闻报道。
- `expert_opinion`：公开专家观点。
- `database`：结构化数据库。
- `internal_note`：内部研究记录。

### 3.3 Relation Strength

`supports` 与 `refutes` 的强度：

- `strong`：直接支持或直接反驳。
- `medium`：间接支持或削弱。
- `weak`：仅提供背景或线索。

## 4. 命题绑定

证据必须绑定命题。命题可以来自：

- Methodology 的 Required Evidence。
- Report 的核心观点。
- Score 的评分维度。
- Evaluation 的反方观点。
- Benchmark 的标准答案。

绑定时应使用 `claim_id`。如果尚未建立命题 ID，Research Agent 应生成临时 ID，并在 Evidence Chain 中统一。

## 5. 证据关系表达

Evidence Chain 使用以下关系：

- `supports`：支持。
- `refutes`：反驳。
- `contextualizes`：提供背景。
- `qualifies`：限定适用范围。
- `conflicts_with`：与另一证据冲突。
- `depends_on`：依赖另一证据。
- `updates`：更新旧证据。

## 6. Agent 输出要求

Research Agent 输出 Evidence DSL 时必须：

1. 不省略必需字段。
2. 不把结论写成来源。
3. 不用“网上资料显示”等模糊来源。
4. 对反方证据使用 `refutes`，而不是混在摘要里。
5. 对缺口使用 `missing_evidence`，并说明后续验证路径。

## 7. 与 JSON Schema 的关系

DSL 是人和 Prompt 友好的表达，`schemas/evidence/evidence-card.schema.json` 是机器校验标准。所有 DSL 对象最终都应能转成 JSON Schema 兼容对象。

