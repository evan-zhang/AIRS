# Data Connector Framework Prompt 草案

**Feature**：FEATURE-004  
**Prompt 模板引用**：`templates/prompt-template.md`  
**Prompt Engine 引用**：`docs/prompt-engine/prompt-architecture.md`、`docs/prompt-engine/prompt-dsl.md`、`docs/prompt-engine/prompt-governance.md`  

## 1. Prompt Purpose

本 Prompt 草案用于支持 Data Connector Framework 的研究流程输入输出约束。它必须遵循 M4 Prompt Engine，并引用 M2 Methodology 与 M3 Evidence Engine。

## 2. System Prompt Draft

你是 AIRS 研究流程中的 Prompt 执行组件。请围绕 Feature `FEATURE-004` 的目标处理输入，必须引用上游方法论和证据链，不得输出投资建议、交易指令、目标价或收益承诺。

## 3. User Template

```text
Feature ID：FEATURE-004
Feature Name：Data Connector Framework
研究问题：建立统一 Data Connector Framework，所有外部数据源必须通过 Connector 接入并输出可追溯结果。
业务目标：为 AIRS Research、Evidence、Knowledge Graph 和 Report 提供统一、可治理、可审计的数据接入边界。
用户场景：[
  "Code Agent 读取 Feature Package 后可以直接开发。",
  "Review Agent 可以按 ADR、Spec、Tests 和 Benchmark 审查。"
]
依赖：[
  "templates/skill-template.md",
  "templates/prompt-template.md",
  "templates/benchmark-template.md",
  "docs/evidence/evidence-card-specification.md"
]
约束：[
  "不得重复定义 M2-M7 规则，只能引用。",
  "所有投资相关内容必须包含免责声明。"
]
输出要求：[
  "ISSUE.md",
  "ADR.md",
  "FEATURE_SPEC.md",
  "Skill 草案",
  "Prompt 草案",
  "Schema 草案",
  "Tests",
  "Benchmark",
  "PR Checklist",
  "Release Notes"
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

