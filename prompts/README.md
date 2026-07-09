# AIRS Prompts 目录

本目录包含 AIRS 项目的所有 Prompt 模板。

---

## 目录结构

```
prompts/
├── README.md          # 本文件
├── _dsl/              # Prompt DSL 定义
├── hot-topic/         # 热点主题分析 Prompt
├── industry/          # 产业分析 Prompt
├── supply-chain/      # 供应链分析 Prompt
├── chokepoint/        # 卡点分析 Prompt
├── financial/         # 财报分析 Prompt
├── news/              # 新闻分析 Prompt
├── evidence/          # 证据相关 Prompt
├── committee/         # 投资委员会 Prompt
├── valuation/         # 估值分析 Prompt
├── risk/              # 风险分析 Prompt
└── report/            # 报告生成 Prompt
```

---

## Prompt 分类

### DSL 定义

- **_dsl/**：Prompt DSL 语法、变量定义、模板系统

### 研究方法论 Prompt

- **hot-topic/**：热点主题分析 Prompt
- **industry/**：产业分析 Prompt
- **supply-chain/**：供应链分析 Prompt
- **chokepoint/**：卡点分析 Prompt

### 数据分析 Prompt

- **financial/**：财报分析 Prompt
- **news/**：新闻分析 Prompt

### 支撑 Prompt

- **evidence/**：证据采集、验证、关联 Prompt
- **committee/**：投资委员会模拟 Prompt
- **valuation/**：估值分析 Prompt
- **risk/**：风险分析 Prompt

### 输出 Prompt

- **report/**：报告生成、反方观点、不确定性标注 Prompt

---

## Prompt 结构

每个 Prompt 文件应包含：

```markdown
# Prompt 标题

## 用途
[说明这个 Prompt 的用途]

## 输入要求
- 必需输入：[变量1, 变量2, ...]
- 可选输入：[变量3, 变量4, ...]

## 输出格式
[说明输出格式]

## Prompt 内容
```
{{variable_name}}
[具体的 Prompt 内容]
```

## 示例
### 输入示例
[示例输入]

### 输出示例
[示例输出]

---

**归属 Milestone**：M[X]
**最后更新**：YYYY-MM-DD
**版本**：vX.X.X
```

---

## 命名规范

### 文件命名

- 使用小写字母和连字符
- ✅ `supply-chain-analysis.md`
- ❌ `SupplyChainAnalysis.md`

### 变量命名

- 使用双花括号包裹
- 使用蛇形命名法
- ✅ `{{industry_name}}`
- ❌ `{{industryName}}`

---

## Prompt DSL

### 变量占位符

使用 `{{variable_name}}` 表示变量占位符：

```markdown
请分析 {{industry}} 产业的供应链结构，
重点关注 {{time_range}} 时间段的变化。
```

### 条件块

使用 `{{#if condition}}...{{/if}}` 表示条件块：

```markdown
{{#if include_risk_analysis}}
## 风险分析
[风险分析内容]
{{/if}}
```

### 循环块

使用 `{{#each items}}...{{/each}}` 表示循环块：

```markdown
{{#each evidence_items}}
- {{title}}：{{description}}
{{/each}}
```

---

## Prompt 编写规范

### 内容规范

1. **清晰明确**：指令清晰，无歧义
2. **结构化**：使用结构化格式
3. **示例驱动**：提供示例输入输出
4. **错误处理**：说明错误处理方式

### 格式规范

1. **标题**：使用 `#` 表示标题
2. **列表**：使用 `-` 作为列表符号
3. **代码块**：使用 ` ``` ` 包裹
4. **变量**：使用 `{{variable_name}}`

### 质量规范

1. **可执行**：可被 Agent 执行
2. **可测试**：可被测试验证
3. **可维护**：易于维护扩展
4. **可复用**：可在多处复用

---

## Prompt 开发流程

### 1. 创建 Prompt 文件

```bash
touch prompts/{category}/{prompt-name}.md
```

### 2. 编写 Prompt 内容

按照 Prompt 结构编写。

### 3. 测试 Prompt

- 使用示例输入测试
- 验证输出格式
- 检查边界情况

### 4. 文档化

- 添加用途说明
- 添加输入输出说明
- 添加使用示例

### 5. 版本管理

在 Prompt 文件末尾添加版本信息。

---

## Prompt 质量标准

### 功能质量

- 能完成预期功能
- 输出格式正确
- 错误处理合理

### 技术质量

- 符合 DSL 规范
- 可被 Agent 执行
- 可测试验证

### 文档质量

- 有清晰用途说明
- 有输入输出说明
- 有使用示例

---

## Prompt 与 Skill 的关系

### Prompt 是 Skill 的实现

每个 Skill 对应一个或多个 Prompt：

```
Skill: skills/supply-chain/
  ├── Prompt: prompts/supply-chain/analysis.md
  ├── Prompt: prompts/supply-chain/visualization.md
  └── Prompt: prompts/supply-chain/verification.md
```

### 调用关系

```
Master Skill
  → 选择方法论
    → 调用对应 Skill
      → 执行对应 Prompt
        → 生成输出
```

---

## 后续扩展

### M2 扩展计划

- 完善研究方法论 Prompt（hot-topic, industry, supply-chain, chokepoint）
- 实现 Prompt DSL

### M3 扩展计划

- 实现证据相关 Prompt
- 完善证据采集、验证、关联 Prompt

### M4 扩展计划

- 实现估值和风险分析 Prompt
- 完善评分 Prompt

### M5 扩展计划

- 实现报告生成 Prompt
- 实现反方观点生成 Prompt
- 实现不确定性标注 Prompt

### M6-M8 扩展计划

- 完善 Prompt 质量
- 优化 Prompt 性能
- 添加更多 Prompt

---

**最后更新**：2026-07-10
**归属 Milestone**：M1: Architecture Foundation
