# AI Expected Output

**Benchmark ID**：BENCH-AI-EXPECTED-OUTPUT  
**版本**：v0.7.0

**免责声明**：本期望输出仅用于 AIRS AI 类 Benchmark 回归测试，不构成投资建议，不提供交易指令、价格预测或收益承诺。

## 1. 输出结构

合格输出应使用 M4 Prompt 格式，并按 `templates/report-template.md` 组织：

1. 报告元数据：Prompt ID、方法论引用、研究对象、版本。
2. 核心观点：限定为研究判断，不输出交易动作。
3. M3 Evidence Card：至少 3 张证据卡，包含 Evidence ID、Evidence Level、Confidence、Weight。
4. Evidence Chain：说明 supports、refutes 和 missing_evidence。
5. M6 Scorecard：包含 Scorecard ID、各维度分数、Overall Score、Confidence Score、Quality Gate。
6. 反方观点：需求端、供给端、技术路线或客户集中度。
7. 不确定性：订单口径、库存、交付、资本开支周期。
8. 风险提示和免责声明。

## 2. 示例片段

```markdown
### M6 Scorecard
- Scorecard ID: SCORECARD-AI-001
- Evidence Score: 84
- Methodology Score: 82
- Report Score: 80
- Confidence Score: 76
- Quality Gate: PASS
- Disclaimer: 仅供研究参考，不构成投资建议
```

## 3. 最低可接受标准

若输出只给出行业叙述，没有 Evidence ID 和 Scorecard，应为 FAIL。若证据完整但反方观点较弱，应为 CONDITIONAL_PASS。若包含强证据、反证、不确定性和免责声明，可为 PASS。

