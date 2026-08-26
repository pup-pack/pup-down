"""Report repository scaffolding differences from the managed template baseline."""

from pathlib import Path

from pup_core.inspect.detect import detect_repository

from pup_down.compare import compare_repository_to_template
from pup_down.templates.baseline import infer_layers
from pup_down.templates.fetch import fetch_template_snapshot
from pup_down.templates.types import TemplateSource

__all__ = ["run"]


def run(
    *,
    root: Path | None = None,
    templates: str = "pup-pack/templates",
    ref: str = "main",
    templates_path: Path | None = None,
) -> int:
    """Report repository changes that may belong in the templates.

    Args:
        root: Repository root. If None, pup-down detects the current repo root.
        templates: GitHub owner/repo for canonical templates.
        ref: Git ref, branch, or tag.
        templates_path: Optional local templates repo path.

    Returns:
        Process exit code.
    """
    repository = detect_repository(root)

    layers = tuple(
        infer_layers(
            repo_root=repository.root,
            repo_name=repository.repo_name,
            files=set(repository.files),
        )
    )

    source = TemplateSource(
        repository=templates,
        ref=ref,
        local_path=templates_path,
    )

    with fetch_template_snapshot(source=source) as snapshot:
        plan = compare_repository_to_template(
            repository=repository,
            layers=layers,
            snapshot=snapshot,
            template_repository=templates,
        )

    for file in plan.files:
        relative_path = file.path.relative_to(repository.root)

        status = file.status.upper().replace("-", " ")
        layer = f" [{file.source_layer}]" if file.source_layer else ""

        print(f"{status:<13} {relative_path}{layer}")

    return 0
