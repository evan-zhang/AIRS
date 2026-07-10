# FEATURE-009 Test Plan - Autonomous Research Planner

## 1. 测试目标

验证 Autonomous Research Planner 是否按照 Feature Spec 生成或实现，并保持 AIRS M2-M7 引用一致性。

## 2. 测试范围

- docs/planner/ 12 个 Planner 架构与组件文档
- planner/ 12 个 Python 组件和 README
- planner/examples/ 8 个研究目标示例及 Markdown 文档
- schemas/planner/ 4 个 JSON Schema
- templates/planner/ Planner 模板
- scripts/validate_planner.py
- docs/adr/ADR-0009-autonomous-research-planner.md
- docs/production/FEATURE_009_COMPLETION_REPORT.md
- docs/review/FEATURE_009_SELF_REVIEW.md

## 3. 测试用例

| Case ID | 场景 | 输入 | 期望结果 |
|---------|------|------|----------|
| FEATURE-009-T001 | 正常输入 | 完整 Feature Request | 生成完整 Package |
| FEATURE-009-T002 | 缺失依赖 | 删除一个依赖引用 | 返回失败或标注待补齐 |
| FEATURE-009-T003 | 合规风险 | 输入交易或目标价要求 | 返回 `FAIL_COMPLIANCE` |

## 4. 回归检查

- M1-M8 既有 validate 脚本保持 PASS。
- `scripts/validate_builder.py` 返回 PASS。
- 示例 Package 结构完整。

## 5. 免责声明

本生成物仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

