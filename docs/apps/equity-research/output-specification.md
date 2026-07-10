# APP-001 输出规范

免责声明：本文档仅定义 APP-001 输出结构与验证规则，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## 顶层对象

APP-001 返回一个字典对象，核心字段如下：

- `app_id`：固定为 `APP-001`。
- `request`：结构化研究请求。
- `company`：Resolver 识别出的公司信息。
- `planner`：Planner 生成的 Research Plan。
- `committee_initial`：研究范围初审。
- `runtime`：Runtime 执行结果。
- `data_collection`：Connector 计划、结果、证据卡和降级说明。
- `analysis`：综合分析、Evidence Chain、Knowledge Graph、Score Card。
- `committee_final`：二次审议。
- `report`：15 段研究报告。
- `memory`：研究沉淀上下文。
- `learning`：反馈与改进建议。

## 15 个必需 Section

1. Executive Summary
2. Company Profile
3. Industry Position
4. Supply Chain / Chokepoint
5. Financial Analysis
6. Valuation
7. Catalysts
8. Risks
9. Counter View
10. Evidence Chain
11. Knowledge Graph
12. Score Card
13. Committee Decision
14. Final Report
15. Appendix (Sources / Traceability)

每个 section 必须包含：

- `facts`
- `inference`
- `assumption`
- `opinion`

Markdown 输出必须对应四个三级标题：

- `### Facts`
- `### Inference`
- `### Assumption`
- `### Opinion`

## 证据与追溯

Evidence Card 必须至少包含：

- `evidence_id`
- `title`
- `source`
- `source_type`
- `url`
- `publication_time`
- `collection_time`
- `confidence`
- `evidence_level`
- `supports`
- `refutes`
- `missing_evidence`
- `traceability`
- `statement_type`
- `disclaimer`

如果真实数据不可用，必须在 `url`、`data.mode` 或 `degradation_notes` 中标注 `SKIP`、`mock` 或降级原因。

## 合规规则

- 不输出买入、卖出、持有、交易指令或收益承诺。
- 不把估值部分写成精确价格预测。
- 不把 Committee Decision 写成投资建议。
- 不把 Score Card 写成投资评级。
- 所有投资相关 Markdown 必须包含 `免责声明` 和 `不构成投资建议`。

