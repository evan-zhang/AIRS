# Benchmark Architecture（Benchmark 架构总览）

**归属 Milestone**：M7: Benchmark & Production Examples  
**版本**：v0.7.0  
**最后更新**：2026-07-10

**免责声明**：本文档仅定义 AIRS 投资研究 Benchmark 的质量评估架构，不构成投资建议，不提供交易指令、价格预测或收益承诺。

## 1. 目标

Benchmark Layer 是 AIRS 第 8 层，用于把 M2 Methodology、M3 Evidence、M4 Prompt、M5 Skill、M6 Score / Evaluation 连接成可回归、可审计、可复用的测试体系。它不替代上游规则，只把上游规则转化为测试输入、标准答案、评分标准和失败样例。

核心目标：

- 检查 Research Agent 是否按 M2 方法论执行，而不是跳步下结论。
- 检查输出是否使用 M3 Evidence Card 和 Evidence Chain。
- 检查 Prompt 输出是否遵守 M4 Prompt 格式、Failure Cases 和免责声明。
- 检查报告是否使用 M6 Scorecard、Quality Gate 和 Evaluation 结果。
- 为后续 M8 生产交付提供回归数据集。

## 2. 分层结构

```
Benchmark Case
  -> Research Intent
  -> Methodology Mapping
  -> Evidence Requirements
  -> Gold Standard
  -> Evaluation Criteria
  -> Expected Output
  -> Failure Cases
  -> Regression Result
```

| 层级 | 责任 | 对接对象 |
|------|------|----------|
| Case Metadata | 定义行业、方法论、难度、版本 | `schemas/benchmark/benchmark.schema.json` |
| Input Layer | 记录研究问题、范围、约束 | M4 Prompt input_schema |
| Evidence Layer | 定义必需证据卡和反证 | M3 Evidence Card |
| Gold Standard | 描述可接受答案边界 | M2 Methodology + M3 Evidence Chain |
| Evaluation Criteria | 定义评分维度和门禁 | M6 Score Engine |
| Expected Output | 约束报告结构与字段 | M4 Prompt Output + M1 Report Template |
| Failure Cases | 记录不可接受行为 | M6 Quality Gate |

## 3. 目录映射

M7 建立六类行业基准：

- `benchmark/ai/`：AI 算力、模型、服务器、应用生态。
- `benchmark/semiconductor/`：芯片设计、制造、设备、材料、封测。
- `benchmark/innovative-drug/`：创新药、临床、商业化、医保和监管。
- `benchmark/robotics/`：工业机器人、人形机器人、核心零部件和自动化。
- `benchmark/new-energy/`：电池、储能、光伏、风电、充电和电网。
- `benchmark/general/`：跨行业通用研究质量、报告格式和合规边界。

每个行业目录在 M7 先提供 5 个标准文件：`template.md`、`gold-standard.md`、`evaluation-criteria.md`、`expected-output.md`、`failure-cases.md`。这些文件是分类基准的种子，不是最终 300+ 用例全集。

## 4. 标准测试流

1. Verification Agent 读取 Benchmark Case。
2. Research Agent 按研究意图执行 M2 方法论。
3. Research Agent 输出 Evidence Card、Evidence Chain、Scorecard 和报告。
4. Verification Agent 用 Gold Standard 检查关键结论边界。
5. Verification Agent 用 Evaluation Criteria 计算 M6 Scorecard。
6. Quality Gate 输出 `PASS`、`CONDITIONAL_PASS` 或 `FAIL`。
7. Regression Dataset 记录本轮结果和差异说明。

## 5. 数据对象

Benchmark 对象必须保留以下引用：

- `methodology_refs`：至少引用一个 `docs/methodology/` 文档。
- `evidence_requirements`：使用 M3 Evidence Card 字段，例如 Evidence ID、Evidence Level、Confidence、Weight、supports、refutes、missing_evidence。
- `prompt_refs`：引用 M4 Prompt ID 或 Prompt 文档路径。
- `scorecard_refs`：引用 M6 Scorecard 或 Score Schema。
- `disclaimer`：必须包含“不构成投资建议”。

## 6. 质量门禁

Benchmark 通过条件：

- 结构符合 `schemas/benchmark/benchmark.schema.json`。
- Gold Standard 不输出交易动作或收益承诺。
- Evaluation Criteria 使用 M6 Score Engine，不重新定义评分体系。
- Expected Output 包含证据链、评分、反方观点、不确定性和免责声明。
- Failure Cases 能覆盖证据缺失、反证缺失、评分缺失、合规缺失和格式缺失。

## 7. 禁止事项

- 禁止把 Benchmark 标准答案写成荐股结论。
- 禁止把 M6 Scorecard 解读为投资评级。
- 禁止复制并改写 M3 Evidence Level 或 M6 Quality Gate 的原始定义。
- 禁止在没有 Evidence Card 的情况下判定研究结论通过。
- 禁止删除失败样例；失败样例是回归测试资产。

