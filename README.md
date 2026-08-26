# pup-down: Professional Python Project Updater (Move Updates Down to Templates)

[![PyPI](https://img.shields.io/pypi/v/pup-down?logo=pypi&label=pypi)](https://pypi.org/project/pup-down/)
[![Docs Site](https://img.shields.io/badge/docs-site-blue?logo=github)](https://pup-pack.github.io/pup-down/)
[![Repo](https://img.shields.io/badge/repo-GitHub-black?logo=github)](https://github.com/pup-pack/pup-down)
[![Python 3.15](https://img.shields.io/badge/python-3.15%2B-blue?logo=python)](./pyproject.toml)
[![License](https://img.shields.io/badge/license-MIT-yellow.svg)](./LICENSE)

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

> Opinionated professional Python project template updater.
> Shows when active repo has more recent files that
> should possibly be copied to templates/.

## Purpose

Professional Python repositories commonly share infrastructure such as:

- editor and Git configuration
- ignore and line-ending rules
- Markdown, YAML, and link checking
- formatting, linting, type checking, and testing
- documentation tooling
- continuous integration
- package and release validation

`pup-down` makes it easy to keep the template files commonly used in
professional projects current and consistent.

## Benefits

`pup-down` is **report-only**.
Each repository fetches the current baseline and applies it on its own terms.
Nothing reaches in from a central place, so:

- **Repo owner is in control.** Run it when you choose.
  No files are updated. A list of changes you might want to copy to the
  canonical template files are provide.

Templates are fetched by **immutable commit SHA**,
so an update always reflects the latest push to the template repository
and every run is pinned to an exact template commit.

Repo type is inferred from the presence of key files
so no extensive configuration is needed.
For example:

- ALL REPOS
- `pyproject.toml` indicates ALL PY REPOS
- `pyproject.toml` + `src` indicates ALL PY SRC REPOS

## Template Source

- [templates](https://github.com/pup-pack/templates)

## Update a Repo based on Templates

```shell
# see what's changed
uvx pup-down

# see what files the command would update (dry run, force latest version)
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

[.annotations/annotations.md](./.annotations/annotations.md)

## Citation

[CITATION.cff](./CITATION.cff)

## License

[MIT](./LICENSE)
