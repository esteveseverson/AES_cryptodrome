# AES Cryptodrome

Este projeto implementa uma aplicação de criptografia simétrica utilizando o algoritmo AES (Advanced Encryption Standard) no modo CBC (Cipher Block Chaining). O objetivo principal é permitir que o usuário cifre e decifre mensagens utilizando uma chave aleatória gerada em tempo de execução.

## Requisitos

Para rodar este projeto, você precisa ter o **Poetry** instalado em seu ambiente. O Poetry é uma ferramenta de gerenciamento de dependências e ambientes virtuais para Python. Abaixo, estão as instruções para configurar o ambiente e rodar o projeto.

### Instalação do Poetry

Se você ainda não tem o Poetry instalado, siga as instruções abaixo para instalar:

#### No Linux/macOS:
1. Execute o seguinte comando no terminal:
   `curl -sSL https://install.python-poetry.org | python3 -`

#### No Windows:
1. Execute o seguinte comando no PowerShell (como administrador):
   `(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicP) | python -`

Após a instalação, verifique se o Poetry foi instalado corretamente executando:

`poetry --version`

## Rodando o Projeto

### Passo 1: Instalar dependências

Para instalar as dependências do projeto, navegue até o diretório onde o projeto está localizado e execute o seguinte comando:

`poetry install`

### Passo 2: Entrar no ambiente virtual

Após a instalação das dependências, ative o ambiente virtual criado pelo Poetry com o comando:

`poetry shell`

Isso irá iniciar o ambiente virtual, onde todas as dependências do projeto estarão disponíveis.

### Passo 3: Rodar o Projeto

Agora, para rodar o projeto, execute o seguinte comando:

`python aes_cryptodrome/app.py`

Isso iniciará o aplicativo de criptografia no terminal, permitindo que você cifre e decifre mensagens utilizando a chave gerada aleatoriamente.

## Bibliotecas Utilizadas

### 1. `pycryptodome`

- **Função**: Biblioteca de criptografia para Python.
- **Descrição**: A `pycryptodome` fornece implementações seguras de vários algoritmos de criptografia, incluindo AES. No projeto, a `pycryptodome` é utilizada para realizar a cifragem e decifração das mensagens utilizando o algoritmo AES no modo CBC.
  
  **Instalação**: A biblioteca é instalada automaticamente com o comando `poetry install`, pois está listada no arquivo `pyproject.toml`.

  **Uso no Projeto**:
  - A função `AES.new()` é usada para criar um objeto de cifra AES.
  - `pad()` e `unpad()` são usados para adicionar e remover padding (preenchimento) nas mensagens, garantindo que o tamanho da mensagem seja múltiplo do tamanho do bloco de 16 bytes do AES.
  - `get_random_bytes()` é utilizado para gerar um vetor de inicialização (IV) aleatório, essencial para o modo CBC.

### 2. `secrets`

- **Função**: Biblioteca padrão para geração de números aleatórios de forma criptograficamente segura.
- **Descrição**: A biblioteca `secrets` é usada para gerar uma chave aleatória de 128 bits para a cifra AES. Ela é mais segura que a função `random` quando se trata de geração de números aleatórios para uso em segurança.

  **Uso no Projeto**:
  - A função `secrets.token_bytes(16)` é usada para gerar a chave de 128 bits (16 bytes) que será utilizada no processo de cifragem e decifração.

### 3. `inquirer`

- **Função**: Biblioteca para criação de interfaces de linha de comando interativas.
- **Descrição**: A biblioteca `inquirer` facilita a criação de menus e formulários interativos no terminal. Usada para criar uma interface amigável para o usuário escolher opções como cifrar, decifrar ou sair do programa.

  **Instalação**: A biblioteca é instalada automaticamente com o comando `poetry install`, pois está listada no arquivo `pyproject.toml`.

  **Uso no Projeto**:
  - `inquirer.List` é utilizado para criar um menu de opções interativas no terminal.
  - `inquirer.Text` é utilizado para capturar mensagens de entrada do usuário para cifragem e decifração de forma estilizada e validada.

### 4. `base64`

- **Função**: Biblioteca padrão para codificação e decodificação de dados em Base64.
- **Descrição**: A biblioteca `base64` é usada para codificar e decodificar as mensagens cifradas. Isso é necessário porque a saída do algoritmo de cifragem pode conter bytes não imprimíveis, e a codificação em Base64 permite representar esses bytes como uma string legível.

  **Uso no Projeto**:
  - `base64.b64encode()` é usado para codificar a mensagem cifrada em Base64 antes de mostrá-la ao usuário.
  - `base64.b64decode()` é usado para decodificar a mensagem cifrada de Base64 antes de decifrá-la.

## Contribuindo

Se você deseja contribuir para este projeto, fique à vontade para enviar pull requests ou abrir issues para relatar problemas ou sugerir melhorias.