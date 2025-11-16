# Shoe Store API
## Descrição do projeto:
###
Este projeto tem como objetivo gerenciar os calçados de uma loja de calçados contemplando as seguintes funcionalidades:

- Gerenciamento de calçados (Create, Update, Delete, List, Get)
- Gerenciamento de tipos de calçados (Create, Update, Delete, List, Get)
- Gerenciamento de atributos de calçados atríbutos aos tipos (Create, Update, Delete, List, Get)
- Documentação da API com Swagger
- Testes automatizados

---

### Pré-requisitos obrigatórios necessários:
![Python](https://img.shields.io/badge/Python-v3.13.7%2B-3776AB?logo=python)
![Django](https://img.shields.io/badge/Django-v5.2.8%2B-092E20?logo=django)
![Poetry](https://img.shields.io/badge/Poetry-v2.2.1%2B-60A5FA?logo=poetry)
![Docker](https://img.shields.io/badge/Docker-v4.50.0%2B-2496ED?logo=docker)

---
### Tecnologias auxiliares e ferramentas opcionais:
![Make](https://img.shields.io/badge/Make-4.4.1%2B-000000?logo=gnu)

---
### Instalação:
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

3. Rodar o banco de dados: ```⚠️Etapa importante!```
```bash
  docker-compose up -d
```

4. Renomear o arquivo `.envtemplate` para `.env` e preencher as variáveis:
```bash
  POSTGRES_DB= #Mesmo nome do banco de dados do arquivo docker-compose.yml
  POSTGRES_USER= #Mesmo nome do usuário do arquivo docker-compose.yml
  POSTGRES_PASSWORD= #Mesma senha do arquivo docker-compose.yml
  POSTGRES_HOST=localhost #Host definida por padrão, não alterar
  POSTGRES_PORT=5432 #Porta definida por padrão, não alterar
  ACCESS_TOKEN_LIFETIME=400 #Tempo de expiração do token
  REFRESH_TOKEN_LIFETIME=7 #Tempo de expiração do refresh token
```

5. Instalar as dependências:
```bash
  command: poetry install
  #ou
  command: make install #(caso tenha o make instalado)
```

6. Criar as migrações:
```bash
  command: poetry run python manage.py makemigrations
  #ou
  command: make makemigrations #(caso tenha o make instalado)
```

7. Aplicar as migrações:
```bash
  command: poetry run python manage.py migrate
  #ou
  command: make migrate #(caso tenha o make instalado)
```

8. Configurar superuser: ```⚠️Etapa importante!```
```bash
  command: poetry run python manage.py createsuperuser
  #ou
  command: make createsuperuser #(caso tenha o make instalado)
```

`Nessa etapa, você deve inserir um nome de usuário, um email e uma senha, confirmando a mesma logo em seguida.`  
`O usuário criado nesta etapa será utilizado para acessar a plataforma de administração da API e também para acessar o sistema na página de login da ShoesStore.`

9. Iniciar o servidor

```bash
  command: poetry run python manage.py runserver
  #ou
  command: make dev
```

10. Informações importantes:

Após iniciar o servidor, as requisições podem ser feitas ao endereço:

ShoesStoreAPI: http://localhost:8000/api/

Tanto pela plataforma de administração do Django quanto pelo front-end no app ShoesStore.  
___
Os endpoints disponíveis estão documentados pelo Swagger no endereço:

Swagger: http://localhost:8000/swagger/.

