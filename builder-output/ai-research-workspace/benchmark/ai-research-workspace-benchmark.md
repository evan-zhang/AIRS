# FEATURE-007 Benchmark 草案 - AI Research Workspace

**Benchmark 模板引用**：`templates/benchmark-template.md`  
**Benchmark Engine 引用**：`docs/benchmark/benchmark-architecture.md`、`docs/benchmark/benchmark-lifecycle.md`、`docs/benchmark/benchmark-governance.md`  

## 1. Benchmark Intent

验证 AI Research Workspace 的输出是否符合 Feature Spec、M3 Evidence、M4 Prompt、M6 Score / Evaluation 与 M7 Benchmark 质量要求。

## 2. Input

- 用户通过 Workspace 创建研究项目并启动 Runtime 会话。
- Research Agent 在 Workspace 中登记任务、证据引用、图谱引用和报告产物。
- Review Agent 通过 Timeline、Snapshot、Audit Log 和 Artifact Registry 复核研究过程。
- Verification Agent 使用 Workspace Export 重放关键研究流程并检查合规边界。

## 3. Expected Output

- docs/workspace/ Workspace 架构与治理文档
- workspace/ 最小可运行 Python Workspace
- workspace/examples/ 五个 Workspace 示例和 Dashboard
- schemas/workspace/ Workspace Schema
- scripts/validate_workspace.py
- ADR-0007-ai-research-workspace.md
- M7_COMPLETION_REPORT.md

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

