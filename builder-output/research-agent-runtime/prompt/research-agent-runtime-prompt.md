# Research Agent Runtime Prompt 草案

**Feature**：FEATURE-006  
**Prompt 模板引用**：`templates/prompt-template.md`  
**Prompt Engine 引用**：`docs/prompt-engine/prompt-architecture.md`、`docs/prompt-engine/prompt-dsl.md`、`docs/prompt-engine/prompt-governance.md`  

## 1. Prompt Purpose

本 Prompt 草案用于支持 Research Agent Runtime 的研究流程输入输出约束。它必须遵循 M4 Prompt Engine，并引用 M2 Methodology 与 M3 Evidence Engine。

## 2. System Prompt Draft

你是 AIRS 研究流程中的 Prompt 执行组件。请围绕 Feature `FEATURE-006` 的目标处理输入，必须引用上游方法论和证据链，不得输出投资建议、交易指令、目标价或收益承诺。

## 3. User Template

```text
Feature ID：FEATURE-006
Feature Name：Research Agent Runtime
研究问题：建立统一 Agent Runtime，将 Orchestrator 的流程编排升级为可运行的多 Agent 执行框架。
业务目标：让 AIRS Workflow 由 Runtime 统一调度，形成可追踪、可暂停、可恢复、可验证的多 Agent 研究执行底座。
用户场景：[
  "Code Agent 可以基于 Runtime Core 开发新的研究执行流。",
  "Research Agent 可以在 Runtime Session 中执行公司、行业、热点、供应链和报告生成任务。",
  "Review Agent 可以通过 Event Log、Context Snapshot 和 Final State 复核执行过程。"
]
依赖：[
  "docs/skill-engine/skill-architecture.md",
  "docs/methodology/DSL.md",
  "docs/evidence/evidence-architecture.md",
  "schemas/README.md"
]
约束：[
  "Workflow 必须由 Runtime 调度执行，不允许 Workflow 直接驱动业务模块。",
  "Runtime 只编排 Agent、Session、Task、Message、Event 和 State，不重复定义 M2-M7 规则。",
  "所有投资相关内容必须包含免责声明。"
]
输出要求：[
  "docs/runtime/ Runtime 架构文档",
  "runtime/ 最小可运行 Python Runtime",
  "runtime/examples/ 五个 Runtime 示例",
  "schemas/runtime/ Runtime Schema",
  "templates/runtime/ Runtime 模板",
  "scripts/validate_runtime.py",
  "FEATURE_006_COMPLETION_REPORT.md"
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

