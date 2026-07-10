# AIRS Schemas 目录

本目录包含 AIRS 项目的所有 Schema 定义。

---

## 目录结构

```
schemas/
├── README.md          # 本文件
├── common/            # 通用 Schema
├── methodology/       # 方法论 Schema
├── research/          # 研究相关 Schema
├── evidence/          # 证据相关 Schema
├── knowledge-graph/   # 知识图谱相关 Schema
├── skills/            # Skill Engine 相关 Schema
├── score/             # 评分相关 Schema
├── benchmark/         # Benchmark 与生产示例 Schema
├── connectors/        # Data Connector Framework 相关 Schema
├── report/            # 报告相关 Schema
└── evaluation/        # 评估相关 Schema
```

---

## Schema 分类

### 通用 Schema

- **common/**：通用数据类型、通用字段定义

### 方法论 Schema

- **methodology/**：方法论结构化定义，与 `docs/methodology/` 的 16 个标准 section 对应
- **methodology/methodology.schema.json**：用于验证方法论 DSL 或结构化方法论对象，要求包含 Purpose、Theory、Background、Inputs、Outputs、Workflow、Required Evidence、Counter Evidence、Confidence 及后续映射字段

### 研究相关 Schema

- **research/**：研究意图、研究计划、研究发现

### 证据相关 Schema

- **evidence/**：证据卡、证据链、证据质量
- **evidence/evidence.schema.json**：Evidence Engine 顶层 Schema，用于封装证据卡集合、证据链集合和治理要求。
- **evidence/evidence-card.schema.json**：证据卡 Schema，定义 Evidence ID、Title、Category、Source、Source Type、URL、Publication Time、Collection Time、Confidence、Evidence Level、Supports、Refutes、Missing Evidence、Weight、Traceability、Version 等 16 个必需字段。
- **evidence/evidence-chain.schema.json**：证据链 Schema，用于描述研究命题、证据卡集合、证据关系、反方证据、缺失证据、整体置信度和免责声明要求。

### 知识图谱相关 Schema

- **schemas/knowledge-graph/**：Knowledge Graph Engine 相关 Schema，用于 FEATURE-002 图谱建模、路径分析和供应链卡脖子分析。
- **schemas/knowledge-graph/knowledge-graph.schema.json**：知识图谱 Schema，要求包含 graph_id、research_question、methodology_refs、evidence_cards、nodes、edges、path_analysis、chokepoint_analysis、disclaimer 和 version。
- Knowledge Graph Schema 必须引用 M2 Methodology 与 M3 Evidence Card，节点类型和关系类型采用受控枚举；图谱分数仅用于研究质量控制，不构成投资建议。

### Prompt 相关 Schema

- **schemas/prompt/**：Prompt Engine 相关 Schema，用于描述生产版 Prompt 文档结构与 Prompt 输出结构。
- **schemas/prompt/prompt.schema.json**：Prompt 文档 Schema，要求包含 Prompt ID、版本、分类、M2 方法论引用、M3 证据规范引用、System Prompt、User Template、Input Schema、Output Schema、Evidence Requirements、Failure Cases、Review Checklist 和免责声明。
- **schemas/prompt/prompt-output.schema.json**：Prompt 输出 Schema，要求输出保留方法论引用、研究问题、核心命题、Evidence Chain、反方观点、不确定性、失败状态和免责声明。

### Skill 相关 Schema

- **schemas/skills/**：Skill Engine 相关 Schema，用于描述生产版 Skill 与 Skill Registry。
- **schemas/skills/skill.schema.json**：单个 Skill 结构 Schema，要求包含 Purpose、Inputs、Outputs、Dependencies、Invoked Prompt、Invoked Methodology、Invoked Evidence、Workflow、Failure Handling、Review Checklist 和免责声明。
- **schemas/skills/skill-registry.schema.json**：Skill Registry Schema，用于记录 Skill ID、版本、状态、入口文件、M4 Prompt 引用、M2 Methodology 引用、M3 Evidence Engine 引用、负责人和审查状态。
- Skill Schema 只用于投资研究流程编排和质量控制，不构成投资建议；生产版 Skill 必须引用 M4/M2/M3，不能内置 Prompt 或重复定义方法论与证据规则。

### 评分相关 Schema

- **score/**：评分维度、评分结果、评分解释
- **score/score.schema.json**：单个评分维度 Schema，要求包含 score_id、score_type、methodology_refs、evidence_refs、raw_score、weight、weighted_score、formula、explanation、confidence 和免责声明。
- **score/scorecard.schema.json**：综合评分卡 Schema，用于汇总多个 Score，要求包含 methodology_refs、evidence_chain_refs、scores、overall_score、overall_grade、confidence_score、quality_gate 和权重审计。
- **score/evaluation.schema.json**：Evaluation Engine 输出 Schema，用于记录评估对象、Scorecard、检查项、总分、Gate 结果、强制失败状态和修复要求。
- Score Schema 只用于研究质量控制和结构化分析，必须引用 M2 Methodology 与 M3 Evidence，不得把评分解释为投资评级或交易建议。

### Benchmark 相关 Schema

- **schemas/benchmark/**：Benchmark 与生产示例相关 Schema，用于 M7 回归测试和质量评估。
- **schemas/benchmark/benchmark.schema.json**：Benchmark 结构 Schema，要求包含 benchmark_id、category、methodology_refs、prompt_refs、evidence_requirements、gold_standard、evaluation_criteria、expected_output、failure_cases 和免责声明。
- **schemas/benchmark/benchmark-result.schema.json**：Benchmark 执行结果 Schema，用于记录 run_id、benchmark_id、agent_id、scorecard_id、overall_score、quality_gate、passed_checks、failed_checks、evidence_gaps 和修复要求。
- **schemas/benchmark/example.schema.json**：Production Example 结构 Schema，用于描述示例 ID、方法论引用、Prompt 引用、Evidence ID、Scorecard、Quality Gate 和报告章节。
- Benchmark Schema 只用于 AIRS 回归测试与研究质量控制，必须复用 M3 Evidence Card、M4 Prompt 和 M6 Scorecard，不构成投资建议。

### Runtime 相关 Schema

- **schemas/runtime/**：FEATURE-006 Research Agent Runtime 相关 Schema，用于描述 Runtime、Agent、Task、Event 和 Session。
- **schemas/runtime/runtime.schema.json**：Runtime 顶层 Schema，记录 runtime_id、workflow_id、tasks、final_state 和免责声明。
- **schemas/runtime/agent.schema.json**：Agent Definition Schema，支持 sync、async、parallel、long_running 和 human_in_the_loop 五类 Agent。
- **schemas/runtime/task.schema.json**：Task Schema，定义 task_id、agent_id、dependencies、input 和 expected_output。
- **schemas/runtime/event.schema.json**：Event Schema，定义 Event Bus 的事件审计字段。
- **schemas/runtime/session.schema.json**：Session Schema，定义 Agent Session 状态和 Context Snapshot。
- Runtime Schema 只用于执行编排、审计和质量控制；Workflow 必须由 Runtime 调度，不得直接驱动 M2-M7 业务模块，不构成投资建议。

### Connector 相关 Schema

- **schemas/connectors/**：FEATURE-004 Data Connector Framework 相关 Schema，用于统一描述 Connector、Data Source 和 Connector Result。
- **schemas/connectors/connector.schema.json**：Connector 注册和治理 Schema，要求包含 Config、Input Schema、Output Schema、Error Handling、Retry Policy、Cache Strategy、Health Check 和 Test Case。
- **schemas/connectors/datasource.schema.json**：Data Source Schema，用于记录来源类型、优先级、治理状态、URL 和版本。
- **schemas/connectors/connector-result.schema.json**：Connector Result Schema，要求所有输出包含 source、url、timestamp、version、trace_id 和 traceability，以便对齐 M3 Evidence Card 的 Source / URL / Timestamp / Version / Traceability 要求。
- Connector Schema 只定义外部数据接入边界，不重复定义 M2 Methodology、M3 Evidence、FEATURE-002 Knowledge Graph 或 FEATURE-003 Report 规则，不构成投资建议。

### Builder 相关 Schema

- **schemas/builder/**：AIRS Builder 相关 Schema，用于 FEATURE-001 Feature Package 生成与验证。
- **schemas/builder/feature-request.schema.json**：Feature Request Schema，用于验证 Builder 输入，要求包含 feature_id、feature_name、feature_summary、business_goal、user_scenarios、dependencies、constraints、expected_outputs 和 risk_level。
- **schemas/builder/feature-package.schema.json**：Feature Package Schema，用于描述 Builder 输出包的结构、artifact 清单和验证状态。
- **schemas/builder/generated-artifact.schema.json**：Generated Artifact Schema，用于描述单个生成物的 artifact_type、path、template_ref、required 和 status。
- Builder Schema 只用于工程开发包生成和质量控制，不重新定义 M2-M7 研究规则，不构成投资建议。

### 报告相关 Schema

- **report/**：报告结构、报告元数据、报告质量

### 评估相关 Schema

- **evaluation/**：评估标准、评估结果、评估报告

---

## Schema 结构

每个 Schema 文件应包含：

```markdown
# Schema 名称

## 用途
[说明这个 Schema 的用途]

## 字段定义

| 字段名 | 类型 | 必需 | 说明 | 示例 |
|--------|------|------|------|------|
| name | string | 是 | 对象名称 | "AI服务器" |
| value | number | 是 | 数值 | 100 |

## 数据类型

- string：字符串
- number：数字（整数/浮点数）
- boolean：布尔值（true/false）
- array：数组
- object：对象
- enum：枚举

## 验证规则
[字段验证规则]

## 示例
\`\`\`json
{
  "name": "AI服务器",
  "value": 100
}
\`\`\`

## 扩展字段
[可选扩展字段]

---

**归属 Milestone**：M[X]
**最后更新**：YYYY-MM-DD
**版本**：vX.X.X
```

---

## 数据类型

### 基本类型

| 类型 | 说明 | 示例 |
|------|------|------|
| string | 字符串 | "AI服务器" |
| number | 数字 | 100, 99.5 |
| boolean | 布尔值 | true, false |
| array | 数组 | [1, 2, 3] |
| object | 对象 | {"key": "value"} |

### 复杂类型

| 类型 | 说明 | 示例 |
|------|------|------|
| enum | 枚举 | "HIGH", "MEDIUM", "LOW" |
| timestamp | 时间戳 | "2026-07-10T00:00:00Z" |
| url | URL | "https://example.com" |
| markdown | Markdown 文本 | "# 标题\n\n内容" |

---

## 命名规范

### 字段命名

- 使用蛇形命名法（snake_case）
- ✅ `industry_name`
- ❌ `industryName`

### 枚举命名

- 使用大写字母和下划线
- ✅ `HIGH_PRIORITY`
- ❌ `highPriority`

---

## Schema 编写规范

### 内容规范

1. **清晰明确**：字段说明清晰
2. **类型明确**：字段类型明确
3. **示例完整**：提供完整示例
4. **验证规则**：说明验证规则

### 格式规范

1. **表格格式**：使用表格展示字段定义
2. **代码块**：使用 JSON 格式展示示例
3. **类型说明**：明确说明字段类型

### 质量规范

1. **完整性**：字段定义完整
2. **准确性**：类型定义准确
3. **可验证**：可验证字段有效性

---

## Schema 开发流程

### 1. 创建 Schema 文件

```bash
touch schemas/{category}/{schema-name}.md
```

### 2. 定义字段

按照 Schema 结构定义字段。

### 3. 编写示例

提供完整的示例数据。

### 4. 验证 Schema

- 检查字段完整性
- 检查类型正确性
- 检查示例有效性

### 5. 文档化

- 添加用途说明
- 添加字段说明
- 添加验证规则

---

## Schema 质量标准

### 内容质量

- 字段定义完整
- 类型定义准确
- 示例正确有效

### 技术质量

- 符合数据类型规范
- 验证规则明确
- 可被系统验证

### 文档质量

- 用途说明清晰
- 字段说明详细
- 示例完整

---

## Schema 与 Prompt 的关系

### Prompt 使用 Schema

Prompt 通过 Schema 定义输入输出格式：

```
Prompt (prompts/supply-chain/analysis.md)
  → 输入 Schema (schemas/research/intent.md)
  → 输出 Schema (schemas/evidence/evidence-card.md)
```

### Schema 验证

- 验证 Prompt 输入格式
- 验证 Agent 输出格式
- 验证数据完整性

---

## 后续扩展

### M2 扩展计划

- 完善研究相关 Schema
- 定义各方法论 Schema

### M3 扩展计划

- 完善证据相关 Schema
- 定义证据链 Schema

### M4 扩展计划

- 完善评分相关 Schema
- 定义评分模型 Schema

### M5 扩展计划

- 完善报告相关 Schema
- 定义报告模板 Schema

### M6-M8 扩展计划

- 完善评估相关 Schema
- 完善 Schema 验证机制

---

**最后更新**：2026-07-10
**归属 Milestone**：M1: Architecture Foundation
