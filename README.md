# Shoe Store API
## Descrição do projeto
###
Este projeto tem como objetivo gerenciar os calçados de uma loja de calçados contemplando as seguintes funcionalidades:

- Gerenciamento de calçados (Create, Update, Delete, List, Get)
- Gerenciamento de tipos de calçados (Create, Update, Delete, List, Get)
- Gerenciamento de atributos de calçados atríbutos aos tipos (Create, Update, Delete, List, Get)

## Pré-requisitos, técnologias e versões utilizadas
![Python](https://img.shields.io/badge/Python-versão%203.13.7%20ou%20superior-3776AB?logo=python&style=for-the-badge)

![Django](https://img.shields.io/badge/Django-versão%205.2.8%20ou%20superior-092E20?logo=django&style=for-the-badge)

![Poetry](https://img.shields.io/badge/Poetry-versão%202.2.1%20ou%20superior-60A5FA?logo=poetry&style=for-the-badge)

![Make](https://img.shields.io/badge/Make-versão%204.4.1%20ou%20superior-000000?logo=gnu&style=for-the-badge)

![Docker](https://img.shields.io/badge/Docker-versão%204.50.0%20ou%20superior-2496ED?logo=docker&style=for-the-badge)

## Instalação
1. Clonar o repositório
```bash
git clone https://github.com/Kaneyio/shoes_store_api.git
```

2. Renomear o arquivo `docker-compose-template.yml` para `docker-compose.yml` e preencher as variáveis:
```bash
  services:
    db:
      image: postgres:15
      container_name: shoes_db
      environment:
        POSTGRES_DB: #Insira um nome para o banco de dados
        POSTGRES_USER: #Insira um nome para o usuário
        POSTGRES_PASSWORD: #Insira uma senha para o usuário
      ports:
        - "5432:5432"
      volumes:
        - pgdata:/var/lib/postgresql/data

  volumes:
    pgdata:
```

3. Renomear o arquivo `.envtemplate` para `.env` e preencher as variáveis:
```bash
  POSTGRES_DB= #Mesmo nome do banco de dados do arquivo docker-compose.yml
  POSTGRES_USER= #Mesmo nome do usuário do arquivo docker-compose.yml
  POSTGRES_PASSWORD= #Mesma senha do usuário do arquivo docker-compose.yml
  POSTGRES_HOST=localhost
  POSTGRES_PORT=5432
  ACCESS_TOKEN_LIFETIME=400
  REFRESH_TOKEN_LIFETIME=7
```

4. Instalar as dependências:
```bash
  poetry install
```

5. Criar as migrações:
```bash
  poetry run python manage.py makemigrations
```

6. Aplicar as migrações:
```bash
  poetry run python manage.py migrate
```

7. Configurar superuser:
```bash
  poetry run python manage.py createsuperuser
```

8. Iniciar o servidor

```bash
  make dev
```

ou 

```bash
  poetry run python manage.py runserver
```

