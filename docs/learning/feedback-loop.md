# Feedback Loop

## 1. 目标

Feedback Loop 把研究过程中的质量信号转化为可重复处理的数据。信号来源包括 Review Agent 的评审意见、Committee 的质询记录、Verification Agent 的 Benchmark 失败项、Report 中的证据缺口、Runtime Memory 的可审计摘要和 Outcome Tracker 的后验观察。

## 2. 流程

1. 收集 Feedback Record，记录 source_type、source_ref、target_module、issue_type、severity 和 evidence_refs。
2. 对反馈做去重和归类，避免同一问题在 Report、Committee 和 Benchmark 中重复计数。
3. 交给 Pattern Miner 识别重复出现的质量缺陷。
4. 交给 Rule Generator 生成候选规则。
5. 交给 Optimizer 生成 Prompt、Methodology、Skill 或 Score 的改进建议。

## 3. 治理要求

每条反馈必须有来源引用。没有来源的反馈只能进入待补证状态，不能生成规则候选。高严重度反馈必须进入 Review Agent Gate，低严重度反馈可以先进入观察队列。

## 免责声明

本文档仅用于 AIRS 工程开发、研究质量控制和持续改进，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

