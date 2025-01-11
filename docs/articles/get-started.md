# Get started


<!-- `.md` and `.py` files are generated from the `.qmd` file. Please edit that file. -->

!!! tip

    To run the code from this article as a Python script:

    ```bash
    python3 examples/get-started.py
    ```

Let’s walk through a typical pkglite for Python workflow.

## Import pkglite

``` python
import pkglite
```

## Python API

Single directory:

``` python
from pkglite import use_pkglite, pack, unpack

dirs = ["path/to/pkg"]
txt = "path/to/pkg.txt"
use_pkglite(dirs)
pack(dirs, output_file=txt)
unpack(txt, output_dir="path/to/output")
```

Multiple directories:

``` python
from pkglite import use_pkglite, pack, unpack

dirs = ["path/to/pkg1", "path/to/pkg2"]
txt = "path/to/pkgs.txt"
use_pkglite(dirs)
pack(dirs, output_file=txt)
unpack(txt, output_dir="path/to/output")
```

## Command line interface

Single directory:

``` bash
# Create a .pkgliteignore file to exclude files from packing
pkglite use path/to/pkg

# Pack a single directory into a text file
pkglite pack path/to/pkg -o path/to/pkg.txt

# Unpack the text file into a directory
pkglite unpack path/to/pkg.txt -o path/to/output
```

Multiple directories:

``` bash
# Create a .pkgliteignore file to exclude files from packing
pkglite use path/to/pkg1 path/to/pkg2

# Pack multiple directories into a text file
pkglite pack path/to/pkg1 path/to/pkg2 -o path/to/pkgs.txt

# Unpack the text file into multiple directories under `output/`
pkglite unpack path/to/pkgs.txt -o path/to/output
```

Run `pkglite --help`, `pkglite use --help`, `pkglite pack --help`, or
`pkglite unpack --help` for more information about the available
subcommands and options.
