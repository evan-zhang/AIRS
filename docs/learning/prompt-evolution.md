# Prompt Evolution

## 1. 目标

Prompt Evolution 根据 Learning Pattern 生成 Prompt 优化建议，重点提升证据引用、反方观点、失败状态和不确定性表达。它不直接改写生产 Prompt，而是输出待评审 Proposal。

## 2. 触发条件

常见触发条件包括 Report 缺少证据引用、Prompt 输出没有区分 Fact 与 Inference、反方观点过弱、风险提示模板化、或 Benchmark 显示某类任务反复失败。

## 3. 优化建议格式

Prompt Proposal 应包含 proposal_id、target、change_type、summary、source_rule、review_status 和 disclaimer。建议必须说明需要新增的输出字段、检查项和失败处理。

## 4. 验证

Prompt 修改必须重新运行 validate_prompt.py、validate_examples.py、validate_report_generator.py 和相关 Feature 验证脚本。未通过回归前不得应用到生产。

## 免责声明

本文档仅用于 AIRS 工程开发、研究质量控制和持续改进，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

