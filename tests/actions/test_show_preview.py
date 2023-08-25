import pytest
from pro_filer.actions.main_actions import show_preview


@pytest.fixture
def context_with_files_and_dirs():
    return {
        "all_files": [
            "src/file1.py",
            "src/file2.py",
            "src/file3.py",
            "src/file4.py",
            "src/file5.py",
            "src/file6.py"
        ],
        "all_dirs": [
            "src",
            "src/dir1",
            "src/dir2",
            "src/dir3",
            "src/dir4",
            "src/dir5"
        ]
    }


def test_show_preview_with_files_and_dirs(capsys, context_with_files_and_dirs):
    show_preview(context_with_files_and_dirs)
    captured = capsys.readouterr()

    assert "Found 6 files and 6 directories" in captured.out
    expected_files = context_with_files_and_dirs["all_files"][:5]
    expected_dirs = context_with_files_and_dirs["all_dirs"][:5]

    expected_files_output = f"First 5 files: {expected_files}"
    expected_dirs_output = f"First 5 directories: {expected_dirs}"

    assert expected_files_output in captured.out
    assert expected_dirs_output in captured.out
