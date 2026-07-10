# Learning Governance

## 1. 治理原则

Learning Governance 确保持续学习不会绕过 AIRS 的合规边界。核心原则是：来源可审计、建议可回滚、人工可评审、验证可复现、生产变更可追踪。

## 2. 权限边界

Learning Engine 不具备自动应用权限。它不能直接修改 Prompt、Methodology、Skill、Score、Report 模板或生产配置。任何变更都必须由 Code Agent 按常规开发流程提交，并由 Review Agent 与 Verification Agent 验证。

## 3. 风险控制

高风险改进需要 ADR，涉及评分权重或报告模板的改动必须记录影响范围。若回归测试失败，候选规则保持 pending 或 rejected，不得进入生产。

## 4. 审计

每个 Proposal 必须保留 source_rule、source_pattern、evidence_refs、review_status、rollback_plan 和 disclaimer。Memory Consolidation 只保存摘要和来源，不保存无法验证的结论。

## 免责声明

本文档仅用于 AIRS 工程开发、研究质量控制和持续改进，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。
