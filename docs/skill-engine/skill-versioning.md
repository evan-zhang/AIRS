# Skill Versioning（Skill 版本管理）

## 1. 版本目标

Skill Versioning 保证 Skill 的输入、输出、依赖和治理状态可追溯。版本管理服务于可复现研究，不用于证明某个结论一定正确。

## 2. 版本格式

Skill 使用语义化版本：

- `v1.0.0`：首次生产可用版本。
- 补丁版本：修正文档表述、自检错误或审查清单，不改变输入输出。
- 次版本：新增可选输入、增强工作流或新增 Prompt 引用，保持兼容。
- 主版本：改变输入输出结构、调用协议或核心依赖，可能不兼容。

## 3. 依赖版本

Skill 必须记录依赖版本或路径：

- M4 Prompt 路径，例如 `prompts/supply-chain/chokepoint-analysis.md`。
- M2 Methodology 路径，例如 `docs/methodology/supply-chain-chokepoint.md`。
- M3 Evidence Schema 路径，例如 `schemas/evidence/evidence-card.schema.json`。
- Skill Schema 路径，例如 `schemas/skills/skill.schema.json`。

当依赖文件发生破坏性变化时，Skill 必须进入 Review 状态，不能继续以 Active 身份被生产调用。

## 4. 变更记录

每次 Skill 版本更新必须记录：

- 变更原因。
- 影响的输入输出字段。
- 影响的 Prompt、Methodology、Evidence 依赖。
- 是否需要重新跑 Benchmark。
- 是否需要人工复核。
- 是否影响历史报告解释。

## 5. 兼容策略

兼容版本允许旧调用继续执行，但必须在响应中返回当前 Skill 版本。非兼容版本必须新建版本号，并在注册表中保留旧版本的退役状态。历史报告只引用生成时使用的 Skill 版本，不自动升级解释。

## 6. 审计要求

Verification Agent 应检查 Skill 文档中的版本、注册表中的版本和 Completion Report 中的版本是否一致。若版本不一致，自检应 FAIL，并要求 Code Agent 修复。

## 7. 合规说明

**免责声明**：版本管理不能被解释为研究结论背书。任何版本的 Skill 输出都仅供研究参考，不构成投资建议，不提供交易指令或收益承诺。
