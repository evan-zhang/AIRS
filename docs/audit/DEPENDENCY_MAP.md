# AIRS Dependency Map

审计日期：2026-07-10

## Current Runtime Dependency Graph

```mermaid
flowchart TD
    User[User / Research Request]
    CLI[CLI: cli/commands]
    API[API: api/routes]
    Web[Static Web UI]
    App[APP-001: apps/equity_research]

    Planner[Planner: planner]
    Contract[Shared Contract: common/contract.py]
    Runtime[Runtime: runtime]
    Connectors[Data Connectors: data_connectors]
    Investment[Investment Engine: investment_engine]
    Committee[Committee: committee]
    Report[Report Generator: report_generator]
    Workspace[Workspace: workspace]
    RuntimeMemory[Runtime Memory: runtime/memory_manager.py]
    Learning[Learning: learning]

    Schema[schemas]
    Templates[templates]
    Prompts[prompts]
    Skills[skills]
    Docs[docs]

    User --> CLI
    User --> API
    Web --> API
    CLI --> App
    API --> App
    API --> Workspace

    App --> Planner
    Planner --> Contract
    Planner --> Runtime
    App --> Runtime
    Runtime --> Contract

    App --> Connectors
    App --> Investment
    App --> Committee
    App --> Report
    App --> RuntimeMemory
    App --> Learning

    Investment --> Report
    Investment --> Schema
    Report --> Templates
    Report --> Schema
    Connectors --> Schema
    Planner --> Schema
    Committee --> Schema

    Prompts -. referenced by .-> Report
    Skills -. referenced by .-> App
    Docs -. referenced by .-> Planner
    Docs -. referenced by .-> Runtime
```

## Intended Architecture vs Current Implementation

Intended chain:

```mermaid
flowchart LR
    Planner --> Orchestrator --> Runtime --> Connector --> Evidence --> KG --> Score --> Committee --> Report --> Workspace --> Memory --> Learning
```

Current implementation:

```mermaid
flowchart LR
    Planner --> Runtime
    Planner --> Contract
    Runtime --> Contract
    App[APP-001] --> Connector
    App --> Investment
    App --> Committee
    App --> Report
    App --> RuntimeMemory
    App --> Learning
    App -. builds locally .-> Evidence
    App -. builds locally .-> KG
    App -. builds locally .-> Score
    Investment -. builds locally .-> Evidence2[Evidence]
    Investment -. builds locally .-> KG2[KG]
    Investment -. builds locally .-> Score2[Score]
```

## Import-Based Observations

Observed import edges:

- `planner/engine.py` imports `common` and `runtime` references.
- `planner/runtime.py` imports `common`.
- `runtime/core.py` imports `common`.
- `apps/equity_research` imports `committee`, `data_connectors`, `investment_engine`, `learning`, `planner`, `report_generator`, `runtime`.
- `api/routes` imports `apps`, `runtime`, `workspace`.
- `cli/commands` imports `apps`.
- `tests/production-e2e` imports almost every Core module, but relies on harness semantics.

## Boundary Risks

1. Orchestrator is referenced by docs and Planner infrastructure refs, but has no executable top-level module.
2. Evidence, KG and Score exist as schemas/docs/modules unevenly; APP-001 and Investment Engine build these objects locally.
3. API and CLI are correctly thin, but inherit APP-001's boundary ambiguity.
4. Workspace, Runtime Memory and Learning are parallel concepts, not a single lifecycle model.

## Stable Dependency Target

Recommended v1.0 Stable minimal target:

```mermaid
flowchart LR
    CLI --> App
    API --> App
    App --> Planner
    Planner --> Runtime
    Runtime --> Contract
    App --> Connectors
    App --> EvidenceValidator[Evidence Validator]
    App --> KGValidator[KG Validator]
    App --> ScoreValidator[Score Validator]
    App --> Committee
    App --> Report
    Report --> QualityGate[Quality Gate]
```

This target avoids a large rewrite while closing the highest-risk contract gaps.
