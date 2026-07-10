# ADR-012: Autonomous Learning Engine

## 状态

Accepted

## 背景

AIRS 已具备 Planner、Runtime、Workspace、Investment Engine、Committee、Report、Evidence、Score 和 Benchmark 等能力，但历史研究中的反馈、评审问题、Committee 分歧、Memory 摘要和 Outcome 偏差仍缺少统一的闭环改进机制。若这些信号只停留在人工复盘中，系统很难持续降低重复质量缺陷。

## 决策

引入 `learning/` Autonomous Learning Engine，作为 Report、Committee、Memory、Outcome 和 Benchmark 之后的持续改进层。它收集 Feedback，跟踪 Outcome，挖掘 Pattern，生成 Rule Candidate，并提出 Prompt、Methodology、Skill 和 Score 的优化建议。

Learning Engine 默认不具备自动应用权限。所有建议状态为 pending_review，必须经过 Review Agent、Verification Agent 和回归脚本后才能进入生产变更。

## 影响

- 新增 `docs/learning/`、`learning/`、`learning/examples/` 和 `schemas/learning/`。
- 新增 `scripts/validate_learning.py`，并把所有既有 validate 脚本作为回归。
- Completion Report 和 Self Review 必须记录 Learning 的已知缺口和上下文来源。

## 后果

正向影响是 AIRS 具备可审计的持续改进闭环。代价是每条规则候选都必须记录来源、证据、回滚策略和评审状态，治理成本更高。

## 免责声明

本文档仅用于 AIRS 工程开发、研究质量控制和持续改进，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

