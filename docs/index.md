# pkglite for Python <img src="assets/logo.png" align="right" width="120" />

[![PyPI version](https://img.shields.io/pypi/v/pkglite)](https://pypi.org/project/pkglite/)
![Python versions](https://img.shields.io/pypi/pyversions/pkglite)
[![CI Tests](https://github.com/pharmaverse/py-pkglite/actions/workflows/ci-tests.yml/badge.svg)](https://github.com/pharmaverse/py-pkglite/actions/workflows/ci-tests.yml)
[![mkdocs](https://github.com/pharmaverse/py-pkglite/actions/workflows/mkdocs.yml/badge.svg)](https://pharmaverse.github.io/py-pkglite/)
[![PyPI Downloads](https://img.shields.io/pypi/dm/pkglite)](https://pypistats.org/packages/pkglite)
![License](https://img.shields.io/pypi/l/pkglite)

A simple framework for packing source packages written in any programming
language into a text file and restoring them into the original directory structure.

Beisdes the Python API, a command line interface is also provided.

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
[use pipx](https://packaging.python.org/en/latest/guides/installing-stand-alone-command-line-tools/).

## Usage

Check out the [getting
started](https://pharmaverse.github.io/py-pkglite/articles/get-started/)
article for the CLI and Python API usage.

See the [design](https://pharmaverse.github.io/py-pkglite/articles/design/)
article about the rationale for this package.

## License

This project is licensed under the terms of the MIT license.
