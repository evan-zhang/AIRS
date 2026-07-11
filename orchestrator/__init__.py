"""AIRS Orchestrator boundary.

The Orchestrator is the only production bridge between Planner output and
Runtime execution. It validates workflow shape and delegates execution to
Runtime without importing app or business-domain modules.

DISCLAIMER: AIRS orchestrates research quality workflows only and does not
provide investment advice.
"""

from .core import Orchestrator, OrchestratorError, run_planned_workflow

__all__ = ["Orchestrator", "OrchestratorError", "run_planned_workflow"]
