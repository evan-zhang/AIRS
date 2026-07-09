# Prompt DSL（Prompt 描述语言）

**归属 Milestone**：M4: Prompt DSL & Prompt Library  
**适用层级**：Prompt Engine  
**免责声明**：Prompt DSL 用于描述投资研究提示词结构，不构成投资建议，不提供交易指令或收益承诺。

## 1. 设计目标

Prompt DSL 用统一结构描述 AIRS 的 Prompt 文档，使 Code Agent 可以创建 Prompt，Research Agent 可以执行 Prompt，Review Agent 可以审查 Prompt，Verification Agent 可以验证 Prompt 是否符合 M2/M3 约束。

## 2. 顶层结构

```yaml
prompt:
  id: prompt.supply_chain.chokepoint_analysis
  version: 0.4.0
  category: supply-chain
  methodology_refs:
    - docs/methodology/supply-chain-chokepoint.md
  evidence_refs:
    - docs/evidence/evidence-card-specification.md
    - docs/evidence/evidence-validation-workflow.md
  sections:
    - System Prompt
    - User Template
    - Input Schema
    - Output Schema
    - Evidence Requirements
    - Failure Cases
    - Review Checklist
```

## 3. 必需字段

| 字段 | 必需 | 说明 |
|------|------|------|
| `id` | 是 | 全局唯一 Prompt ID |
| `version` | 是 | 语义化版本 |
| `category` | 是 | Prompt 分类 |
| `methodology_refs` | 是 | 对应 M2 方法论文档 |
| `evidence_refs` | 是 | 对应 M3 证据规范 |
| `input_variables` | 是 | User Template 可使用的变量 |
| `output_contract` | 是 | 输出结构契约 |
| `compliance` | 是 | 免责声明与禁止表达 |

## 4. 变量语法

- 使用 `{{variable_name}}` 表示必填变量。
- 使用 `{{#if optional_variable}}...{{/if}}` 表示可选内容。
- 使用 `{{#each evidence_cards}}...{{/each}}` 表示列表渲染。
- 变量名使用 snake_case，禁止混用大小写。

## 5. 七段式 Prompt 文档

每个生产版 Prompt 必须包含以下 7 个二级标题：

1. `## 1. System Prompt（系统提示词）`
2. `## 2. User Template（用户输入模板）`
3. `## 3. Input Schema（输入数据结构）`
4. `## 4. Output Schema（输出数据结构）`
5. `## 5. Evidence Requirements（证据要求）`
6. `## 6. Failure Cases（失效场景）`
7. `## 7. Review Checklist（审查清单）`

每个 section 必须有可执行内容，System Prompt 必须是完整可直接使用的中文提示词。

## 6. 与 M2/M3 的关系

Prompt DSL 只记录引用关系和执行契约：

- `methodology_refs` 指向 M2 的 Purpose、Inputs、Outputs、Workflow、Required Evidence、Counter Evidence、Failure Cases、Confidence。
- `evidence_refs` 指向 M3 的 Evidence Card、Evidence Chain、Evidence Level、Review Standard、Validation Workflow。
- 若 M2/M3 规则更新，Prompt 通过版本更新同步引用，不在本 DSL 中重复维护规则全文。

## 7. 验证要求

Verification Agent 至少检查：

1. Prompt 文件存在且包含 7 个必需 section。
2. Prompt 引用了至少一个 M2 方法论。
3. Evidence Requirements 引用了 M3 Evidence Card 或 Evidence Chain。
4. Prompt 包含免责声明和禁止荐股要求。
5. JSON Schema 合法，且能够描述输入输出结构。

