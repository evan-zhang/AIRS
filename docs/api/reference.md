# AIRS API Reference

免责声明：AIRS API 仅用于投资研究流程编排、证据追溯和质量控制，不构成投资建议。

## GET /health

返回服务状态、版本、Python 版本和 endpoint 列表。

## GET /workspace

返回一个 Workspace 示例状态，包含 project、session、artifact、timeline 和 audit log。

## GET /memory

返回 Runtime Memory 示例状态。

## POST /research

运行通用研究任务。

请求示例：

```json
{
  "symbol": "NVDA",
  "market": "US",
  "research_question": "分析 NVIDIA 的财务、估值、供应链和风险"
}
```

## POST /company

运行公司研究任务。支持 `company`、`symbol`、`market`、`research_question`。

## POST /theme

运行主题研究任务。支持 `theme`、`symbol`、`market`。

## POST /report

运行报告生成型研究任务，返回 APP-001 完整结果。

所有响应均为 JSON，并包含 `disclaimer` 字段。

