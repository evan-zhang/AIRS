# AIRS Semantic Versioning（语义化版本规范）

**版本**：v1.0.0  
**适用范围**：AIRS V1.0 及后续版本

## 1. 版本格式

AIRS 使用语义化版本：

```text
MAJOR.MINOR.PATCH
```

示例：

- `1.0.0`：第一个生产版本。
- `1.1.0`：向后兼容的功能新增。
- `1.0.1`：向后兼容的问题修复。
- `2.0.0`：不兼容的结构或治理变更。

## 2. Major 规则

以下变更必须提升 Major：

- 改变核心目录结构且不兼容旧引用。
- 改变 Methodology、Prompt、Skill、Evidence、Score、Benchmark 的核心 Schema 语义。
- 删除或重命名生产级公开文件。
- 改变质量门禁 PASS / FAIL 语义。
- 改变“不构成投资建议”的合规边界。

## 3. Minor 规则

以下变更提升 Minor：

- 新增 Methodology、Prompt、Skill、Score 维度、Benchmark 分类或 Example。
- 新增治理流程或生产文档。
- 新增验证脚本但保持旧脚本可用。
- 增强现有文档，不破坏已有引用。

## 4. Patch 规则

以下变更提升 Patch：

- 修正文档错字或表述不清。
- 修复验证脚本边界错误。
- 补充遗漏免责声明。
- 修复 CHANGELOG、Release Notes 或支持文档中的非结构性问题。

## 5. Pre-release 规则

预发布版本格式：

```text
1.1.0-alpha.1
1.1.0-beta.1
1.1.0-rc.1
```

使用规则：

- alpha：功能仍在建设。
- beta：功能完整但需要更多验证。
- rc：候选发布，必须运行完整生产检查。

## 6. Release 规则

正式 Release 必须：

1. 更新 `CHANGELOG.md`。
2. 更新 Release Notes。
3. 运行 `scripts/production_check.py`。
4. 通过 Final Quality Gate。
5. 创建 Git tag。

## 7. 免责声明

版本号只表示 AIRS 工程和治理交付成熟度，不表示任何投资研究结论质量，不构成投资建议，不提供交易指令或收益承诺。
