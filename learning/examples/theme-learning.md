# Theme Learning Example

## Feedback Input

- 主题研究的反方观点偏弱，只列出风险，没有形成可证伪假设。
- Committee 要求补充不同扩散路径下的失败场景。

## Pattern Mining

Learning Engine 将反馈归并为 `prompt/weak_counter_argument`，识别 Prompt 中反方观点约束不足。

## Rule Generation

生成规则候选：主题研究 Prompt 必须要求至少一个强反方观点、一个中等反方观点和一个弱反方观点，并说明证据等级。

## Optimization Suggestions

- Prompt：增加反方观点强度枚举。
- Skill：在主题扩散工作流中加入反方证据采集任务。
- Report：把反方观点与不确定性单独成节。

## 免责声明

本示例仅用于 AIRS 工程开发与研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

