# Semiconductor Expected Output

**Benchmark ID**：BENCH-SEMICONDUCTOR-EXPECTED-OUTPUT  
**版本**：v0.7.0

**免责声明**：本期望输出仅用于 AIRS 半导体类 Benchmark 回归测试，不构成投资建议，不提供交易指令、价格预测或收益承诺。

## 1. 输出结构

期望输出必须包含：

- Prompt ID 和 M4 Prompt 输入摘要。
- 方法论引用：供应链卡点、产业生命周期或财报异常。
- 至少 3 张 M3 Evidence Card，包含 Evidence ID、Evidence Level、Confidence、Weight。
- Evidence Chain，说明 supports、refutes 和 missing_evidence。
- M6 Scorecard，包含 Scorecard ID、Overall Score、Confidence Score 和 Quality Gate。
- 反方观点：库存周期、客户认证、技术路线、政策变化。
- 不确定性：良率、交付周期、收入确认、客户集中度。
- 免责声明。

## 2. 示例片段

```markdown
### Evidence Chain
- EV-20260710-SC01 supports: 设备认证进展支持卡点命题。
- EV-20260710-SC02 refutes: 库存周期回落削弱短期需求强度。
- Missing Evidence: 缺少客户批量订单和良率爬坡数据。
```

## 3. M6 Gate

Quality Gate 为 PASS 时，报告必须同时满足证据完整、Scorecard 完整和合规完整。若 Evidence Card 完整但客户验证缺口较大，应输出 CONDITIONAL_PASS。

