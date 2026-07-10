# FEATURE-012 Benchmark 草案 - Autonomous Learning Engine

**Benchmark 模板引用**：`templates/benchmark-template.md`  
**Benchmark Engine 引用**：`docs/benchmark/benchmark-architecture.md`、`docs/benchmark/benchmark-lifecycle.md`、`docs/benchmark/benchmark-governance.md`  

## 1. Benchmark Intent

验证 Autonomous Learning Engine 的输出是否符合 Feature Spec、M3 Evidence、M4 Prompt、M6 Score / Evaluation 与 M7 Benchmark 质量要求。

## 2. Input

- Research Agent 完成报告后，Learning Engine 汇总 Report、Evidence、Score、Committee 与实际 Outcome 的偏差，生成改进建议。
- Review Agent 发现证据缺口、逻辑跳跃或反方观点薄弱时，Learning Engine 将问题沉淀为 Pattern 与 Rule Candidate。
- Verification Agent 运行 Benchmark 后，Learning Engine 分析失败样本，提出 Prompt、Methodology、Skill 和 Score 权重优化方案。

## 3. Expected Output

- docs/learning/ 11 个 Learning 架构、反馈、Outcome、模式、规则、优化和治理文档
- learning/ 12 个 Python 核心组件、README 和 6 个学习示例
- schemas/learning/ 4 个 JSON Schema
- scripts/validate_learning.py
- docs/adr/ADR-012-autonomous-learning-engine.md
- docs/production/FEATURE_012_COMPLETION_REPORT.md
- docs/review/FEATURE_012_SELF_REVIEW.md

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

