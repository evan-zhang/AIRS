# Recommendation Standards

免责声明：本文档仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

Investment Research Engine 通过 Runtime 调度 Recommendation Review，确保每条关键语句都能回到 Evidence、Score 和 Report 产物。

## Statement Types

### Fact

Fact 是可追溯证据直接支持的事实陈述。必须有 Evidence Card 引用，置信度通常高于 0.75，且文本应明确来自公告、报告、披露、公开数据或已记录 Connector Result。

### Inference

Inference 是从一个或多个 Fact 推导出来的分析判断。必须列出推导依据和证据引用，且需要标注置信度和可能推翻该推导的反方证据。

### Assumption

Assumption 是情景条件或模型前提。必须用“假设、若、如果、情景”等方式标明条件性，不得伪装成事实。Assumption 需要列出需要后续验证的数据。

### Opinion

Opinion 是研究者对证据强弱、研究优先级或复核路径的主观判断。Opinion 可以没有直接证据引用，但必须清楚标注为观点，不能变成交易指令。

## Mandatory Coverage

每份 Recommendation 至少包含一条 Fact、一条 Inference、一条 Assumption 和一条 Opinion。缺少任一类型时，质量门禁不得高于 CONDITIONAL_PASS。

## Forbidden Language

禁止输出确定性投资建议、买入或卖出指令、目标价、收益保证、盈利保证、自动化交易动作。Score、Grade、Gate、Research Stance 只能解释研究质量或后续复核优先级。

## Review Checklist

- 是否每条关键语句都有 statement type。
- Fact 是否有 Evidence Card。
- Inference 是否说明推导和反方证据。
- Assumption 是否条件化表达。
- Opinion 是否避免交易动作。
- Final Research Report 是否包含免责声明和缺失证据。
