# Architecture Decision Records（ADR）

**归属 Milestone**：M2 Methodology Core  
**用途**：记录 AIRS 架构、方法论、Schema、Skill、Prompt 和 Benchmark 的重要设计决策。

## 1. ADR 目的

ADR 用于保存“为什么这样设计”的上下文，避免后续 Agent 只看到结果而不了解决策原因。凡是影响跨模块接口、长期维护方式、验证规则或合规边界的设计，都应新增 ADR。

## 2. 适用范围

- 修改 AIRS 分层架构、Agent 协作方式或核心目录结构。
- 新增或改变 Methodology、Schema、Prompt DSL、评分规则或 Benchmark 规则。
- 为了解决一致性问题而修改已通过验收的 M1 顶层文件。
- 引入会影响后续 M3-M8 的技术约束或合规约束。

## 3. 命名规范

ADR 文件使用递增编号和短横线命名：

```text
0001-methodology-layer-contract.md
0002-evidence-card-identity.md
```

编号一经创建不得复用。被替代的 ADR 不删除，应在状态中标注 Superseded，并指向新 ADR。

## 4. ADR 模板

```markdown
# ADR-000X: 决策标题

**状态**：Proposed | Accepted | Superseded | Deprecated  
**日期**：YYYY-MM-DD  
**归属 Milestone**：M[X]  

## Context（背景）
[说明问题、约束和触发原因]

## Decision（决策）
[说明采用的方案]

## Alternatives（备选方案）
[说明被放弃的方案和原因]

## Consequences（影响）
[说明正面影响、负面影响、迁移成本和后续工作]

## Validation（验证）
[说明如何验证该决策被正确执行]
```

## 5. 审查要求

ADR 必须说明决策背景、备选方案和验证方式。若 ADR 涉及投资研究输出，必须明确“不构成投资建议”的合规边界。

