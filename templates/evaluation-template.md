# AIRS Evaluation 模板

**免责声明**：本评估仅用于研究质量验证，不构成投资建议、投资评级、交易指令、目标价或收益承诺。

## 1. 元数据

| 字段 | 内容 |
|------|------|
| Evaluation ID | EVAL-[YYYYMMDD-XXX] |
| Version | v0.6.0 |
| Evaluated Artifact | [artifact_id] |
| Artifact Type | scorecard / prompt_output / skill_output / report / benchmark_case |
| Scorecard ID | SCORECARD-[ID] |
| Reviewer | [Review Agent / Verification Agent] |

## 2. 总体结论

- Total Score：[0-100]
- Gate Result：PASS / CONDITIONAL_PASS / FAIL
- Force Fail Triggered：Yes / No
- Can Publish：Yes / No

## 3. 检查结果

| Check | Status | Score | Finding | Fix Required |
|-------|--------|-------|---------|--------------|
| Schema Check | PASS / WARN / FAIL | [0-100] | [发现] | [修复] |
| Evidence Check | PASS / WARN / FAIL | [0-100] | [发现] | [修复] |
| Score Check | PASS / WARN / FAIL | [0-100] | [发现] | [修复] |
| Counter-view Check | PASS / WARN / FAIL | [0-100] | [发现] | [修复] |
| Compliance Check | PASS / WARN / FAIL | [0-100] | [发现] | [修复] |
| Regression Check | PASS / WARN / FAIL | [0-100] | [发现] | [修复] |

## 4. 强制失败项

- [ ] 缺少免责声明
- [ ] 出现买入、卖出、持有、目标价或收益承诺
- [ ] 核心结论无 Evidence Card 支撑
- [ ] Evidence Score 缺失
- [ ] 反方观点缺失
- [ ] 权重无法解释

## 5. 修复要求

1. [修复项]
2. [修复项]
3. [修复项]

## 6. Reviewer Notes

[评审说明]

