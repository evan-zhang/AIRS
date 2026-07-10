# Autonomous Research Planner Prompt 草案

**Feature**：FEATURE-009  
**Prompt 模板引用**：`templates/prompt-template.md`  
**Prompt Engine 引用**：`docs/prompt-engine/prompt-architecture.md`、`docs/prompt-engine/prompt-dsl.md`、`docs/prompt-engine/prompt-governance.md`  

## 1. Prompt Purpose

本 Prompt 草案用于支持 Autonomous Research Planner 的研究流程输入输出约束。它必须遵循 M4 Prompt Engine，并引用 M2 Methodology 与 M3 Evidence Engine。

## 2. System Prompt Draft

你是 AIRS 研究流程中的 Prompt 执行组件。请围绕 Feature `FEATURE-009` 的目标处理输入，必须引用上游方法论和证据链，不得输出投资建议、交易指令、目标价或收益承诺。

## 3. User Template

```text
Feature ID：FEATURE-009
Feature Name：Autonomous Research Planner
研究问题：建立 AIRS 最上层 Autonomous Research Planner，把用户研究目标拆解为可执行 Research Plan，并生成 Runtime、Workflow、Methodology、Connector、Skill、KG、Evidence、Score、Report 的完整执行链路。
业务目标：确保任何 Runtime 都不能直接接收用户请求，必须先经过 Planner 完成目标解析、范围约束、依赖规划、资源预算、置信度评估和执行计划生成。
用户场景：[
  "Research Agent 接收公司、行业、主题、供应链、卡点、政策、组合或对比研究目标后，Planner 先生成结构化 Research Plan。",
  "Runtime 只接收 Planner 输出的 Runtime Plan、Workflow Spec 和 Task Graph，不接收原始用户输入。",
  "Review Agent 和 Verification Agent 根据 Planner 产物复核目标拆解、证据链预期、成本预算、风险和合规边界。"
]
依赖：[
  "docs/orchestrator/orchestrator-architecture.md",
  "docs/runtime/runtime-architecture.md",
  "docs/investment-engine/engine-architecture.md",
  "schemas/runtime/runtime.schema.json",
  "schemas/investment/investment-request.schema.json",
  "schemas/evidence/evidence-chain.schema.json",
  "schemas/knowledge-graph/knowledge-graph.schema.json",
  "schemas/score/scorecard.schema.json",
  "templates/report/research-report-template.md"
]
约束：[
  "Planner 是 AIRS 最上层入口，Runtime 不允许直接接收用户请求。",
  "Planner 只生成研究计划和执行链路，不执行外部数据采集，不生成荐股、交易指令、目标价或收益承诺。",
  "所有计划必须保留 Evidence、KG、Score、Report、Review 和 Verification 引用。"
]
输出要求：[
  "docs/planner/ 12 个 Planner 架构与组件文档",
  "planner/ 12 个 Python 组件和 README",
  "planner/examples/ 8 个研究目标示例及 Markdown 文档",
  "schemas/planner/ 4 个 JSON Schema",
  "templates/planner/ Planner 模板",
  "scripts/validate_planner.py",
  "docs/adr/ADR-0009-autonomous-research-planner.md",
  "docs/production/FEATURE_009_COMPLETION_REPORT.md",
  "docs/review/FEATURE_009_SELF_REVIEW.md"
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

