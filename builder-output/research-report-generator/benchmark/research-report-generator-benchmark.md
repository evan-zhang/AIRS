# FEATURE-003 Benchmark 草案 - Research Report Generator

**Benchmark 模板引用**：`templates/benchmark-template.md`  
**Benchmark Engine 引用**：`docs/benchmark/benchmark-architecture.md`、`docs/benchmark/benchmark-lifecycle.md`、`docs/benchmark/benchmark-governance.md`  

## 1. Benchmark Intent

验证 Research Report Generator 的输出是否符合 Feature Spec、M3 Evidence、M4 Prompt、M6 Score / Evaluation 与 M7 Benchmark 质量要求。

## 2. Input

- 研究人员输入研究主题、Evidence Cards、Knowledge Graph 和 Scorecard 后生成标准报告。
- Review Agent 可以按统一章节检查证据引用、反方观点、不确定性和免责声明。
- Verification Agent 可以通过脚本验证报告结构、引用完整性和质量门禁。

## 3. Expected Output

- docs/report-generator/ 架构、流程和 Pipeline 文档
- report_generator/ Python 核心实现
- schemas/report/ 报告 Schema
- templates/report/ 12 核心章节报告模板
- examples/reports/ 两个生产示例
- scripts/validate_report_generator.py 专项验收脚本

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

