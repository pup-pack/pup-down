"""Command-line interface for pup-down.

Compare the current repository infrastructure with its canonical templates.

Commands:
uv run pup-down

Equivalent uvx usage after release:
uvx pup-down
uvx pup-down@latest
"""

import argparse
from collections.abc import Sequence
from pathlib import Path

from pup_down.commands import update

__all__ = ["build_parser", "main"]


def build_parser() -> argparse.ArgumentParser:
    """Build the argument parser."""
    parser = argparse.ArgumentParser(
        prog="pup-down",
        description=(
            "Compare the current repository infrastructure with the "
            "canonical templates and report template drift."
        ),
    )

    parser.add_argument(
        "--root",
        type=Path,
        default=None,
        help=(
            "Repository root to update. Defaults to the nearest parent "
            "directory containing .git, or the current directory."
        ),
    )
    parser.add_argument(
        "--templates",
        default="pup-pack/templates",
        help=(
            "GitHub owner/repo for canonical templates. Defaults to pup-pack/templates."
        ),
    )
    parser.add_argument(
        "--ref",
        default="main",
        help="Git ref, branch, or tag to fetch templates from. Defaults to main.",
    )
    parser.add_argument(
        "--templates-path",
        type=Path,
        default=None,
        help=(
            "Optional local templates repository path. If provided, templates "
            "are read from disk instead of GitHub raw URLs."
        ),
    )

    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Run the command-line interface.

    Args:
        argv: Optional command-line arguments. If None, uses sys.argv.

    Returns:
        Exit code from the update command.
    """
    parser = build_parser()
    args = parser.parse_args(argv)

    return update.run(
        root=args.root,
        templates=args.templates,
        ref=args.ref,
        templates_path=args.templates_path,
    )


if __name__ == "__main__":
    raise SystemExit(main())
