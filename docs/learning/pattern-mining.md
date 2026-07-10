# Pattern Mining

## 1. 目标

Pattern Mining 从反馈和 Outcome 中识别重复出现的研究质量问题，例如 evidence_gap、weak_counter_argument、scope_drift、decision_record_gap、source_traceability_gap 和 outcome_variance。

## 2. 方法

Pattern Miner 按 target_module 与 issue_type 聚合反馈，统计频次、严重度组合、证据引用和置信度。它关注重复质量信号，而不是研究结论本身。一个 Pattern 必须能够回溯到 Feedback Record 或 Outcome Record。

## 3. 输出

Pattern 输出包括 pattern_id、pattern_type、target_module、description、frequency、severity_mix、evidence_refs、confidence 和 disclaimer。置信度只是治理优先级，不代表投资确定性。

## 4. 与其他模块关系

Pattern Miner 引用 Evidence、Score、Committee、Report 和 Runtime Memory 的结果，但不重新定义这些模块。它的结果交给 Rule Generator 生成候选规则，再由 Review Agent 决定是否采纳。

## 免责声明

本文档仅用于 AIRS 工程开发、研究质量控制和持续改进，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

