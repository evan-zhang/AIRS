# AIRS Builder Governance

**归属 Feature**：FEATURE-001 AIRS Builder  
**版本**：v1.1.0-draft  
**最后更新**：2026-07-10  

## 1. 治理原则

AIRS Builder 是“工程交付物生成器”，不是新的投资研究方法论层。它必须服从 AIRS V1.0 的 M1-M8 体系，并通过引用方式复用已有资产。

**免责声明**：本文档仅用于 AIRS 工程治理和研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## 2. 权责边界

Builder 负责：

- 读取 Feature Request。
- 生成 Feature Package。
- 生成开发、审查、测试和发布材料。
- 执行结构完整性和合规检查。

Builder 不负责：

- 创建投资结论。
- 执行交易或自动化下单。
- 预测价格。
- 替代 Methodology / Evidence / Prompt / Skill / Score / Evaluation / Benchmark 的规范。
- 判断某项投资是否值得买入或卖出。

## 3. 模板治理

模板位于 `templates/builder/`。模板必须遵循：

- Issue、ADR、Feature Spec 可以定义工程交付结构。
- Skill 模板必须引用 `templates/skill-template.md` 与 `docs/skill-engine/`。
- Prompt 模板必须引用 `templates/prompt-template.md` 与 `docs/prompt-engine/`。
- Benchmark 模板必须引用 `templates/benchmark-template.md` 与 `docs/benchmark/`。
- Schema 模板可以给出 JSON Schema 骨架，但不能改变 AIRS 已有 Schema 的语义。

## 4. 变更治理

如果 Builder 生成的新 Feature 需要修改历史 M1-M8 内容，Code Agent 必须：

1. 在 Feature Package 的 `ADR.md` 中说明原因。
2. 在仓库 `CHANGELOG.md` 中记录变更。
3. 如影响架构或治理，新增正式 ADR。
4. 在 Completion Report 中说明修改范围、原因和验证结果。

未涉及历史内容的 Feature 不应重写已有文档。

## 5. 合规治理

所有 Builder 生成物必须包含以下合规边界：

- 仅用于投资研究流程、工程开发、质量控制或教育研究。
- 不构成投资建议。
- 不提供买入、卖出、持有建议。
- 不提供目标价、收益承诺或确定性判断。
- 必须保留风险、不确定性和反方观点要求。

禁止表达包括但不限于：直接给出买入或卖出动作、承诺投资结果、承诺盈利、给出确定性目标价格等表述。

## 6. 评审治理

Builder Package 的评审维度：

| 维度 | 检查问题 |
|------|----------|
| 完整性 | 是否包含 10 个标准生成物 |
| 引用性 | 是否引用而非复制 M2-M7 规则 |
| 可执行性 | Code Agent 是否可直接执行 |
| 可验证性 | 是否有 Tests 与 Benchmark |
| 合规性 | 是否包含免责声明且无禁止表达 |
| 可追溯性 | Issue、ADR、Spec、Release Notes 是否互相引用 |

## 7. 风险治理

Builder 的主要风险：

- 模板漂移：Builder 模板与 M4/M5/M7 模板不一致。
- 过度生成：生成空壳文档或无法执行的测试。
- 规则重复：把已有 AIRS 层规则复制成新标准。
- 合规遗漏：生成物缺少免责声明。
- 依赖失真：引用不存在的上游资产。

治理措施：

- 使用 `registry.py` 管理模板清单。
- 使用 `validate_builder.py` 做本地验证。
- 在示例包中展示真实、可审查的内容。
- 在 ADR 中记录 Builder 采用轻量模板生成的决策。
