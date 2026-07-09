# Benchmark Classification（Benchmark 分类标准）

**归属 Milestone**：M7: Benchmark & Production Examples  
**版本**：v0.7.0  
**最后更新**：2026-07-10

**免责声明**：本文档仅定义 AIRS Benchmark 分类规则，不构成投资建议，不提供交易指令、价格预测或收益承诺。

## 1. 分类目标

Benchmark 分类用于保证测试覆盖均衡。分类不代表行业投资价值排序，也不代表 AIRS 对任何资产的偏好。

分类目标：

- 覆盖 M2 方法论。
- 覆盖 M3 Evidence 类型。
- 覆盖 M6 Score 维度。
- 覆盖正例、边界例、反例。
- 支持 M8 扩展为 300+ 可执行用例。

## 2. 行业分类

| 分类 | 目录 | 典型场景 | 推荐方法论 |
|------|------|----------|------------|
| AI | `benchmark/ai/` | 算力供需、模型应用、AI 服务器、云厂商 CapEx | supply-chain-chokepoint, theme-expansion, risk |
| Semiconductor | `benchmark/semiconductor/` | 先进制程、设备材料国产化、库存周期 | supply-chain-chokepoint, industry-lifecycle, financial-anomaly |
| Innovative Drug | `benchmark/innovative-drug/` | 临床进展、医保准入、商业化、管线风险 | policy-driven, risk, valuation |
| Robotics | `benchmark/robotics/` | 零部件降本、量产节奏、人形机器人主题扩散 | theme-expansion, supply-chain-chokepoint, counter-consensus |
| New Energy | `benchmark/new-energy/` | 电池材料、储能、光伏供需、政策驱动 | industry-lifecycle, policy-driven, risk |
| General | `benchmark/general/` | 报告格式、证据链、评分卡、合规边界 | evidence-chain, risk, counter-consensus |

## 3. 方法论分类

每个 Benchmark 必须至少映射一个 M2 方法论：

- `supply-chain-chokepoint`：检查关键环节、瓶颈证据、替代路径。
- `theme-expansion`：检查主题传播路径、受益链条和伪相关剔除。
- `industry-lifecycle`：检查成长、成熟、衰退阶段判断。
- `policy-driven`：检查政策文本、执行路径和落地不确定性。
- `financial-anomaly`：检查财务口径、异常指标和解释替代性。
- `valuation`：检查估值方法适配性和敏感性，不输出价格预测。
- `risk`：检查风险触发条件、影响路径和缓释因素。
- `counter-consensus`：检查反共识证据和反方观点强度。
- `evidence-chain`：检查证据卡、证据关系和缺失证据。

## 4. 难度分类

| 难度 | 定义 | 期望能力 |
|------|------|----------|
| EASY | 单一行业、单一方法论、证据需求明确 | 能按模板输出完整结构 |
| MEDIUM | 多证据、多维度评分、存在轻微反证 | 能处理证据权重和不确定性 |
| HARD | 多行业、多方法论、存在强反方或数据冲突 | 能做情景化判断和 Quality Gate 解释 |

## 5. 用例类型

| 类型 | 目的 | 示例 |
|------|------|------|
| POSITIVE | 验证 Agent 能输出合格研究报告 | AI 服务器供应链卡点 |
| BOUNDARY | 验证 Agent 能处理证据不足 | 创新药临床数据未读出 |
| NEGATIVE | 验证 Agent 能拒绝违规或低质量输出 | 用户要求交易动作 |
| REGRESSION | 固定回归样例 | 完整投资研究报告 |
| COMPLIANCE | 检查免责声明和禁用表达 | 报告合规边界 |

## 6. 评分映射

分类文件不定义新评分，只引用 M6：

- Evidence Score：检查 Evidence Level、Confidence、Weight、supports、refutes、missing_evidence。
- Methodology Score：检查是否遵循 M2 Workflow。
- Prompt Score：检查 M4 Prompt 输入输出格式。
- Skill Score：检查 M5 Skill 调用、Failure Handling 和依赖引用。
- Report Score：检查报告结构、反方观点、不确定性和免责声明。
- Risk Score：检查风险识别和风险披露。
- Confidence Score：检查结论置信度是否与证据一致。
- Overall Score：聚合为 Scorecard，并进入 Quality Gate。

## 7. 覆盖率指标

M7 种子覆盖要求：

- 6 个行业分类均有 5 个基准文件。
- 每个行业至少引用 2 种方法论。
- 每个行业均包含 Gold Standard、Evaluation Criteria、Expected Output 和 Failure Cases。
- 所有行业文件均包含免责声明。

M8 扩展目标：

- 每个行业至少 50 个可执行 case。
- 每个方法论至少 30 个 case。
- 每个 Score 维度至少 20 个回归样例。

