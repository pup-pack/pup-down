# pup-down

<img src="images/pup.png" alt="pup logo" width="110">

`pup-down` identifies repository infrastructure changes that may belong
in the canonical project templates.

It is a read-only companion to `pup-up`.

Where `pup-up` brings maintained template changes into a repository,
`pup-down` looks in the opposite direction: it compares the current
repository with its applicable templates and reports files that differ.

## Purpose

Professional Python repositories evolve during real project work.

A repository may contain a newer version of shared infrastructure such as:

- editor and Git configuration
- ignore and line-ending rules
- Markdown, YAML, and link-checking configuration
- Python tooling configuration
- documentation tooling configuration
- continuous integration workflows
- release and package validation surfaces

It can be difficult to remember which repository contains the newest
version of a shared file.

`pup-down` compares the current repository with the canonical templates
and identifies differences that may represent improvements that should
be moved down into the templates.

## Design Model

`pup-down` is intentionally read-only.

It:

1. **Detects the repository** and its applicable template layers.
2. **Fetches the canonical templates** used for that repository type.
3. **Compares managed files** in the repository with the template versions.
4. **Uses Git history** to determine which version changed more recently.
5. **Reports the result** without modifying either repository.

Typical results include:

- `CURRENT` when the repository and template versions match.
- `REPO NEWER` when the repository version changed more recently.
- `TEMPLATE NEWER` when the template version changed more recently.
- `DELETED IN REPO` when a managed template file is absent from the repository.

The result supports human review rather than automatic template modification.

## Template Layers

Templates are applied as ordered layers.

Later layers may override files from earlier layers.

The standard layer model increases in specificity:

- `ALL` for files shared by all repositories.
- `ALL-PY` for Python repository tooling.
- `ALL-PY-SRC` for Python repositories with a `src/` package layout.

Layers are additive across managed files while allowing a more specific
layer to supersede an earlier version of the same file.

## Repository Comparison

`pup-down` considers the managed files supplied by the applicable
template layers.

Project-specific source code, tests, notebooks, data, SQL files,
documentation, and other files outside the managed template baseline
are not candidates for template synchronization.

The command reports status only.

It does not copy files into the templates and does not modify the
current repository.

## See Also

- [API](./api.md)
