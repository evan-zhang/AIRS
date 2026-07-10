# {{feature_id}} Test Plan - {{feature_name}}

## 1. 测试目标

验证 {{feature_name}} 是否按照 Feature Spec 生成或实现，并保持 AIRS M2-M7 引用一致性。

## 2. 测试范围

{{expected_outputs_markdown}}

## 3. 测试用例

| Case ID | 场景 | 输入 | 期望结果 |
|---------|------|------|----------|
| {{feature_id}}-T001 | 正常输入 | 完整 Feature Request | 生成完整 Package |
| {{feature_id}}-T002 | 缺失依赖 | 删除一个依赖引用 | 返回失败或标注待补齐 |
| {{feature_id}}-T003 | 合规风险 | 输入交易或目标价要求 | 返回 `FAIL_COMPLIANCE` |

## 4. 回归检查

- M1-M8 既有 validate 脚本保持 PASS。
- `scripts/validate_builder.py` 返回 PASS。
- 示例 Package 结构完整。

## 5. 免责声明

{{disclaimer}}

