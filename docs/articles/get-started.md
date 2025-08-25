# Get started

## Python API

Import pkglite:

```python
import pkglite as pkg
```

### Single directory

Pack a single directory into a text file and unpack it:

```python
dirs = ["path/to/pkg"]
txt = "path/to/pkg.txt"
pkg.use_pkglite(dirs)
pkg.pack(dirs, output_file=txt)
pkg.unpack(txt, output_dir="path/to/output")
```

### Multiple directories

Pack multiple directories into a text file and unpack it:

```python
dirs = ["path/to/pkg1", "path/to/pkg2"]
txt = "path/to/pkgs.txt"
pkg.use_pkglite(dirs)
pkg.pack(dirs, output_file=txt)
pkg.unpack(txt, output_dir="path/to/output")
```

The `use_pkglite()` function creates a `.pkgliteignore` file to exclude files
from the packing scope.

## Command line interface

### Single directory

Pack a single directory into a text file and unpack it:

```bash
pkglite use path/to/pkg
pkglite pack path/to/pkg -o path/to/pkg.txt
pkglite unpack path/to/pkg.txt -o path/to/output
```

### Multiple directories

Pack multiple directories into a text file and unpack it:

```bash
pkglite use path/to/pkg1 path/to/pkg2
pkglite pack path/to/pkg1 path/to/pkg2 -o path/to/pkgs.txt
pkglite unpack path/to/pkgs.txt -o path/to/output
```

The `pkglite use` subcommand creates a `.pkgliteignore` file to exclude
files from the packing scope.

Run

```bash
pkglite --help
pkglite use --help
pkglite pack --help
pkglite unpack --help
```

for more information about the available subcommands and their options.
