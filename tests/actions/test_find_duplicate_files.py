import pytest
from unittest.mock import patch
from pro_filer.actions.main_actions import find_duplicate_files  # NOQA


# Fixture para fornecer contexto com arquivos
@pytest.fixture
def context_with_files(tmp_path):
    file_1 = tmp_path / "file_1.txt"
    file_1.write_text("testando")

    file_2 = tmp_path / "file_2.txt"
    file_2.write_text("testando")

    return {"all_files": [str(file_1), str(file_2)]}


# Testa a função find_duplicate_files quando a lista de combinações é vazia
def test_find_duplicate_files_empty_list(context_with_files):
    with patch("itertools.combinations", return_value=[]):
        duplicates = find_duplicate_files(context_with_files)
        assert duplicates == []


# Testa a função find_duplicate_files quando um arquivo não é encontrado
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


# Testa a função find_duplicate_files quando não há arquivos duplicados
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


# Testa a função find_duplicate_files para identificar arquivos duplicados
def test_find_duplicated_files(context_with_files):
    duplicated = find_duplicate_files(context_with_files)

    assert len(duplicated) == 1
    assert len(duplicated[0]) == 2


# Testa a função find_duplicate_files para identificar arquivos duplicados
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
