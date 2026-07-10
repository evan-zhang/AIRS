# FEATURE-003 Feature Spec - Research Report Generator

## 1. Feature 摘要

生成统一结构的 AIRS 投资研究报告，自动汇总 Methodology、Evidence、Knowledge Graph、Prompt、Skill、Score 和 Evaluation 输出。

## 2. Business Goal

把 M1-M6 和 FEATURE-002 的研究资产组合为可审查、可追溯、可验证且合规的标准研究报告。

## 3. Scope

### In Scope

- docs/report-generator/ 架构、流程和 Pipeline 文档
- report_generator/ Python 核心实现
- schemas/report/ 报告 Schema
- templates/report/ 12 核心章节报告模板
- examples/reports/ 两个生产示例
- scripts/validate_report_generator.py 专项验收脚本

### Out of Scope

- 自动交易或下单执行。
- 个性化投资建议。
- 目标价、收益承诺或确定性价格预测。
- 重写 M2-M7 已有规范。

## 4. User Scenarios

- 研究人员输入研究主题、Evidence Cards、Knowledge Graph 和 Scorecard 后生成标准报告。
- Review Agent 可以按统一章节检查证据引用、反方观点、不确定性和免责声明。
- Verification Agent 可以通过脚本验证报告结构、引用完整性和质量门禁。

## 5. Dependencies

- M1 项目结构与生产治理
- M2 Methodology Layer
- M3 Evidence Engine
- FEATURE-002 Knowledge Graph Engine
- M4 Prompt Engine
- M5 Skill Engine
- M6 Score/Evaluation Engine

## 6. Constraints

- 不得输出荐股、自动交易、交易指令、目标价或收益承诺。
- 所有报告必须包含免责声明。
- 报告核心结论必须引用 Evidence Card、KG Summary 和 Scorecard。
- 必须保留反方观点、缺失证据与不确定性。

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

`MEDIUM`

## 10. Disclaimer

本生成物仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

