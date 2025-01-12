import os
from pathlib import Path
from typing import List, Callable, Tuple, Optional

from pathspec import PathSpec

from .classify import classify_file
from .cli import (
    print_action,
    print_sub_action,
    print_success,
    format_path,
    format_count,
)


def load_ignore_matcher(directory: str) -> Callable[[str], bool]:
    """
    Load ignore patterns from a `.pkgliteignore` file in the directory.

    Args:
        directory (str): Path to the directory to pack.

    Returns:
        function: A matcher function that returns True if a path
        should be ignored, False otherwise.
    """
    abs_dir = os.path.abspath(os.path.expanduser(directory))
    ignore_path = os.path.join(abs_dir, ".pkgliteignore")

    if not os.path.exists(ignore_path):
        return lambda path: False

    with open(ignore_path, "r") as f:
        patterns = f.readlines()

    spec = PathSpec.from_lines("gitwildmatch", patterns)

    def matcher(path: str) -> bool:
        """
        Check if a path matches any ignore pattern.

        Args:
            path (str): Path to check against ignore patterns.
                Should be relative to the base directory.

        Returns:
            bool: True if path should be ignored, False otherwise.
        """
        if os.path.isabs(path):
            path = os.path.relpath(path, abs_dir)

        # Convert Windows path separators to forward slashes
        norm_path = path.replace(os.sep, "/")

        return spec.match_file(norm_path)

    return matcher


def get_package_name(directory: str) -> str:
    """
    Derive the package name from the directory name.

    Args:
        directory (str): Path to the directory.

    Returns:
        str: The base name of the directory path.
    """
    return os.path.basename(os.path.normpath(directory))


def create_file_metadata(package_name: str, relative_path: str, file_type: str) -> str:
    """
    Create file metadata string.

    Args:
        package_name (str): Name of the package.
        relative_path (str): Relative path of the file within the package.
        file_type (str): Type of the file ('text' or 'binary').

    Returns:
        str: Formatted metadata string.
    """
    return (
        f"Package: {package_name}\n"
        f"File: {relative_path}\n"
        f"Format: {file_type}\n"
        "Content:\n"
    )


def read_text_content(file_path: str) -> str:
    """
    Read text file content and format it.

    Args:
        file_path (str): Path to the text file to read from.

    Returns:
        str: Formatted text content.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return "".join("  " + line for line in f)


def read_binary_content(file_path: str) -> str:
    """
    Read binary file content and format it in hex format.

    Args:
        file_path (str): Path to the binary file to read from.

    Returns:
        str: Formatted binary content.
    """
    with open(file_path, "rb") as f:
        content = f.read().hex()
        return "".join(
            f"  {content[i : i + 128]}\n" for i in range(0, len(content), 128)
        )


def read_file_content(file_path: str, file_type: str) -> str:
    """
    Read and format file content based on type.

    Args:
        file_path (str): Path to the file to read from.
        file_type (str): Type of the file ('text' or 'binary').

    Returns:
        str: Formatted file content.
    """
    return (
        read_text_content(file_path)
        if file_type == "text"
        else read_binary_content(file_path)
    )


def process_single_file(
    file_path: str,
    directory: str,
    package_name: str,
    ignore_matcher: Callable[[str], bool],
) -> Optional[str]:
    """
    Process a single file and return its formatted content.

    Args:
        file_path (str): Path to the file to process.
        directory (str): Base directory path.
        package_name (str): Name of the package.
        ignore_matcher (function): Function to check if file should be ignored.

    Returns:
        Optional[str]: Formatted file content if not ignored, None otherwise.
    """
    if ignore_matcher(file_path):
        return None

    relative_path = os.path.relpath(file_path, directory)
    file_type = classify_file(file_path)

    return (
        create_file_metadata(package_name, relative_path, file_type)
        + read_file_content(file_path, file_type)
        + "\n"
    )


def create_header() -> str:
    """
    Create the pkglite header string.

    Returns:
        str: Formatted header string.
    """
    return (
        "# Generated by py-pkglite: do not edit by hand\n"
        "# Use `pkglite unpack` to restore the packages\n\n"
    )


def pack(
    input_dirs: str | List[str] | Path,
    output_file: str | Path = Path("pkglite.txt"),
    quiet: bool = False,
) -> None:
    """
    Pack files from one or multiple directories into a text file.

    Args:
        input_dirs (str or list or Path): Path or list of paths to the
            directories to pack.
        output_file (str or Path): Path to the output file.
            Default is 'pkglite.txt'.
        quiet (bool): If True, suppress output messages. Default False.
    """
    dirs = [input_dirs] if isinstance(input_dirs, (str, Path)) else input_dirs
    abs_dirs = [os.path.abspath(os.path.expanduser(str(d))) for d in dirs]
    abs_output = os.path.abspath(os.path.expanduser(str(output_file)))

    os.makedirs(os.path.dirname(abs_output), exist_ok=True)

    with open(abs_output, "w", encoding="utf-8") as out:
        out.write(create_header())

        for directory in abs_dirs:
            ignore_matcher = load_ignore_matcher(directory)
            package_name = get_package_name(directory)

            all_files = [
                (os.path.join(root, file), root, file)
                for root, _, files in os.walk(directory)
                for file in files
                if not ignore_matcher(os.path.join(root, file))
            ]

            if not quiet:
                print_action("Packing", package_name)
                for file_path, root, file in all_files:
                    rel_path = os.path.relpath(file_path, directory)
                    print_sub_action("Reading", rel_path, path_type="source")
                    if content := process_single_file(
                        file_path, directory, package_name, ignore_matcher
                    ):
                        out.write(content)
            else:
                for file_path, _, _ in all_files:
                    if content := process_single_file(
                        file_path, directory, package_name, ignore_matcher
                    ):
                        out.write(content)

    if not quiet:
        print_success(
            f"Packed {format_count(len(abs_dirs))} packages into {format_path(abs_output, path_type='target')}"
        )
