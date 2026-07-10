# Investment Research Engine Prompt 草案

**Feature**：FEATURE-008  
**Prompt 模板引用**：`templates/prompt-template.md`  
**Prompt Engine 引用**：`docs/prompt-engine/prompt-architecture.md`、`docs/prompt-engine/prompt-dsl.md`、`docs/prompt-engine/prompt-governance.md`  

## 1. Prompt Purpose

本 Prompt 草案用于支持 Investment Research Engine 的研究流程输入输出约束。它必须遵循 M4 Prompt Engine，并引用 M2 Methodology 与 M3 Evidence Engine。

## 2. System Prompt Draft

你是 AIRS 研究流程中的 Prompt 执行组件。请围绕 Feature `FEATURE-008` 的目标处理输入，必须引用上游方法论和证据链，不得输出投资建议、交易指令、目标价或收益承诺。

## 3. User Template

```text
Feature ID：FEATURE-008
Feature Name：Investment Research Engine
研究问题：构建统一 Investment Research Engine，调度 Runtime、Skill、Prompt、Evidence、Knowledge Graph、Score、Report 和 Workspace，形成可执行投资研究全流程。
业务目标：把 M1-M7 与 M8 基础设施串联成可复核、可验证、可审计的研究引擎，支持主题、公司、行业、供应链、风险、催化剂和报告生成。
用户场景：[
  "Research Agent 接收研究意图后，由 Engine 统一生成研究计划、证据链、图谱、评分卡和报告。",
  "Review Agent 使用 Facts、Inference、Assumption、Opinion 标注检查研究结论来源类型。",
  "Verification Agent 运行 Engine 示例和自检脚本，确认不输出确定性投资建议或收益承诺。"
]
依赖：[
  "docs/runtime/runtime-architecture.md",
  "docs/orchestrator/",
  "docs/workspace/workspace-architecture.md",
  "docs/data-connectors/connector-interface.md",
  "docs/methodology/",
  "docs/evidence/",
  "docs/prompt-engine/",
  "schemas/evidence/evidence-card.schema.json",
  "schemas/knowledge-graph/knowledge-graph.schema.json",
  "schemas/score/scorecard.schema.json",
  "templates/report/research-report-template.md"
]
约束：[
  "Engine 只编排既有底层服务，不绕过 Runtime、Workspace 或 Evidence 规则。",
  "Recommendation 必须区分 Facts、Inference、Assumption 和 Opinion。",
  "不得输出确定性投资建议、交易指令、目标价或收益承诺。"
]
输出要求：[
  "docs/investment-engine/ Engine 架构、管线、创意生成和推荐标准文档",
  "investment_engine/ 最小可运行 Python 研究引擎",
  "investment_engine/examples/ 五个研究案例",
  "schemas/investment/ 投资研究请求、命题和推荐 Schema",
  "templates/investment/ 报告与命题模板",
  "scripts/validate_investment_engine.py",
  "ADR-0008-investment-research-engine.md",
  "FEATURE_008_COMPLETION_REPORT.md"
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

