# Committee Lifecycle

免责声明：本文档仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## 生命周期阶段

1. Planner Gate：检查 `planner_generated=true`、研究范围、预算、证据预期和 Runtime 边界。
2. Session Open：创建 Committee Session，登记参与角色和议程。
3. Opening Opinions：Bull、Bear、Financial、Industry 等角色提出初始观点。
4. Evidence Challenge：Evidence Reviewer 按 M3 Evidence Chain 检查证据缺口。
5. Counter Argument：Devil's Advocate 强制提出替代解释和失败情景。
6. Consensus Building：Moderator 汇总共识、分歧、降级条件和未决问题。
7. Vote：Voting Engine 记录每个角色的 APPROVE、CONDITIONAL_APPROVE 或 REJECT。
8. Decision Record：Recorder 输出 Research Engine Gate、Minority Report 和 Follow-up Tasks。

## 状态

Session 状态包括 `OPEN`、`IN_DEBATE`、`EVIDENCE_CHALLENGE`、`VOTING`、`DECIDED` 和 `BLOCKED`。状态只描述审议过程，不代表投资评级。

## 退出条件

通过条件是达到 Quorum、无硬性合规失败、证据缺口有后续任务、反方观点被记录。阻断条件是 Planner Gate 缺失、证据链不可审计、出现交易指令或多数角色 REJECT。
