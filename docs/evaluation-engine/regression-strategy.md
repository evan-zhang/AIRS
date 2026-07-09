# Regression Strategy（回归策略）

**归属 Milestone**：M6 Score Engine & Evaluation Engine  
**版本**：v0.6.0  
**最后更新**：2026-07-10

**免责声明**：回归策略用于系统质量验证，不构成投资建议或投资评级。

## 1. 目标

Regression Strategy 确保 M6 新增的 Score Engine 和 Evaluation Engine 不破坏 M1-M5 已通过交付物，并为 M7 Benchmark 建立可重复验证路径。

## 2. 回归范围

- M1：目录、顶层文档、自检脚本。
- M2：方法论 16 section 与 Future Score Mapping。
- M3：Evidence Card、Evidence Chain、Evidence Level、Confidence、Weight。
- M4：Prompt Engine、Prompt Schema、生产版 Prompt。
- M5：Skill Engine、Skill Schema、生产版 Skill。
- M6：Score docs、scoring docs、score schema、templates、evaluation docs。

## 3. 回归命令

```bash
python3 scripts/validate_m1.py
python3 scripts/validate_m2.py
python3 scripts/validate_evidence.py
python3 scripts/validate_prompt.py
python3 scripts/validate_skill.py
python3 scripts/validate_score.py
python3 scripts/validate_evaluation.py
```

全部必须 PASS。

## 4. 失败处理

- 结构缺失：补齐文件或路径。
- Schema 失败：修复 JSON 格式和必需字段。
- 一致性失败：优先修改 M6 新增文件，不修改 M1-M5 已 PASS 文件。
- 合规失败：删除违规表达并补充免责声明。

## 5. M7 扩展

M7 Benchmark 应把每个质量门禁转换为测试用例，记录输入、预期 Gate、实际 Gate 和差异解释。

