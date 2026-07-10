# Consensus Building

免责声明：本文档仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## 原则

Consensus Building 不追求所有角色完全一致，而是明确哪些部分已经被证据支持、哪些部分仍是假设、哪些部分需要后续验证。共识必须能够被 Review Agent 复核，也必须能被 Verification Agent 用脚本检查。

## 共识等级

- Full Consensus：关键证据、反方观点和风险处理均通过。
- Conditional Consensus：主体逻辑可进入后续研究，但存在补证、降级或时间窗口限制。
- No Consensus：证据不足、逻辑冲突或合规边界不满足。

## 记录要求

Consensus Record 必须包含 agreed points、unresolved questions、decision threshold、minority report 和 follow-up tasks。未决问题不是缺陷，只要被明确记录并进入后续任务即可。

共识构建阶段承接 Planner 计划，输出给 Research Engine Gate，用于决定继续研究、条件继续或阻断。
