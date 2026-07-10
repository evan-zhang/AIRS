# 重复与冗余报告 (DUPLICATION_REPORT)

## 1. 重复 Schema
- `schemas/committee/` vs `schemas/runtime/` — 存在 8 个重复定义的 status 字段。
- `templates/builder/` 下模板与 `templates/report/` 等已有模板部分重叠。

## 2. 重复 Prompt / DSL
- `prompts/` 下 Prompt 与 `templates/builder/prompt-template.md` 存在结构重叠。
- DSL 定义在 `docs/prompt-engine/` 和 `templates/builder/` 两处出现。

## 3. 重复验证逻辑
- `scripts/validate_m6.py` 与 `scripts/validate_score.py` 功能重叠 — 都校验 scoring/。
- `scripts/validate_examples.py` 与 `scripts/validate_benchmark.py` 校验范围重叠。
- 建议合并为统一的 `validate_core.py`。

## 4. 废弃代码
- `src/` 目录存在但无实际业务代码。
- `benchmark/` 与 `docs/benchmark/` 内容重叠。

## 5. 建议清理
1. 删除 `src/` 目录。
2. 合并 validate_m6 + validate_score + validate_evaluation 为一个脚本。
3. 统一模板索引，避免 builder templates 与 core templates 重叠。
