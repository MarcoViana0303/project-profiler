import pytest
from pro_filer.actions.main_actions import show_preview


# Define uma fixture que retorna um dicionário com nomes de arquivos
#  e diretórios simulados
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


# Testa a função show_preview utilizando a fixture context_with_files_and_dirs
def test_show_preview_with_files_and_dirs(capsys, context_with_files_and_dirs):
    # Chama a função show_preview com o contexto da fixture
    show_preview(context_with_files_and_dirs)

    # Captura a saída impressa no console durante a execução da função
    captured = capsys.readouterr()

    # Verifica se a mensagem sobre o número de arquivos e diretórios é
    # exibida na saída
    assert "Found 6 files and 6 directories" in captured.out

    # Obtém os primeiros 5 nomes de arquivos e diretórios esperados
    expected_files = context_with_files_and_dirs["all_files"][:5]
    expected_dirs = context_with_files_and_dirs["all_dirs"][:5]

    # Gera as strings esperadas para os nomes de arquivos e diretórios
    expected_files_output = f"First 5 files: {expected_files}"
    expected_dirs_output = f"First 5 directories: {expected_dirs}"

    # Verifica se as strings esperadas estão presentes na saída capturada
    assert expected_files_output in captured.out
    assert expected_dirs_output in captured.out
