# Methodology Review Checklist（方法论审查清单）

**归属 Milestone**：M2 Methodology Core  
**适用对象**：`docs/methodology/` 下的方法论文档、Methodology DSL 和 Methodology Schema。  
**免责声明**：本清单用于研究质量审查，不构成投资建议、交易建议或法律意见。

## 1. 审查目标

该清单用于 Review Agent 和 Verification Agent 检查方法论文档是否完整、可执行、可验证、可扩展，并符合 AIRS “证据驱动、反方思考、不确定性标注、可解释、可测试”的原则。

## 2. 必检项

- 是否包含 16 个标准 section。
- 每个 section 是否有实质内容，且不是占位符。
- 是否包含明确免责声明。
- 是否定义输入、输出、工作流、必需证据和反证。
- 是否禁止荐股、自动交易、价格预测和无证据结论。
- 是否能映射到后续 Prompt、Skill、Score 和 Benchmark。

## 3. 评分维度

总分 100 分，建议 80 分及以上为 PASS。

| 维度 | 分值 | 评分标准 |
|------|------|----------|
| 结构完整性 | 15 | 16 个 section 齐全、命名清晰、顺序稳定 |
| 方法论实质 | 15 | Purpose、Theory、Background 有具体解释，不是泛泛描述 |
| 可执行性 | 15 | Inputs、Outputs、Workflow 可被 Research Agent 执行 |
| 证据要求 | 15 | Required Evidence 明确证据类型、等级和交叉验证 |
| 反方与失败场景 | 15 | Counter Evidence 和 Failure Cases 能识别误用与结论失效 |
| 置信度与不确定性 | 10 | Confidence 说明评估因素和降级条件 |
| 后续映射 | 10 | Benchmark、Prompt、Skill、Score 映射具体可复用 |
| 合规边界 | 5 | 明确不构成投资建议，禁止交易指令和价格预测 |

## 4. PASS/FAIL 标准

### PASS

- 16 个 section 全部存在。
- 总分不低于 80 分。
- 必检项无合规失败。
- 自检脚本 `python3 scripts/validate_m2.py` 输出 PASS。

### CONDITIONAL PASS

- 总分 70-79 分。
- 不存在合规失败，但部分 section 需要补充证据、反证或后续映射。
- 必须在 Self Review 中列出修复计划。

### FAIL

- 缺少任一标准 section。
- 任一必需 section 为空壳或只有标题。
- 缺少免责声明。
- 出现荐股、自动交易、确定性价格预测或收益承诺。
- 自检脚本输出 FAIL 且未修复。

## 5. Review Agent 输出格式

```markdown
# Methodology Review Result

**结论**：PASS / CONDITIONAL PASS / FAIL  
**总分**：XX/100  

## 主要发现
[列出问题和证据]

## 必须修复
[列出阻断项]

## 建议优化
[列出非阻断改进]

## 合规检查
[说明是否存在荐股、交易或价格预测内容]
```

