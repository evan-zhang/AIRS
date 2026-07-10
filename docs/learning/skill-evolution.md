# Skill Evolution

## 1. 目标

Skill Evolution 关注 Skill 工作流中的执行质量，例如输入不完整、证据未校验、失败处理缺失、Committee Follow-up 未闭环或 Runtime 状态没有被记录。

## 2. 优化范围

Skill Proposal 可以建议增加输入 Schema 检查、Evidence Chain 门禁、Review Checklist、失败回退、Runtime Event 记录和 Memory Consolidation。它不能把 Skill 变成自动交易或荐股工具。

## 3. 与 Runtime 关系

Skill 仍由 Runtime 调度。Learning Engine 可以建议 Runtime 事件中增加学习信号，但不能绕过 Runtime 直接执行业务模块。

## 4. 验证

Skill 更新需要运行 validate_skill.py、validate_runtime.py、validate_committee.py 和 validate_learning.py，并在 Self Review 中说明新增风险。

## 免责声明

本文档仅用于 AIRS 工程开发、研究质量控制和持续改进，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

