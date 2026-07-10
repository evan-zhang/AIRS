# FEATURE-007 Test Plan - AI Research Workspace

## 1. 测试目标

验证 AI Research Workspace 是否按照 Feature Spec 生成或实现，并保持 AIRS M2-M7 引用一致性。

## 2. 测试范围

- docs/workspace/ Workspace 架构与治理文档
- workspace/ 最小可运行 Python Workspace
- workspace/examples/ 五个 Workspace 示例和 Dashboard
- schemas/workspace/ Workspace Schema
- scripts/validate_workspace.py
- ADR-0007-ai-research-workspace.md
- M7_COMPLETION_REPORT.md

## 3. 测试用例

| Case ID | 场景 | 输入 | 期望结果 |
|---------|------|------|----------|
| FEATURE-007-T001 | 正常输入 | 完整 Feature Request | 生成完整 Package |
| FEATURE-007-T002 | 缺失依赖 | 删除一个依赖引用 | 返回失败或标注待补齐 |
| FEATURE-007-T003 | 合规风险 | 输入交易或目标价要求 | 返回 `FAIL_COMPLIANCE` |

## 4. 回归检查

- M1-M8 既有 validate 脚本保持 PASS。
- `scripts/validate_builder.py` 返回 PASS。
- 示例 Package 结构完整。

## 5. 免责声明

本生成物仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

