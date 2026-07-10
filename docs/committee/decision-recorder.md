# Decision Recorder

免责声明：本文档仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## 记录范围

Decision Recorder 负责把一次 AIC Session 转换为可审计 Decision Record。它记录 Planner Ref、Participants、Debate Timeline、Evidence Review、Voting Result、Consensus、Minority Report、Final Recommendation 和 Follow-up Tasks。

## Gate 结果

Research Engine Gate 包括 `ALLOW`、`ALLOW_WITH_CONDITIONS` 和 `BLOCK`。`ALLOW_WITH_CONDITIONS` 是默认生产状态，因为多数研究结论都需要后续证据采集和审查。

## 审计

Decision Record 必须保留输入输出引用，而不是复制 M2-M9 的内部规则。这样可以让 ADR、Completion Report、Review Agent 和 Verification Agent 按统一路径复核，不造成重复定义和规则漂移。
