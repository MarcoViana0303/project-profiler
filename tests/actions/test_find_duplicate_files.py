import pytest
from unittest.mock import patch
from pro_filer.actions.main_actions import find_duplicate_files  # NOQA


@pytest.fixture
def context_with_files(tmp_path):
    arq_1 = tmp_path / "arq_1.txt"
    arq_1.write_text("test content" * 8)

    aqr_2 = tmp_path / "aqr_2.txt"
    aqr_2.write_text("test content" * 8)

    arq_3 = tmp_path / "arq_3.txt"
    arq_3.write_text("corinthians")

    return {"all_files": [str(arq_1), str(aqr_2), str(arq_3)]}


def test_find_duplicate_files_empty_list(context_with_files):
    with patch("itertools.combinations", return_value=[]):
        duplicates = find_duplicate_files(context_with_files)
        assert duplicates == []


def test_find_duplicate_files_file_not_found(context_with_files):
    with patch("itertools.combinations", return_value=[
        ("file1.txt", "file2.txt"),
        ("file1.txt", "file3.txt"),
        ("file2.txt", "file3.txt"),
        ("file1.txt", "file4.txt"),
        ("file2.txt", "file4.txt"),
        ("file3.txt", "file4.txt"),
    ]):
        with patch("filecmp.cmp", side_effect=[True, True, FileNotFoundError]):
            with pytest.raises(ValueError, match="All files must exist"):
                find_duplicate_files(context_with_files)


def test_find_duplicate_files_no_duplicates(context_with_files):
    with patch("itertools.combinations", return_value=[
        ("file1.txt", "file2.txt"),
        ("file1.txt", "file3.txt"),
        ("file1.txt", "file4.txt"),
        ("file2.txt", "file3.txt"),
        ("file2.txt", "file4.txt"),
        ("file3.txt", "file4.txt"),
    ]):
        with patch("filecmp.cmp", side_effect=[False] * 6):
            duplicates = find_duplicate_files(context_with_files)
            assert duplicates == []


def test_find_duplicated_files(context_with_files):
    duplicated = find_duplicate_files(context_with_files)

    assert len(duplicated) == 1
    assert len(duplicated[0]) == 2


def test_find_duplicate_files_with_duplicates(context_with_files):
    with patch("itertools.combinations", return_value=[
        ("file1.txt", "file2.txt"),
        ("file1.txt", "file3.txt"),
        ("file2.txt", "file3.txt"),
        ("file1.txt", "file4.txt"),
        ("file2.txt", "file4.txt"),
        ("file3.txt", "file4.txt"),
    ]):
        with patch("filecmp.cmp", side_effect=[True] * 6):
            duplicates = find_duplicate_files(context_with_files)
            expected_duplicates = [
                ("file1.txt", "file2.txt"),
                ("file1.txt", "file3.txt"),
                ("file2.txt", "file3.txt"),
                ("file1.txt", "file4.txt"),
                ("file2.txt", "file4.txt"),
                ("file3.txt", "file4.txt"),
            ]
            assert duplicates == expected_duplicates
