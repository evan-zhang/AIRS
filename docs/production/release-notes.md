# AIRS V1.0 Release Notes（发布说明）

**版本**：v1.0.0  
**发布日期**：2026-07-10  
**里程碑**：M8 Production Release

## 1. 发布摘要

AIRS V1.0 完成 M1-M8 全部生产交付。从架构基础、方法论、证据、Prompt、Skill、Score、Evaluation、Benchmark 到 Production 治理，项目已经形成可阅读、可审查、可验证的 AI 投资研究 Agent 方法论框架。

## 2. 本次新增

本次 M8 新增：

- 生产指南、部署指南、升级指南、维护指南、治理指南、发布清单、发布说明。
- 生产验收清单、最终质量门禁、回归测试流程。
- 语义化版本规范和 Release Workflow。
- GitHub Issue 模板、PR 模板、CODEOWNERS、SECURITY、SUPPORT。
- Release 验收脚本和生产聚合检查脚本。
- M8 Completion Report、Project Health Report、Final Review。

## 3. 本次完善

本次 M8 完善：

- README：补充 V1.0 Production 状态、功能清单和最终免责声明。
- CONTRIBUTING：补充 V1.0 贡献流程、版本规范和发布流程引用。
- CHANGELOG：新增 v1.0.0 发布记录。
- ROADMAP：标注 M1-M8 全部完成，补充 V1.x / V2 路线。
- LICENSE：确认 MIT License 和免责声明无需修改。

## 4. 质量状态

V1.0 发布要求所有 validate 脚本和生产聚合检查 PASS。最终执行结果记录在 `docs/production/M8_COMPLETION_REPORT.md`。

## 5. 已知限制

- AIRS V1.0 是生产级规范库，不是完整运行时系统。
- 尚未实现真实数据源接入。
- 尚未实现 Prompt 渲染器、Skill 调度器和 Scorecard runner。
- Benchmark 当前是分类种子和生产示例，尚未扩展到 300+ 可执行 case。
- Markdown 到 JSON Schema 的自动转换和深度校验尚未完成。

## 6. 升级建议

V1.x 建议优先补齐运行时、结构化转换器、Benchmark runner 和更多生产示例。V2.0 可进一步建设数据接入、知识图谱、Agent 调度和持续评估平台。

## 7. 免责声明

AIRS V1.0 仅用于投资研究流程增强、质量控制和教育研究，不构成投资建议，不提供荐股、交易指令、目标价或收益承诺。所有投资决策应由使用者独立判断并自行承担风险。
