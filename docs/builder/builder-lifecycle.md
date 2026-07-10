# AIRS Builder Lifecycle

**归属 Feature**：FEATURE-001 AIRS Builder  
**版本**：v1.1.0-draft  
**最后更新**：2026-07-10  

## 1. 生命周期概览

Builder Lifecycle 描述一个 Feature 从提出到交付给 Code Agent 的完整流转。它服务于工程开发，不直接执行投资研究，不输出投资建议。

```text
Draft Request → Intake Review → Package Generation → Package Validation → Code Agent Handoff → Review → Release Note
```

**免责声明**：本文档仅用于 AIRS 工程流程与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## 2. Draft Request

Feature 请求以 YAML 形式提交，起点是 `templates/builder/feature-request-template.yaml`。请求必须说明：

- Feature 要解决的问题。
- 业务目标和用户场景。
- 依赖的 AIRS 层。
- 期望生成物。
- 约束和风险等级。

Draft Request 不要求一次性完美，但必须足够让 Builder 判断生成边界。

## 3. Intake Review

Intake Review 检查请求是否适合 Builder 处理：

- 是否属于 AIRS 工程能力建设。
- 是否需要新增或修改 Methodology、Evidence、Prompt、Skill、Score、Evaluation、Benchmark。
- 是否触及自动交易、荐股、收益承诺或价格预测等禁止范围。
- 是否需要新增 ADR。

如果 Feature 需要改变 M1-M8 已验收内容，必须在 Feature Package 中说明原因，并要求 Code Agent 更新 CHANGELOG 与 ADR。

## 4. Package Generation

Builder 根据注册模板生成 Feature Package。生成过程要求：

- 所有路径稳定可预测。
- 每个生成物都有 Feature ID。
- 每个生成物都有验收标准。
- 投资相关内容都包含免责声明。
- Skill、Prompt、Benchmark 输出只引用既有模板，不复制底层规则。

## 5. Package Validation

Package Validation 是 Builder 生命周期中的强制环节。验证内容包括：

- 文件完整性。
- JSON Schema 合法性。
- Markdown 实质内容。
- 引用一致性。
- 合规免责声明。
- 禁止表达检查。

当前实现由 `scripts/validate_builder.py` 执行。

## 6. Code Agent Handoff

通过验证后，Feature Package 可交付给 Code Agent。Code Agent 应按以下顺序读取：

1. `ISSUE.md`
2. `ADR.md`
3. `FEATURE_SPEC.md`
4. `skill/`
5. `prompt/`
6. `schema/`
7. `tests/`
8. `benchmark/`
9. `PR_CHECKLIST.md`
10. `RELEASE_NOTES.md`

Handoff 的目标是让 Code Agent 直接进入 Go 模式，减少反复确认。

## 7. Review

Review Agent 对 Builder 生成物的关注点：

- Feature 目标是否清楚。
- 依赖是否真实存在。
- 测试是否可执行。
- Benchmark 是否能约束输出质量。
- 是否保留反方观点、不确定性和免责声明。
- 是否避免把 Builder 变成新的研究规则来源。

## 8. Release Note

每个 Feature Package 都必须包含 `RELEASE_NOTES.md`，用于说明：

- 本 Feature 新增了什么。
- 是否影响已有 M1-M8 内容。
- 是否存在迁移要求。
- 是否存在已知限制。
- 是否仍然遵守 AIRS 投资研究免责声明。

## 9. 生命周期状态

| 状态 | 含义 | 允许动作 |
|------|------|----------|
| DRAFT | 请求初稿 | 补充字段、调整范围 |
| READY_FOR_GENERATION | 可生成 | 执行 Builder |
| GENERATED | 已生成 | 运行验证 |
| VALIDATED | 已通过验证 | 交付 Code Agent |
| NEEDS_FIX | 生成物需修复 | 修复请求或模板 |
| RELEASED | Feature 已进入发布记录 | 归档与回归 |

