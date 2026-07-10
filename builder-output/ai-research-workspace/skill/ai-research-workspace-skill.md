# AI Research Workspace Skill 草案

**Feature**：FEATURE-007  
**Skill 模板引用**：`templates/skill-template.md`  
**Skill Engine 引用**：`docs/skill-engine/skill-architecture.md`、`docs/skill-engine/skill-invocation.md`、`docs/skill-engine/skill-governance.md`  

## 1. Purpose

本 Skill 草案用于实现 AI Research Workspace 的开发入口。它必须遵循 M5 Skill Engine，并引用既有 M2 Methodology、M3 Evidence、M4 Prompt 和 M6/M7 质量资产。

## 2. Inputs

- `feature_request`：结构化 Feature 请求。
- `research_context`：可选研究上下文。
- `evidence_refs`：M3 Evidence Card / Evidence Chain 引用。
- `constraints`：[
  "Workspace 是统一入口，但不绕过 Runtime 调度 Agent。",
  "Workspace 只保存引用、状态、产物、快照和审计记录，不生成投资建议。",
  "所有投资研究相关内容必须包含免责声明。"
]

## 3. Outputs

- docs/workspace/ Workspace 架构与治理文档
- workspace/ 最小可运行 Python Workspace
- workspace/examples/ 五个 Workspace 示例和 Dashboard
- schemas/workspace/ Workspace Schema
- scripts/validate_workspace.py
- ADR-0007-ai-research-workspace.md
- M7_COMPLETION_REPORT.md

## 4. Dependencies

- docs/runtime/runtime-architecture.md
- runtime/core.py
- schemas/runtime/runtime.schema.json
- schemas/evidence/evidence-card.schema.json
- schemas/knowledge-graph/knowledge-graph.schema.json
- templates/report/research-report-template.md

## 5. Workflow

1. 校验输入范围与合规边界。
2. 选择或确认上游 Methodology、Evidence 与 Prompt 引用。
3. 调用 M4 Prompt 草案，不内置 Prompt 正文。
4. 绑定 M3 Evidence Card / Evidence Chain。
5. 输出结构化结果、缺失证据、反方观点、不确定性和免责声明。

## 6. Failure Handling

- `FAIL_INPUT_INCOMPLETE`：Feature 或研究上下文字段不足。
- `FAIL_DEPENDENCY_MISSING`：声明依赖不存在或未被验证。
- `FAIL_EVIDENCE_INSUFFICIENT`：证据不足或不可追溯。
- `FAIL_COMPLIANCE`：请求触及荐股、交易指令、目标价或收益承诺。

## 7. Review Checklist

- [ ] 已引用 `templates/skill-template.md`。
- [ ] 已引用 M5 Skill Engine。
- [ ] 未重复定义 M2-M7 规则。
- [ ] 包含反方观点、不确定性和免责声明要求。

## 8. 免责声明

本生成物仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

