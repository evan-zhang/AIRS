"""Stable release gate helpers.

These checks intentionally separate structural/demo success from real-data
release readiness. Mock, skip, fallback, and unknown sources are degraded and
must not be counted as real production PASS.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


DISCLAIMER = "AIRS Stable 发布门禁仅用于工程质量检查，不构成投资建议。"
DEGRADED_MODE_PREFIXES = ("mock", "skip", "fallback", "unknown")


@dataclass
class ReleaseGateResult:
    passed: bool
    status: str
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    unverified: list[str] = field(default_factory=list)
    details: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "passed": self.passed,
            "status": self.status,
            "errors": self.errors,
            "warnings": self.warnings,
            "unverified": self.unverified,
            "details": self.details,
            "disclaimer": DISCLAIMER,
        }


def mode_is_degraded(mode: str | None) -> bool:
    normalized = str(mode or "unknown").strip().lower()
    return not normalized or normalized.startswith(DEGRADED_MODE_PREFIXES)


def evaluate_connector_lineage(
    lineage: dict[str, Any],
    *,
    require_real_sources: bool,
    min_real_sources: int = 1,
    allow_degraded: bool = False,
) -> ReleaseGateResult:
    real_sources = list(lineage.get("real_sources", []))
    degraded_sources = sorted(
        set(
            list(lineage.get("mock_sources", []))
            + list(lineage.get("skipped_sources", []))
            + list(lineage.get("fallback_sources", []))
            + list(lineage.get("unknown_sources", []))
        )
    )
    errors: list[str] = []
    warnings: list[str] = []

    if require_real_sources and len(real_sources) < min_real_sources:
        errors.append(f"real source count {len(real_sources)} is below required minimum {min_real_sources}")
    if require_real_sources and degraded_sources and not allow_degraded:
        errors.append(f"degraded sources are not allowed for Stable real-data PASS: {degraded_sources}")
    if degraded_sources:
        warnings.append(f"degraded sources present: {degraded_sources}")

    status = "PASS" if not errors else "FAIL"
    return ReleaseGateResult(
        passed=not errors,
        status=status,
        errors=errors,
        warnings=warnings,
        details={
            "real_sources": real_sources,
            "degraded_sources": degraded_sources,
            "require_real_sources": require_real_sources,
            "min_real_sources": min_real_sources,
            "allow_degraded": allow_degraded,
        },
    )


def unverified_gate(reason: str, *, details: dict[str, Any] | None = None) -> ReleaseGateResult:
    return ReleaseGateResult(
        passed=False,
        status="UNVERIFIED",
        unverified=[reason],
        details=details or {},
    )
