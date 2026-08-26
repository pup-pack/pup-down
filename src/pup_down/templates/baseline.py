"""Baseline layer inference and managed file declarations."""

from pathlib import Path

from pup_down.templates.types import (
    TemplateFile,
    TemplateSnapshot,
)

__all__ = ["PRESERVE_PATTERNS", "infer_layers"]

PRESERVE_PATTERNS: tuple[str, ...] = (
    "README.md",
    "artifacts/**",
    "data/**",
    "docs/**",
    "notebooks/**",
    "sql/**",
    "src/**",
    "tests/**",
)


def infer_layers(*, repo_root: Path, repo_name: str, files: set[str]) -> list[str]:
    """Infer additive template layers based strictly on file existence."""
    # 1. Identify physical markers
    has_py = "pyproject.toml" in files
    has_src = (repo_root / "src").is_dir()
    is_ts = "package.json" in files

    # 2. Build Layers (Ordered by specificity)
    layers: list[str] = ["ALL"]

    # Base Tooling
    if has_py:
        layers.append("ALL-PY")
    elif is_ts:
        layers.append("ALL-TS")

    # Structural Overlays
    if has_py and has_src:
        layers.append("ALL-PY-SRC")

    return layers


def list_template_files(
    *,
    snapshot: TemplateSnapshot,
    layers: tuple[str, ...] | list[str],
) -> list[TemplateFile]:
    """Return effective template files for the selected additive layers.

    Later layers override earlier layers for the same target path.

    Args:
        snapshot: Resolved canonical template snapshot.
        layers: Ordered additive template layers.

    Returns:
        Effective template files ordered by target path.
    """
    by_target: dict[str, TemplateFile] = {}

    for layer in layers:
        layer_root = snapshot.root / layer

        if not layer_root.is_dir():
            continue

        for source_path in sorted(layer_root.rglob("*")):
            if not source_path.is_file():
                continue

            relative_path = source_path.relative_to(layer_root).as_posix()

            if _ignore_template_internal_file(relative_path):
                continue

            target_path = relative_path.removesuffix(".template")

            by_target[target_path] = TemplateFile(
                layer=layer,
                template_path=relative_path,
                target_path=target_path,
            )

    return sorted(
        by_target.values(),
        key=lambda item: item.target_path,
    )


def _ignore_template_internal_file(path: str) -> bool:
    """Return whether a template repository file is internal metadata."""
    path_obj = Path(path)

    if path_obj.name == ".DS_Store":
        return True

    if "__pycache__" in path_obj.parts:
        return True

    return path_obj.suffix == ".pyc"
