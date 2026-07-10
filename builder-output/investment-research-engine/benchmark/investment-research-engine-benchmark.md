# FEATURE-008 Benchmark 草案 - Investment Research Engine

**Benchmark 模板引用**：`templates/benchmark-template.md`  
**Benchmark Engine 引用**：`docs/benchmark/benchmark-architecture.md`、`docs/benchmark/benchmark-lifecycle.md`、`docs/benchmark/benchmark-governance.md`  

## 1. Benchmark Intent

验证 Investment Research Engine 的输出是否符合 Feature Spec、M3 Evidence、M4 Prompt、M6 Score / Evaluation 与 M7 Benchmark 质量要求。

## 2. Input

- Research Agent 接收研究意图后，由 Engine 统一生成研究计划、证据链、图谱、评分卡和报告。
- Review Agent 使用 Facts、Inference、Assumption、Opinion 标注检查研究结论来源类型。
- Verification Agent 运行 Engine 示例和自检脚本，确认不输出确定性投资建议或收益承诺。

## 3. Expected Output

- docs/investment-engine/ Engine 架构、管线、创意生成和推荐标准文档
- investment_engine/ 最小可运行 Python 研究引擎
- investment_engine/examples/ 五个研究案例
- schemas/investment/ 投资研究请求、命题和推荐 Schema
- templates/investment/ 报告与命题模板
- scripts/validate_investment_engine.py
- ADR-0008-investment-research-engine.md
- FEATURE_008_COMPLETION_REPORT.md

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

