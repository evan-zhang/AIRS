"""Template registry for AIRS Builder."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class ArtifactTemplate:
    """Registered template and output mapping for one generated artifact."""

    name: str
    template: str
    output: str
    is_json: bool = False

    def output_path(self, slug: str) -> Path:
        return Path(self.output.format(slug=slug))


ARTIFACTS: tuple[ArtifactTemplate, ...] = (
    ArtifactTemplate("issue", "templates/builder/issue-template.md", "ISSUE.md"),
    ArtifactTemplate("adr", "templates/builder/adr-template.md", "ADR.md"),
    ArtifactTemplate("feature_spec", "templates/builder/feature-spec-template.md", "FEATURE_SPEC.md"),
    ArtifactTemplate("skill", "templates/builder/skill-template.md", "skill/{slug}-skill.md"),
    ArtifactTemplate("prompt", "templates/builder/prompt-template.md", "prompt/{slug}-prompt.md"),
    ArtifactTemplate("schema", "templates/builder/schema-template.json", "schema/{slug}.schema.json", True),
    ArtifactTemplate("tests", "templates/builder/test-template.md", "tests/test-{slug}.md"),
    ArtifactTemplate("benchmark", "templates/builder/benchmark-template.md", "benchmark/{slug}-benchmark.md"),
    ArtifactTemplate("pr_checklist", "templates/builder/pr-checklist-template.md", "PR_CHECKLIST.md"),
    ArtifactTemplate("release_notes", "templates/builder/release-notes-template.md", "RELEASE_NOTES.md"),
)


def all_artifacts() -> tuple[ArtifactTemplate, ...]:
    """Return registered Builder artifacts in generation order."""

    return ARTIFACTS

