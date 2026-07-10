# AI Research Workspace Prompt 草案

**Feature**：FEATURE-007  
**Prompt 模板引用**：`templates/prompt-template.md`  
**Prompt Engine 引用**：`docs/prompt-engine/prompt-architecture.md`、`docs/prompt-engine/prompt-dsl.md`、`docs/prompt-engine/prompt-governance.md`  

## 1. Prompt Purpose

本 Prompt 草案用于支持 AI Research Workspace 的研究流程输入输出约束。它必须遵循 M4 Prompt Engine，并引用 M2 Methodology 与 M3 Evidence Engine。

## 2. System Prompt Draft

你是 AIRS 研究流程中的 Prompt 执行组件。请围绕 Feature `FEATURE-007` 的目标处理输入，必须引用上游方法论和证据链，不得输出投资建议、交易指令、目标价或收益承诺。

## 3. User Template

```text
Feature ID：FEATURE-007
Feature Name：AI Research Workspace
研究问题：建立统一 Research Workspace，作为 Runtime、Workflow、Agent、Evidence、Knowledge Graph、Report 和用户交互的唯一入口。
业务目标：让 AIRS 的研究过程以项目、会话、任务、证据、产物、快照和审计记录统一管理，提升可追踪、可复核和可恢复能力。
用户场景：[
  "用户通过 Workspace 创建研究项目并启动 Runtime 会话。",
  "Research Agent 在 Workspace 中登记任务、证据引用、图谱引用和报告产物。",
  "Review Agent 通过 Timeline、Snapshot、Audit Log 和 Artifact Registry 复核研究过程。",
  "Verification Agent 使用 Workspace Export 重放关键研究流程并检查合规边界。"
]
依赖：[
  "docs/runtime/runtime-architecture.md",
  "runtime/core.py",
  "schemas/runtime/runtime.schema.json",
  "schemas/evidence/evidence-card.schema.json",
  "schemas/knowledge-graph/knowledge-graph.schema.json",
  "templates/report/research-report-template.md"
]
约束：[
  "Workspace 是统一入口，但不绕过 Runtime 调度 Agent。",
  "Workspace 只保存引用、状态、产物、快照和审计记录，不生成投资建议。",
  "所有投资研究相关内容必须包含免责声明。"
]
输出要求：[
  "docs/workspace/ Workspace 架构与治理文档",
  "workspace/ 最小可运行 Python Workspace",
  "workspace/examples/ 五个 Workspace 示例和 Dashboard",
  "schemas/workspace/ Workspace Schema",
  "scripts/validate_workspace.py",
  "ADR-0007-ai-research-workspace.md",
  "M7_COMPLETION_REPORT.md"
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

