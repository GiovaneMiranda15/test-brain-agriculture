# Cadastro de Produtores Rurais

Este projeto é uma aplicação de cadastro de produtores rurais com funcionalidades de CRUD (Criar, Ler, Atualizar, Excluir) e um dashboard para visualização de métricas sobre fazendas e culturas.

## Índice

1. [Pré-requisitos](#pré-requisitos)
2. [Instalação](#instalação)
3. [Configuração](#configuração)
4. [Uso](#uso)
5. [Endpoints da API](#endpoints-da-api)
6. [Dashboard](#dashboard)
7. [Validação](#validação)
8. [Contribuindo](#contribuindo)
9. [Licença](#licença)

## Pré-requisitos

- Python 3.8 ou superior
- PostgreSQL

## Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu-usuario/cadastro-produtores-rurais.git
   cd cadastro-produtores-rurais
   ```

2. **Crie e ative um ambiente virtual:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure o banco de dados PostgreSQL:**

   Crie um banco de dados PostgreSQL com o nome `agricultura` (ou o nome desejado) e ajuste as credenciais na variável de ambiente `DATABASE_URL`.

## Configuração

1. **Variáveis de Ambiente:**

   Configure a variável de ambiente `DATABASE_URL` para apontar para o seu banco de dados PostgreSQL. Você pode fazer isso criando um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

   ```
   DATABASE_URL=postgresql://usuario:senha@localhost:5432/agricultura
   ```

   Substitua `usuario`, `senha`, `localhost` e `agricultura` pelos valores apropriados para sua configuração.

2. **Crie o banco de dados e as tabelas:**

   Certifique-se de que o banco de dados foi criado e execute as migrações para criar as tabelas necessárias:

   ```bash
   flask db upgrade
   ```

## Uso

1. **Inicie a aplicação:**

   ```bash
   flask run
   ```

   A aplicação estará disponível em `http://127.0.0.1:5000`.

2. **Interaja com a API:**

   Você pode usar ferramentas como `curl`, `Postman` ou `Insomnia` para interagir com os endpoints da API descritos abaixo.

## Endpoints da API

### Produtores Rurais

- **Cadastrar Produtor**

  - **Método:** `POST`
  - **URL:** `/produtor/`
  - **Corpo da Requisição:**

    ```json
    {
      "cpf_cnpj": "12345678900",
      "nome_produtor": "João Silva",
      "nome_fazenda": "Fazenda São João",
      "cidade": "São Paulo",
      "estado": "SP",
      "area_total": 100.00,
      "area_agricultavel": 80.00,
      "area_vegetacao": 20.00,
      "culturas": [
        {
          "cultura": "Soja",
          "area": 50.00
        },
        {
          "cultura": "Milho",
          "area": 30.00
        }
      ]
    }
    ```

- **Atualizar Produtor**

  - **Método:** `PUT`
  - **URL:** `/produtor/<id>`
  - **Corpo da Requisição:** Similar ao cadastro, mas com os dados atualizados.

- **Buscar Todos os Produtores**

  - **Método:** `GET`
  - **URL:** `/produtor/`

- **Buscar Produtor por ID**

  - **Método:** `GET`
  - **URL:** `/produtor/<id>`

- **Excluir Produtor**

  - **Método:** `DELETE`
  - **URL:** `/produtor/<id>`

### Dashboard

- **Obter Dados do Dashboard**

  - **Método:** `GET`
  - **URL:** `/dashboard/`
  - **Resposta:**

    ```json
    {
      "total_fazendas": 10,
      "total_area": 1000.00,
      "estados": {
        "SP": 5,
        "MG": 3
      },
      "culturas": {
        "Soja": 7,
        "Milho": 4
      },
      "uso_solo": {
        "Agricultável": 800.00,
        "Vegetação": 200.00
      }
    }
    ```

## Validação

- **Validação de CPF e CNPJ**

  - Utiliza a biblioteca `validate_docbr` para validar os documentos.
  - Remove caracteres especiais e verifica a validade do número.

- **Validação de Dados**

  - Verifica se a soma das áreas agricultável e de vegetação não excede a área total da fazenda.

## Contribuindo

Se você deseja contribuir para o projeto, siga estas etapas:

1. Fork o repositório.
2. Crie uma branch para suas alterações.
3. Faça um pull request com suas mudanças.

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).

---

Esse README fornece uma visão geral completa do projeto, instruções para instalação e configuração, e detalhes sobre como usar a API e o dashboard. Você pode ajustar os detalhes conforme necessário para atender às necessidades específicas do seu projeto.