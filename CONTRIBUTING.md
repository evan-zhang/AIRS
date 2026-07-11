# AIRS 贡献指南

## 贡献方式

欢迎为 AIRS 项目做出贡献！你可以通过以下方式参与：

- 新增 Skill
- 新增 Prompt
- 新增 Methodology
- 新增 Benchmark
- 新增 Schema
- 新增 Example
- 改进文档
- 修复问题

---

## V1.0 Production 贡献流程

AIRS V1.0 已进入 Production Release。所有贡献必须遵守生产治理流程：

1. 先创建 Issue，说明问题、影响范围、验收标准和合规边界。
2. 修改最小必要文件，避免重写 M1-M8 已 PASS 核心内容。
3. 若修改 README、ROADMAP、ARCHITECTURE、AGENTS、SKILL、CONTRIBUTING、LICENSE、CHANGELOG 或已 PASS 核心规范，必须新增 ADR 并说明原因。
4. 更新 `CHANGELOG.md`。
5. 运行相关 validate 脚本。
6. 生产发布前运行 `python3 scripts/production_check.py`。
7. PR 必须填写 `.github/pull_request_template.md` 中的验证和合规检查。

版本规范见 `docs/governance/semantic-versioning.md`。发布流程见 `docs/governance/release-workflow.md`。

### V1.0 合规边界

所有贡献不得引入：

- 荐股内容
- 自动交易能力
- 具体买入、卖出、持有指令
- 目标价预测
- 收益承诺
- 无证据、无反方观点、无不确定性标注的投资研究输出

所有投资研究相关新增内容必须包含“不构成投资建议”免责声明。

---

## 新增 Skill

### Skill 结构

每个 Skill 应包含以下文件：

```
skills/{skill-name}/
├── README.md              # Skill 说明文档
├── skill.md               # Skill 主文件
├── prompt.md              # Prompt 模板
├── schema.md              # 输入输出 Schema
├── examples/              # 使用示例
└── tests/                 # 测试用例
```

### Skill README 要求

README.md 必须包含：

- Skill 用途说明
- 激活条件
- 输入要求
- 输出格式
- 使用示例
- 依赖关系

### Skill 开发流程

1. 在 `skills/` 创建 Skill 目录
2. 编写 README.md
3. 实现 Skill 逻辑
4. 定义输入输出 Schema
5. 添加使用示例
6. 编写测试用例
7. 运行自检
8. 更新相关文档

### Skill 质量标准

- 有清晰的用途说明
- 输入输出明确
- 有使用示例
- 有测试覆盖
- 符合项目规范

---

## 新增 Prompt

### Prompt 结构

```
prompts/{category}/{prompt-name}.md
```

### Prompt 编写规范

1. **文件命名**：使用小写字母和连字符
   - ✅ `supply-chain-analysis.md`
   - ❌ `SupplyChainAnalysis.md`

2. **Prompt 结构**：
   ```markdown
   # Prompt 标题
   
   ## 用途
   [说明这个 Prompt 的用途]
   
   ## 输入要求
   - 必需输入：[列出必需输入]
   - 可选输入：[列出可选输入]
   
   ## 输出格式
   [说明输出格式]
   
   ## Prompt 内容
   [实际的 Prompt 内容]
   
   ## 示例
   [输入示例和输出示例]
   ```

3. **Prompt DSL**：
   - 使用 `_dsl/` 目录定义 Prompt DSL
   - 复杂 Prompt 拆分为多个子 Prompt
   - 使用变量占位符 `{{variable_name}}`

### Prompt 质量标准

- 用途明确
- 输入输出清晰
- 有使用示例
- 可被 Agent 执行
- 符合规约要求

---

## 新增 Methodology

### Methodology 结构

```
docs/methodology/{methodology-name}/
├── README.md              # 方法论说明
├── workflow.md            # 工作流程
├── prompt.md              # Prompt 模板
└── schema.md              # Schema 定义
```

### Methodology README 要求

- 方法论核心思想
- 适用场景
- 不适用场景
- 理论基础
- 实施步骤
- 局限性

### Methodology 开发流程

1. 在 `docs/methodology/` 创建目录
2. 编写 README.md
3. 定义工作流程
4. 编写 Prompt 模板
5. 定义 Schema
6. 在 `prompts/` 创建对应 Prompt
7. 添加 Benchmark 用例

---

## 新增 Benchmark

### Benchmark 结构

```
benchmark/{category}/{case-name}/
├── README.md              # 用例说明
├── input.md               # 输入数据
├── expected-output.md     # 期望输出
└── metadata.json          # 元数据
```

### Benchmark 分类

| 目录 | 用途 |
|------|------|
| ai/ | AI 相关测试用例 |
| semiconductor/ | 半导体相关测试用例 |
| innovative-drug/ | 创新药相关测试用例 |
| robotics/ | 机器人相关测试用例 |
| new-energy/ | 新能源相关测试用例 |
| general/ | 通用测试用例 |

### Benchmark 编写规范

1. **README.md**：说明测试目的和覆盖场景
2. **input.md**：标准化的输入格式
3. **expected-output.md**：期望的输出结果
4. **metadata.json**：元数据（难度、类别、优先级）

### Benchmark 质量标准

- 测试目的明确
- 输入标准化
- 期望输出可验证
- 元数据完整

---

## 新增 Schema

### Schema 结构

```
schemas/{category}/{schema-name}.md
```

### Schema 编写规范

1. **Schema 结构**：
   ```markdown
   # Schema 名称
   
   ## 用途
   [说明这个 Schema 的用途]
   
   ## 字段定义
   
   | 字段名 | 类型 | 必需 | 说明 |
   |--------|------|------|------|
   | name | string | 是 | 对象名称 |
   | value | number | 是 | 数值 |
   
   ## 示例
   [示例数据]
   ```

2. **数据类型**：
   - string：字符串
   - number：数字
   - boolean：布尔值
   - array：数组
   - object：对象
   - enum：枚举

### Schema 分类

| 目录 | 用途 |
|------|------|
| common/ | 通用 Schema |
| research/ | 研究相关 Schema |
| evidence/ | 证据相关 Schema |
| score/ | 评分相关 Schema |
| report/ | 报告相关 Schema |
| evaluation/ | 评估相关 Schema |

---

## 新增 Example

### Example 结构

```
examples/{category}/{example-name}.md
```

### Example 编写规范

1. **结构**：
   ```markdown
   # 示例标题
   
   ## 场景说明
   [说明这个示例的场景]
   
   ## 输入
   \`\`\`
   [输入数据]
   \`\`\`
   
   ## 输出
   \`\`\`
   [输出结果]
   \`\`\`
   
   ## 分析
   [分析输入输出的关系]
   ```

2. **分类**：
   - examples/reports/：报告示例
   - examples/evidence/：证据示例
   - examples/scores/：评分示例
   - examples/workflows/：工作流示例

---

## 提交规范

### 提交前自检

在提交任何更改前，必须运行：

```bash
python scripts/check_structure.py
python scripts/validate_m1.py
```

确保：
- ✅ 目录结构完整
- ✅ 文件命名规范
- ✅ 文档格式正确
- ✅ 无违规内容
- ✅ 有免责声明

### 提交信息格式

```
{type}: {subject}

{body}

{footer}
```

**Type**：
- feat：新功能
- fix：修复
- docs：文档
- style：格式调整
- refactor：重构
- test：测试
- chore：杂项

**示例**：
```
feat: 新增供应链卡点分析 Skill

- 实现 supply-chain Skill
- 添加相关 Prompt
- 添加 Schema 定义
- 添加测试用例

归属 Milestone：M3
```

---

## 代码/文档规范

### 文档规范

1. **语言**：中文
2. **格式**：Markdown
3. **标题层级**：不超过 3 级
4. **列表**：使用 `-` 作为列表符号
5. **代码块**：使用 ` ``` ` 包裹，指定语言

### 命名规范

1. **文件命名**：
   - 使用小写字母和连字符
   - ✅ `supply-chain-analysis.md`
   - ❌ `SupplyChainAnalysis.md`

2. **目录命名**：
   - 使用小写字母和连字符
   - ✅ `skills/hot-topic/`
   - ❌ `skills/HotTopic/`

### 格式规范

1. **标题**：使用 `#` 表示标题
2. **强调**：使用 `**` 加粗
3. **列表**：使用 `-` 作为无序列表
4. **引用**：使用 `>` 表示引用
5. **分隔线**：使用 `---` 表示

---

## 质量标准

### 内容质量

- 有实际内容，非空壳
- 有明确目的和范围
- 有清晰的输入输出
- 有使用示例
- 有免责声明（如适用）

### 技术质量

- 符合项目架构
- 可被 Agent 执行
- 可被测试验证
- 可维护扩展

### 合规质量

- 不违规荐股
- 不预测价格
- 不给出绝对化结论
- 包含必要免责声明

---

## Review 流程

### 自检

提交前运行：

```bash
# 检查结构
python scripts/check_structure.py

# 验证 M1
python scripts/validate_m1.py
```

### Review 检查点

1. **结构检查**：
   - 文件位置是否正确
   - 命名是否符合规范
   - 目录结构是否完整

2. **内容检查**：
   - 文档是否完整
   - 是否有实际内容
   - 是否有使用示例

3. **质量检查**：
   - 是否符合架构
   - 是否可执行
   - 是否可测试

4. **合规检查**：
   - 是否有违规内容
   - 是否有免责声明
   - 是否有不确定性标注

---

## 问题反馈

### 反馈渠道

- GitHub Issues
- Completion Report
- 直接反馈给 Code Agent

### 反馈模板

```markdown
## 问题描述
[清晰描述问题]

## 复现步骤
1. [步骤1]
2. [步骤2]
3. [步骤3]

## 期望行为
[期望的正确行为]

## 实际行为
[实际发生的错误]

## 环境信息
- 系统：[操作系统]
- Agent：[Agent 类型]
- 版本：[AIRS 版本]
```

---

## 获取帮助

### 文档资源

- [README.md](./README.md)：项目概览
- [ARCHITECTURE.md](./ARCHITECTURE.md)：系统架构
- [AGENTS.md](./AGENTS.md)：Agent 协作
- [SKILL.md](./SKILL.md)：Master Skill
- [ROADMAP.md](./ROADMAP.md)：项目规划

### 目录资源

- `docs/`：详细文档
- `examples/`：使用示例
- `templates/`：模板文件

---

## 致谢

感谢所有为 AIRS 项目做出贡献的开发者和研究者！

---

**最后更新**：2026-07-10
**当前版本**：v1.0.0 Stable
