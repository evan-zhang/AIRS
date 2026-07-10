# Learning Architecture

## 1. 定位

Autonomous Learning Engine 位于 Report、Review、Committee、Runtime Memory、Benchmark 和 Production Governance 之后，是 AIRS 的闭环改进层。它不接收用户研究问题，不直接执行投资研究，也不替代 Planner、Research Engine、Evidence、Score 或 Report。它只接收已经产生的研究资产、评审意见和 Outcome 观察，把重复质量问题转化为可审计的改进候选。

## 2. 架构

```
Report / Committee / Memory / Outcome
        ↓
Feedback Collector
        ↓
Outcome Tracker
        ↓
Pattern Miner
        ↓
Rule Generator
        ↓
Prompt / Methodology / Skill / Score Optimizer
        ↓
Review Agent Gate + Memory Consolidation
```

## 3. 输入输出

输入包括 Feedback Record、Outcome Record、Committee Decision、Report Review、Benchmark Result 和 Runtime Memory 摘要。输出包括 Learning Pattern、Rule Candidate、Optimization Proposal、Governance Record 和 Memory Consolidation。

## 4. 边界

Learning Engine 只能生成候选建议。任何 Prompt、Methodology、Skill 或 Score 权重变更必须经过 Review Agent、Verification Agent 和回归脚本。Memory 只作为上下文摘要，不替代 Evidence Chain。

## 免责声明

本文档仅用于 AIRS 工程开发、研究质量控制和持续改进，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

