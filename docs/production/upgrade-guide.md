# AIRS Upgrade Guide（升级指南）

**版本**：v1.0.0  
**适用范围**：从 V1.0 升级到 V1.x / V2.0  
**面向角色**：Code Agent、Release Manager、治理负责人

## 1. 升级原则

AIRS 升级必须遵守向后兼容和可审计原则。生产版本中的 Methodology、Prompt、Skill、Schema、Score、Evaluation、Benchmark 和 Example 互相关联，任何单点升级都需要检查上下游引用。

## 2. 版本升级分类

- Patch：修正文档错字、脚本边界错误、说明遗漏，不改变结构化接口。
- Minor：新增方法论、Prompt、Skill、Benchmark、Example 或治理流程，保持兼容。
- Major：改变核心 Schema、目录结构、质量门禁语义或 Agent 协作协议。

详细规则见 `docs/governance/semantic-versioning.md`。

## 3. 升级前准备

升级前必须：

1. 阅读当前 `CHANGELOG.md` 和最新 Completion Report。
2. 确认变更涉及哪些里程碑产物。
3. 建立 Issue 或 RFC，说明目标、范围、风险和回滚方式。
4. 若修改核心规范或顶层文件，新增 ADR。
5. 建立回归测试清单。

## 4. 升级执行流程

1. 创建升级分支。
2. 修改最小必要文件。
3. 更新相关文档、模板和 Schema 引用。
4. 更新 `CHANGELOG.md`。
5. 运行对应 validate 脚本。
6. 运行 `python3 scripts/production_check.py`。
7. 生成或更新升级说明。
8. 提交 PR 并等待 Code Review 和 Verification Review。

## 5. 兼容性检查

升级必须检查：

- Methodology 是否仍有 Required Evidence 和 Counter Evidence。
- Prompt 是否仍引用 M2/M3 且包含 Failure Cases。
- Skill 是否仍引用 M4 Prompt、M2 Methodology 和 M3 Evidence。
- Score 是否仍可解释且不被描述为投资评级。
- Evaluation 是否保留 PASS / CONDITIONAL_PASS / FAIL。
- Benchmark 是否仍包含 Evidence、Scorecard、Quality Gate、反方观点和不确定性。

## 6. 升级失败处理

如果升级失败：

- 不要删除失败记录。
- 恢复到升级前分支状态或创建修复提交。
- 在 PR 中说明失败原因。
- 如果已经发布，按 patch 版本发布修复。
- 如果涉及合规风险，优先修正免责声明、禁止表达和报告边界。

## 7. 免责声明

AIRS 升级指南仅用于项目治理和生产维护。升级后的研究输出仍然不构成投资建议，不提供买卖指令、目标价或收益承诺。
