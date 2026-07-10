# Knowledge Graph Engine 工作流

**归属 Feature**：FEATURE-002 Knowledge Graph Engine  
**免责声明**：本文档仅用于 AIRS 工程开发、投资研究质量控制和系统验证，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## 1. 输入

知识图谱构建需要四类输入：

- 研究问题：必须明确产业、公司、产品、政策或风险边界。
- Methodology 引用：至少一个 M2 方法论，例如 `supply-chain-chokepoint`。
- Evidence Card：来自 M3 Evidence Engine，包含 `evidence_id`、来源、支持命题、反方观点、缺失证据和权重。
- 实体与关系草稿：由 Research Agent 根据方法论拆解得出。

## 2. 构建步骤

1. 定义图谱 ID、标题、研究问题和版本。
2. 装载 Evidence Card，并确认每张证据卡满足 M3 Schema。
3. 创建节点，节点必须包含 `node_id`、`node_type`、`label`、`source_refs`、`confidence`。
4. 创建边，边必须包含 `edge_id`、`from_node`、`to_node`、`relation_type`、`evidence_refs`、`directionality`。
5. 对关键节点补充 `attributes`，用于卡点分析，例如供给稀缺、替代难度、扩产难度、认证周期、议价能力和证据质量。
6. 运行 Validator，修复未知节点、未知 Evidence、非法类型和缺失免责声明。
7. 运行 Path Analyzer，生成至少一条从上游约束到下游影响的传导路径。
8. 运行 Chokepoint Analyzer，生成至少一个卡点分析结果。

## 3. Review 要点

Review Agent 应检查：

- 图谱是否引用 M2 Methodology。
- 节点和边是否都绑定 Evidence 或 source refs。
- 反方证据是否真实存在，而不是空泛陈述。
- `missing_evidence` 是否说明仍需追踪的产能、交期、良率、临床数据、政策变量或商业化数据。
- 卡点分数是否被正确解释为研究质量控制信号，而不是投资评级。

## 4. 失败场景

- 只有节点没有边，无法形成可解释路径。
- 边引用不存在的 Evidence Card。
- 把行业热度、股价表现或市场传闻当成卡点证据。
- 示例输出没有免责声明。
- 路径分析没有证据覆盖。
- 卡点分析没有反方证据或缺失证据。

## 5. 输出

标准输出应包含完整 JSON 图谱、路径分析、卡点分析和合规免责声明。Markdown 报告可引用 `templates/knowledge-graph/knowledge-graph-template.md`，分析摘要可引用 `templates/knowledge-graph/chokepoint-analysis-template.md`。

