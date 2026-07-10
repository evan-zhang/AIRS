# FEATURE-004 Feature Spec - Data Connector Framework

## 1. Feature 摘要

建立统一 Data Connector Framework，所有外部数据源必须通过 Connector 接入并输出可追溯结果。

## 2. Business Goal

为 AIRS Research、Evidence、Knowledge Graph 和 Report 提供统一、可治理、可审计的数据接入边界。

## 3. Scope

### In Scope

- ISSUE.md
- ADR.md
- FEATURE_SPEC.md
- Skill 草案
- Prompt 草案
- Schema 草案
- Tests
- Benchmark
- PR Checklist
- Release Notes

### Out of Scope

- 自动交易或下单执行。
- 个性化投资建议。
- 目标价、收益承诺或确定性价格预测。
- 重写 M2-M7 已有规范。

## 4. User Scenarios

- Code Agent 读取 Feature Package 后可以直接开发。
- Review Agent 可以按 ADR、Spec、Tests 和 Benchmark 审查。

## 5. Dependencies

- templates/skill-template.md
- templates/prompt-template.md
- templates/benchmark-template.md
- docs/evidence/evidence-card-specification.md

## 6. Constraints

- 不得重复定义 M2-M7 规则，只能引用。
- 所有投资相关内容必须包含免责声明。

## 7. Functional Requirements

- 生成物必须可被 Code Agent 读取和执行。
- Schema 必须是合法 JSON Schema。
- Tests 必须描述可复现的验收步骤。
- Benchmark 必须引用 M7 Benchmark 模板和 M6 质量门禁。
- Skill、Prompt、Benchmark 必须引用 AIRS 既有层，不复制底层规则。

## 8. Acceptance Criteria

- `python3 scripts/validate_builder.py` 返回 PASS。
- 回归验证脚本保持 PASS。
- Release Notes 记录 Feature 影响和限制。
- 所有生成物包含免责声明。

## 9. Risk Level

`HIGH`

## 10. Disclaimer

本生成物仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

