# AIRS V1.0 Release Checklist（发布清单）

**版本**：v1.0.0  
**适用范围**：M8 Production Release  
**状态**：用于发布前最终核验

## 1. 结构检查

- [x] 顶层文件存在：README、ARCHITECTURE、AGENTS、SKILL、ROADMAP、CONTRIBUTING、LICENSE、CHANGELOG。
- [x] M1-M7 Completion Report 存在。
- [x] M8 Production 文档存在。
- [x] `.github/` 治理文件存在。
- [x] `docs/governance/semantic-versioning.md` 存在。
- [x] `docs/governance/release-workflow.md` 存在。

## 2. 内容检查

- [x] README 标注 V1.0 Production 状态。
- [x] ROADMAP 标注 M1-M8 完成。
- [x] CHANGELOG 记录 v1.0.0 release。
- [x] CONTRIBUTING 引用版本规范和发布流程。
- [x] LICENSE 保持 MIT License，并包含投资研究免责声明。

## 3. 质量检查

- [x] 所有 M1-M8 validate 脚本可运行。
- [x] `scripts/production_check.py` 可聚合执行。
- [x] Final Quality Gate 已定义 PASS 标准。
- [x] Production Acceptance Checklist 覆盖结构、内容、质量、安全。
- [x] Regression Test Process 定义回归测试选择和报告格式。

## 4. 安全与合规检查

- [x] SECURITY.md 明确安全报告方式和范围。
- [x] SUPPORT.md 明确支持边界。
- [x] GitHub Issue 与 PR 模板要求合规说明。
- [x] 投资相关内容包含“不构成投资建议”免责声明。
- [x] 无自动交易、荐股、目标价或收益承诺能力声明。

## 5. 发布检查

- [x] M8 Completion Report 已生成。
- [x] Project Health Report 已生成。
- [x] Final Review 已生成。
- [x] Release Notes 已生成。
- [x] 已知技术债和风险已公开记录。

## 6. 发布结论

若 `scripts/production_check.py` 输出 `FINAL RESULT: PASS`，且本清单无阻断项，AIRS V1.0 可以作为 Production Release 发布。

## 7. 免责声明

本发布清单只证明 AIRS 项目满足定义的工程与治理发布条件，不代表任何投资研究结论有效，不构成投资建议，不提供交易指令或收益承诺。
