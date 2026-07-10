# FEATURE-003 Test Plan - Research Report Generator

## 1. 测试目标

验证 Research Report Generator 是否按照 Feature Spec 生成或实现，并保持 AIRS M2-M7 引用一致性。

## 2. 测试范围

- docs/report-generator/ 架构、流程和 Pipeline 文档
- report_generator/ Python 核心实现
- schemas/report/ 报告 Schema
- templates/report/ 12 核心章节报告模板
- examples/reports/ 两个生产示例
- scripts/validate_report_generator.py 专项验收脚本

## 3. 测试用例

| Case ID | 场景 | 输入 | 期望结果 |
|---------|------|------|----------|
| FEATURE-003-T001 | 正常输入 | 完整 Feature Request | 生成完整 Package |
| FEATURE-003-T002 | 缺失依赖 | 删除一个依赖引用 | 返回失败或标注待补齐 |
| FEATURE-003-T003 | 合规风险 | 输入交易或目标价要求 | 返回 `FAIL_COMPLIANCE` |

## 4. 回归检查

- M1-M8 既有 validate 脚本保持 PASS。
- `scripts/validate_builder.py` 返回 PASS。
- 示例 Package 结构完整。

## 5. 免责声明

本生成物仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

