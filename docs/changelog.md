# Changelog

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
