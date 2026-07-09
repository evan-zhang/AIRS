# AIRS Skills 目录

本目录包含 AIRS 项目的所有 Skill 模块。

---

## 目录结构

```
skills/
├── master/           # Master Skill（总控）
├── hot-topic/        # 热点主题分析 Skill
├── industry/         # 产业分析 Skill
├── supply-chain/     # 供应链分析 Skill
├── chokepoint/       # 卡点分析 Skill
├── financial/        # 财报分析 Skill
├── news/             # 新闻分析 Skill
├── evidence/         # 证据管理 Skill
├── committee/        # 投资委员会 Skill
├── valuation/        # 估值分析 Skill
├── risk/             # 风险分析 Skill
├── report/           # 报告生成 Skill
└── verification/     # 验证检查 Skill
```

---

## Skill 分类

### 核心控制 Skill

- **master/**：Master Skill，总控入口，协调所有其他 Skill

### 研究分析 Skill

- **hot-topic/**：热点主题分析
- **industry/**：产业分析
- **supply-chain/**：供应链分析
- **chokepoint/**：卡点分析
- **financial/**：财报分析
- **news/**：新闻分析

### 支撑 Skill

- **evidence/**：证据管理
- **committee/**：投资委员会模拟
- **valuation/**：估值分析
- **risk/**：风险分析
- **report/**：报告生成
- **verification/**：验证检查

---

## Skill 结构

每个 Skill 应包含以下文件：

```
skills/{skill-name}/
├── README.md          # Skill 说明文档（必需）
├── skill.md           # Skill 主文件（必需）
├── prompt.md          # Prompt 模板（必需）
├── schema.md          # 输入输出 Schema（必需）
├── examples/          # 使用示例（可选）
└── tests/             # 测试用例（可选）
```

---

## Skill README 要求

每个 Skill 的 README.md 必须包含：

```markdown
# Skill 名称

## 用途
[说明这个 Skill 的用途]

## 激活条件
[说明何时激活这个 Skill]

## 输入要求
- 必需输入：[列出必需输入]
- 可选输入：[列出可选输入]

## 输出格式
[说明输出格式]

## 工作流程
1. [步骤1]
2. [步骤2]
3. [步骤3]

## 依赖关系
- 上游 Skill：[依赖的 Skill]
- 下游 Skill：[被依赖的 Skill]

## 使用示例
[示例输入和输出]

## 质量标准
[这个 Skill 的质量标准]

## 禁止事项
[这个 Skill 禁止做的事]

## 后续扩展
[后续扩展计划]

---

**归属 Milestone**：M[X]
**最后更新**：YYYY-MM-DD
```

---

## 命名规范

### 目录命名

- 使用小写字母和连字符
- ✅ `supply-chain/`
- ❌ `SupplyChain/`

### 文件命名

- 使用小写字母和连字符
- ✅ `skill.md`
- ❌ `Skill.md`

---

## Skill 开发流程

### 1. 创建 Skill 目录

```bash
mkdir skills/{skill-name}
```

### 2. 编写 README.md

按照 Skill README 要求编写。

### 3. 实现 Skill 逻辑

- 编写 skill.md
- 编写 prompt.md
- 编写 schema.md

### 4. 添加示例

在 examples/ 添加使用示例。

### 5. 编写测试

在 tests/ 编写测试用例。

### 6. 自检验证

```bash
python scripts/check_structure.py
```

---

## Skill 质量标准

### 内容质量

- 有清晰的用途说明
- 有明确的激活条件
- 有清晰的输入输出
- 有使用示例

### 技术质量

- 符合项目架构
- 可被 Master Skill 调用
- 有错误处理
- 有测试覆盖

### 合规质量

- 不违规荐股
- 不预测价格
- 不给出绝对化结论
- 包含必要免责声明（如适用）

---

## Skill 依赖关系

```
master (总控)
  ├── hot-topic
  ├── industry
  ├── supply-chain
  │   └── chokepoint
  ├── financial
  ├── news
  ├── evidence (支撑所有 Skill)
  ├── committee
  ├── valuation
  ├── risk
  ├── report
  └── verification
```

---

## 后续扩展

### M2 扩展计划

- 实现核心研究 Skill（hot-topic, industry, supply-chain, chokepoint）

### M3 扩展计划

- 实现证据 Skill
- 完善 evidence Skill 集成

### M4 扩展计划

- 实现估值和风险 Skill
- 完善 Skill 间协作

### M5 扩展计划

- 实现报告生成 Skill
- 完善报告模板

### M6 扩展计划

- 实现验证检查 Skill
- 完善 Skill 质量保证

---

**最后更新**：2026-07-10
**归属 Milestone**：M1: Architecture Foundation
