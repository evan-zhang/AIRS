# AIRS Evidence Card Template（证据卡模板）

**模板版本**：v0.3.0  
**适用 Schema**：`schemas/evidence/evidence-card.schema.json`  
**免责声明**：本模板用于投资研究证据管理，不构成投资建议，不提供买卖指令、目标价或收益承诺。

---

## 1. 必需字段

| 字段 | 填写内容 |
|------|----------|
| **Evidence ID** | `EV-YYYYMMDD-XXXX` |
| **Title** | [证据标题] |
| **Category** | [financial / supply_chain / industry / policy / management / valuation / risk / market / counter_evidence / background / other] |
| **Source** | [来源名称] |
| **Source Type** | [company_filing / regulatory_filing / government_policy / official_statistics / industry_report / broker_research / news / expert_opinion / database / internal_note / other] |
| **URL** | [公开 URL、内部文档路径，或不可公开访问原因] |
| **Publication Time** | [YYYY-MM-DDTHH:MM:SS+08:00] |
| **Collection Time** | [YYYY-MM-DDTHH:MM:SS+08:00] |
| **Confidence** | [0.00-1.00 或 LOW/MEDIUM/HIGH] |
| **Evidence Level** | [A/B/C/D/E] |
| **Supports** | [支持的具体命题，必须可验证] |
| **Refutes** | [反驳或削弱的具体命题；如无，说明检查范围] |
| **Missing Evidence** | [仍缺少的关键证据；如无，说明为什么] |
| **Weight** | [0.00-1.00，仅代表研究证据权重，不代表投资评级] |
| **Traceability** | [采集者、采集方法、来源定位、处理步骤、审查者、下游引用] |
| **Version** | [语义化版本，例如 0.3.0] |

---

## 2. 证据摘要

[用 1-2 段说明证据内容。摘要必须区分事实、观点和推断。]

## 3. 原始内容摘录

[粘贴短摘录、关键数据或表格摘要。避免复制长篇原文；必要时只记录定位信息。]

## 4. 支持命题

| Claim ID | 命题 | 支持强度 | 说明 |
|----------|------|----------|------|
| C-001 | [命题] | strong / medium / weak | [证据如何支持] |

## 5. 反驳命题

| Claim ID | 命题 | 反驳强度 | 说明 |
|----------|------|----------|------|
| C-002 | [命题] | strong / medium / weak | [证据如何削弱] |

## 6. 缺失证据

- [缺失证据 1：说明为什么重要，以及后续如何验证]
- [缺失证据 2：如没有，写明“未发现关键缺口，已检查范围包括...”]

## 7. 证据等级判断

| 维度 | 判断 | 说明 |
|------|------|------|
| 来源可靠性 | [高/中/低] | [说明] |
| 时间匹配度 | [高/中/低] | [说明] |
| 可验证性 | [高/中/低] | [说明] |
| 独立性 | [高/中/低] | [说明] |
| 相关性 | [高/中/低] | [说明] |

## 8. 追溯记录

- **Collected By**：[Research Agent / 人员]
- **Reviewed By**：[Review Agent / 人员，如未审查写 N/A]
- **Collection Method**：[搜索、数据库查询、公告读取、人工录入等]
- **Source Locator**：[URL、页码、章节、表格编号、内部路径]
- **Transformations**：[摘要、翻译、单位换算、口径统一等]
- **Downstream References**：[报告章节、证据链 ID、评分维度]

## 9. 审查状态

- **Review Status**：[DRAFT / IN_REVIEW / APPROVED / APPROVED_WITH_LIMITATION / NEEDS_UPDATE / DEPRECATED / REJECTED]
- **Review Notes**：[审查意见、限制条件和需修正项]

## 10. 版本记录

| Version | Date | Change | Reason |
|---------|------|--------|--------|
| 0.3.0 | YYYY-MM-DD | 初始创建 | M3 Evidence Engine |

