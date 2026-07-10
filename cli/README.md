# AIRS CLI

免责声明：AIRS CLI 仅用于投资研究流程编排、证据追溯和工程质量控制，不构成投资建议，不提供荐股、自动交易、交易指令、目标价或收益承诺。

## Commands

- `python3 cli/airs.py init`：初始化 `.airs/airs.yaml`。
- `python3 cli/airs.py run "分析 NVIDIA 的财务、估值、供应链和风险" --symbol NVDA --market US --output runs/nvidia.json --markdown runs/nvidia.md`：运行研究任务。
- `python3 cli/airs.py demo nvidia`：运行内置 Demo。
- `python3 cli/airs.py validate`：运行产品化验证。
- `python3 cli/airs.py validate --all`：运行全部 `scripts/validate_*.py`。

CLI 使用 Python 标准库 `argparse`，直接调用 `apps/equity_research` 的 APP-001 编排入口，不引入第三方依赖。

