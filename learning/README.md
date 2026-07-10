# Learning Engine README

`learning/` 是 FEATURE-012 Autonomous Learning Engine 的最小可运行实现。它从 Feedback、Outcome、Committee、Memory、Report、Benchmark 和 Review 中提取质量信号，生成 Pattern、Rule Candidate 和 Optimization Proposal。

## 边界

- Learning Engine 只生成改进建议，不自动修改 Prompt、Methodology、Skill 或 Score。
- 所有建议必须保留来源、证据引用、人工评审状态和回滚计划。
- Memory Consolidation 只保存可审计摘要，不把 Memory 当成证据来源。

## 入口

```python
from learning import ContinuousImprovementEngine

result = ContinuousImprovementEngine().run(payload)
```

输出包含 `feedback`、`outcomes`、`patterns`、`rules`、`optimizations`、`governance` 和 `memory_consolidation`。

## 免责声明

本模块仅用于 AIRS 工程开发、研究质量控制和持续改进，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。
