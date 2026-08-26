"""Compare current repository scaffolding with canonical templates."""

from datetime import datetime

from pup_core.base.types import RepositoryContext

from pup_down.base.types import ComparisonFile, ComparisonPlan, FileStatus
from pup_down.git_history import local_last_changed, remote_last_changed
from pup_down.templates.baseline import list_template_files
from pup_down.templates.render import read_rendered_template
from pup_down.templates.types import TemplateSnapshot

__all__ = ["compare_repository_to_template"]


def compare_repository_to_template(
    *,
    repository: RepositoryContext,
    layers: tuple[str, ...],
    snapshot: TemplateSnapshot,
    template_repository: str,
) -> ComparisonPlan:
    """Compare repository scaffolding with the effective template baseline.

    Args:
        repository: Detected repository context.
        layers: Effective additive template layers for the repository.
        snapshot: Resolved canonical template snapshot.
        template_repository: GitHub owner/repo for canonical templates.

    Returns:
        Complete read-only comparison plan.
    """
    template_files = list_template_files(
        snapshot=snapshot,
        layers=layers,
    )

    comparisons: list[ComparisonFile] = []

    for template_file in template_files:
        target_path = repository.root / template_file.target_path

        template_text = read_rendered_template(
            snapshot=snapshot,
            template_file=template_file,
            repository=repository,
        )

        if not target_path.exists():
            comparisons.append(
                ComparisonFile(
                    path=target_path,
                    status="deleted-in-repo",
                    source_layer=template_file.layer,
                    source_path=template_file.template_path,
                    repo_text=None,
                    template_text=template_text,
                )
            )
            continue

        if not target_path.is_file():
            continue

        try:
            repo_text = target_path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue

        if repo_text == template_text:
            status: FileStatus = "current"
            repo_changed = None
            template_changed = None
        else:
            repo_changed = local_last_changed(
                repo_root=repository.root,
                path=template_file.target_path,
            )

            template_source_path = (
                f"{template_file.layer}/{template_file.template_path}"
            )

            if snapshot.from_local:
                template_changed = local_last_changed(
                    repo_root=snapshot.root,
                    path=template_source_path,
                )
            else:
                template_changed = remote_last_changed(
                    repository=template_repository,
                    path=template_source_path,
                    ref=snapshot.ref,
                )

            status = _classify_difference(
                repo_changed=repo_changed,
                template_changed=template_changed,
            )

        comparisons.append(
            ComparisonFile(
                path=target_path,
                status=status,
                source_layer=template_file.layer,
                source_path=template_file.template_path,
                repo_text=repo_text,
                template_text=template_text,
                repo_changed=repo_changed,
                template_changed=template_changed,
            )
        )

    return ComparisonPlan(
        target=repository,
        layers=layers,
        files=tuple(comparisons),
    )


def _classify_difference(
    *,
    repo_changed: datetime | None,
    template_changed: datetime | None,
) -> FileStatus:
    """Classify differing content using last-change Git timestamps."""
    if repo_changed is None or template_changed is None:
        return "different"

    if repo_changed > template_changed:
        return "repo-newer"

    if template_changed > repo_changed:
        return "template-newer"

    return "different"
