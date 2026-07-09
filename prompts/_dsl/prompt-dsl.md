# AIRS Prompt DSL 规范

**版本**：v0.4.0  
**归属 Milestone**：M4: Prompt DSL & Prompt Library  
**免责声明**：本规范用于描述 AIRS Prompt，不构成投资建议，不提供买卖指令、目标价或收益承诺。

## 1. 目的

Prompt DSL 为 AIRS 的生产版 Prompt 提供统一结构。它把 M2 方法论、M3 Evidence Engine、输入变量、输出结构和审查要求绑定在同一份文档契约中。

## 2. 必需结构

每个 Prompt 必须包含：

- `metadata`：Prompt ID、名称、版本、分类、审查状态。
- `methodology_refs`：至少一个 M2 方法论文档路径。
- `evidence_refs`：至少一个 M3 Evidence 文档路径。
- `input_schema`：输入字段及必需性。
- `output_schema`：输出字段及必需性。
- `sections`：七个标准 Markdown section。
- `compliance`：免责声明和禁止表达。

## 3. Markdown Section

生产版 Prompt 的 Markdown 标题必须使用：

```text
## 1. System Prompt（系统提示词）
## 2. User Template（用户输入模板）
## 3. Input Schema（输入数据结构）
## 4. Output Schema（输出数据结构）
## 5. Evidence Requirements（证据要求）
## 6. Failure Cases（失效场景）
## 7. Review Checklist（审查清单）
```

## 4. 变量

变量使用 `{{snake_case}}`。输入变量必须在 Input Schema 中出现。可选变量必须说明默认处理方式。缺少必填变量时，Prompt 必须返回缺失字段清单，而不是继续推断。

## 5. 合规

所有 Prompt 必须包含以下约束：

- 输出仅供投资研究参考，不构成投资建议。
- 不提供买入、卖出、持有、目标价或收益承诺。
- 证据不足时必须标注 `missing_evidence` 和不确定性。
- 任何核心结论必须可追溯到 Evidence Card 或 Evidence Chain。

