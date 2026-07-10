# Knowledge Graph 输出模板

**Graph ID**：`{{graph_id}}`  
**标题**：`{{title}}`  
**研究问题**：`{{research_question}}`  
**Methodology 引用**：`{{methodology_refs}}`  

## 1. 节点

逐项列出节点 ID、类型、标签、置信度、source refs 和 Evidence Binding。节点类型必须来自受控集合：company、industry、product、supply_chain_node、policy、event、evidence、claim、risk。

## 2. 关系

逐项列出边 ID、起点、终点、关系类型、Evidence refs、反方证据、缺失证据和方向性。关系类型必须来自受控集合：supports、refutes、depends_on、belongs_to、affected_by、competes_with、has_risk。

## 3. 路径分析

列出关键路径的节点序列、边序列、证据覆盖、路径置信度和解释。路径分析只描述研究推理链，不输出投资操作建议。

## 4. 卡脖子分析

列出候选卡点节点、分数、风险等级、驱动因素、证据、反方证据和缺失证据。分数只用于研究质量控制，不构成评级。

## 5. 免责声明

本图谱仅用于 AIRS 工程开发、投资研究质量控制和系统验证，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

