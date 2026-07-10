# Voting Mechanism

免责声明：本文档仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## 投票选项

- APPROVE：允许进入 Research Engine 或报告下一阶段，但仍不代表投资建议。
- CONDITIONAL_APPROVE：允许继续研究，但必须完成补证、降级或复核任务。
- REJECT：阻断流程，要求 Planner 或 Research Engine 重新处理。

## Quorum

标准 Session 至少需要 6 个有效角色投票，且必须包含 Evidence Reviewer、Devil's Advocate 和 Moderator 的记录。若证据挑战失败或合规边界失败，即使多数同意也不得通过。

## 结果解释

Voting Result 是研究流程门禁，不是投资评级。它只决定是否允许 Research Engine 继续执行、是否需要补证、是否需要 Review Agent 复核，以及 Final Recommendation 是否可进入报告草案。
