# FEATURE-009 Benchmark 草案 - Autonomous Research Planner

**Benchmark 模板引用**：`templates/benchmark-template.md`  
**Benchmark Engine 引用**：`docs/benchmark/benchmark-architecture.md`、`docs/benchmark/benchmark-lifecycle.md`、`docs/benchmark/benchmark-governance.md`  

## 1. Benchmark Intent

验证 Autonomous Research Planner 的输出是否符合 Feature Spec、M3 Evidence、M4 Prompt、M6 Score / Evaluation 与 M7 Benchmark 质量要求。

## 2. Input

- Research Agent 接收公司、行业、主题、供应链、卡点、政策、组合或对比研究目标后，Planner 先生成结构化 Research Plan。
- Runtime 只接收 Planner 输出的 Runtime Plan、Workflow Spec 和 Task Graph，不接收原始用户输入。
- Review Agent 和 Verification Agent 根据 Planner 产物复核目标拆解、证据链预期、成本预算、风险和合规边界。

## 3. Expected Output

- docs/planner/ 12 个 Planner 架构与组件文档
- planner/ 12 个 Python 组件和 README
- planner/examples/ 8 个研究目标示例及 Markdown 文档
- schemas/planner/ 4 个 JSON Schema
- templates/planner/ Planner 模板
- scripts/validate_planner.py
- docs/adr/ADR-0009-autonomous-research-planner.md
- docs/production/FEATURE_009_COMPLETION_REPORT.md
- docs/review/FEATURE_009_SELF_REVIEW.md

## 4. Evaluation Criteria

- Evidence 引用完整。
- Prompt 输出结构符合 M4。
- Skill 编排符合 M5。
- 质量门禁引用 M6。
- Benchmark 格式引用 M7。
- 不输出投资建议、交易指令、目标价或收益承诺。

## 5. Failure Cases

- 缺少 Evidence Chain。
- 缺少反方观点。
- 缺少不确定性。
- 缺少免责声明。
- 重复定义 M2-M7 规则而不是引用。

## 6. 免责声明

本生成物仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

