# Committee Architecture

免责声明：本文档仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## 定位

Autonomous Investment Committee（AIC）位于 Autonomous Research Planner 之后、Investment Research Engine 之前。Planner 生成 Research Plan、范围、预算、Runtime Plan 和证据预期；AIC 对这些计划进行多角色审议；Research Engine 只执行 AIC 通过或有条件通过的研究任务。

## 架构流

```
User Intent -> Planner -> AIC -> Research Engine -> Runtime / Evidence / KG / Score / Report
```

AIC 不重新定义 M2 方法论、M3 证据、M6 评分、FEATURE-002 图谱、FEATURE-006 Runtime 或 FEATURE-008 Engine。它只读取这些模块的引用，并产生 Committee Session、Vote、Consensus、Decision Record、Minority Report 和 Follow-up Tasks。

## 关键对象

- Committee Session：一次审议的完整上下文。
- Participants：Bull、Bear、Financial、Industry、Risk、Portfolio、Evidence Reviewer、Devil's Advocate、Moderator。
- Debate Timeline：按议程记录发言、质询和复核。
- Voting Result：结构化表决结果。
- Decision Record：Research Engine Gate 结果与后续任务。

## 质量边界

任何结论必须区分事实、推断、假设和观点。AIC 可以允许后续研究、要求补证、降级置信度或阻断执行，但不得输出个性化投资建议、自动交易动作、目标价或收益承诺。
