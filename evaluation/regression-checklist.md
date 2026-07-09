# Regression Checklist（回归检查清单）

**归属 Milestone**：M6  
**免责声明**：回归检查用于系统质量验证，不构成投资建议。

## 1. 自检命令

- [ ] `python3 scripts/validate_m1.py`
- [ ] `python3 scripts/validate_m2.py`
- [ ] `python3 scripts/validate_evidence.py`
- [ ] `python3 scripts/validate_prompt.py`
- [ ] `python3 scripts/validate_skill.py`
- [ ] `python3 scripts/validate_score.py`
- [ ] `python3 scripts/validate_evaluation.py`

## 2. 一致性检查

- [ ] Evidence Score 对接 Evidence Level / Confidence / Weight。
- [ ] Methodology Score 对接 M2 Future Score Mapping。
- [ ] Prompt Score 对接 M4 Prompt Engine。
- [ ] Skill Score 对接 M5 Skill Engine。
- [ ] Evaluation Gate 不重复定义 M2-M5 规则。

## 3. 失败处理

优先修复 M6 新增文件；如必须修改 M1-M5 文件，必须更新 CHANGELOG、新增 ADR，并在 M6 Completion Report 说明原因。

