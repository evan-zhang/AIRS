# FEATURE-010 Benchmark 草案 - Autonomous Investment Committee

**Benchmark 模板引用**：`templates/benchmark-template.md`  
**Benchmark Engine 引用**：`docs/benchmark/benchmark-architecture.md`、`docs/benchmark/benchmark-lifecycle.md`、`docs/benchmark/benchmark-governance.md`  

## 1. Benchmark Intent

验证 Autonomous Investment Committee 的输出是否符合 Feature Spec、M3 Evidence、M4 Prompt、M6 Score / Evaluation 与 M7 Benchmark 质量要求。

## 2. Input

- Planner 生成 Research Plan 后，AIC 先审查研究范围、方法论、证据预期和风险预算，再决定是否允许进入 Research Engine。
- Research Agent 产生阶段性结论时，AIC 组织 Bull、Bear、Financial、Industry、Risk、Portfolio、Evidence Reviewer 和 Devil's Advocate 交叉质询。
- Review Agent 和 Verification Agent 根据 AIC 的 Vote、Minority Report 和 Decision Record 复核质量门禁。

## 3. Expected Output

- docs/committee/ 12 个 Committee 架构与治理文档
- committee/ 11 个 Python 核心组件和 README
- committee/examples/ 6 个生产级 Committee 示例
- schemas/committee/ 4 个 JSON Schema
- templates/committee/ Committee 模板
- scripts/validate_committee.py
- docs/adr/ADR-0010-autonomous-investment-committee.md
- docs/production/M10_COMPLETION_REPORT.md
- docs/review/M10_SELF_REVIEW.md

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

