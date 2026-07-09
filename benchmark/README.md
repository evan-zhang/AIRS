# AIRS Benchmark 目录

本目录包含 AIRS 项目的测试基准。

---

## 目录结构

```
benchmark/
├── README.md              # 本文件
├── ai/                    # AI 相关测试用例
├── semiconductor/         # 半导体相关测试用例
├── innovative-drug/        # 创新药相关测试用例
├── robotics/              # 机器人相关测试用例
├── new-energy/            # 新能源相关测试用例
└── general/               # 通用测试用例
```

---

## Benchmark 概述

Benchmark 是测试 AIRS 系统有效性的基础，包含各种场景的测试用例和标准答案。

### 目标

- 覆盖所有方法论
- 覆盖所有主要行业
- 覆盖各种复杂度场景
- 提供可验证的标准答案

### 数量目标

| Milestone | 目标数量 |
|-----------|----------|
| M7 | 300+ 测试用例 |
| M8 | 500+ 测试用例 |

---

## 测试用例结构

每个测试用例包含：

```
benchmark/{category}/{case-name}/
├── README.md              # 用例说明
├── input.md               # 输入数据
├── expected-output.md     # 期望输出
└── metadata.json          # 元数据
```

---

## 测试用例分类

### 按行业分类

| 目录 | 说明 |
|------|------|
| ai/ | AI、LLM、算力相关 |
| semiconductor/ | 芯片、半导体设备、材料相关 |
| innovative-drug/ | 创新药、医疗器械相关 |
| robotics/ | 机器人、自动化相关 |
| new-energy/ | 新能源、储能相关 |
| general/ | 通用测试用例 |

### 按方法论分类

| 方法论 | 测试用例数 |
|--------|-----------|
| 供应链卡脖子分析 | 50+ |
| 主题扩散分析 | 30+ |
| 产业生命周期分析 | 30+ |
| 政策与监管驱动分析 | 30+ |
| 财报异常语言分析 | 30+ |
| 新闻事件影响分析 | 30+ |
| 反共识验证 | 30+ |

---

## 命名规范

### 目录命名

- 使用小写字母和连字符
- ✅ `ai/llm-server-2024/`
- ❌ `AI/LLMServer2024/`

### 文件命名

- 使用小写字母和连字符
- ✅ `input.md`
- ❌ `Input.md`

---

## metadata.json 格式

```json
{
  "case_id": "AI-001",
  "title": "AI服务器供应链分析",
  "category": "supply-chain",
  "industry": "ai",
  "difficulty": "medium",
  "priority": "high",
  "methodology": "supply-chain-chokepoint",
  "created_at": "2026-07-10",
  "version": "0.1.0"
}
```

---

## Benchmark 开发流程

### 1. 创建用例目录

```bash
mkdir -p benchmark/{category}/{case-name}
```

### 2. 编写 README.md

说明测试目的和覆盖场景。

### 3. 准备输入数据

按照 Schema 定义输入格式。

### 4. 准备期望输出

提供标准答案。

### 5. 编写元数据

填写 metadata.json。

### 6. 验证测试

运行测试，验证可执行性。

---

## 后续扩展

### M7 扩展计划

- 实现 300+ 测试用例
- 覆盖所有方法论
- 覆盖所有主要行业

### M8 扩展计划

- 扩展到 500+ 测试用例
- 完善测试覆盖
- 优化测试性能

---

**最后更新**：2026-07-10
**归属 Milestone**：M1: Architecture Foundation
