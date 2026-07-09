# Regression Dataset（回归数据集说明）

**归属 Milestone**：M7: Benchmark & Production Examples  
**版本**：v0.7.0  
**最后更新**：2026-07-10

**免责声明**：本文档仅说明 AIRS 示例与 Benchmark 的回归数据集组织方式，不构成投资建议，不提供交易指令、价格预测或收益承诺。

## 1. 数据集目标

Regression Dataset 用于在 AIRS 迭代时固定一组可复现样例，检查系统是否保持 M1-M6 的质量边界。它不是投资组合，不表达行业偏好，也不用于真实交易。

## 2. 数据集组成

M7 数据集由两部分组成：

- Benchmark 分类文件：六个行业目录，每类 5 个基准文件。
- Production Examples：六个生产示例，覆盖供应链、主题扩散、证据报告、估值、风险和完整研究报告。

## 3. 回归字段

每条回归记录应包含：

| 字段 | 说明 |
|------|------|
| dataset_id | 回归数据集 ID |
| artifact_path | 文件路径 |
| artifact_type | benchmark / example |
| methodology_refs | M2 方法论引用 |
| prompt_refs | M4 Prompt 引用 |
| evidence_ids | M3 Evidence Card ID |
| scorecard_id | M6 Scorecard ID |
| quality_gate | PASS / CONDITIONAL_PASS / FAIL |
| known_gaps | 已知缺口 |
| disclaimer | 免责声明 |

## 4. 最小 M7 回归集

| 类型 | 数量 | 路径 |
|------|------|------|
| Benchmark docs | 4 | `docs/benchmark/` |
| Example docs | 2 | `docs/examples/` |
| Benchmark seed files | 30 | `benchmark/{category}/` |
| Production examples | 6 | `examples/` |
| Benchmark schemas | 3 | `schemas/benchmark/` |
| Templates | 2 | `templates/` |

## 5. 回归执行

M7 必须运行 9 个脚本：

```bash
python3 scripts/validate_m1.py
python3 scripts/validate_m2.py
python3 scripts/validate_evidence.py
python3 scripts/validate_prompt.py
python3 scripts/validate_skill.py
python3 scripts/validate_score.py
python3 scripts/validate_evaluation.py
python3 scripts/validate_benchmark.py
python3 scripts/validate_examples.py
```

全部返回 `RESULT: PASS` 后，M7 才能标记为通过。

## 6. 差异管理

当回归失败时，必须先定位：

- 文件缺失。
- 结构字段缺失。
- Evidence Card 缺失。
- Scorecard 缺失。
- Quality Gate 缺失。
- 免责声明缺失。
- 出现合规禁止表达。

修复后重新运行全部 9 个脚本，并在 M7 Completion Report 中记录结果。

## 7. M8 扩展建议

M8 可将 M7 文档型回归集扩展为机器可执行数据集：

- 为每个 Benchmark 增加 `metadata.json`。
- 为每个示例增加结构化 `example.json`。
- 增加自动 Scorecard runner。
- 增加报告差异比较工具。
- 增加历史回归结果仓库。

