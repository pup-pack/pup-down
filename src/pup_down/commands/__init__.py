"""Command modules for pup-down.

Each command module exposes a stable run(...) -> int entry point.

The CLI parser lives in pup_down.cli.
Behavior lives here.
"""

from pup_down.commands import update

__all__ = ["update"]
