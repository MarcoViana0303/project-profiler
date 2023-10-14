<h3 align="center">
  Projeto Pro-filer
  <br /><br />
</h3>

## Observação

Trabalhei em uma aplicação com uma interface de linha de comando (CLI) que recebe como entrada um caminho (diretório ou arquivo) e gera um relatório com informações sobre o caminho informado.

<br />
<details>
  <summary><strong>:memo: Habilidades trabalhadas </strong></summary>
<br />

- Encontrei bugs no código de uma aplicação escrita em Python;
- Corrigi bugs no código de uma aplicação escrita em Python;
- Criei testes para uma aplicação escrita em Python;
- Utilizei o `pytest` para criar testes automatizados em uma aplicação escrita em Python.

</details>

<br />

  Para rodar a aplicação, irá precisar de: [Git](https://git-scm.com), [VS Code](https://code.visualstudio.com/), [Node.js](https://nodejs.org/) e [NPM](https://www.npmjs.com/).

<br />

Clone o projeto

```bash
git clone git@github.com:MarcoViana0303/project-profiler.git
```

Entre no diretório do projeto

```bash
cd project-profiler
```

<br /> 

<details>
  <summary><strong>🏕️ Ambiente Virtual</strong></summary>
  <br />
  O Python oferece um recurso chamado de ambiente virtual, onde permite sua máquina rodar sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas.
  
  1. **criar o ambiente virtual**
  ```bash
  python3 -m venv .venv
  ```

  2. **ativar o ambiente virtual**
  ```bash
  source .venv/bin/activate
  ```

  3. **atualize o pip**

  ```bash
  python3 -m pip install --upgrade pip
  ```

  4. **instalar as dependências no ambiente virtual**

  ```bash
  python3 -m pip install -r dev-requirements.txt
  ```
  Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente.
  Quando precisar desativar o ambiente virtual, execute o comando `deactivate`. Lembre-se de ativar novamente quando voltar a trabalhar no projeto.
  O arquivo `dev-requirements.txt` instalará todas as dependências que serão utilizadas no projeto, ele está agindo como se fosse um `package.json` de um projeto `Node.js`. Se você desejar instalar uma nova dependência, basta adicioná-la no arquivo `dev-requirements.txt` e executar o comando `python3 -m pip install -r dev-requirements.txt` novamente.
  Se o VS Code não reconhecer as dependências instaladas no ambiente virtual criado, será necessário informar o caminho do interpretador Python. Para isso, abra o VS Code e pressione `Ctrl + Shift + P` (no Mac, `Cmd + Shift + P`) e digite `Python: Select Interpreter`. Selecione o interpretador que possui o caminho `./.venv/bin/python` no nome.
</details>

<br />

<details>
  <summary><strong>🛠 Testes</strong></summary>
  <br />
  Para executar os testes certifique-se de que você está com o ambiente virtual ativado.
  <strong>Executar os testes</strong>
  
  ```bash
  python3 -m pytest
  ```

  O arquivo `pyproject.toml` já configura corretamente o `pytest`. Entretanto, caso você tenha problemas com isso e queira explicitamente uma saída completa, o comando é:
  ```bash
  python3 -m pytest -s -vv --continue-on-collection-errors
  ```

  O `pytest` possui diversos parâmetros que podem ser utilizados para executar os testes de diferentes formas. Alguns exemplos são:
  ```bash
  python3 -m pytest tests/test_nome_do_arquivo.py  # Executa todos os testes do arquivo de testes especificado
  python3 -m pytest tests/test_nome_do_arquivo.py::test_nome_do_teste  # Executa apenas o teste especificado
  python3 -m pytest -k expressao  # Executa apenas os testes que contém a expressão informada como substring
  python3 -m pytest -x  # Executa os testes até encontrar o primeiro erro
  ```

</details>

## Feedback

Encontrou algum erro ou está com alguma dúvida? Não deixe de entrar em contato comigo!


## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/marco-viana2022/)
[![gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](https://marcoviana.dev@gmail.com/)
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://marcoviana-dev.vercel.app/)
