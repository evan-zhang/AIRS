# Research Report Generator 流程

**Feature**：FEATURE-003 Research Report Generator  
**版本**：v0.1.0  

**免责声明**：本文档仅用于 AIRS 工程开发、研究质量控制和流程验证，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## 1. 输入准备

Research Agent 先完成研究任务，准备以下输入：

- 研究问题、研究范围和报告标题。
- M2 Methodology 引用，例如 `supply-chain-chokepoint`、`industry-lifecycle`、`counter-consensus`。
- M3 Evidence Cards，必须包含支持命题、反方观点、缺失证据、权重、来源和追溯信息。
- FEATURE-002 Knowledge Graph，必须包含 Evidence 绑定、路径分析和卡点分析。
- M6 Scorecard，必须包含 Overall Score、Confidence Score、Quality Gate 和免责声明。
- M4 Prompt 与 M5 Skill 引用。

## 2. Pipeline 执行

`ReportPipeline.run(payload)` 执行以下步骤：

1. 归一化输入：若 payload 未显式提供 Evidence Cards，则从 Knowledge Graph 的 `evidence_cards` 复制。
2. 校验输入：检查必填字段、免责声明、Evidence 引用、Scorecard 引用和 Quality Gate。
3. Evidence 编排：生成 Evidence 引用表、Evidence Chain 汇总和缺失证据列表。
4. KG 编排：统计节点、关系、路径、Top Chokepoint、卡点驱动和 KG Evidence Refs。
5. Score 编排：汇总 Scorecard ID、维度分、Overall Score、Confidence Score 和 Quality Gate。
6. Section Compose：输出 12 个固定章节。
7. Markdown Render：生成最终 Markdown 研究报告。

## 3. Review Agent 使用方式

Review Agent 按章节检查：

- 核心观点是否引用 Evidence、KG 和 Scorecard。
- Evidence 引用是否能追溯到 Evidence Card。
- KG Summary 是否引用 FEATURE-002 输出，不另造图谱结论。
- Score Summary 是否保留 M6 Quality Gate。
- 反方观点和不确定性是否有实质内容。
- 是否含有免责声明和禁止表达检查。

## 4. Verification Agent 使用方式

Verification Agent 运行：

```bash
python3 scripts/validate_report_generator.py
```

该脚本会检查文档、Schema、模板、Builder Package、Python 实现、两个生产示例、Pipeline 渲染、Evidence/KG/Score 引用完整性和合规表达。通过后再运行 M1-M7、FEATURE-002 和 FEATURE-003 的回归脚本。

## 5. 失败处理

输入缺少 Evidence Card、KG Evidence 引用无法匹配、Scorecard 缺少免责声明、报告缺失核心章节或出现投资建议表达时，Pipeline 或验证脚本必须失败。失败后 Code Agent 需要补齐输入、修复实现或更新示例，并重新运行全量回归。

