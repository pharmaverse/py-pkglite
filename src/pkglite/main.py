from pathlib import Path
from typing import Annotated

import typer

from .pack import pack as pack_impl
from .unpack import unpack as unpack_impl
from .use import use_pkglite as use_pkglite_impl

app = typer.Typer()


@app.callback()
def callback():
    """
    pkglite - Plain text representations for packages written in any programming language
    """


@app.command()
def pack(
    input_dirs: list[Path],
    output_file: Annotated[Path, typer.Option("--output-file", "-o")] = Path(
        "pkglite.txt"
    ),
    quiet: Annotated[bool, typer.Option("--quiet", "-q")] = False,
):
    """
    Pack files from one or multiple directories into a text file.

    Args:
        input_dirs: One or more directories to pack.
        output_file: Output file path. Default is `pkglite.txt`.
        quiet: Suppress output messages.
    """
    pack_impl(input_dirs, output_file=output_file, quiet=quiet)


@app.command()
def unpack(
    input_file: Path,
    output_dir: Annotated[Path, typer.Option("--output-dir", "-o")] = Path("."),
    quiet: Annotated[bool, typer.Option("--quiet", "-q")] = False,
):
    """
    Unpack files from a text file into the specified directory.

    Args:
        input_file: The text file to unpack.
        output_dir: Directory to unpack into. Default is the current directory.
        quiet: Suppress output messages.
    """
    unpack_impl(input_file, output_dir=output_dir, quiet=quiet)


@app.command()
def use(
    input_dirs: list[Path],
    force: Annotated[bool, typer.Option("--force", "-f")] = False,
    quiet: Annotated[bool, typer.Option("--quiet", "-q")] = False,
):
    """
    Copy the `.pkgliteignore` template into one or more directories.

    Args:
        directories: One or more directories to add `.pkgliteignore` to.
        force: Overwrite existing `.pkgliteignore` files.
        quiet: Suppress output messages.
    """
    use_pkglite_impl(input_dirs, force=force, quiet=quiet)
