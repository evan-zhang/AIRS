# Committee Governance

免责声明：本文档仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## 治理原则

AIC 的治理目标是提高研究结论的可解释性、可审计性和抗偏误能力。任何角色都不能绕过 Planner Gate、Evidence Challenge、Counter Argument、Voting 和 Decision Record。

## 版本与变更

Committee Schema、角色定义和投票阈值变更必须通过 ADR 记录。示例、模板和验证脚本应同步更新。新增角色必须说明是否复用既有 AIRS 能力，禁止新增与 Evidence、Score、Runtime 或 Engine 重复的职责。

## 合规

AIC 全部文档、代码输出、示例和 Schema 必须包含免责声明。若出现荐股、自动交易、交易指令、目标价或收益承诺，验证脚本必须失败。

治理规则要求 AIC 永远位于 Planner 与 Research Engine 之间，不允许任何 Agent 绕过该门禁直接输出投资结论。
