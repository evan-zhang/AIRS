# M10 Completion Report: Autonomous Investment Committee

免责声明：本文档仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## Scope

M10 / FEATURE-010 已交付 Autonomous Investment Committee（AIC）。AIC 位于 Planner 之后、Research Engine 之前，对任何投资研究结论执行多角色讨论、交叉验证、反方质疑、证据复核、共识构建和最终表决。

## Delivered Artifacts

- `builder/requests/feature-request-autonomous-investment-committee.yaml`
- `builder-output/autonomous-investment-committee/`
- `docs/committee/` 12 个 Committee 文档
- `committee/` 11 个 Python 核心组件和 README
- `committee/examples/` 6 个生产级 Committee 示例
- `schemas/committee/` 4 个 JSON Schema
- `templates/committee/` 2 个模板
- `scripts/validate_committee.py`
- `docs/adr/ADR-0010-autonomous-investment-committee.md`
- `docs/review/M10_SELF_REVIEW.md`

## Validation

`scripts/validate_committee.py` 覆盖 FEATURE-010 静态文件、Python 组件导入、6 个可执行示例、Schema、模板、Builder Package、CHANGELOG、Schema README、AIC 位于 Planner 后和 Research Engine 前的一致性，以及现有全部 `validate_*` 回归脚本。

当前仓库在新增 `validate_committee.py` 后实际包含 19 个 `validate_*` 脚本。脚本会自动枚举并运行除自身以外的 18 个回归脚本，再执行 Committee 自检。

## Key Decisions

- AIC 是 Research Engine 的前置门禁。
- AIC 只记录审议、证据挑战、反方观点、投票和 Decision，不复制 M2-M9 的业务规则。
- Final Recommendation 只能描述是否允许进入后续研究、哪些条件需要补证、哪些结论需要降级。

## Known Gaps

- 当前 AIC 为 deterministic 本地实现，尚未接入真实 LLM 多 Agent 对话。
- Evidence Challenge 当前检查结构和引用，真实证据强度仍依赖 M3 Evidence Engine。
- Vote 阈值为启发式规则，后续可按研究类型配置。
- 当前仓库实际验证脚本总数为 19 个，不是任务描述中的 20 个；未发现缺失的第 20 个 `validate_*.py` 文件。
