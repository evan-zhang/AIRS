# AIRS Governance Guide（治理指南）

**版本**：v1.0.0  
**适用范围**：AIRS V1.0 生产治理  
**面向角色**：治理负责人、Code Agent、Review Agent、Verification Agent

## 1. 治理目标

AIRS 治理的目标是确保投资研究 Agent 的生产资产可追溯、可审查、可测试、可维护，并严格遵守“不构成投资建议”的边界。

## 2. 治理对象

治理覆盖：

- Methodology：研究方法论。
- Evidence：证据卡、证据链、证据等级。
- Prompt：Prompt DSL、Prompt 模板和生产 Prompt。
- Skill：Skill 调用、组合、版本、注册。
- Score：评分维度、权重和综合评分。
- Evaluation：质量门禁、回归策略、评审 Rubric。
- Benchmark：测试用例、Gold Standard、Failure Cases。
- Production：发布、部署、维护、安全和支持流程。

## 3. 角色职责

Code Agent：

- 按规范创建和修改文件。
- 运行自检脚本。
- 更新 Completion Report 和 CHANGELOG。

Research Agent：

- 按 Methodology 和 Skill 生成研究输出。
- 绑定 Evidence Chain。
- 输出反方观点和不确定性。

Review Agent：

- 检查证据完整性、逻辑一致性、反方观点强度和免责声明。
- 标注质量缺口。

Verification Agent：

- 运行 validate 脚本和生产检查。
- 生成回归和验收报告。

## 4. 变更治理

所有生产变更必须满足：

1. 有清晰变更目的。
2. 有影响范围说明。
3. 有自检结果。
4. 有 CHANGELOG 记录。
5. 修改核心顶层文件或已 PASS 核心规范时，必须新增 ADR。
6. 投资相关内容必须保留免责声明。

## 5. 审查门禁

生产变更不得合入，除非：

- `scripts/production_check.py` PASS。
- Release Checklist 全部关键项 PASS。
- 无未解释的技术债隐瞒。
- 无荐股、自动交易、价格预测或收益承诺。
- FINAL_REVIEW 如实记录风险。

## 6. 记录要求

治理记录至少包括：

- Issue 或任务说明。
- PR 描述。
- Review 结论。
- 验证结果。
- Release Notes。
- ADR 或 RFC（如适用）。

## 7. 免责声明

AIRS 治理流程用于约束研究质量和系统发布质量，不构成投资建议，不提供任何证券买卖建议、目标价或收益承诺。
