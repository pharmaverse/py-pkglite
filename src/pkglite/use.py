import os
import shutil
import importlib.resources as pkg_resources
from pathlib import Path
from typing import List, Tuple

import pkglite.templates
from .cli import print_success, print_warning, format_path


def process_directory(
    template: Path, directory: str | Path, force: bool, quiet: bool
) -> Tuple[str, bool]:
    """
    Process a single directory and create/overwrite `.pkgliteignore` file.

    Args:
        template (Path): Path to the template `.pkgliteignore` file to copy from.
        directory (str or Path): Path to the directory to process.
        force (bool): If True, overwrite existing `.pkgliteignore` file.
        quiet (bool): If True, suppress output messages.

    Returns:
        Tuple[str, bool]: A tuple containing:
            - str: Path to the `.pkgliteignore` file.
            - bool: Whether the file was created/overwritten.

    Raises:
        OSError: If there are permission errors creating directory or copying file.
    """
    dir_path = Path(os.path.abspath(os.path.expanduser(str(directory))))
    ignore_path = str(dir_path / ".pkgliteignore")

    if os.path.exists(ignore_path) and not force:
        if not quiet:
            print_warning(
                f"Skipping: {format_path('.pkgliteignore', path_type='target')} already exists in {format_path(str(dir_path), path_type='target')}"
            )
        return ignore_path, False

    dir_path.mkdir(parents=True, exist_ok=True)
    shutil.copy(template, ignore_path)

    if not quiet:
        action = "Overwrote" if os.path.exists(ignore_path) and force else "Created"
        print_success(
            f"{action} {format_path('.pkgliteignore', path_type='target')} in {format_path(str(dir_path), path_type='target')}"
        )
    return ignore_path, True


def use_pkglite(
    input_dirs: str | Path | list[str | Path], force: bool = False, quiet: bool = False
) -> List[str]:
    """
    Copy the `.pkgliteignore` template into one or more directories.

    Args:
        input_dirs (str or Path or list): Path or list of paths to directories
            where `.pkgliteignore` should be placed.
        force (bool): If True, overwrite existing `.pkgliteignore` files. Default is False.
        quiet (bool): If True, suppress output messages. Default is False.

    Returns:
        list: Paths to the newly created or existing `.pkgliteignore` files.
    """
    dirs = [input_dirs] if isinstance(input_dirs, (str, Path)) else input_dirs

    template_file = pkg_resources.files(pkglite.templates) / "pkgliteignore.txt"

    with pkg_resources.as_file(template_file) as template:
        results = [
            process_directory(template, directory, force, quiet) for directory in dirs
        ]

    return [path for path, _ in results]
