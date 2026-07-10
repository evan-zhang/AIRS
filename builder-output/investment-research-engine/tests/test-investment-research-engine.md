# FEATURE-008 Test Plan - Investment Research Engine

## 1. 测试目标

验证 Investment Research Engine 是否按照 Feature Spec 生成或实现，并保持 AIRS M2-M7 引用一致性。

## 2. 测试范围

- docs/investment-engine/ Engine 架构、管线、创意生成和推荐标准文档
- investment_engine/ 最小可运行 Python 研究引擎
- investment_engine/examples/ 五个研究案例
- schemas/investment/ 投资研究请求、命题和推荐 Schema
- templates/investment/ 报告与命题模板
- scripts/validate_investment_engine.py
- ADR-0008-investment-research-engine.md
- FEATURE_008_COMPLETION_REPORT.md

## 3. 测试用例

| Case ID | 场景 | 输入 | 期望结果 |
|---------|------|------|----------|
| FEATURE-008-T001 | 正常输入 | 完整 Feature Request | 生成完整 Package |
| FEATURE-008-T002 | 缺失依赖 | 删除一个依赖引用 | 返回失败或标注待补齐 |
| FEATURE-008-T003 | 合规风险 | 输入交易或目标价要求 | 返回 `FAIL_COMPLIANCE` |

## 4. 回归检查

- M1-M8 既有 validate 脚本保持 PASS。
- `scripts/validate_builder.py` 返回 PASS。
- 示例 Package 结构完整。

## 5. 免责声明

本生成物仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

