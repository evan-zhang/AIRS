# ADR-0001: M7 增强 Benchmark Case 模板免责声明

**状态**：Accepted  
**日期**：2026-07-10  
**归属 Milestone**：M7 Benchmark & Production Examples

**免责声明**：本 ADR 仅用于记录 AIRS Benchmark 模板治理决策，不构成投资建议，不提供交易指令、价格预测或收益承诺。

## Context（背景）

M7 新增 `scripts/validate_benchmark.py` 后，Benchmark 模板需要与 M7 的统一合规检查保持一致。M1 已有 `templates/benchmark-case-template.md` 具备完整基准用例结构，但文件开头没有显式免责声明。由于 M7 的 Benchmark 校验要求模板文件包含“免责声明”和“不构成投资建议”，若不增强该模板，M7 回归会出现合规缺口。

该变更触及 M1 已 PASS 文件，因此按任务要求新增 ADR，并在 CHANGELOG 与 M7 Completion Report 中说明原因。

## Decision（决策）

在 `templates/benchmark-case-template.md` 顶部增加一条简短免责声明：

- 明确模板仅用于 AIRS Benchmark 用例编写与质量测试。
- 明确不构成投资建议。
- 明确不提供交易指令、价格预测或收益承诺。

不修改该模板的字段结构、验收标准、评分细则或 M1 原有语义。

## Alternatives（备选方案）

1. **只放宽 M7 校验脚本**：会降低合规一致性，且不能解决模板本身缺少显式免责声明的问题。
2. **新建替代模板并弃用 M1 模板**：会造成模板重复，不符合 M7 “禁止重复定义已有规则”的要求。
3. **在 M7 新模板中覆盖旧模板**：会增加迁移成本，并可能破坏 M1 使用方式。

最终选择最小增强旧模板，保持向后兼容。

## Consequences（影响）

正面影响：

- M1 Benchmark Case 模板与 M7 合规检查一致。
- 后续 Benchmark 用例从模板层继承免责声明边界。
- 不改变既有模板结构，向后兼容。

负面影响：

- M7 对 M1 已 PASS 文件产生一次受控修改，需要 ADR、CHANGELOG 和 Completion Report 记录。

## Validation（验证）

已通过以下脚本验证：

```bash
python3 scripts/validate_m1.py
python3 scripts/validate_benchmark.py
```

并在 M7 全量回归中与 M1-M6 其他脚本一起验证通过。

