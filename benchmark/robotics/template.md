# Robotics Benchmark Template

**Benchmark ID**：BENCH-ROBOTICS-TEMPLATE  
**行业分类**：robotics  
**方法论引用**：`docs/methodology/theme-expansion.md`, `docs/methodology/supply-chain-chokepoint.md`, `docs/methodology/counter-consensus.md`  
**Prompt 引用**：`prompts/hot-topic/theme-expansion.md`, `prompts/evidence/counter-consensus.md`  
**版本**：v0.7.0

**免责声明**：本 Benchmark 仅用于 AIRS 机器人研究质量测试，不构成投资建议，不提供交易指令、价格预测或收益承诺。

## 1. 测试场景

机器人类用例测试 Agent 是否能区分工业机器人、人形机器人、核心零部件、软件控制、传感器和量产验证。主题扩散必须识别真实收入关联和伪相关风险。

## 2. M4 Prompt 输入

- Prompt ID：`PROMPT-THEME-EXPANSION`
- 研究问题：人形机器人主题如何扩散到可验证产业链环节？
- 输出要求：M3 Evidence Card、Evidence Chain、M6 Scorecard、Quality Gate、反方观点、不确定性和免责声明。

## 3. M3 Evidence 要求

| Evidence ID | Evidence Level | Confidence | Weight | Supports | Refutes | Missing Evidence |
|-------------|----------------|------------|--------|----------|---------|------------------|
| EV-20260710-RB01 | B | MEDIUM | 0.20 | 零部件订单或客户验证支持扩散 | 尚未形成规模收入 | 量产交付数据 |
| EV-20260710-RB02 | A | HIGH | 0.25 | 公司财报披露相关收入 | 收入占比仍低 | 客户集中度 |

## 4. M6 Scorecard 要求

Scorecard 必须检查 Theme Score、Evidence Score、Risk Score 和 Confidence Score。Quality Gate PASS 要求区分主题热度、产品验证和财务贡献。

## 5. 反方观点与不确定性

反方观点应包括量产慢于预期、成本下降不足、应用场景不足、客户订单取消或竞争路线变化。不确定性必须标注样机到量产的转换风险。

