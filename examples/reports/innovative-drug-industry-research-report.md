# 创新药产业研究报告

**Report ID**：REPORT-20260710-INNOVATIVE-DRUG
**版本**：0.1.0
**方法论引用**：`supply-chain-chokepoint`, `industry-lifecycle`, `evidence-chain`

**免责声明**：本报告仅用于 AIRS 投资研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## 1. 报告元数据

- Report ID：`REPORT-20260710-INNOVATIVE-DRUG`
- 研究主题：创新药产业研究报告
- Prompt 引用：`prompts/report/generation.md`
- Skill 引用：`skills/report/report-skill.md`
- Evidence 数量：3
- KG 引用：`KG-20260710-INNOVATIVE-DRUG`
- Scorecard 引用：`SCORECARD-INNOVATIVE-DRUG-REPORT-001`

## 2. 研究问题与范围

创新药产业链中研发、临床、审评、商业化和支付环节的关键约束如何被证据验证？

## 3. 方法论引用

- `supply-chain-chokepoint`：沿用 M2 方法论，不在报告层重写研究规则。
- `industry-lifecycle`：沿用 M2 方法论，不在报告层重写研究规则。
- `evidence-chain`：沿用 M2 方法论，不在报告层重写研究规则。

## 4. 核心观点

创新药产业研究应把研发管线、临床成功率、审评政策、商业化能力和支付约束放在同一证据链中评估。 该观点至少引用 [EV-20260710-DRG1] 靶点发现到临床转化存在长周期约束（来源：AIRS 示例证据库；等级：B；置信度：0.72），并由 KG 卡点 `N-DRG-CLINICAL` 与 Scorecard `SCORECARD-INNOVATIVE-DRUG-REPORT-001` 共同约束。

## 5. Evidence 引用表

| Evidence ID | 标题 | 类别 | 来源类型 | 等级 | 权重 | 支持命题 | 反方或限制 |
|---|---|---|---|---|---:|---|---|
| EV-20260710-DRG1 | 靶点发现到临床转化存在长周期约束 | industry | industry_report | B | 0.34 | 临床转化和入组效率是创新药研发路径的重要约束。 | 突破性疗法和优先审评可能缩短部分项目周期。 |
| EV-20260710-DRG2 | CMC 与放大生产影响商业化进度 | supply_chain | expert_opinion | B | 0.33 | CMC、质量体系和放大生产会影响创新药上市与供应稳定性。 | 成熟 CDMO 资源可部分缓解生产放大瓶颈。 |
| EV-20260710-DRG3 | 医保准入与商业化放量不确定性 | counter_evidence | government_policy | B | 0.33 | 医保准入、支付能力和医生教育会影响商业化兑现。 | 仅用研发进度解释产业链约束是不完整的。 |

## 6. Evidence Chain 汇总

- [EV-20260710-DRG1] 靶点发现到临床转化存在长周期约束（来源：AIRS 示例证据库；等级：B；置信度：0.72）
- [EV-20260710-DRG2] CMC 与放大生产影响商业化进度（来源：AIRS 示例证据库；等级：B；置信度：0.7）
- [EV-20260710-DRG3] 医保准入与商业化放量不确定性（来源：AIRS 示例证据库；等级：B；置信度：0.68）

## 7. Knowledge Graph 汇总

- KG ID：`KG-20260710-INNOVATIVE-DRUG`
- 图谱标题：创新药产业链知识图谱
- 节点 / 关系 / 路径：6 / 5 / 1
- Top Chokepoint：临床试验入组与终点验证（节点：`N-DRG-CLINICAL`；分数：0.864；风险：HIGH）
- 卡点驱动：供给稀缺；替代难度高；扩产难度高；认证周期长；证据质量较高
- KG Evidence Refs：`EV-20260710-DRG1`, `EV-20260710-DRG2`, `EV-20260710-DRG3`

## 8. Score Summary

- Scorecard ID：`SCORECARD-INNOVATIVE-DRUG-REPORT-001`
- Overall Score / Grade：80 / B
- Confidence Score：75
- Quality Gate：`PASS`
- 维度分：Evidence Score: 81；Knowledge Graph Score: 80；Report Score: 85；Risk Score: 74；Counter Evidence Score: 78
- Score Evidence Refs：`EV-20260710-DRG1`, `EV-20260710-DRG2`, `EV-20260710-DRG3`
- Score Disclaimer：仅供研究参考，不构成投资建议

## 9. 反方观点

- 临床阶段数据不能简单外推为获批和商业化成功。
- 医保控费和医院准入可能压缩创新药商业化空间。
- 同靶点竞争、专利到期和国际化不确定性会削弱产业链判断。

## 10. 不确定性与缺口

- EV-20260710-DRG1: 需要补充具体适应症入组速度和终点达成数据。
- EV-20260710-DRG2: 需要补充具体产品批次成功率、质量偏差和产能利用率。
- EV-20260710-DRG3: 需要补充医保谈判结果、院内准入和真实世界使用数据。

## 11. 风险提示

- 证据口径、披露时点和统计样本可能不一致。
- Knowledge Graph 的路径与卡点结果依赖当前节点和边定义。
- Scorecard 是研究质量门禁，不代表投资评级或收益判断。

## 12. 免责声明

本报告仅用于 AIRS 投资研究质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。
