"""Typed records for pup-down comparison."""

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Literal

from pup_core.base.types import RepositoryContext

__all__ = [
    "ComparisonFile",
    "ComparisonPlan",
    "FileStatus",
]


FileStatus = Literal[
    "current",
    "different",
    "repo-newer",
    "template-newer",
    "added-in-repo",
    "deleted-in-repo",
]


@dataclass(frozen=True)
class ComparisonFile:
    """A single scaffolding file considered by pup-down."""

    path: Path
    status: FileStatus
    source_layer: str | None
    source_path: str | None
    repo_text: str | None
    template_text: str | None
    repo_changed: datetime | None = None
    template_changed: datetime | None = None


@dataclass(frozen=True)
class ComparisonPlan:
    """Complete read-only comparison for a target repository."""

    target: RepositoryContext
    layers: tuple[str, ...]
    files: tuple[ComparisonFile, ...]
