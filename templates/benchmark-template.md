# AIRS Benchmark 模板

**Benchmark ID**：BENCH-[CATEGORY]-[000]  
**行业分类**：[ai / semiconductor / innovative-drug / robotics / new-energy / general]  
**方法论引用**：[docs/methodology/*.md]  
**Prompt 引用**：[prompts/**/*.md]  
**版本**：v0.7.0

**免责声明**：本 Benchmark 仅用于 AIRS 投资研究质量测试，不构成投资建议，不提供交易指令、价格预测或收益承诺。

## 1. 研究意图

- 研究问题：
- 研究范围：
- 时间范围：
- 地理范围：
- 数据源约束：

## 2. M4 Prompt 输入

```json
{
  "prompt_id": "PROMPT-ID",
  "research_question": "",
  "methodology_refs": [],
  "evidence_refs": [],
  "output_requirements": ["Evidence Card", "Evidence Chain", "Scorecard", "免责声明"]
}
```

## 3. M3 Evidence 要求

| Evidence ID | Evidence Level | Confidence | Weight | Supports | Refutes | Missing Evidence |
|-------------|----------------|------------|--------|----------|---------|------------------|
| EV-YYYYMMDD-0001 | A/B/C | HIGH/MEDIUM/LOW | 0.00 | 命题 | 反命题 | 缺失证据 |

## 4. Gold Standard

标准答案应说明：

- 可接受的核心观点边界。
- 必需证据链。
- 必需反方观点。
- 必需不确定性。
- 不得输出交易动作或收益承诺。

## 5. M6 Evaluation Criteria

| Score 维度 | 权重 | 通过要求 |
|------------|------|----------|
| Evidence Score | 0.25 | Evidence Card 完整且证据等级合理 |
| Methodology Score | 0.15 | 遵循 M2 Workflow |
| Prompt Score | 0.10 | 遵循 M4 Prompt 格式 |
| Report Score | 0.20 | 报告结构完整 |
| Risk Score | 0.15 | 风险和反方观点充分 |
| Confidence Score | 0.15 | 置信度与证据一致 |

Quality Gate：PASS / CONDITIONAL_PASS / FAIL。

## 6. Expected Output

输出必须包含：

- 核心观点。
- Evidence Chain。
- M6 Scorecard。
- 反方观点。
- 不确定性标注。
- 风险提示。
- 免责声明。

## 7. Failure Cases

- 缺少 Evidence ID。
- 缺少 Evidence Level、Confidence 或 Weight。
- 缺少 Scorecard。
- 缺少反方观点。
- 缺少免责声明。
- 输出交易动作、价格预测或收益承诺。

