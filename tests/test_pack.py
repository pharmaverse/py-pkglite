from pathlib import Path

import pytest

from pkglite.pack import pack, load_ignore_matcher


def test_pack_single_directory(tmp_path):
    """Test packing a single directory with text and binary files."""
    test_dir = tmp_path / "mypackage"
    test_dir.mkdir()

    (test_dir / "test.py").write_text("print('hello')\n")
    (test_dir / "data.bin").write_bytes(bytes([0x00, 0xFF]))
    (test_dir / ".pkgliteignore").write_text("*.pyc\n")

    output_file = tmp_path / "output.txt"

    pack(str(test_dir), output_file=str(output_file))

    assert output_file.exists()
    content = output_file.read_text()
    assert "Package: mypackage" in content
    assert "File: test.py" in content
    assert "Format: text" in content
    assert "print('hello')" in content
    assert "File: data.bin" in content
    assert "Format: binary" in content


def test_pack_with_ignore_patterns(tmp_path):
    """Test that .pkgliteignore patterns are respected."""
    test_dir = tmp_path / "mypackage"
    test_dir.mkdir()

    (test_dir / "include.py").write_text("keep this")
    (test_dir / "exclude.pyc").write_text("ignore this")
    (test_dir / ".pkgliteignore").write_text("*.pyc\n")

    output_file = tmp_path / "output.txt"

    pack(str(test_dir), output_file=str(output_file))

    content = output_file.read_text()
    assert "File: include.py" in content
    assert "File: exclude.pyc" not in content


def test_load_ignore_matcher(tmp_path):
    """Test ignore pattern matching functionality."""
    test_dir = tmp_path / "mypackage"
    test_dir.mkdir()
    (test_dir / ".pkgliteignore").write_text("*.pyc\n__pycache__/\n")

    matcher = load_ignore_matcher(str(test_dir))

    # Convert Windows paths to use forward slashes
    def normalize_path(path):
        return str(path).replace("\\", "/")

    assert matcher(normalize_path(test_dir / "test.pyc")) is True
    assert matcher(normalize_path(test_dir / "__pycache__/module.py")) is True
    assert matcher(normalize_path(test_dir / ".git/")) is False
