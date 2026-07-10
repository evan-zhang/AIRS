# FEATURE-NEWS-001 Feature Spec - News Connector

## 1. Feature 摘要

News Connector 将新闻事件输入标准化为 AIRS Evidence 与 Event 对象，使 Research Agent 可以在事件影响分析中使用可追溯、可审查的新闻证据。

## 2. Scope

### In Scope

- 新闻元数据：source、url、published_at、collected_at、language。
- 事件归一化：event_type、event_time、entities、affected_scope。
- 证据映射：facts、interpretations、claims、evidence_refs。
- 风险标注：source_risk、timeliness_risk、interpretation_risk。
- 反方信息：counter_sources、missing_evidence、uncertainties。

### Out of Scope

- 真实新闻 API 集成。
- 实时行情联动。
- 自动交易、投资建议或价格预测。
- 替代 M3 Evidence Validation。

## 3. Functional Requirements

- FR-1：每条新闻必须生成或绑定 Evidence Card。
- FR-2：必须区分事实陈述、媒体解读和研究推断。
- FR-3：必须记录新闻发布时间与采集时间。
- FR-4：必须输出反方来源或缺失证据。
- FR-5：Prompt 必须遵循 M4 Prompt Engine。
- FR-6：Skill 必须遵循 M5 Skill Engine。
- FR-7：Benchmark 必须验证事件归一化和合规边界。

## 4. Acceptance Criteria

- 10 个 Builder artifact 全部存在。
- Schema 为合法 JSON Schema。
- 测试计划覆盖正常新闻、低可信来源、冲突来源和合规失败。
- Benchmark 包含评估维度和失败场景。

## 5. 免责声明

本规格仅用于 AIRS 工程开发与投资研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

