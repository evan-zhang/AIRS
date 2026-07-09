# AIRS Scorecard 模板

**免责声明**：本评分卡仅用于投资研究质量控制和结构化分析，不构成投资建议、投资评级、交易指令、目标价或收益承诺。

## 1. 元数据

| 字段 | 内容 |
|------|------|
| Scorecard ID | SCORECARD-[YYYYMMDD-XXX] |
| Version | v0.6.0 |
| Artifact Type | prompt_output / skill_output / report / benchmark_case / research_run |
| Methodology Refs | docs/methodology/[name].md |
| Evidence Chain Refs | ECHAIN-[ID] |
| Created By | [Agent] |
| Reviewed By | [Agent] |

## 2. 综合评分

| 项目 | 结果 |
|------|------|
| Overall Score | [0-100] |
| Overall Grade | A / B / C / D / E |
| Confidence Score | [0-100] |
| Quality Gate | PASS / CONDITIONAL_PASS / FAIL |

## 3. 维度评分

| 维度 | 原始分 | 权重 | 加权分 | 证据引用 | 说明 |
|------|--------|------|--------|----------|------|
| Evidence Score | [分数] | 0.25 | [分数] | [Evidence IDs] | [解释] |
| Methodology Score | [分数] | 0.15 | [分数] | [Refs] | [解释] |
| Prompt Score | [分数] | 0.10 | [分数] | [Refs] | [解释] |
| Skill Score | [分数] | 0.10 | [分数] | [Refs] | [解释] |
| Report Score | [分数] | 0.15 | [分数] | [Refs] | [解释] |
| Risk Score | [分数] | 0.10 | [分数] | [Refs] | [解释] |
| Confidence Score | [分数] | 0.10 | [分数] | [Refs] | [解释] |
| Theme Score | [分数] | 0.05 | [分数] | [Refs] | [解释] |

## 4. 权重审计

| 维度 | 调整前 | 调整后 | 调整原因 |
|------|--------|--------|----------|
| [维度] | [值] | [值] | [原因] |

## 5. 扣分项

| 扣分项 | 扣分 | 原因 | 修复建议 |
|--------|------|------|----------|
| missing_evidence | [0-20] | [原因] | [建议] |
| counter_evidence | [0-15] | [原因] | [建议] |
| compliance | PASS / FAIL | [原因] | [建议] |

## 6. 置信度与不确定性

- Evidence Confidence：[0-1 或说明]
- Missing Evidence Impact：[说明]
- Counter Evidence Pressure：[说明]
- Confidence Downgrade Reasons：[说明]

## 7. Quality Gate

- Gate Result：PASS / CONDITIONAL_PASS / FAIL
- Force Fail Triggered：Yes / No
- Required Fixes：[修复项]
- Publication Readiness：Yes / No

