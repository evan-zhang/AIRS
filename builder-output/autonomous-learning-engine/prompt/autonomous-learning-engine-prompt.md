# Autonomous Learning Engine Prompt 草案

**Feature**：FEATURE-012  
**Prompt 模板引用**：`templates/prompt-template.md`  
**Prompt Engine 引用**：`docs/prompt-engine/prompt-architecture.md`、`docs/prompt-engine/prompt-dsl.md`、`docs/prompt-engine/prompt-governance.md`  

## 1. Prompt Purpose

本 Prompt 草案用于支持 Autonomous Learning Engine 的研究流程输入输出约束。它必须遵循 M4 Prompt Engine，并引用 M2 Methodology 与 M3 Evidence Engine。

## 2. System Prompt Draft

你是 AIRS 研究流程中的 Prompt 执行组件。请围绕 Feature `FEATURE-012` 的目标处理输入，必须引用上游方法论和证据链，不得输出投资建议、交易指令、目标价或收益承诺。

## 3. User Template

```text
Feature ID：FEATURE-012
Feature Name：Autonomous Learning Engine
研究问题：建立 AIRS Autonomous Learning Engine，从历史研究、Committee、Memory、Report 与 Outcome 中提取反馈、挖掘模式、生成规则并提出 Prompt、Methodology、Skill 与 Score 优化建议。
业务目标：让 AIRS 在不输出荐股、不自动交易、不预测价格的前提下，形成可审计、可回滚、可评审的研究质量闭环，持续提升证据充分性、反方观点强度、评分校准和报告一致性。
用户场景：[
  "Research Agent 完成报告后，Learning Engine 汇总 Report、Evidence、Score、Committee 与实际 Outcome 的偏差，生成改进建议。",
  "Review Agent 发现证据缺口、逻辑跳跃或反方观点薄弱时，Learning Engine 将问题沉淀为 Pattern 与 Rule Candidate。",
  "Verification Agent 运行 Benchmark 后，Learning Engine 分析失败样本，提出 Prompt、Methodology、Skill 和 Score 权重优化方案。"
]
依赖：[
  "docs/runtime/memory-manager.md",
  "docs/orchestrator/orchestrator-architecture.md",
  "docs/investment-engine/engine-architecture.md",
  "docs/committee/committee-architecture.md",
  "schemas/evidence/evidence-chain.schema.json",
  "schemas/score/scorecard.schema.json",
  "schemas/report/report.schema.json",
  "schemas/committee/committee-decision.schema.json"
]
约束：[
  "Learning Engine 只生成质量改进建议，不直接修改生产 Prompt、Methodology、Skill 或 Score 权重。",
  "所有学习建议必须保留来源、证据、置信度、适用范围、回滚策略和人工评审状态。",
  "所有产物必须包含免责声明，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。"
]
输出要求：[
  "docs/learning/ 11 个 Learning 架构、反馈、Outcome、模式、规则、优化和治理文档",
  "learning/ 12 个 Python 核心组件、README 和 6 个学习示例",
  "schemas/learning/ 4 个 JSON Schema",
  "scripts/validate_learning.py",
  "docs/adr/ADR-012-autonomous-learning-engine.md",
  "docs/production/FEATURE_012_COMPLETION_REPORT.md",
  "docs/review/FEATURE_012_SELF_REVIEW.md"
]
```

## 4. Input Schema

```json
{
  "feature_id": "string",
  "research_question": "string",
  "evidence_cards": "array",
  "methodology_refs": "array",
  "output_requirements": "array"
}
```

## 5. Output Schema

```json
{
  "summary": "string",
  "evidence_chain": {},
  "counter_arguments": [],
  "uncertainties": [],
  "failure_status": "string",
  "disclaimer": "string"
}
```

## 6. Review Checklist

- [ ] 已引用 `templates/prompt-template.md`。
- [ ] 已引用 M4 Prompt Engine。
- [ ] 已引用 M3 Evidence 要求。
- [ ] 输出包含反方观点、不确定性和免责声明。

## 7. 免责声明

本生成物仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

