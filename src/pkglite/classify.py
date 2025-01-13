import os
from typing import FrozenSet


def is_text_file(path: str, n: int | None = None) -> bool:
    """
    Classify any file as text or binary.

    Algorithm adopted from "A Fast Method for Identifying Plain Text Files"
    in zlib (`doc/txtvsbin.txt`).

    Args:
        path: File path.
        n: Maximal number of bytes to read. Defaults to file size.

    Returns:
        True if the file is text, False if binary.
    """
    ALLOW: FrozenSet[int] = frozenset([9, 10, 13] + list(range(32, 256)))
    BLOCK: FrozenSet[int] = frozenset(list(range(0, 7)) + list(range(14, 32)))

    with open(path, "rb") as file:
        bytecode = bytes(file.read(n or os.path.getsize(path)))

    if not bytecode:
        return False

    cond1 = any(b in ALLOW for b in bytecode)
    cond2 = not any(b in BLOCK for b in bytecode)

    return cond1 and cond2


def classify_file(path: str) -> str:
    """
    Classify file as text or binary.

    Args:
        path: Path to the file to classify.

    Returns:
        `'text'` if the file is detected as text, `'binary'` otherwise.
    """
    return "text" if is_text_file(path) else "binary"
