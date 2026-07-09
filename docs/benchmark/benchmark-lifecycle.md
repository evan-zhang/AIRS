# Benchmark Lifecycle（Benchmark 生命周期）

**归属 Milestone**：M7: Benchmark & Production Examples  
**版本**：v0.7.0  
**最后更新**：2026-07-10

**免责声明**：本文档仅用于 AIRS Benchmark 生命周期管理，不构成投资建议，不提供交易指令、价格预测或收益承诺。

## 1. 生命周期状态

| 状态 | 含义 | 进入条件 | 退出条件 |
|------|------|----------|----------|
| DRAFT | 初稿 | 新增用例或分类文件 | 完成字段、证据和免责声明 |
| IN_REVIEW | 审查中 | 结构完整，可被 Review Agent 检查 | 审查通过或退回 |
| APPROVED | 已批准 | 通过结构、证据、评分和合规检查 | 进入回归数据集 |
| REGRESSION_ACTIVE | 回归中 | 已纳入固定回归集 | 版本升级或废弃 |
| NEEDS_UPDATE | 需更新 | 来源过期、方法论变化、评分体系变化 | 修复后重新审查 |
| DEPRECATED | 已废弃 | 行业场景不再有效或被新用例替代 | 保留审计记录 |

## 2. 创建流程

Benchmark 创建必须从研究目的开始，而不是从结论开始：

1. 定义研究问题和范围。
2. 选择 M2 方法论，例如供应链卡脖子、主题扩散、估值、风险或反共识。
3. 列出必需 Evidence Card 类型、Evidence Level 下限和缺失证据处理。
4. 写入 Gold Standard，说明可接受答案边界。
5. 写入 Evaluation Criteria，引用 M6 Score Engine。
6. 写入 Expected Output，约束报告结构。
7. 写入 Failure Cases，覆盖常见失败。
8. 运行 `scripts/validate_benchmark.py`。

## 3. 审查流程

Review Agent 审查以下内容：

- 是否有明确 Benchmark ID、行业、方法论和版本。
- 是否引用 M3 Evidence Card，而不是散文式证据描述。
- 是否引用 M6 Scorecard 和 Quality Gate。
- 是否包含反方观点、不确定性、风险提示和免责声明。
- 是否避免交易动作、价格预测和收益承诺。

审查输出：

```markdown
## Benchmark Review
- Review Status: PASS / PASS_WITH_LIMITATION / FAIL
- Evidence Mapping:
- Score Mapping:
- Compliance Finding:
- Required Fix:
```

## 4. 回归流程

每次 AIRS 核心规范变化后，Verification Agent 必须运行：

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

任一脚本失败时，M7 交付不能进入 PASS。若失败来自 M1-M6 已 PASS 文件，必须先判断是否为 M7 兼容性问题；只有确有一致性必要时才修改旧文件，并记录 ADR、CHANGELOG 和 M7 Completion Report。

## 5. 版本规则

- patch：文字修正、示例补充、不改变验收含义。
- minor：新增行业场景、调整证据需求、增强失败样例。
- major：方法论映射、评分门禁或 Schema 结构变化。

版本记录必须保留变更原因、影响范围和回归结果。

## 6. 废弃规则

Benchmark 不应直接删除。废弃时应保留：

- 原 Benchmark ID。
- 废弃原因。
- 替代用例 ID。
- 最后一次回归结果。
- 是否影响历史评估可比性。

## 7. 生命周期合规底线

任何状态下，Benchmark 文档都必须声明“不构成投资建议”。若文档缺少免责声明、出现交易指令或把评分表达为投资结论，Quality Gate 必须输出 `FAIL`。

