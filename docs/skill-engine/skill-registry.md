# Skill Registry（Skill 注册表）

## 1. 注册表目的

Skill Registry 是 Master Skill 查找和调用生产版 Skill 的唯一入口。注册表记录 Skill 的能力边界、版本、依赖 Prompt、依赖方法论、依赖 Evidence Engine 组件和治理状态，避免不同 Agent 以不同方式调用同一个 Skill。

## 2. 注册字段

每条注册记录至少包含：

- `skill_id`：全局唯一，例如 `airs.skill.supply_chain.v1`。
- `name`：中文与英文名称。
- `version`：语义化版本。
- `status`：Draft、Review、Active、Deprecated、Archived、Rejected。
- `entrypoint`：Skill 文档路径。
- `invoked_prompts`：M4 Prompt 路径列表。
- `invoked_methodologies`：M2 方法论文档路径列表。
- `invoked_evidence`：M3 Evidence 文档或 Schema 路径列表。
- `input_contract`：输入字段摘要。
- `output_contract`：输出字段摘要。
- `owner_agent`：负责维护的 Agent 类型。
- `review_status`：最近一次审查结论。
- `disclaimer_required`：是否强制输出免责声明。

## 3. 注册规则

只有满足以下条件的 Skill 可以进入 Active：

- 文档存在且包含十个必需 section。
- 至少引用一个 M4 Prompt。
- 至少引用一个 M2 Methodology。
- 至少引用一个 M3 Evidence Engine 组件。
- 没有内置 Prompt 正文。
- 没有重复定义 Evidence Level、证据字段或方法论判断规则。
- 自检脚本输出 PASS。

## 4. 查找策略

Master Skill 按研究意图选择 Skill。供应链卡点问题优先调用 Supply Chain Skill；证据链质量问题调用 Evidence Skill；估值合理性问题调用 Valuation Skill；风险与反方观点调用 Risk Skill；最终输出调用 Report Skill；系统验收调用 Verification Skill。

当多个 Skill 都可处理同一任务时，按以下顺序决策：

1. 用户意图与 Skill Purpose 的匹配度。
2. Methodology 与研究问题的匹配度。
3. Evidence 需求是否可满足。
4. Prompt 是否处于可用状态。
5. 最近 Review 结论是否 PASS。

## 5. 注册表维护

Code Agent 新增 Skill 后必须同步更新注册表 Schema 和 Completion Report。后续若创建实际 registry 数据文件，应符合 `schemas/skills/skill-registry.schema.json`。本 M5 阶段先交付注册表规范与 Schema，不创建运行时数据库。

## 6. 合规说明

注册表是能力路由工具，不代表任何研究结论有效，也不构成投资建议。所有通过注册表调度的投资研究输出都必须保留免责声明和不确定性标注。

