import pytest
from pro_filer.actions.main_actions import show_preview


@pytest.fixture
def context_with_files_and_dirs():
    return {
        "all_files": [
            "file1.txt",
            "file2.txt",
            "file3.txt",
            "file4.txt",
            "file5.txt",
        ],
        "all_dirs": [
            "dir1",
            "dir2",
            "dir3",
            "dir4",
            "dir5",
        ],
    }


def test_show_preview_with_files_and_dirs(capsys, context_with_files_and_dirs):
    show_preview(context_with_files_and_dirs)
    captured = capsys.readouterr()

    assert "Found 5 files and 5 directories" in captured.out
    expected_files = ['file1.txt',
                      'file2.txt',
                      'file3.txt',
                      'file4.txt',
                      'file5.txt']
    expected_dirs = ['dir1', 'dir2', 'dir3', 'dir4', 'dir5']

    expected_files_output = f"First 5 files: {expected_files}"
    expected_dirs_output = f"First 5 directories: {expected_dirs}"

    assert expected_files_output in captured.out
    assert expected_dirs_output in captured.out
