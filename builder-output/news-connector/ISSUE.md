# FEATURE-NEWS-001 - News Connector

## 背景

News Connector 用于把新闻事件接入 AIRS 研究流程，将新闻文本、事件实体、时间线、影响对象、证据卡和反方观点组织为结构化输入。它不替代 M3 Evidence Engine，也不判断新闻是否意味着买入或卖出，只为事件影响分析提供可验证输入。

## 业务目标

- 将新闻事件转换为可追溯 Evidence Card。
- 支持新闻事件影响分析、政策驱动分析和主题扩散分析。
- 为 Research Agent 提供事件上下文，为 Review Agent 提供来源、时间、置信度和反方观点检查入口。

## 用户场景

- Research Agent 需要分析某条新闻对行业链条的潜在影响。
- Review Agent 需要判断新闻来源是否可靠、是否存在二次报道偏差。
- Verification Agent 需要通过 Benchmark 检查新闻事件是否被正确归一化。
- Code Agent 需要实现一个可插拔的新闻接入模块。

## 依赖

- M2 Methodology：`docs/methodology/policy-driven.md`、`docs/methodology/theme-expansion.md`、`docs/methodology/evidence-chain.md`
- M3 Evidence：`docs/evidence/evidence-card-specification.md`、`docs/evidence/evidence-validation-workflow.md`
- M4 Prompt：`templates/prompt-template.md`
- M5 Skill：`templates/skill-template.md`
- M6 Evaluation：`docs/evaluation-engine/evaluation-workflow.md`
- M7 Benchmark：`templates/benchmark-template.md`

## 期望输出

- News Connector Skill 草案。
- News Event Prompt 草案。
- 新闻事件 Schema。
- 测试计划和 Benchmark。
- PR Checklist 与 Release Notes。

## 验收标准

- 新闻事件必须包含 source、published_at、event_type、entities、claims、evidence_refs。
- 必须区分事实、媒体解读和推断。
- 必须包含反方信息、缺失证据和不确定性。
- 不输出交易建议、目标价或收益承诺。

## 免责声明

本示例仅用于 AIRS 工程开发与投资研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

