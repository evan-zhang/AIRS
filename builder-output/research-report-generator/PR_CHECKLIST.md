# FEATURE-003 PR Checklist - Research Report Generator

## 1. 文件完整性

- [ ] `ISSUE.md`
- [ ] `ADR.md`
- [ ] `FEATURE_SPEC.md`
- [ ] `skill/<slug>-skill.md`
- [ ] `prompt/<slug>-prompt.md`
- [ ] `schema/<slug>.schema.json`
- [ ] `tests/test-<slug>.md`
- [ ] `benchmark/<slug>-benchmark.md`
- [ ] `PR_CHECKLIST.md`
- [ ] `RELEASE_NOTES.md`

## 2. 一致性

- [ ] 引用 M2-M7 既有规范。
- [ ] 未重复定义 Methodology / Evidence / Prompt / Skill / Score / Evaluation / Benchmark 规则。
- [ ] 所有 JSON 文件可解析。
- [ ] 所有 Markdown 有实质内容。

## 3. 验证

- [ ] `python3 scripts/validate_builder.py`
- [ ] M1-M8 回归验证脚本。

## 4. 合规

- [ ] 包含免责声明。
- [ ] 不构成投资建议。
- [ ] 无荐股、自动交易、交易指令、目标价或收益承诺。

## 5. 免责声明

本生成物仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

