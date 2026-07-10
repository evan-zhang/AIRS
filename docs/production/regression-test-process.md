# AIRS Regression Test Process（回归测试流程）

**版本**：v1.0.0  
**适用范围**：AIRS V1.0 及后续 V1.x 维护

## 1. 回归目标

回归测试用于确保新增或修改内容不会破坏 M1-M8 已验收能力。AIRS 的回归测试以脚本验证、文档引用检查、合规关键词检查和生产清单检查为主。

## 2. 测试用例选择策略

每次变更至少选择：

- 相关里程碑 validate 脚本。
- 所有上游依赖里程碑 validate 脚本。
- `scripts/validate_release.py`。
- `scripts/production_check.py`。

示例：

- 修改 Prompt：运行 validate_m1、validate_m2、validate_evidence、validate_prompt、validate_release、production_check。
- 修改 Skill：运行 validate_m1 至 validate_skill、validate_release、production_check。
- 修改 Benchmark：运行 validate_benchmark、validate_examples、validate_release、production_check。
- 修改顶层文件：运行 validate_m1、validate_release、production_check，并更新 CHANGELOG 与 ADR。

## 3. 回归执行流程

1. 确认变更范围。
2. 运行最小相关脚本。
3. 若通过，运行完整生产检查。
4. 若失败，修复最小范围。
5. 重新运行失败脚本和生产检查。
6. 记录命令、结果、失败项和修复项。

## 4. 回归报告格式

回归报告至少包含：

```markdown
# 回归测试报告

## 变更范围
[说明变更文件和影响模块]

## 执行命令
[列出命令]

## 结果摘要
PASS / FAIL

## 失败项
[如无失败，写“无”]

## 修复记录
[说明修复内容]

## 剩余风险
[说明未覆盖风险]
```

## 5. 回归阻断项

以下问题必须阻断发布：

- 投资相关内容缺少免责声明。
- 出现交易建议、自动交易、目标价或收益承诺。
- JSON Schema 无法解析。
- 核心引用文件缺失。
- `production_check.py` 失败。

## 6. 免责声明

回归测试只能证明 AIRS 工程交付满足既定质量规则，不能证明任何投资结论正确，不构成投资建议，不提供交易指令或收益承诺。
