# Resource Planner

免责声明：本文档仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## 职责

Resource Planner 估算研究计划需要的 Connector、Methodology、Skill、Workspace Artifact 和人工复核资源。

## 资源类型

- Connector：公开资料、政策、公告、行业报告、组合快照等。
- Methodology：M2 方法论引用。
- Skill：M5 生产 Skill 引用。
- Workspace Artifact：Research Goal、Research Plan、Evidence Plan、KG Plan、Score Plan、Report Plan。
- Human Review：Review Agent 或人工复核门禁。

## 输出

Resource Planner 输出 `resource_profile`、`connectors`、`methodologies`、`skills`、`workspace_artifacts`、`max_concurrency` 和 `human_review_required`。

## 治理

Resource Planner 只估算资源，不发起真实联网采集，不触发 Runtime。
