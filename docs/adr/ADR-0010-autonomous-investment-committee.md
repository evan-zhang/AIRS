# ADR-0010: Autonomous Investment Committee

免责声明：本文档仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## Status

Accepted

## Context

FEATURE-009 已建立 Autonomous Research Planner，FEATURE-008 已建立 Investment Research Engine。Planner 能把用户研究目标拆解为 Research Plan，但如果 Planner 之后直接进入 Engine，阶段性结论仍可能缺少多角色质疑、证据挑战、少数意见保留和最终表决记录。

AIRS 的核心理念要求证据驱动、反方思考、不确定性标注和可解释性。因此需要在 Planner 与 Research Engine 之间增加一个可验证的 Committee Gate。

## Decision

新增 `committee/`、`docs/committee/`、`schemas/committee/`、`templates/committee/` 和 `scripts/validate_committee.py`。Autonomous Investment Committee 位于 Planner 之后、Research Engine 之前，负责：

- 多角色参与：Bull、Bear、Financial、Industry、Risk、Portfolio、Evidence Reviewer、Devil's Advocate、Moderator。
- Debate Timeline：记录议程、质询、证据挑战和反方观点。
- Evidence Challenge：复用 M3 Evidence Card / Evidence Chain。
- Voting Mechanism：形成 APPROVE、CONDITIONAL_APPROVE 或 REJECT。
- Decision Record：记录 Research Engine Gate、Minority Report 和 Follow-up Tasks。

## Consequences

- Research Engine 不再只依赖 Planner 输出，而是依赖 AIC Decision Record。
- Review Agent 可以审查反方观点和少数报告是否充分。
- Verification Agent 可以运行 `scripts/validate_committee.py` 验证 AIC 与 M1-M9 的一致性。
- AIC 不直接采集数据、不计算 Score、不生成最终投资建议，避免与既有模块重复。

## Alternatives Considered

让 Research Engine 内置 Committee 逻辑可以减少一个目录，但会让 Engine 同时承担研究执行、反方质疑、投票和治理记录。单独设置 AIC 可以让 Planner、Committee、Engine 三层边界更清楚，也便于独立验证和审计。
