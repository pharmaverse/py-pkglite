# Changelog

## py-pkglite 0.1.9

### Documentation

- Improved installation instructions in `README.md` by adding explicit
  `pipx` installation command and adding option to use `uvx` to try the
  CLI tool without installing it (#53).

### Maintenance

- Added GitHub Actions workflow to run `ruff check` for code linting (#55).
- Updated GitHub Actions workflows to use `actions/checkout@v6` (#55).
- Updated badges in `README.md` (#55).

## py-pkglite 0.1.8

### Linting

- Added ruff linter configuration to `pyproject.toml` with popular rule sets
  including pycodestyle, Pyflakes, pyupgrade, flake8-bugbear, flake8-simplify,
  and isort (#50).
- Fixed `ruff check` linting issues including UP006, UP015, UP035, F401, E501,
  B007, B904, and SIM102 (#50).

## py-pkglite 0.1.7

### Maintenance

- Added Python 3.14 support and set as default development environment (#47).
- Updated GitHub Actions workflows to use the latest `checkout` and
  `setup-python` versions (#47).
- Refactored the logo generation script to use ImageMagick, removing the
  previous R and hexSticker dependency (#46).

## py-pkglite 0.1.6

### Documentation

- Switched all articles to native Markdown and simplified the docs sync process;
  removed `nbconvert` and `jupyter` from dev dependencies (#41).
- Added mypy and pharmaverse badges to the README (#39, #43).

## py-pkglite 0.1.5

### Typing

- Add mypy as a development dependency and resolve all mypy type checking issues (#34).

### Maintenance

- Add a GitHub Actions workflow to run mypy checks (#35).

### Documentation

- Shorten and improve clarity of the package description (#36).

## py-pkglite 0.1.4

### Maintenance

- Removed download statistics badge from `README.md` due to availability issues
  with the service (#28).
- Update documentation code font to improve readability (#29, #30).
- Use Python 3.13.7 for the default package development environment (#31).

## py-pkglite 0.1.3

### Maintenance

- Manage project with uv (#24).

## py-pkglite 0.1.2

### Documentation

- Use absolute URL to replace relative path for the logo image in `README.md`,
  to make it render properly on PyPI (#20).
- Improve logo and favicon images generation workflow for better font rendering (#22).

## py-pkglite 0.1.1

### Improvements

- Rewrite packed file parser with finite state machines to improve code readability (#16).
- Use isort to sort import statements for all Python files (#15).

## py-pkglite 0.1.0

### Typing

- Refactor type hints to use built-in generics and base abstract classes
  following typing best practices (#11).
- Use PEP 604 style shorthand syntax for union and optional types (#10).

### Bug fixes

- Use pathspec to handle ignore pattern matching. This makes the packing
  feature work properly under Windows (#7).

### Improvements

- Read and write text files using UTF-8 encoding on all platforms (#7).
