# Autonomous Investment Committee

免责声明：本文档仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

`committee/` 是 FEATURE-010 的最小可运行实现。AIC 位于 Planner 之后、Research Engine 之前：Planner 负责生成 Research Plan，AIC 负责多角色审议、证据挑战、反方质疑、共识构建和投票记录，Research Engine 只能执行 AIC 允许的研究范围。

## 组件

- `coordinator.py`：统一入口 `AutonomousInvestmentCommittee.run()`。
- `role_registry.py`：注册 Bull、Bear、Financial、Industry、Risk、Portfolio、Evidence Reviewer、Devil's Advocate 和 Moderator。
- `analysts.py`：四类分析师提出正反、财务和产业意见。
- `experts.py`：行业、风险和组合专家补充审查。
- `reviewer.py`：证据复核和 Devil's Advocate 挑战。
- `moderator.py`：议程、边界和禁用表达检查。
- `voting_engine.py`：结构化 Vote 与 Quorum 判断。
- `consensus_engine.py`：共识等级、保留问题和降级条件。
- `recorder.py`：Decision Record、Minority Report 和后续任务。

## 边界

AIC 不替代 Evidence、Score、Knowledge Graph、Runtime、Report 或 Investment Research Engine。它只引用既有 M1-M9 能力，形成可审计的 Committee Session、Vote、Consensus 和 Decision。所有输出必须保留免责声明，并禁止交易动作、收益承诺和目标价。
