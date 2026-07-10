# AIRS Final Quality Gate（最终质量门禁）

**版本**：v1.0.0  
**适用范围**：AIRS V1.0 发布前最终门禁

## 1. 门禁目标

Final Quality Gate 用于判断 AIRS 是否可以进入 Production Release。门禁关注工程完整性、内容一致性、合规边界、验证结果和治理记录。

## 2. PASS 标准

必须同时满足：

1. `scripts/production_check.py` 输出 `FINAL RESULT: PASS`。
2. `scripts/validate_release.py` 输出 `RESULT: PASS`。
3. M1-M7 既有验证脚本全部 PASS。
4. README、ROADMAP、CONTRIBUTING、CHANGELOG 状态一致。
5. `.github/` 治理文件完整。
6. M8 最终报告存在且有实质内容。
7. 所有投资相关 M8 文档包含免责声明。

## 3. CONDITIONAL_PASS 标准

V1.0 最终发布不接受 CONDITIONAL_PASS。若存在非阻断技术债，应在 FINAL_REVIEW 中记录，但自检与发布门禁仍必须 PASS。

## 4. FAIL 标准

出现任一情况即 FAIL：

- 任一 validate 脚本失败。
- 缺少 M8 生产文档、治理文档、GitHub 文件或最终报告。
- 顶层文件状态互相矛盾。
- 出现荐股、自动交易、目标价或收益承诺表达。
- FINAL_REVIEW 隐瞒已知技术债或风险。
- 修改核心文件但未记录 CHANGELOG 或 ADR。

## 5. 门禁执行人

- Code Agent：修复文件和脚本问题。
- Review Agent：检查内容质量和合规边界。
- Verification Agent：执行脚本并记录结果。
- Release Manager：确认发布结论。

## 6. 门禁输出

门禁输出应包含：

- 执行时间。
- 执行命令。
- PASS / FAIL 结果。
- 失败项列表。
- 修复建议。
- 发布结论。

## 7. 免责声明

Final Quality Gate 只验证 AIRS 项目生产交付质量，不验证任何具体投资结论，不构成投资建议，不提供交易指令或收益承诺。
