# Outcome Tracking

## 1. 目标

Outcome Tracking 用于比较研究报告中的预期、假设和不确定性标注与后续可观察结果之间的差异。它不是价格预测模块，也不生成交易信号，只用于评估研究质量和校准证据权重。

## 2. Outcome Record

Outcome Record 至少包含 research_ref、expected_result、observed_result、horizon、variance_level、evidence_refs 和 lessons。expected_result 必须来自报告或 Committee 记录，observed_result 必须来自可审计来源。

## 3. 使用方式

当 Outcome 与研究预期差异较大时，Learning Engine 不直接判定研究错误，而是检查是否存在证据不足、反方观点薄弱、评分过度自信或方法论适用边界不清。差异会进入 Pattern Miner，并可能生成 score_calibration 建议。

## 4. 约束

Outcome Tracking 不允许输出买卖建议、目标价或收益承诺。它只说明研究流程需要改进的环节。

## 免责声明

本文档仅用于 AIRS 工程开发、研究质量控制和持续改进，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

