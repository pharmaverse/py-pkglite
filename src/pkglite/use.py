import importlib.resources as pkg_resources
import os
import shutil
from collections.abc import Sequence
from pathlib import Path

import pkglite.templates

from .cli import format_path, print_success, print_warning


def process_directory(
    template: Path, directory: str | Path, force: bool, quiet: bool
) -> tuple[str, bool]:
    """
    Process a single directory and create/overwrite `.pkgliteignore` file.

    Args:
        template: Path to the template `.pkgliteignore` file to copy from.
        directory: Path to the directory to process.
        force: If True, overwrite existing `.pkgliteignore` file.
        quiet: If True, suppress output messages.

    Returns:
        A tuple containing the `.pkgliteignore` path and whether it was
        created or overwritten.
    """
    dir_path = Path(os.path.abspath(os.path.expanduser(str(directory))))
    ignore_path = str(dir_path / ".pkgliteignore")

    if os.path.exists(ignore_path) and not force:
        if not quiet:
            print_warning(
                "Skipping: "
                f"{format_path('.pkgliteignore', path_type='target')} already exists "
                f"in {format_path(str(dir_path), path_type='target')}"
            )
        return ignore_path, False

    dir_path.mkdir(parents=True, exist_ok=True)
    shutil.copy(template, ignore_path)

    if not quiet:
        action = "Overwrote" if os.path.exists(ignore_path) and force else "Created"
        print_success(
            f"{action} "
            f"{format_path('.pkgliteignore', path_type='target')} in "
            f"{format_path(str(dir_path), path_type='target')}"
        )
    return ignore_path, True


def use_pkglite(
    input_dirs: str | Path | Sequence[str | Path],
    force: bool = False,
    quiet: bool = False,
) -> list[str]:
    """
    Copy the `.pkgliteignore` template into one or more directories.

    Args:
        input_dirs: Path or sequence of paths to directories for `.pkgliteignore`.
        force: If True, overwrite existing `.pkgliteignore` files.
        quiet: If True, suppress output messages.

    Returns:
        Paths to the newly created or existing `.pkgliteignore` files.
    """
    dirs = [input_dirs] if isinstance(input_dirs, (str, Path)) else input_dirs

    template_file = pkg_resources.files(pkglite.templates) / "pkgliteignore.txt"

    with pkg_resources.as_file(template_file) as template:
        results = [
            process_directory(template, directory, force, quiet) for directory in dirs
        ]

    return [path for path, _ in results]
