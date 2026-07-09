# Skill Lifecycle（Skill 生命周期）

## 1. 生命周期状态

Skill 从提出到退役分为六个状态：

- **Draft**：初稿阶段，允许 Code Agent 创建文档和 Schema，但不能作为生产 Skill 调用。
- **Review**：Review Agent 检查 Prompt、Methodology、Evidence 引用是否完整。
- **Active**：通过自检和人工复核后可被 Master Skill 调用。
- **Deprecated**：能力被替代，保留兼容窗口，不再新增调用。
- **Archived**：历史保留，仅供审计。
- **Rejected**：未通过治理或合规检查，不允许进入注册表。

## 2. 创建流程

创建 Skill 时必须先确定研究职责，然后选择现有 M4 Prompt、M2 Methodology 和 M3 Evidence 组件。Code Agent 只能在 `skills/` 下写 Skill 文档和必要 Schema，不能把 Prompt 文本复制到 Skill，也不能把方法论规则改写成 Skill 专属规则。

创建步骤：

1. 定义 Skill ID、名称、版本和适用范围。
2. 选择至少一个生产版 Prompt。
3. 选择至少一个 M2 方法论文档。
4. 选择 Evidence Card / Evidence Chain 规范。
5. 填写十个必需 section。
6. 运行 `scripts/validate_skill.py`。

## 3. 审查流程

Review Agent 按照 `docs/skill-engine/skill-governance.md` 检查：

- 依赖是否真实存在。
- Prompt 是否来自 M4 Prompt Library。
- 方法论是否来自 `docs/methodology/`。
- 证据规则是否引用 M3，而不是重复定义。
- 输出是否包含失败状态和免责声明。
- 是否存在交易指令、收益承诺或价格预测。

## 4. 变更流程

Active Skill 的变更必须记录原因、影响范围和兼容策略。若只新增引用或补充审查项，可以小版本更新；若改变输入输出结构或调用顺序，必须提升中版本；若破坏兼容性，需要新建 Skill 版本并保留旧版本退役计划。

## 5. 退役流程

当 Skill 被替代、依赖 Prompt 停用、方法论过期或证据规则升级导致不兼容时，进入 Deprecated 状态。退役说明必须写明替代 Skill、停止接收新调用的日期、历史输出的审计方式和未完成任务的迁移路径。

## 6. 失败状态

Skill 允许失败，并且应该明确失败。典型失败包括：输入研究范围不清、Prompt 不存在、方法论不匹配、Evidence Card 不足、反方证据缺失、输出无免责声明。失败输出必须包含 `failure_type`、`missing_inputs`、`retry_hint` 和 `disclaimer_required`。

## 7. 合规说明

生命周期治理只用于投资研究质量控制，不构成投资建议。任何生命周期状态都不能把 AIRS Skill 解释为投资顾问、自动交易系统或价格预测系统。

