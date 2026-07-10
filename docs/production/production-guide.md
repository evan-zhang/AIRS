# AIRS Production Guide（生产指南）

**版本**：v1.0.0  
**适用范围**：AIRS V1.0 Production Release  
**面向角色**：运维人员、Verification Agent、Code Agent、治理负责人

## 1. 生产定位

AIRS V1.0 是面向 AI Agent 的投资研究方法论框架。生产交付形态以 Markdown 规范、JSON Schema、Prompt、Skill、Benchmark、Example、自检脚本和治理文档为主，不包含自动交易、不包含实时行情服务、不包含个性化投资建议。

生产运行的核心目标是：

- 保证研究流程可追溯：Methodology、Prompt、Skill、Evidence、Score、Evaluation、Benchmark 均能互相引用。
- 保证研究输出可审查：所有研究结论必须带证据链、反方观点、不确定性和免责声明。
- 保证发布可验证：所有里程碑验证脚本和 `scripts/production_check.py` 必须 PASS。
- 保证变更可治理：生产变更必须经过 Issue、PR、自检、Review、Release Checklist。

## 2. 生产目录

生产负责人需要重点维护以下目录：

- `docs/production/`：生产指南、部署、维护、验收、最终审查和里程碑报告。
- `docs/governance/`：版本规范、发布流程、ADR/RFC 等治理材料。
- `.github/`：Issue 模板、PR 模板、CODEOWNERS、安全策略和支持指南。
- `scripts/`：所有 M1-M8 自检脚本与生产聚合检查脚本。
- `benchmark/` 与 `examples/`：回归验证用例和生产示例。

## 3. 生产运行原则

1. 任何发布前必须运行完整生产检查。
2. 任何投资研究相关新增内容必须包含“不构成投资建议”免责声明。
3. 不得把 Score、Quality Gate、Benchmark 结果解释为买入、卖出、持有、目标价或收益承诺。
4. 不得跳过 Evidence Chain、Counter Evidence、Missing Evidence 和 Uncertainty 标注。
5. 顶层核心文件的生产变更必须记录在 CHANGELOG，并在 ADR 中说明原因。

## 4. 标准生产操作

生产发布前执行：

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
python3 scripts/validate_release.py
python3 scripts/production_check.py
```

全部脚本输出 `RESULT: PASS` 或最终 `FINAL RESULT: PASS` 后，才允许进入发布标记。

## 5. 生产异常处理

当自检失败时：

1. 保留失败输出，不要覆盖或删除失败证据。
2. 定位失败文件和失败检查项。
3. 只修复与失败相关的最小范围文件。
4. 重新运行失败脚本。
5. 重新运行 `scripts/production_check.py`。
6. 在相关 Completion Report 或 Release Notes 中记录修复。

## 6. 生产交付边界

V1.0 可以用于：

- 构建和评审 AI 投资研究 Agent。
- 训练 Agent 遵守证据、反方和不确定性要求。
- 建立投研 Prompt、Skill、Benchmark 和质量门禁。
- 作为后续运行时系统的规范基础。

V1.0 不可以用于：

- 自动下单或自动交易。
- 直接生成个性化买卖建议。
- 输出无证据支撑的投资结论。
- 以 Benchmark 或 Score 结果替代投资判断。

## 7. 免责声明

AIRS V1.0 仅用于投资研究流程、质量控制和教育研究，不构成投资建议，不提供买入、卖出、持有、目标价或收益承诺。投资有风险，使用者应独立判断并自行承担后果。
