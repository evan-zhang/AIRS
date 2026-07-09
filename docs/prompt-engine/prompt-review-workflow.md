# Prompt Review Workflow（Prompt 审查工作流）

**归属 Milestone**：M4: Prompt DSL & Prompt Library  
**适用层级**：Review Agent → Verification Agent  
**免责声明**：本文档用于提示词审查流程，不构成投资建议，不提供交易指令或收益承诺。

## 1. 审查目标

Prompt Review 的目标是判断一个 Prompt 是否可以被 AIRS Skill 安全调用。审查不评价投资结论正确与否，而评价 Prompt 是否能稳定地产生证据驱动、反方充分、边界清楚且合规的研究输出。

## 2. 输入材料

Review Agent 审查时应读取：

- 待审 Prompt 文档。
- 对应 M2 方法论文档。
- M3 Evidence Card 与 Evidence Chain 规范。
- Prompt Schema 与 Output Schema。
- 最近一次 `validate_prompt.py` 结果。

## 3. 审查步骤

1. 检查七个必需 section 是否存在且有实质内容。
2. 检查 System Prompt 是否可直接使用。
3. 检查 User Template 是否覆盖 Input Schema 必填变量。
4. 检查 Output Schema 是否包含结论、证据链、反方观点、不确定性、失败状态和免责声明。
5. 检查 Evidence Requirements 是否引用 M3，而不是重复定义或分叉规则。
6. 检查 Failure Cases 是否覆盖证据不足、证据冲突、方法论不适配和合规失败。
7. 给出 PASS、PASS_WITH_LIMITATION 或 FAIL。

## 4. 审查输出

```markdown
## Prompt Review

- Prompt ID：
- Prompt Version：
- Review Result：PASS / PASS_WITH_LIMITATION / FAIL
- Score：0-100
- Methodology Alignment：
- Evidence Alignment：
- Compliance：
- Required Fixes：
- Limitations：
```

## 5. 强制 FAIL 条件

- 缺少免责声明或允许输出交易建议。
- System Prompt 不是完整可执行提示词。
- 未引用任何 M2 方法论。
- Evidence Requirements 未引用 M3 Evidence Card 或 Evidence Chain。
- 输出结构不包含反方观点、不确定性或缺失证据。

