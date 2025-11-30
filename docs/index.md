# pkglite for Python <img src="assets/logo.png" align="right" width="120" />

[![PyPI version](https://img.shields.io/pypi/v/pkglite)](https://pypi.org/project/pkglite/)
![Python versions](https://img.shields.io/pypi/pyversions/pkglite)
[![pharmaverse py-pkglite badge](http://pharmaverse.org/shields/pkglite.svg)](https://pharmaverse.org)
[![CI tests](https://github.com/pharmaverse/py-pkglite/actions/workflows/ci-tests.yml/badge.svg)](https://github.com/pharmaverse/py-pkglite/actions/workflows/ci-tests.yml)
[![Mypy check](https://github.com/pharmaverse/py-pkglite/actions/workflows/mypy.yml/badge.svg)](https://github.com/pharmaverse/py-pkglite/actions/workflows/mypy.yml)
[![Ruff check](https://github.com/pharmaverse/py-pkglite/actions/workflows/ruff-check.yml/badge.svg)](https://github.com/pharmaverse/py-pkglite/actions/workflows/ruff-check.yml)
[![mkdocs](https://github.com/pharmaverse/py-pkglite/actions/workflows/mkdocs.yml/badge.svg)](https://pharmaverse.github.io/py-pkglite/)
![License](https://img.shields.io/pypi/l/pkglite)

A simple framework for packing source projects of any language into portable
text files and restoring them into the original directory structure.

Besides the Python API, a command line interface is also provided.

## Installation

You can install pkglite for Python from PyPI:

```bash
pip install pkglite
```

Or install the development version from GitHub:

```bash
git clone https://github.com/pharmaverse/py-pkglite.git
cd py-pkglite
python3 -m pip install -e .
```

To install the command line tool globally,
[use pipx](https://packaging.python.org/en/latest/guides/installing-stand-alone-command-line-tools/):

```bash
pipx install pkglite
```

You can also use `uvx` to [try the tool without installing
it](https://docs.astral.sh/uv/guides/tools/):

```bash
uvx pkglite --help
```

## Usage

Check out the [getting
started](https://pharmaverse.github.io/py-pkglite/articles/get-started/)
article for the CLI and Python API usage.

See the [design](https://pharmaverse.github.io/py-pkglite/articles/design/)
article about the rationale for this package.

## License

This project is licensed under the terms of the MIT license.
