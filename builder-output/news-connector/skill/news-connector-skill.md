# News Connector Skill 草案

**Feature**：FEATURE-NEWS-001  
**Skill 模板引用**：`templates/skill-template.md`  
**Skill Engine 引用**：`docs/skill-engine/skill-architecture.md`、`docs/skill-engine/skill-invocation.md`  

## 1. Purpose

News Connector Skill 负责把新闻事件转换为 AIRS 研究流程可消费的结构化事件对象和 Evidence Card 引用。它不判断投资动作，不重写新闻事件方法论。

## 2. Inputs

- `news_items`：新闻标题、正文摘要、来源、URL、发布时间。
- `target_scope`：行业、公司、政策或主题范围。
- `methodology_refs`：政策驱动、主题扩散、证据链等方法论引用。
- `evidence_policy`：M3 Evidence 验证要求引用。

## 3. Outputs

- `normalized_events`：归一化新闻事件。
- `evidence_cards`：新闻对应 Evidence Card 草案或引用。
- `impact_hypotheses`：影响假设，必须标注不确定性。
- `counter_sources`：冲突或反方来源。
- `missing_evidence`：缺失证据。
- `disclaimer`：合规免责声明。

## 4. Workflow

1. 校验新闻来源、发布时间和 URL。
2. 抽取事件、实体、影响对象和事实陈述。
3. 区分事实、媒体解读和研究推断。
4. 生成 Evidence Card 引用并绑定 M3 字段。
5. 输出反方来源、缺失证据、不确定性和免责声明。

## 5. Failure Handling

- `FAIL_SOURCE_UNTRUSTED`：来源无法识别或可信度过低。
- `FAIL_EVENT_AMBIGUOUS`：事件类型或主体不清。
- `FAIL_EVIDENCE_INSUFFICIENT`：缺少可追溯来源。
- `FAIL_COMPLIANCE`：用户要求买卖建议、目标价或收益承诺。

## 6. 免责声明

本 Skill 草案仅用于 AIRS 工程开发与投资研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

