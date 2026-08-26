"""Git history helpers for pup-down."""

from datetime import datetime
import json
import os
from pathlib import Path
import subprocess
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

__all__ = [
    "local_last_changed",
    "remote_last_changed",
]


def local_last_changed(
    *,
    repo_root: Path,
    path: str,
) -> datetime | None:
    """Return when a local repository file was last changed in Git."""
    result = subprocess.run(
        [
            "git",
            "log",
            "-1",
            "--format=%cI",
            "--",
            path,
        ],
        cwd=repo_root,
        capture_output=True,
        text=True,
        check=False,
    )

    if result.returncode != 0:
        return None

    value = result.stdout.strip()

    if not value:
        return None

    try:
        return datetime.fromisoformat(value)
    except ValueError:
        return None


def remote_last_changed(
    *,
    repository: str,
    path: str,
    ref: str,
) -> datetime | None:
    """Return when a file was last changed in a GitHub repository."""
    encoded_path = quote(path, safe="/")

    url = (
        f"https://api.github.com/repos/{repository}/commits"
        f"?path={encoded_path}&sha={quote(ref, safe='')}&per_page=1"
    )

    headers = {
        "User-Agent": "pup-down",
        "Accept": "application/vnd.github+json",
    }

    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")

    if token:
        headers["Authorization"] = f"Bearer {token}"

    request = Request(url, headers=headers)

    try:
        with urlopen(request, timeout=30) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except HTTPError, URLError, json.JSONDecodeError:
        return None

    if not payload:
        return None

    value = payload[0].get("commit", {}).get("committer", {}).get("date")

    if not value:
        return None

    try:
        return datetime.fromisoformat(value)
    except ValueError:
        return None
