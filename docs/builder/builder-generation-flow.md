# AIRS Builder Generation Flow

**归属 Feature**：FEATURE-001 AIRS Builder  
**版本**：v1.1.0-draft  
**最后更新**：2026-07-10  

## 1. 生成流程目标

Builder Generation Flow 说明 `builder/main.py` 如何把 YAML Feature Request 转换为 Feature Package。该流程面向 Code Agent 开发交付，不生成投资建议。

**免责声明**：本文档仅用于 AIRS 工程开发、质量控制和研究流程治理，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## 2. 输入文件

输入示例：

```bash
python3 builder/main.py templates/builder/feature-request-template.yaml
```

Feature Request 必须包含：

- `feature_id`
- `feature_name`
- `feature_summary`
- `business_goal`
- `user_scenarios`
- `dependencies`
- `constraints`
- `expected_outputs`
- `risk_level`

## 3. 步骤一：读取 YAML

`builder/main.py` 优先使用 PyYAML。若本地环境未安装 PyYAML，则使用内置的最小 YAML 解析器处理 Builder 模板所需的简单结构。

读取后生成 `request` 字典，并保留原始字段，供模板渲染使用。

## 4. 步骤二：校验必需字段

校验规则：

- 必需字段不能为空。
- `risk_level` 必须是 `LOW`、`MEDIUM`、`HIGH` 或 `CRITICAL`。
- `expected_outputs` 至少包含一个输出项。
- `feature_id` 必须是稳定编号。

失败时返回非零退出码，并输出失败原因。

## 5. 步骤三：规范化上下文

规范化输出：

```json
{
  "feature_slug": "knowledge-graph-engine",
  "package_dir": "builder-output/knowledge-graph-engine",
  "artifact_paths": {
    "issue": "ISSUE.md",
    "adr": "ADR.md",
    "feature_spec": "FEATURE_SPEC.md"
  }
}
```

Slug 生成规则：

- 转小写。
- 非字母数字字符替换为 `-`。
- 移除首尾 `-`。
- 连续 `-` 合并。

## 6. 步骤四：依赖检查

依赖检查只检查本地引用是否可解释，不扩展上游规则：

- `templates/skill-template.md`
- `templates/prompt-template.md`
- `templates/benchmark-template.md`
- `docs/skill-engine/`
- `docs/prompt-engine/`
- `docs/benchmark/`
- `docs/evidence/`
- `docs/methodology/`

如果 Feature Request 声明了不存在的具体文件，Builder 应在 Issue 或 Spec 中标注待补齐依赖。

## 7. 步骤五：生成 10 个 Artifact

Builder 使用 `builder/registry.py` 中的注册表确定 artifact 类型、模板路径和输出路径。

生成物：

| Artifact | 输出路径 | 作用 |
|----------|----------|------|
| issue | `ISSUE.md` | Code Agent 任务入口 |
| adr | `ADR.md` | Feature 级架构决策 |
| feature_spec | `FEATURE_SPEC.md` | 功能规格 |
| skill | `skill/<slug>-skill.md` | Skill 开发草案 |
| prompt | `prompt/<slug>-prompt.md` | Prompt 开发草案 |
| schema | `schema/<slug>.schema.json` | Feature 数据结构草案 |
| tests | `tests/test-<slug>.md` | 测试说明 |
| benchmark | `benchmark/<slug>-benchmark.md` | Benchmark 草案 |
| pr_checklist | `PR_CHECKLIST.md` | PR 合并前检查 |
| release_notes | `RELEASE_NOTES.md` | 发布说明 |

## 8. 步骤六：写入输出目录

输出目录固定为：

```text
builder-output/<feature-slug>/
```

已有文件默认覆盖，适合在本地迭代生成。正式开发时，Code Agent 应在提交前阅读 diff，避免覆盖人工编辑。

## 9. 步骤七：验证

生成后执行：

```bash
python3 scripts/validate_builder.py
```

验证通过后，Feature Package 才能进入 Code Agent 开发流程。

## 10. 失败处理

| 失败类型 | 处理方式 |
|----------|----------|
| YAML 读取失败 | 输出错误并停止 |
| 必需字段缺失 | 输出缺失字段清单 |
| 风险等级无效 | 要求改为标准枚举 |
| 模板不存在 | 输出模板路径并停止 |
| 写入失败 | 输出目标路径和异常 |
| 验证失败 | 修复生成物后重跑 |

