"""Exception types.

Repository-detection and path-safety errors are shared and re-exported from
pup-core so callers can catch them from a single pup-down namespace.
"""

from pup_core.base.errors import RepositoryDetectionError, UnsafePathError

__all__ = [
    "PupDownError",
    "RepositoryDetectionError",
    "TemplateFetchError",
    "UnsafePathError",
]


class PupDownError(Exception):
    """Base exception for pup-down."""


class TemplateFetchError(PupDownError):
    """Raised when template content cannot be fetched."""

    def __init__(self, message: str) -> None:
        """Initialize the error."""
        super().__init__(message)
