# Prompt Lifecycle（Prompt 生命周期）

**归属 Milestone**：M4: Prompt DSL & Prompt Library  
**适用层级**：Prompt Engine → Review Agent → Verification Agent  
**免责声明**：本文档用于提示词研发流程管理，不构成投资建议，不提供交易指令或收益承诺。

## 1. 生命周期状态

| 状态 | 含义 | 允许动作 |
|------|------|----------|
| DRAFT | 初稿，尚未审查 | 编写、补充、局部测试 |
| IN_REVIEW | 已提交审查 | Review Agent 审查 |
| APPROVED | 通过审查，可被 Skill 调用 | 版本发布、使用 |
| APPROVED_WITH_LIMITATION | 限制通过 | 指定场景使用，必须记录限制 |
| NEEDS_REVISION | 需要修改 | Code Agent 修复 |
| DEPRECATED | 已废弃 | 禁止新任务使用 |
| REJECTED | 审查失败 | 不得被生产 Skill 调用 |

## 2. 创建流程

1. Code Agent 读取相关 M2 方法论和 M3 Evidence 文档。
2. 从 `templates/prompt-template.md` 复制结构。
3. 填写七个必需 section。
4. 在 Evidence Requirements 中引用 M3 规范。
5. 在 Failure Cases 中列出合规失败、证据失败、方法论不适配。
6. 运行 `python3 scripts/validate_prompt.py`。

## 3. 审查流程

Review Agent 使用 `evaluation/rubrics/prompt-review-checklist.md` 审查以下维度：

- 是否准确引用 M2 方法论。
- 是否通过 M3 Evidence Card 组织证据。
- System Prompt 是否可直接执行。
- Output Schema 是否能支持后续 Report、Evaluation、Benchmark。
- 是否包含反方观点、不确定性和免责声明。

## 4. 使用流程

Skill 调用 Prompt 时必须传入 Input Schema 要求的字段。若输入不足，Prompt 应输出缺失字段和后续补证路径，而不是编造结论。

## 5. 更新流程

Prompt 更新必须说明：

- 更新原因：方法论变更、证据规范变更、失败案例修复、输出格式优化。
- 影响范围：哪些 Skill、Benchmark、Report 会受影响。
- 兼容性：是否保持原 Input Schema 和 Output Schema。
- 自检结果：M1、M2、M3、M4 验证脚本是否通过。

## 6. 废弃流程

当 Prompt 与当前 M2/M3 规范不兼容，或存在无法通过轻量修复解决的合规风险时，应标记为 DEPRECATED 或 REJECTED。废弃文档必须说明替代 Prompt 和迁移路径。

