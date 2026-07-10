# Investment Research Engine Architecture

免责声明：本文档仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## Purpose

Investment Research Engine 是 M1-M7 基础设施之上的统一编排层。它不替代 Methodology、Skill、Prompt、Evidence、Knowledge Graph、Score、Runtime 或 Workspace，而是把这些模块按可审计顺序连接起来，生成可复核的研究产物。

## Architecture

Engine 输入 `investment-request`，先交给 Runtime 形成 Workflow，再按研究阶段调用主题发现、公司发现、行业发现、供应链、卡脖子、命题、风险、催化剂、可比、组合影响和 Recommendation 组件。每个组件只生成结构化片段，并保留底层服务引用。

核心边界：

- Runtime：负责 Agent 调度、事件、状态和执行时间线。
- Workspace：负责项目、会话、任务、产物、快照和审计。
- Data Connectors：负责外部数据接入，Engine 不直接抓取外部数据。
- Methodology：定义研究方法，Engine 只引用方法论。
- Skill：执行可复用研究能力，Engine 只声明调用关系。
- Prompt：约束 Agent 输出格式和失败处理。
- Evidence：提供证据卡、证据链、反方证据和缺失证据。
- Knowledge Graph：表达产业链节点、依赖路径和卡脖子结构。
- Score：汇总证据质量、卡点强度、风险控制和质量门禁。
- Report：把结构化结果渲染成最终研究报告。

## Component Map

`investment_engine/pipeline.py` 是唯一统一调度入口。其余模块保持单一职责：`theme_discovery.py` 识别主题信号，`company_discovery.py` 识别研究对象，`industry_discovery.py` 判断行业阶段，`supply_chain.py` 建立产业链，`chokepoint.py` 识别瓶颈，`thesis_generator.py` 生成命题，`risk.py` 和 `catalyst.py` 生成风险与催化剂，`comparable.py` 和 `portfolio_impact.py` 支持横向比较与组合影响，`recommendation.py` 管理合规表达。

## Governance

Engine 输出必须包含免责声明、证据引用、反方证据、缺失证据和不确定性。任何 Recommendation 都必须区分 Facts、Inference、Assumption 和 Opinion；不得把 Score、Gate 或 Research Stance 表述为买卖动作、目标价或收益承诺。
