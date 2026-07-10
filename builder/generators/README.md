# Builder Generators

本目录预留给后续细分生成器，例如 Issue Generator、ADR Generator、Schema Generator 和 Benchmark Generator。

当前 FEATURE-001 采用 `builder/main.py` 中的轻量生成流程，所有 artifact 类型由 `builder/registry.py` 注册。后续如果生成逻辑变复杂，可以把各类 artifact 拆分到本目录，但仍需保持以下原则：

- 只生成 Feature Package，不执行投资研究。
- 引用 M2-M7 既有规范，不重复定义规则。
- 输出必须可被 `scripts/validate_builder.py` 检查。
- 投资相关内容必须包含免责声明。

**免责声明**：本目录仅用于 AIRS 工程开发和研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

