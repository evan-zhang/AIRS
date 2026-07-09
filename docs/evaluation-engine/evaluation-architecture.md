# Evaluation Architecture（评估架构总览）

**归属 Milestone**：M6 Score Engine & Evaluation Engine  
**版本**：v0.6.0  
**最后更新**：2026-07-10

**免责声明**：Evaluation Engine 仅用于 AIRS 研究质量验证，不构成投资建议，不提供交易指令、目标价或收益承诺。

## 1. 目标

Evaluation Engine 对 Score、Report、Skill、Prompt、Evidence 和 Benchmark 输出进行统一质量验证。它不替代 Score Engine 计算分数，而是判断产物是否可以进入报告、回归测试或生产交付。

## 2. 架构位置

```text
Score Engine
    ↓
Evaluation Engine
    ↓
Quality Gate
    ↓
Report / Benchmark / Production Review
```

## 3. 核心能力

- 质量门禁：PASS、CONDITIONAL_PASS、FAIL。
- 反方观点审查：检查反方观点是否有证据支撑。
- 不确定性审查：检查 confidence 是否与证据等级和缺口一致。
- 合规审查：检查免责声明和禁止输出。
- 回归审查：对 M1-M6 自检结果与关键文件做一致性验证。

## 4. 输入输出

输入：

- Scorecard。
- Evidence Chain。
- Prompt Output。
- Skill Run Trace。
- Report Draft。
- Benchmark Case（如有）。

输出：

- Evaluation Report。
- Quality Gate Result。
- Regression Checklist Result。
- Fix Suggestions。

## 5. Agent 职责

| Agent | 职责 |
|-------|------|
| Research Agent | 提供可验证研究产物 |
| Review Agent | 执行质量评审和改进建议 |
| Verification Agent | 运行自检和回归测试 |
| Code Agent | 维护 schema、模板、脚本和文档 |

## 6. 强制失败条件

- 缺少免责声明。
- 输出买入、卖出、持有、目标价或收益承诺。
- 核心结论无 Evidence Card 支撑。
- Evidence Score 缺失。
- 权重总和无法归一化且无解释。
- 反方观点完全缺失。

