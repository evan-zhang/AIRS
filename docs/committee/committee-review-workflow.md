# Committee Review Workflow

免责声明：本文档仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## Review Agent 工作流

Review Agent 读取 Committee Session、Vote、Consensus 和 Decision Record，检查证据挑战是否充分、反方观点是否实质、少数报告是否被保留、Final Recommendation 是否符合 Recommendation Schema。

## Verification Agent 工作流

Verification Agent 运行 `scripts/validate_committee.py`，检查 `docs/committee/`、`committee/`、`schemas/committee/`、`templates/committee/`、6 个示例、ADR、Completion Report、Self Review 和全部现有回归脚本。

## 通过标准

通过标准不是观点正确，而是流程完整：Planner Gate 明确、角色覆盖完整、证据挑战存在、反方观点存在、投票结果可追溯、少数报告保留、后续任务明确、免责声明完整。

Review Workflow 的核心检查是 Planner 产物是否被 Committee 审议，以及 Research Engine 是否只接收 Decision Record 允许的任务范围。
