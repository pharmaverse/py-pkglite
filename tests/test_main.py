from pathlib import Path
from unittest.mock import patch, Mock

import pytest
from typer.testing import CliRunner

from pkglite.main import app

runner = CliRunner()


@pytest.fixture
def mock_pack():
    with patch("pkglite.main.pack_impl") as mock:
        yield mock


@pytest.fixture
def mock_unpack():
    with patch("pkglite.main.unpack_impl") as mock:
        yield mock


@pytest.fixture
def mock_use():
    with patch("pkglite.main.use_pkglite_impl") as mock:
        yield mock


def test_pack_command_default_output(mock_pack, tmp_path):
    """Test pack command with default output file"""
    input_dir = tmp_path / "test_dir"
    input_dir.mkdir()

    result = runner.invoke(app, ["pack", str(input_dir)])

    assert result.exit_code == 0
    mock_pack.assert_called_once_with(
        [Path(str(input_dir))], output_file=Path("pkglite.txt"), quiet=False
    )


def test_pack_command_multiple_inputs(mock_pack, tmp_path):
    """Test pack command with multiple input directories"""
    dir1 = tmp_path / "dir1"
    dir2 = tmp_path / "dir2"
    dir1.mkdir()
    dir2.mkdir()
    output = tmp_path / "output.txt"

    result = runner.invoke(
        app, ["pack", str(dir1), str(dir2), "--output-file", str(output)]
    )
    assert result.exit_code == 0
    mock_pack.assert_called_once_with(
        [Path(str(dir1)), Path(str(dir2))], output_file=Path(str(output)), quiet=False
    )

    mock_pack.reset_mock()

    result = runner.invoke(app, ["pack", str(dir1), str(dir2), "-o", str(output)])
    assert result.exit_code == 0
    mock_pack.assert_called_once_with(
        [Path(str(dir1)), Path(str(dir2))], output_file=Path(str(output)), quiet=False
    )


def test_unpack_command_default_output(mock_unpack, tmp_path):
    """Test unpack command with default output directory"""
    input_file = tmp_path / "pkglite.txt"
    input_file.touch()

    result = runner.invoke(app, ["unpack", str(input_file)])

    assert result.exit_code == 0
    mock_unpack.assert_called_once_with(
        Path(str(input_file)), output_dir=Path("."), quiet=False
    )


def test_unpack_command_custom_output(mock_unpack, tmp_path):
    """Test unpack command with custom output directory"""
    input_file = tmp_path / "pkglite.txt"
    output_dir = tmp_path / "output"
    input_file.touch()

    result = runner.invoke(
        app, ["unpack", str(input_file), "--output-dir", str(output_dir)]
    )
    assert result.exit_code == 0
    mock_unpack.assert_called_once_with(
        Path(str(input_file)), output_dir=Path(str(output_dir)), quiet=False
    )

    mock_unpack.reset_mock()

    result = runner.invoke(app, ["unpack", str(input_file), "-o", str(output_dir)])
    assert result.exit_code == 0
    mock_unpack.assert_called_once_with(
        Path(str(input_file)), output_dir=Path(str(output_dir)), quiet=False
    )


def test_use_command_default(mock_use, tmp_path):
    """Test use command with single directory and default options"""
    target_dir = tmp_path / "test_dir"
    target_dir.mkdir()

    result = runner.invoke(app, ["use", str(target_dir)])

    assert result.exit_code == 0
    mock_use.assert_called_once_with([Path(str(target_dir))], force=False, quiet=False)


def test_use_command_with_force(mock_use, tmp_path):
    """Test use command with force flag"""
    target_dir = tmp_path / "test_dir"
    target_dir.mkdir()

    result = runner.invoke(app, ["use", "--force", str(target_dir)])
    assert result.exit_code == 0
    mock_use.assert_called_once_with([Path(str(target_dir))], force=True, quiet=False)

    mock_use.reset_mock()

    result = runner.invoke(app, ["use", "-f", str(target_dir)])
    assert result.exit_code == 0
    mock_use.assert_called_once_with([Path(str(target_dir))], force=True, quiet=False)


def test_use_command_multiple_dirs_with_force(mock_use, tmp_path):
    """Test use command with multiple directories and force flag"""
    dir1 = tmp_path / "dir1"
    dir2 = tmp_path / "dir2"
    dir1.mkdir()
    dir2.mkdir()

    result = runner.invoke(app, ["use", "--force", str(dir1), str(dir2)])
    assert result.exit_code == 0
    mock_use.assert_called_once_with(
        [Path(str(dir1)), Path(str(dir2))], force=True, quiet=False
    )

    mock_use.reset_mock()

    result = runner.invoke(app, ["use", "-f", str(dir1), str(dir2)])
    assert result.exit_code == 0
    mock_use.assert_called_once_with(
        [Path(str(dir1)), Path(str(dir2))], force=True, quiet=False
    )


def test_quiet_flag_propagation():
    """Test quiet flag propagation across all commands"""
    with patch("pkglite.main.pack_impl") as mock_pack, patch(
        "pkglite.main.unpack_impl"
    ) as mock_unpack, patch("pkglite.main.use_pkglite_impl") as mock_use:
        runner.invoke(app, ["pack", "dir", "--quiet"])
        assert mock_pack.call_args[1]["quiet"] is True

        runner.invoke(app, ["unpack", "file.txt", "--quiet"])
        assert mock_unpack.call_args[1]["quiet"] is True

        runner.invoke(app, ["use", "dir", "--quiet"])
        assert mock_use.call_args[1]["quiet"] is True

        mock_pack.reset_mock()
        mock_unpack.reset_mock()
        mock_use.reset_mock()

        runner.invoke(app, ["pack", "dir", "-q"])
        assert mock_pack.call_args[1]["quiet"] is True

        runner.invoke(app, ["unpack", "file.txt", "-q"])
        assert mock_unpack.call_args[1]["quiet"] is True

        runner.invoke(app, ["use", "dir", "-q"])
        assert mock_use.call_args[1]["quiet"] is True


def test_help_messages():
    """Test help messages for all commands"""
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "pkglite" in result.stdout

    result = runner.invoke(app, ["pack", "--help"])
    assert result.exit_code == 0
    assert "Pack files" in result.stdout
    assert "--output-file  -o" in result.stdout
    assert "--quiet        -q" in result.stdout

    result = runner.invoke(app, ["unpack", "--help"])
    assert result.exit_code == 0
    assert "Unpack files" in result.stdout
    assert "--output-dir  -o" in result.stdout
    assert "--quiet       -q" in result.stdout

    result = runner.invoke(app, ["use", "--help"])
    assert result.exit_code == 0
    assert "pkgliteignore" in result.stdout
    assert "--force  -f" in result.stdout
    assert "--quiet  -q" in result.stdout
