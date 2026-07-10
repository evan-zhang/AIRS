# AIRS Builder Architecture

**归属 Feature**：FEATURE-001 AIRS Builder  
**版本**：v1.1.0-draft  
**最后更新**：2026-07-10  
**适用对象**：Code Agent、Review Agent、Verification Agent  

## 1. 目标

AIRS Builder 用于把一个结构化 Feature 请求转换为可交付给 Code Agent 开发的完整 Feature Package。Builder 不生成投资结论，不提供荐股、交易指令、目标价或收益承诺；它只生成工程交付物、治理材料、测试材料和与 AIRS M2-M7 体系兼容的开发输入。

Builder 的核心目标是：

- 将模糊 Feature 意图标准化为可验证的工程包。
- 强制每个 Feature Package 绑定 Issue、ADR、Feature Spec、Skill、Prompt、Schema、Tests、Benchmark、PR Checklist 和 Release Notes。
- 通过模板引用 M4 Prompt Engine、M5 Skill Engine、M7 Benchmark，而不是重新定义这些层的规则。
- 为 Code Agent 提供可执行、可审查、可回归的开发边界。

**免责声明**：本 Builder 仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## 2. 架构总览

```text
Feature Request YAML
        ↓
Normalize
        ↓
Dependency Check
        ↓
Generate Artifacts
        ↓
Validate
        ↓
Package
        ↓
builder-output/<feature-slug>/
```

Builder 采用轻量本地生成架构。当前版本不依赖远程服务，不接入实时数据源，不执行投资研究，只处理本地 YAML、Markdown 和 JSON 模板。

## 3. 输入层：Feature Request

输入是一个 YAML 文件，必须符合 `schemas/builder/feature-request.schema.json` 的字段要求。核心字段包括：

- `feature_id`：Feature 编号，例如 `FEATURE-001`。
- `feature_name`：Feature 名称。
- `feature_summary`：功能摘要。
- `business_goal`：业务目标。
- `user_scenarios`：用户场景清单。
- `dependencies`：依赖的 AIRS 层、文档、Schema 或模板。
- `constraints`：合规、技术、范围和交付约束。
- `expected_outputs`：期望生成物。
- `risk_level`：LOW / MEDIUM / HIGH / CRITICAL。

## 4. Normalize

Normalize 阶段负责把用户输入整理成 Builder 内部上下文：

- 生成稳定 `feature_slug`，用于输出目录。
- 补齐标准 artifact 路径。
- 规范依赖引用，例如 `M4 Prompt Engine`、`M5 Skill Engine`、`M7 Benchmark`。
- 检查 Feature 是否触及 AIRS 禁止范围。

Normalize 不改变 Feature 的业务含义，只把它转成可落盘、可检查、可审查的结构。

## 5. Dependency Check

Dependency Check 负责确认 Feature Package 引用的上游资产存在：

- 方法论相关需求引用 `docs/methodology/`。
- 证据相关需求引用 `docs/evidence/` 与 `schemas/evidence/`。
- Prompt 相关需求引用 `templates/prompt-template.md` 与 `docs/prompt-engine/`。
- Skill 相关需求引用 `templates/skill-template.md` 与 `docs/skill-engine/`。
- Benchmark 相关需求引用 `templates/benchmark-template.md` 与 `docs/benchmark/`。

若依赖缺失，Builder 应生成失败状态，不应静默生成不完整包。

## 6. Generate Artifacts

Artifact 生成阶段输出 10 类文件：

1. `ISSUE.md`
2. `ADR.md`
3. `FEATURE_SPEC.md`
4. `skill/<slug>-skill.md`
5. `prompt/<slug>-prompt.md`
6. `schema/<slug>.schema.json`
7. `tests/test-<slug>.md`
8. `benchmark/<slug>-benchmark.md`
9. `PR_CHECKLIST.md`
10. `RELEASE_NOTES.md`

每个生成物必须包含：

- Feature 元数据。
- 上游 AIRS 层引用。
- 验收标准。
- 风险与不确定性。
- 合规免责声明。

## 7. Validate

Validate 阶段至少检查：

- 输出目录结构完整。
- 10 个标准文件存在。
- Schema 文件是合法 JSON。
- Markdown 文件不是空壳。
- 文档包含“免责声明”和“不构成投资建议”。
- Skill、Prompt、Benchmark 文件明确引用 M5、M4、M7 对应模板。
- Package 不包含交易建议、价格预测或收益承诺。

## 8. Package

Package 阶段把生成结果写入：

```text
builder-output/<feature-slug>/
```

该目录就是交给 Code Agent 的开发包。Code Agent 可以从 `ISSUE.md` 理解任务，从 `FEATURE_SPEC.md` 理解规格，从 `ADR.md` 理解决策，从 `tests/` 和 `benchmark/` 理解验收边界。

## 9. 与 AIRS M2-M7 的关系

Builder 是工程层，不替代 AIRS 研究层：

- 不重复定义 M2 Methodology。
- 不重复定义 M3 Evidence。
- 不重复定义 M4 Prompt DSL。
- 不重复定义 M5 Skill Engine。
- 不重复定义 M6 Score / Evaluation。
- 不重复定义 M7 Benchmark 标准。

Builder 只做“生成引用这些层的开发包”。

