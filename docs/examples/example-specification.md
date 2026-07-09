# Example Specification（示例规范）

**归属 Milestone**：M7: Benchmark & Production Examples  
**版本**：v0.7.0  
**最后更新**：2026-07-10

**免责声明**：本文档仅定义 AIRS 生产示例格式，不构成投资建议，不提供交易指令、价格预测或收益承诺。

## 1. 目标

生产示例用于展示 AIRS 从研究意图到报告输出的端到端形态。示例不是投资建议，也不是实时研究结论，而是用于验证 M4 Prompt 格式、M3 Evidence Card、M6 Scorecard 和 M6 Evaluation Gate 是否能在同一产物中协同工作。

## 2. 示例类型

M7 建立六个生产级示例：

- Supply Chain Report 示例。
- Theme Expansion Report 示例。
- Evidence Report 示例。
- Valuation Report 示例。
- Risk Report 示例。
- Complete Investment Research Report 示例。

## 3. 必需结构

每个示例必须包含：

1. 示例元数据：示例 ID、标题、版本、方法论引用、Prompt 引用、Scorecard 引用。
2. M4 Prompt 输入：研究问题、研究范围、数据源约束、输出格式要求。
3. M3 Evidence Card：至少 2 张证据卡，包含 Evidence ID、Evidence Level、Confidence、Weight、supports、refutes、missing_evidence。
4. Evidence Chain：说明证据如何支持或削弱命题。
5. M6 Scorecard：包含多个 Score 维度、综合评分、Confidence Score 和 Quality Gate。
6. 报告正文：核心观点、研究方法、证据链、评分、反方观点、不确定性、风险提示。
7. 免责声明：必须包含“不构成投资建议”。

## 4. Prompt 格式要求

示例中的 Prompt 输入应引用 M4 Prompt 文档，保留：

- `prompt_id`
- `methodology_refs`
- `evidence_refs`
- `input_schema`
- `output_schema`
- `failure_cases`
- `disclaimer`

若示例不是完整 Prompt JSON，也必须以 Markdown 方式保留这些字段。

## 5. Evidence Card 要求

示例不得只写“有证据显示”。必须使用证据卡结构：

```markdown
### Evidence Card
- Evidence ID:
- Title:
- Category:
- Source Type:
- Evidence Level:
- Confidence:
- Supports:
- Refutes:
- Missing Evidence:
- Weight:
```

Evidence Level 与 Confidence 的含义引用 M3，不在示例中重新定义。

## 6. Scorecard 要求

示例必须使用 M6 Scorecard：

```markdown
### M6 Scorecard
- Scorecard ID:
- Methodology Refs:
- Evidence Chain Refs:
- Scores:
- Overall Score:
- Confidence Score:
- Quality Gate:
- Disclaimer:
```

Scorecard 仅用于研究质量控制，不代表投资评级。

## 7. 合规要求

所有示例必须：

- 包含反方观点和不确定性。
- 标注数据时效和缺失证据。
- 避免交易动作、价格预测、收益承诺和个性化建议。
- 明确说明仅供研究参考，不构成投资建议。

## 8. 验收标准

示例通过条件：

- 文档内容超过最小实质内容阈值。
- 包含 `Prompt ID`、`Evidence ID`、`Evidence Level`、`Scorecard`、`Quality Gate`。
- 包含“不构成投资建议”。
- 与 M2-M6 规则一致，不重复定义核心规范。

