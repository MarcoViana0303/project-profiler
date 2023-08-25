import pytest
from datetime import date
from unittest.mock import patch
from pro_filer.actions.main_actions import show_details


@pytest.fixture
def context_existing_file():
    return {"base_path": "path/to/existing_file.txt"}


@pytest.fixture
def context_non_existing_file():
    return {"base_path": "path/to/non_existing_file.txt"}


def test_show_details_existing_file(capsys, context_existing_file):
    mtime = 1678838400  # Timestamp for a specific date
    expected_mod_date = date.fromtimestamp(mtime)

    with patch("os.path.exists", return_value=True):
        with patch("os.path.getsize", return_value=1234):
            with patch("os.path.isdir", return_value=False):
                with patch("os.path.splitext", return_value=("", ".txt")):
                    with patch("os.path.getmtime", return_value=mtime):
                        expected_output = (
                            f"File name: existing_file.txt\n"
                            f"File size in bytes: 1234\n"
                            f"File type: file\n"
                            f"File extension: .txt\n"
                            f"Last modified date: {expected_mod_date}\n"
                        )
                        show_details(context_existing_file)
                        captured = capsys.readouterr()
                        assert captured.out == expected_output


def test_show_details_non_existing_file(capsys, context_non_existing_file):
    with patch("os.path.exists", return_value=False):
        expected_output = "File 'non_existing_file.txt' does not exist\n"
        show_details(context_non_existing_file)
        captured = capsys.readouterr()
        assert captured.out == expected_output


def test_show_details_file_extension_none(capsys, tmp_path):
    file_content = ""
    file_path = tmp_path / "out_file"

    with open(file_path, "w") as file:
        file.write(file_content)

    context = {"base_path": str(file_path)}
    show_details(context)
    captured = capsys.readouterr()
    assert "File extension: [no extension]" in captured.out
