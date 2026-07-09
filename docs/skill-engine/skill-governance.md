# Skill Governance（Skill 治理）

## 1. 治理目标

Skill Governance 定义 Skill Engine 的质量、合规、审计和责任边界。治理重点不是让 Skill 输出更像结论，而是确保每个结论可追溯、可质疑、可失败、可复核。

## 2. 角色责任

- **Code Agent**：创建或修改 Skill 文档、Schema、模板和自检脚本，运行全部验证。
- **Research Agent**：按 Skill 调用协议执行研究，不绕过 Prompt Engine。
- **Review Agent**：检查证据完整性、方法论一致性、反方观点和不确定性。
- **Verification Agent**：运行脚本、检查结构、检查合规边界和失败状态。

## 3. 强制规则

每个生产版 Skill 必须：

- 包含十个必需 section。
- 引用至少一个 M4 Prompt。
- 引用至少一个 M2 Methodology。
- 引用 M3 Evidence Card / Evidence Chain 规范。
- 输出免责声明。
- 输出失败处理方式。
- 输出 Review Checklist。

每个生产版 Skill 禁止：

- 内置 Prompt 正文。
- 重写方法论理论。
- 重新定义证据等级或证据卡字段。
- 输出交易指令、收益承诺、价格预测或个性化投资建议。
- 省略反方观点、缺失证据或不确定性。

## 4. 审查维度

Review Agent 按 100 分制审查：

- 结构完整性 20 分。
- Prompt 引用一致性 20 分。
- Methodology 引用一致性 20 分。
- Evidence Engine 引用一致性 20 分。
- 合规与失败处理 20 分。

任一强制规则失败，整体结论为 FAIL。

## 5. 例外处理

若某个研究任务无法获得足够证据，Skill 应输出证据缺口和后续采集建议，而不是补全结论。若用户要求交易动作、明确价格预测或收益承诺，Skill 必须拒绝并说明 AIRS 只提供研究框架。

## 6. 审计记录

Skill 输出应保留 Skill ID、版本、调用时间、Prompt 路径、Methodology 路径、Evidence Chain ID、Review Checklist 结果和免责声明。审计记录用于质量控制，不用于对外承诺研究结果。

## 7. 合规说明

AIRS Skill Engine 是投资研究方法论框架的一部分，不构成投资建议。所有输出仅供研究参考，投资有风险，决策需由使用者自行负责。

