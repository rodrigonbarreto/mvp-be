# API CRUD em Python - PUC RJ

## Visão Geral

Este projeto é uma API simples de CRUD (Create, Read, Update, Delete) para gerenciamento de usuários. 

- `id` (inteiro, auto-gerado)
- `name` (string)
- `age` (inteiro)

## Funcionalidades

- **Operações CRUD**: Create, Read, Update, Delete para gerenciamento de usuários.
- **Funcionalidade de busca**: Implementa um parâmetro de consulta `search` para filtrar usuários sem necessidade de uma ação separada.
- **Documentação Swagger**: Documentação interativa da API gerada automaticamente e disponível em `/apidocs/`.

## Stack Tecnológica

- **Linguagem de Programação**: Python 3.12.0
- **Framework**: Flask 3.1.0
- **Banco de Dados**: SQLite
- **ORM**: Flask-SQLAlchemy (baseado em SQLAlchemy)
- **Documentação da API**: Flasgger

## Requisitos

Certifique-se de que você possui o Python 3.12 instalado em sua máquina.

## Configuração

### Passo 1: Clone o repositório

```bash
git clone git@github.com:rodrigonbarreto/mvp-be.git
cd mvp-be
```

### Passo 2: Configure um ambiente virtual

#### Em Linux/MacOS:

```bash
python3 -m venv .venv
source .venv/bin/activate # Linux/MacOS, perdão não sei o comando para windows
```

### Passo 3: Instale as dependências

```bash
pip install -r requirements.txt
```

### Passo 4: Execute o projeto

Para iniciar a aplicação, use o seguinte comando:

```bash
# Para popular o banco de dados
# O comando seed.py cria um banco de dados SQLite e popula com alguns usuários de exemplo
python seed.py 
flask run
```

A API estará disponível em: [http://127.0.0.1:5000](http://127.0.0.1:5000)

### Documentação Swagger

A documentação interativa da API está disponível em: [http://127.0.0.1:5000/apidocs/](http://127.0.0.1:5000/apidocs/)

## Explicação das Escolhas de Design

1. **Ações CRUD**:  O Projeto é um simples crud de usuário

2. **Implementação de Busca**: Em vez de criar uma rota separada para busca como (search_user), eu escolhi usar um parametro get `search` na rota de listagem de usuários para filtrar os usuários. 

3. **Código em Inglês**: Todo o código foi escrito em inglês, pois fica mais para qualquer pessoa ter acesso.

## Ambiente de Desenvolvimento

Eu usei o PyCharm mas  você pode usar qualquer editor de texto ou IDE de sua preferência.

- **Repositório FE:** [https://github.com/rodrigonbarreto/mvp-fe](https://github.com/rodrigonbarreto/mvp-fe)
- **Repositório BE:** [https://github.com/rodrigonbarreto/mvp-be](https://github.com/rodrigonbarreto/mvp-be)