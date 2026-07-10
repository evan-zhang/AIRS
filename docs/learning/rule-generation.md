# Rule Generation

## 1. 目标

Rule Generation 把 Pattern 转化为可评审的 Rule Candidate。Rule Candidate 是改进建议，不是生产规则。它必须包含来源模式、适用模块、规则文本、理由、证据引用、人工评审要求和回滚计划。

## 2. 规则类型

- Prompt Guardrail：要求 Prompt 输出包含证据、反方观点和不确定性。
- Methodology Step：要求方法论补充适用边界、失败场景和证据最低标准。
- Skill Workflow Gate：要求 Skill 在执行中增加输入校验、证据检查和失败处理。
- Score Calibration：要求评分对低证据置信度、Outcome 偏差和缺失反方证据进行惩罚。

## 3. 审批

所有 Rule Candidate 默认状态为 candidate，必须经过 Review Agent 和 Verification Agent。只有回归测试通过且人工确认后，才能进入生产规则库。

## 免责声明

本文档仅用于 AIRS 工程开发、研究质量控制和持续改进，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

