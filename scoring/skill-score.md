# Skill Score（Skill 质量评分）

**归属 Milestone**：M6  
**版本**：v0.6.0  
**免责声明**：Skill 评分用于执行编排质量控制，不构成投资建议。

## 1. 评分目的

Skill Score 衡量 M5 Skill 是否正确引用 Prompt、Methodology、Evidence，是否具备输入输出、依赖、工作流、失败处理和审查清单。

## 2. 评分维度

| 维度 | 权重 | 规则 |
|------|------|------|
| 文档结构 | 0.15 | 十段式结构是否完整 |
| Prompt 引用 | 0.15 | 是否引用 M4 Prompt |
| Methodology 引用 | 0.15 | 是否引用 M2 方法论 |
| Evidence 引用 | 0.15 | 是否引用 M3 Evidence |
| Workflow 可执行性 | 0.15 | 步骤是否可执行 |
| Failure Handling | 0.15 | 失败是否可返回 |
| 合规边界 | 0.10 | 是否禁止交易建议 |

## 3. 计算公式

```text
skill_score = sum(check_score_i * weight_i) - unresolved_dependency_penalty
```

引用路径不存在时每项扣 15；内置 Prompt 正文或重复定义证据等级时最高不得超过 60。

## 4. 输入输出

输入：Skill 文档、Skill run trace、skill.schema.json、skill-registry.schema.json。  
输出：skill_score、dependency_findings、runtime_findings、fix_required。

## 5. 与 Evidence / Methodology 的关系

Skill Score 只检查引用和执行 trace，不复制或重写 M2/M3/M4 规则。

## 6. 权重建议

Overall Score 默认权重 0.10；运行时集成测试可提高到 0.20。

