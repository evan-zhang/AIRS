# General Benchmark Template

**Benchmark ID**：BENCH-GENERAL-TEMPLATE  
**行业分类**：general  
**方法论引用**：`docs/methodology/evidence-chain.md`, `docs/methodology/risk.md`, `docs/methodology/counter-consensus.md`  
**Prompt 引用**：`prompts/evidence/evidence-chain.md`, `prompts/report/generation.md`  
**版本**：v0.7.0

**免责声明**：本 Benchmark 仅用于 AIRS 通用研究质量测试，不构成投资建议，不提供交易指令、价格预测或收益承诺。

## 1. 测试场景

通用类用例不绑定单一行业，重点测试报告结构、证据链、反方观点、不确定性、Scorecard 和合规边界。它用于发现 Agent 在任何行业都可能出现的基础质量问题。

## 2. M4 Prompt 输入

- Prompt ID：`PROMPT-EVIDENCE-CHAIN` 或 `PROMPT-REPORT-GENERATION`
- 研究问题：给定研究材料能否形成可审计的证据链和合格报告？
- 输出要求：M3 Evidence Card、Evidence Chain、M6 Scorecard、Quality Gate、反方观点、不确定性和免责声明。

## 3. M3 Evidence 要求

| Evidence ID | Evidence Level | Confidence | Weight | Supports | Refutes | Missing Evidence |
|-------------|----------------|------------|--------|----------|---------|------------------|
| EV-20260710-GN01 | A | HIGH | 0.25 | 支持核心命题 | 存在口径差异 | 替代数据源 |
| EV-20260710-GN02 | B | MEDIUM | 0.20 | 支持背景判断 | 证据时效不足 | 更新数据 |

## 4. M6 Scorecard 要求

Scorecard 必须覆盖 Evidence Score、Prompt Score、Report Score、Risk Score 和 Confidence Score。Quality Gate PASS 要求报告结构完整，且没有合规缺失。

## 5. 反方观点与不确定性

反方观点必须实质化，不能只写“可能存在风险”。不确定性必须绑定数据来源、时间口径、模型假设或缺失证据。

