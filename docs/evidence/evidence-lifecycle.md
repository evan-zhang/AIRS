# Evidence Lifecycle（证据生命周期）

**归属 Milestone**：M3 Evidence Engine  
**版本**：v0.3.0  
**最后更新**：2026-07-10

**免责声明**：证据生命周期管理只服务于研究复核，不构成投资建议，不保证任何投资结果。

---

## 1. 生命周期状态

| 状态 | 说明 | 可否用于核心结论 |
|------|------|------------------|
| `DRAFT` | 初始采集，未审查 | 否 |
| `IN_REVIEW` | 正在审查 | 否 |
| `APPROVED` | 审查通过 | 是 |
| `APPROVED_WITH_LIMITATION` | 有限制通过 | 可用但必须披露限制 |
| `NEEDS_UPDATE` | 时间或口径需要更新 | 不建议 |
| `DEPRECATED` | 已过期或被替代 | 否 |
| `REJECTED` | 来源或内容不合格 | 否 |

## 2. 创建

Evidence Card 创建时必须记录：

- 采集 Agent。
- 采集时间。
- 原始来源。
- 初始 Evidence Level。
- 初始支持/反驳命题。

默认状态为 `DRAFT`。

## 3. 审查

Review Agent 将状态更新为 `APPROVED`、`APPROVED_WITH_LIMITATION`、`NEEDS_UPDATE` 或 `REJECTED`。任何等级、权重或置信度调整都必须写入 Traceability。

## 4. 使用

Report Layer 引用证据时必须保留 Evidence ID。若使用 `APPROVED_WITH_LIMITATION` 证据，报告中必须出现限制说明和不确定性标注。

## 5. 更新

以下情况触发更新：

- 来源发布修订版。
- 新财报、新公告或新政策覆盖旧信息。
- 反方证据显著增强。
- 原 URL 失效，需要替代路径。
- 方法论或评分规则升级。

更新时不得覆盖旧版本，应提升 `version` 并保留变更记录。

## 6. 废弃

证据废弃原因包括：

- 来源不可复核。
- 被后续官方材料推翻。
- 时间窗口不再适用。
- 与研究命题无关。
- 审查发现重大错误。

废弃证据不得删除，应保留 Evidence ID、废弃原因和替代证据 ID，以便审计。

## 7. 版本规则

采用语义化版本：

- 补充字段或修正错别字：patch，例如 `0.3.1`。
- 调整 Evidence Level、Confidence、Weight：minor，例如 `0.4.0`。
- 来源或命题发生重大变化：major，例如 `1.0.0`。

## 8. 保存与引用

M3 只定义规范，不要求建立真实证据库。后续实现时，Evidence Card 可存储为 JSON、Markdown 或数据库记录，但对外接口必须保持 Schema 兼容。

