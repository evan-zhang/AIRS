# AIRS Builder

`builder/` 是 FEATURE-001 的本地生成器目录，用于把 YAML Feature Request 转换为完整 Feature Package。

## 目录结构

```text
builder/
├── README.md
├── main.py
├── registry.py
└── generators/
    └── README.md
```

## 使用方式

```bash
python3 builder/main.py templates/builder/feature-request-template.yaml
```

输出目录：

```text
builder-output/<feature-slug>/
```

## 生成物

Builder 默认生成 10 个文件：

- `ISSUE.md`
- `ADR.md`
- `FEATURE_SPEC.md`
- `skill/<slug>-skill.md`
- `prompt/<slug>-prompt.md`
- `schema/<slug>.schema.json`
- `tests/test-<slug>.md`
- `benchmark/<slug>-benchmark.md`
- `PR_CHECKLIST.md`
- `RELEASE_NOTES.md`

## 设计边界

Builder 只生成工程开发包，不执行投资研究，不提供投资建议。Skill、Prompt、Benchmark 草案必须引用既有 M5、M4、M7 模板，不能重复定义 AIRS 研究规则。

**免责声明**：本目录内容仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

