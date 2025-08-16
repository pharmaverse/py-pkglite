# Changelog

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
