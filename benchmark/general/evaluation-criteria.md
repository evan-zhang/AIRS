# General Evaluation Criteria

**Benchmark ID**：BENCH-GENERAL-EVALUATION-CRITERIA  
**版本**：v0.7.0

**免责声明**：本评估标准仅用于 AIRS 通用 Benchmark 的质量门禁，不构成投资建议，不提供交易指令、价格预测或收益承诺。

## 1. M6 评分映射

| Score 维度 | 权重 | 通用通过要求 |
|------------|------|--------------|
| Evidence Score | 0.25 | M3 Evidence Card 字段完整 |
| Methodology Score | 0.10 | 方法论引用明确，不跳过 Workflow |
| Prompt Score | 0.15 | M4 Prompt 输入输出约束完整 |
| Report Score | 0.25 | 报告结构完整，包含反方观点、不确定性和免责声明 |
| Risk Score | 0.10 | 风险点与证据或缺口绑定 |
| Confidence Score | 0.15 | 置信度与 Evidence Level 和 Missing Evidence 一致 |

## 2. Quality Gate

PASS 要求 Overall Score >= 80，且没有强制失败项。CONDITIONAL_PASS 适用于轻微证据缺口且已明确披露。FAIL 适用于缺少 Evidence ID、Evidence Level、Scorecard、Quality Gate、反方观点或免责声明。

## 3. 通用检查项

评估必须检查：是否引用 M2 Methodology，是否使用 M3 Evidence Card，是否保留 M4 Prompt ID，是否输出 M6 Scorecard，是否有反方观点和不确定性。

## 4. 合规检查

任何交易动作、收益承诺、确定性预测或个性化结论均触发 FAIL。Scorecard 不得被解释为投资评级。

## 5. M7 一致性声明

本评估标准直接检查 M3 Evidence 字段，包括 Evidence ID、Evidence Level、Confidence、Weight、supports、refutes 和 missing_evidence，并将结果映射到 M6 Scorecard 和 Quality Gate。
