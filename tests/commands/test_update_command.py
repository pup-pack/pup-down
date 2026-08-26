"""Tests for the update command."""

from pathlib import Path

from pytest import CaptureFixture

from pup_down.commands import update


def test_update_command_reports_current_file(
    tmp_path: Path,
    capsys: CaptureFixture[str],
) -> None:
    """The update command should report current files when content already matches."""
    repo = tmp_path / "example-python-repo"
    repo.mkdir()
    (repo / ".git").mkdir()
    (repo / "pyproject.toml").write_text(
        """
[project]
name = "example-python-repo"
version = "0.1.0"
""".strip()
        + "\n",
        encoding="utf-8",
    )
    (repo / ".editorconfig").write_text("root = true\n", encoding="utf-8")

    templates = tmp_path / "templates"
    (templates / "ALL").mkdir(parents=True)
    (templates / "ALL-PY").mkdir(parents=True)
    (templates / "ALL-PY-SRC").mkdir(parents=True)

    (templates / "ALL" / ".editorconfig").write_text(
        "root = true\n",
        encoding="utf-8",
    )

    exit_code = update.run(
        root=repo,
        templates_path=templates,
    )

    captured = capsys.readouterr()

    assert exit_code == 0
    assert "CURRENT       .editorconfig [ALL]" in captured.out
