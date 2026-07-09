# Robotics Expected Output

**Benchmark ID**：BENCH-ROBOTICS-EXPECTED-OUTPUT  
**版本**：v0.7.0

**免责声明**：本期望输出仅用于 AIRS 机器人类 Benchmark 回归测试，不构成投资建议，不提供交易指令、价格预测或收益承诺。

## 1. 输出结构

期望输出必须包含：

- M4 Prompt ID、研究问题和输出约束。
- 方法论引用：主题扩散、供应链卡点或反共识。
- M3 Evidence Card：订单、收入、验证或反方证据。
- Evidence Chain：主题 -> 环节 -> 证据 -> 风险。
- M6 Scorecard：Theme Score、Evidence Score、Risk Score、Quality Gate。
- 反方观点：量产、成本、需求、技术路线。
- 不确定性：样机到量产、客户导入、成本曲线。
- 免责声明。

## 2. 示例片段

```markdown
### M6 Scorecard
- Scorecard ID: SCORECARD-ROBOTICS-001
- Theme Score: 78
- Evidence Score: 72
- Risk Score: 70
- Confidence Score: 68
- Quality Gate: CONDITIONAL_PASS
- Disclaimer: 仅供研究参考，不构成投资建议
```

## 3. Gate 期望

若缺少量产交付和财务贡献证据，即使主题路径完整，也应降低 Confidence Score。完整报告必须包含反方观点、不确定性和免责声明。

## 4. M7 一致性声明

期望输出必须逐项列出 M3 Evidence 字段，包括 Evidence ID、Evidence Level、Confidence、Weight，并纳入 M6 Scorecard 与 Quality Gate。
