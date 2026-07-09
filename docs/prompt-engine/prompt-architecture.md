# Prompt Architecture（Prompt 架构总览）

**归属 Milestone**：M4: Prompt DSL & Prompt Library  
**适用层级**：Methodology Layer → Research Skill Layer → Evidence Layer → Evaluation Layer → Report Layer  
**免责声明**：本文档仅定义 AIRS 投资研究 Prompt Engine 架构，不构成投资建议，不提供买卖指令、目标价或收益承诺。

## 1. 目标

Prompt Engine 的目标是把 M2 Methodology Core 与 M3 Evidence Engine 转化为可执行、可审查、可版本化的 Prompt Library。所有 Skill 在执行研究任务时必须调用 Prompt，所有 Prompt 必须引用对应的 M2 方法论，并通过 M3 Evidence Card 与 Evidence Chain 组织证据。

M4 不重新定义方法论规则，也不重新定义证据等级规则。Prompt 只负责把既有规则装配成可执行指令、输入模板、输出 Schema、失败处理和审查清单。

## 2. 架构位置

```text
User Intent
    ↓
Methodology Selector（选择 M2 方法论）
    ↓
Prompt Engine（加载 Prompt DSL、输入 Schema、系统提示词）
    ↓
Research Skill（执行研究）
    ↓
Evidence Engine（生成 Evidence Card / Evidence Chain）
    ↓
Evaluation / Report（反方观点、风险、报告输出）
```

Prompt Engine 是 Skill 与 Methodology/Evidence 的接口层。它不直接采集数据，不直接计算评分，也不替代 Review Agent；它为这些模块提供稳定的提示词契约。

## 3. 核心对象

| 对象 | 职责 | 存放位置 |
|------|------|----------|
| Prompt DSL | 定义 Prompt 元数据、变量、输入输出、证据要求和审查项 | `prompts/_dsl/` |
| Prompt Document | 面向 Agent 的完整提示词文档 | `prompts/{category}/` |
| Prompt Schema | 验证 Prompt 文档结构和输出结构 | `schemas/prompt/` |
| Prompt Template | 新 Prompt 的标准空模板 | `templates/prompt-template.md` |
| Prompt Review Checklist | Review Agent 审查 Prompt 的 Rubric | `evaluation/rubrics/prompt-review-checklist.md` |

## 4. 依赖关系

Prompt 必须显式引用：

- 至少一个 M2 方法论文档，例如 `docs/methodology/supply-chain-chokepoint.md`。
- M3 Evidence Card 规范：`docs/evidence/evidence-card-specification.md`。
- M3 Evidence Chain 规范：`docs/evidence/evidence-architecture.md` 或 `docs/evidence/evidence-validation-workflow.md`。
- 合规底线：研究输出必须包含免责声明，且不得给出荐股、交易或价格预测。

## 5. 调用流程

1. Research Agent 接收研究意图并选择 M2 方法论。
2. Skill 根据方法论和任务类别选择 Prompt 文件。
3. Prompt Engine 校验输入是否满足 Input Schema。
4. Prompt Engine 渲染 User Template 中的变量。
5. Agent 执行 System Prompt，生成结构化输出。
6. 输出必须包含 Evidence Card 引用、反方观点、不确定性和免责声明。
7. Review Agent 使用 Prompt Review Checklist 审查 Prompt 与输出质量。

## 6. 质量原则

- **方法论单一来源**：研究步骤来自 M2，不在 Prompt 中另起一套规则。
- **证据单一来源**：证据字段、等级、缺口、追溯来自 M3，不在 Prompt 中重写。
- **结构可验证**：每个 Prompt 必须有 Input Schema 与 Output Schema。
- **失败可识别**：每个 Prompt 必须列出数据不足、证据冲突、反方不足、合规失败等失败场景。
- **合规优先**：任何投资研究输出必须说明不构成投资建议。

## 7. 禁止事项

- 禁止在 Prompt 中输出“建议买入、建议卖出、目标价、保证收益”等表达。
- 禁止用无来源的概括性判断替代 Evidence Card。
- 禁止把 Evidence Level、评分或置信度解释为投资评级。
- 禁止绕过 M2 方法论直接生成结论。
- 禁止在 Prompt 中复制粘贴 M2/M3 的完整规则并形成分叉版本。

