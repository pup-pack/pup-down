# pup-down: Reports Repo Infrastructure Changes That Belong in Templates

[![PyPI](https://img.shields.io/pypi/v/pup-down?logo=pypi&label=pypi)](https://pypi.org/project/pup-down/)
[![Docs Site](https://img.shields.io/badge/docs-site-blue?logo=github)](https://pup-pack.github.io/pup-down/)
[![Repo](https://img.shields.io/badge/repo-GitHub-black?logo=github)](https://github.com/pup-pack/pup-down)
[![Python 3.15](https://img.shields.io/badge/python-3.15%2B-blue?logo=python)](https://github.com/pup-pack/pup-down/blob/main/pyproject.toml)
[![uv managed](https://img.shields.io/badge/uv-managed-DE5FE9)](https://docs.astral.sh/uv/)
[![ty type checked](https://img.shields.io/badge/ty-type_checked-2F80ED)](https://docs.astral.sh/ty/)
[![Zensical docs](https://img.shields.io/badge/Zensical-docs-purple)](https://zensical.org/)
[![MIT](https://img.shields.io/badge/license-MIT-yellow.svg)](https://github.com/pup-pack/pup-down/blob/main/LICENSE)

[![CI](https://github.com/pup-pack/pup-down/actions/workflows/ci-python-zensical.yml/badge.svg?branch=main)](https://github.com/pup-pack/pup-down/actions/workflows/ci-python-zensical.yml)
[![Docs-Deploy](https://github.com/pup-pack/pup-down/actions/workflows/deploy-zensical.yml/badge.svg?branch=main)](https://github.com/pup-pack/pup-down/actions/workflows/deploy-zensical.yml)
[![Pre-Release](https://github.com/pup-pack/pup-down/actions/workflows/pre-release.yml/badge.svg?branch=main)](https://github.com/pup-pack/pup-down/actions/workflows/pre-release.yml)
[![Release](https://github.com/pup-pack/pup-down/actions/workflows/release-pypi.yml/badge.svg)](https://github.com/pup-pack/pup-down/actions/workflows/release-pypi.yml)
[![Links](https://github.com/pup-pack/pup-down/actions/workflows/links.yml/badge.svg?branch=main)](https://github.com/pup-pack/pup-down/actions/workflows/links.yml)
[![Dependabot](https://img.shields.io/badge/Dependabot-enabled-brightgreen.svg)](https://github.com/pup-pack/pup-down/security)

<img
src="https://raw.githubusercontent.com/pup-pack/pup-down/main/docs/images/pup.png"
alt="pup logo"
width="110">

> Report-only. Compares the active repository's infrastructure
> against canonical templates and lists the files the repo
> has moved ahead on that may be worth copying back upstream.

## Purpose

Professional Python repositories commonly share infrastructure such as:

- editor and Git configuration
- ignore and line-ending rules
- Markdown, YAML, and link checking
- formatting, linting, type checking, and testing
- documentation tooling
- continuous integration
- package and release validation

`pup-down` makes it easy to identify infrastructure improvements made
during recent work that should possibly be copied back to the canonical
templates.

## Benefits

`pup-down` is **report-only**.
Each repository fetches the current baseline and compares it with its
own infrastructure.
Nothing reaches in from a central place, so:

**Repo owner is in control.** Run it when you choose.
No files are updated.
A list of changes to possibly copy to the
canonical template files is provided.

Templates are fetched by **immutable commit SHA**,
so an update always reflects the latest push to the template repository
and every run is pinned to an exact template commit.

Repo type is inferred from the presence of key files
so no extensive configuration is needed.
For example:

- ALL REPOS
- `pyproject.toml` indicates ALL PY REPOS
- `pyproject.toml` + `src` indicates ALL PY SRC REPOS

## Default Template Source

- [templates](https://github.com/pup-pack/templates)

## Compare a Repo with Templates

```shell
# compare with canonical templates
uvx pup-down@latest

# compare using the latest published pup-down version
uvx pup-down@latest
```

## Developer Command Reference

<details>
<summary>Show command reference</summary>

### In a machine terminal

Open a machine terminal where you want the project:

```shell
git clone https://github.com/pup-pack/pup-down

cd pup-down
code .
```

### In a VS Code terminal

```shell
uv self update
uv python pin 3.15

uv python install
uv lock --upgrade
uv sync

uv run pre-commit install
uv run pre-commit autoupdate

git add -A
uv run pre-commit run --all-files
# repeat if changes were made
uv run pre-commit run --all-files

# run locally to test
uv run pup-down

# types, tests, docs
uv run ty check
uv run python -m pytest
uv run python -m zensical build

# save progress
git add -A
git commit -m "update"
git push -u origin main
```

</details>

## Documentation

- [Documentation](https://pup-pack.github.io/pup-down/)

## Annotations

[.annotations/annotations.md](https://github.com/pup-pack/pup-down/blob/main/.annotations/annotations.md)

## Citation

[CITATION.cff](https://github.com/pup-pack/pup-down/blob/main/CITATION.cff)

## License

[MIT](https://github.com/pup-pack/pup-down/blob/main/LICENSE)
