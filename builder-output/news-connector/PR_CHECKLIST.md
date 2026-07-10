# News Connector PR Checklist

- [ ] 10 个 Builder artifact 均存在。
- [ ] Schema 为合法 JSON。
- [ ] Skill 引用 `templates/skill-template.md` 与 M5 Skill Engine。
- [ ] Prompt 引用 `templates/prompt-template.md` 与 M4 Prompt Engine。
- [ ] Benchmark 引用 `templates/benchmark-template.md` 与 M7 Benchmark。
- [ ] 新闻事实、解读和推断已区分。
- [ ] 反方来源、缺失证据和不确定性字段完整。
- [ ] 未修改 M1-M8 已验收内容，或已新增 ADR 和 CHANGELOG 说明。
- [ ] 运行 `python3 scripts/validate_builder.py`。
- [ ] 运行 M1-M8 回归验证脚本。

## 免责声明

本 PR Checklist 仅用于 AIRS 工程开发与投资研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

