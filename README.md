# pkglite for Python

pkglite for Python provides a simple framework and command line interface for
packing source packages written in any programming language into a text file
and restoring them into the original directory structure.

## Installation

You can install pkglite for Python from PyPI:

```bash
pip3 install pkglite
```

Or install the development version from GitHub:

```bash
git clone https://github.com/<placeholder-github-org>/py-pkglite.git
cd py-pkglite
python3 -m pip install -e .
```

## Usage

### CLI

Single directory:

```bash
# Create a .pkgliteignore file to exclude files from packing
pkglite use path/to/pkg

# Pack a single directory into a text file
pkglite pack path/to/pkg -o path/to/pkg.txt

# Unpack the text file into a directory
pkglite unpack path/to/pkg.txt -o path/to/output
```

Multiple directories:

```bash
# Create a .pkgliteignore file to exclude files from packing
pkglite use path/to/pkg1 path/to/pkg2

# Pack multiple directories into a text file
pkglite pack path/to/pkg1 path/to/pkg2 -o path/to/pkgs.txt

# Unpack the text file into multiple directories under `output/`
pkglite unpack path/to/pkgs.txt -o path/to/output
```

Run `pkglite --help`, `pkglite use --help`, `pkglite pack --help`,
or `pkglite unpack --help` for more information about the available
subcommands and options.

To install the command line tool globally,
[use pipx](https://packaging.python.org/en/latest/guides/installing-stand-alone-command-line-tools/).

### Python API

Single directory:

```python
from pkglite import use_pkglite, pack, unpack

dirs = ["path/to/pkg"]
txt = "path/to/pkg.txt"
use_pkglite(dirs)
pack(dirs, output_file=txt)
unpack(txt, output_dir="path/to/output")
```

Multiple directories:

```python
from pkglite import use_pkglite, pack, unpack

dirs = ["path/to/pkg1", "path/to/pkg2"]
txt = "path/to/pkgs.txt"
use_pkglite(dirs)
pack(dirs, output_file=txt)
unpack(txt, output_dir="path/to/output")
```

## Why pkglite for Python?

Building on our experience with pkglite for R,
we identified several limitations and unmet needs:

- **Broader scope**: Extend support for packing and unpacking packages
  across any programming language, without R-specific assumptions.
- **Optimized tooling**: Simplify packing logic by classifying files
  based on content rather than file extensions.
- **Engineering-friendly interface**: Besides the language-specific API,
  provide a command-line interface (CLI) to better integrate with
  standard engineering workflows.

We made a few key design changes from pkglite for R to implement the above goals:

- Introduced a `.pkgliteignore` configuration file to control packing scope,
  following the gitignore standard.
- Adopted content-based file type classification for unsupervised file discovery.
- Built in Python for better flexibility and accessibility.

## License

This project is licensed under the terms of the MIT license.
