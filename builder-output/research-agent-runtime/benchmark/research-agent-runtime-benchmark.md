# FEATURE-006 Benchmark 草案 - Research Agent Runtime

**Benchmark 模板引用**：`templates/benchmark-template.md`  
**Benchmark Engine 引用**：`docs/benchmark/benchmark-architecture.md`、`docs/benchmark/benchmark-lifecycle.md`、`docs/benchmark/benchmark-governance.md`  

## 1. Benchmark Intent

验证 Research Agent Runtime 的输出是否符合 Feature Spec、M3 Evidence、M4 Prompt、M6 Score / Evaluation 与 M7 Benchmark 质量要求。

## 2. Input

- Code Agent 可以基于 Runtime Core 开发新的研究执行流。
- Research Agent 可以在 Runtime Session 中执行公司、行业、热点、供应链和报告生成任务。
- Review Agent 可以通过 Event Log、Context Snapshot 和 Final State 复核执行过程。

## 3. Expected Output

- docs/runtime/ Runtime 架构文档
- runtime/ 最小可运行 Python Runtime
- runtime/examples/ 五个 Runtime 示例
- schemas/runtime/ Runtime Schema
- templates/runtime/ Runtime 模板
- scripts/validate_runtime.py
- FEATURE_006_COMPLETION_REPORT.md

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

