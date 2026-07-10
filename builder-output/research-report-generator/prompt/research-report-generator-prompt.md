# Research Report Generator Prompt 草案

**Feature**：FEATURE-003  
**Prompt 模板引用**：`templates/prompt-template.md`  
**Prompt Engine 引用**：`docs/prompt-engine/prompt-architecture.md`、`docs/prompt-engine/prompt-dsl.md`、`docs/prompt-engine/prompt-governance.md`  

## 1. Prompt Purpose

本 Prompt 草案用于支持 Research Report Generator 的研究流程输入输出约束。它必须遵循 M4 Prompt Engine，并引用 M2 Methodology 与 M3 Evidence Engine。

## 2. System Prompt Draft

你是 AIRS 研究流程中的 Prompt 执行组件。请围绕 Feature `FEATURE-003` 的目标处理输入，必须引用上游方法论和证据链，不得输出投资建议、交易指令、目标价或收益承诺。

## 3. User Template

```text
Feature ID：FEATURE-003
Feature Name：Research Report Generator
研究问题：生成统一结构的 AIRS 投资研究报告，自动汇总 Methodology、Evidence、Knowledge Graph、Prompt、Skill、Score 和 Evaluation 输出。
业务目标：把 M1-M6 和 FEATURE-002 的研究资产组合为可审查、可追溯、可验证且合规的标准研究报告。
用户场景：[
  "研究人员输入研究主题、Evidence Cards、Knowledge Graph 和 Scorecard 后生成标准报告。",
  "Review Agent 可以按统一章节检查证据引用、反方观点、不确定性和免责声明。",
  "Verification Agent 可以通过脚本验证报告结构、引用完整性和质量门禁。"
]
依赖：[
  "M1 项目结构与生产治理",
  "M2 Methodology Layer",
  "M3 Evidence Engine",
  "FEATURE-002 Knowledge Graph Engine",
  "M4 Prompt Engine",
  "M5 Skill Engine",
  "M6 Score/Evaluation Engine"
]
约束：[
  "不得输出荐股、自动交易、交易指令、目标价或收益承诺。",
  "所有报告必须包含免责声明。",
  "报告核心结论必须引用 Evidence Card、KG Summary 和 Scorecard。",
  "必须保留反方观点、缺失证据与不确定性。"
]
输出要求：[
  "docs/report-generator/ 架构、流程和 Pipeline 文档",
  "report_generator/ Python 核心实现",
  "schemas/report/ 报告 Schema",
  "templates/report/ 12 核心章节报告模板",
  "examples/reports/ 两个生产示例",
  "scripts/validate_report_generator.py 专项验收脚本"
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

