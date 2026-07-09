# AIRS Agent 协作规范

## Agent 类型

AIRS 系统中涉及 4 种 Agent 类型：

1. **Code Agent**：负责代码开发和项目构建
2. **Research Agent**：负责执行投资研究任务
3. **Review Agent**：负责研究报告评审
4. **Verification Agent**：负责系统验证与测试

---

## Code Agent

### 工作方式

Code Agent 是 AIRS 项目的核心开发者，负责：

- 创建和维护项目结构
- 编写和优化 Prompt
- 实现 Skill 逻辑
- 构建 Benchmark
- 编写自检脚本

### 典型工作流程

```
1. 读取项目文档（README, ARCHITECTURE, AGENTS, SKILL）
    ↓
2. 理解当前任务（从 M1_TASK_LIST 或用户指令）
    ↓
3. 按规范创建/修改文件
    ↓
4. 运行自检脚本
    ↓
5. 修复发现的问题
    ↓
6. 更新 Completion Report
```

### Loop/Go 模式

**Go 模式**（直接执行）：
- 用户指令明确（如："完成 M1 Task 3"）
- 按计划直接执行
- 不反复确认

**Loop 模式**（迭代优化）：
```python
while not pass_check():
    create_or_update_files()
    run_self_check()
    find_gaps()
    fix_issues()
```

### 失败处理

| 失败类型 | 处理方式 |
|----------|----------|
| 文件创建失败 | 检查路径权限，重新创建 |
| 内容验证失败 | 补充缺失内容，更新文件 |
| 自检失败 | 修复问题，重新自检 |
| 无法完成的任务 | 在 Completion Report 中说明，给出建议 |

### 禁止事项

❌ Code Agent 禁止：
- 生成荐股内容
- 实现自动交易功能
- 忽略免责声明
- 跳过自检流程
- 创建无法验证的内容

### 支持环境

Code Agent 可在以下环境运行：
- OpenClaw
- Codex
- Claude Code
- Cursor
- Gemini CLI
- 其他支持 Loop/Go 的 Code Agent 平台

---

## Research Agent

### 工作方式

Research Agent 负责执行投资研究任务：

- 接收研究意图
- 选择研究方法论
- 执行具体研究
- 采集证据
- 生成报告

### 典型工作流程

```
1. 接收研究意图（如："分析 AI 服务器供应链卡点"）
    ↓
2. 调用 Methodology Layer 选择方法论
    ↓
3. 执行 Research Skill（如：supply-chain Skill）
    ↓
4. 采集证据（Evidence Layer）
    ↓
5. 进行评分（Score Layer）
    ↓
6. 生成反方观点（Evaluation Layer）
    ↓
7. 输出报告（Report Layer）
```

### 输入要求

**必需输入**：
- 研究问题（清晰、具体）
- 研究范围（行业 / 公司 / 时间段）

**可选输入**：
- 数据源偏好
- 评分权重
- 报告格式

### 输出要求

**必需输出**：
- 核心研究结论
- 完整证据链
- 多维度评分
- 反方观点
- 不确定性标注

**禁止输出**：
- 直接荐股建议
- 具体买入/卖出指令
- 价格预测

---

## Review Agent

### 工作方式

Review Agent 负责评审研究报告质量：

- 检查证据完整性
- 验证逻辑一致性
- 评估反方观点强度
- 标注不确定性合理性

### 评审维度

| 维度 | 检查项 |
|------|--------|
| 证据完整性 | 证据是否充分？证据链是否完整？ |
| 逻辑一致性 | 推理是否严密？有无逻辑漏洞？ |
| 反方观点强度 | 是否有实质性的反方观点？ |
| 不确定性标注 | 不确定性是否合理标注？ |
| 报告格式 | 是否符合报告模板？ |

### 评审输出

- 评审报告
- 改进建议
- 质量评分

---

## Verification Agent

### 工作方式

Verification Agent 负责系统验证与测试：

- 执行 Benchmark 测试
- 验证系统功能
- 检查性能指标
- 生成测试报告

### 测试类型

1. **功能测试**：验证各层功能是否正常
2. **Benchmark 测试**：运行测试用例，对比标准答案
3. **性能测试**：检查系统响应时间
4. **合规测试**：检查是否包含免责声明等合规要求

### 测试流程

```
1. 读取 Benchmark 用例
    ↓
2. 执行测试
    ↓
3. 收集结果
    ↓
4. 对比标准答案
    ↓
5. 生成测试报告
```

---

## Agent 协作流程

### 完整研究流程

```
用户 → Research Agent → 研究报告
                ↓
          Review Agent → 评审报告
                ↓
      Verification Agent → 质量验证
```

### 开发流程

```
用户 → Code Agent → 创建/更新代码
                ↓
          Code Agent → 运行自检
                ↓
      Verification Agent → 系统验证
```

---

## 协作接口

### Agent 间通信

所有 Agent 通过统一的 Schema 通信：

- 研究意图 Schema
- 证据卡 Schema
- 评分 Schema
- 报告 Schema

### 错误处理

| 错误类型 | 处理方式 |
|----------|----------|
| 输入格式错误 | 返回错误提示，说明正确格式 |
| 数据获取失败 | 记录错误，尝试备用数据源 |
| 超时错误 | 返回部分结果，标注超时 |
| 逻辑错误 | 记录错误，返回错误报告 |

---

## Agent 质量标准

### Code Agent 质量标准

- 代码符合项目结构规范
- 文档完整，可读性强
- 自检脚本可运行
- Completion Report 真实反映完成情况

### Research Agent 质量标准

- 研究结论有充分证据支撑
- 包含实质性反方观点
- 不确定性标注合理
- 不违规荐股

### Review Agent 质量标准

- 评审客观公正
- 改进建议具体可行
- 评审报告结构完整

### Verification Agent 质量标准

- 测试覆盖全面
- 测试结果可复现
- 测试报告准确

---

## Agent 开发指南

### 新增 Agent

如果要新增一种 Agent 类型：

1. 在 `docs/architecture/` 添加 Agent 设计文档
2. 定义 Agent 输入输出 Schema
3. 实现 Agent 核心逻辑
4. 编写 Agent 测试
5. 更新本 AGENTS.md

### Agent 测试

每种 Agent 都应该有：

- 单元测试
- 集成测试
- Benchmark 测试
- 错误处理测试

---

**最后更新**：2026-07-10
**当前版本**：v0.1.0 (M1)
