from pathlib import Path

import pytest

from pkglite.use import use_pkglite


def test_use_pkglite_single_directory(tmp_path):
    """Test creating .pkgliteignore in a single directory."""
    test_dir = tmp_path / "test_dir"
    test_dir.mkdir()

    result = use_pkglite(str(test_dir))

    assert len(result) == 1
    ignore_file = test_dir / ".pkgliteignore"
    assert ignore_file.exists()
    content = ignore_file.read_text()
    assert "__pycache__/" in content
    assert "*.py[cod]" in content
    assert ".git/" in content


def test_use_pkglite_multiple_directories(tmp_path):
    """Test creating .pkgliteignore in multiple directories."""
    test_dirs = [tmp_path / "dir1", tmp_path / "dir2"]
    for d in test_dirs:
        d.mkdir()

    result = use_pkglite([str(d) for d in test_dirs])

    assert len(result) == 2
    for d in test_dirs:
        ignore_file = d / ".pkgliteignore"
        assert ignore_file.exists()
        content = ignore_file.read_text()
        assert "__pycache__/" in content
        assert "*.py[cod]" in content


def test_use_pkglite_existing_file_no_force(tmp_path):
    """Test handling of existing .pkgliteignore files without force flag."""
    test_dir = tmp_path / "test_dir"
    test_dir.mkdir()

    ignore_file = test_dir / ".pkgliteignore"
    ignore_file.write_text("existing content")

    result = use_pkglite(str(test_dir))

    assert len(result) == 1
    assert ignore_file.read_text() == "existing content"


def test_use_pkglite_existing_file_with_force(tmp_path):
    """Test handling of existing .pkgliteignore files with force flag."""
    test_dir = tmp_path / "test_dir"
    test_dir.mkdir()

    ignore_file = test_dir / ".pkgliteignore"
    ignore_file.write_text("existing content")

    result = use_pkglite(str(test_dir), force=True)

    assert len(result) == 1
    content = ignore_file.read_text()
    assert ignore_file.exists()
    assert "existing content" not in content
    assert "__pycache__/" in content
    assert "*.py[cod]" in content


def test_use_pkglite_multiple_existing_files_with_force(tmp_path):
    """Test force overwrite of multiple existing .pkgliteignore files."""
    test_dirs = [tmp_path / "dir1", tmp_path / "dir2"]
    for d in test_dirs:
        d.mkdir()
        ignore_file = d / ".pkgliteignore"
        ignore_file.write_text("existing content")

    result = use_pkglite([str(d) for d in test_dirs], force=True)

    assert len(result) == 2
    for d in test_dirs:
        ignore_file = d / ".pkgliteignore"
        assert ignore_file.exists()
        content = ignore_file.read_text()
        assert "existing content" not in content
        assert "__pycache__/" in content
        assert "*.py[cod]" in content
