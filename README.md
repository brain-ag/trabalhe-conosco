# Projeto de exemplo com Django Ninja

``` bash
https://django-ninja.dev/
```

## O que o projeto faz?

* O usuário deverá ter a possibilidade de cadastrar, editar, e excluir produtores rurais.
* O sistema deverá validar CPF e CNPJ digitados incorretamente.
* A soma de área agrícultável e vegetação, não deverá ser maior que a área total da fazenda
* Cada produtor pode plantar mais de uma cultura em sua Fazenda.
* A plataforma deverá ter um Dashboard que exiba:
* Total de fazendas em quantidade
* Total de fazendas em hectares (área total)
* Gráfico de pizza por estado.
* Gráfico de pizza por cultura.
* Gráfico de pizza por uso de solo (Área agricultável e vegetação)

## Como rodar o projeto na sua máquina local?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```bash
git clone "repositorio atual" projetoagricultor
cd projetoagricultor

# Crie a virtualenv
python -m venv .venv

# Crie a virtualenv utilizando Makefile
make create-venv

# Ative a virtualenv
source .venv/bin/activate  # Linux
.venv\Scripts\activate  # Windows

# Instale os pacotes
pip install -r requirements/dev.txt

# Instale os pacotes utilizando Makefile
make setup-dev

# Crie o arquivo de variáveis de ambiente
cp .env.sample .env

# Suba os containers
docker-compose up -d

# Suba os containers utilizado Makefile
make up

# Build os containers
docker-compose up -d --build

# Build os containers utilizado Makefile
make build

# Rode as migrações
python manage.py makemigrations
python manage.py migrate

# Carregue os dados iniciais
python manage.py loaddata fixtures/initial.json

python manage.py runserver
```

## Como rodar o projeto 100% pelo Docker?

```bash
git clone "repositorio atual" projetoagricultor
cd projetoagricultor

# Suba os containers
docker-compose up -d

docker container exec -it app_name python manage.py createsuperuser

# Rode os testes
docker container exec -it app_name pytest

# Gere alguns dados randômicos
docker container exec -it app_name python manage.py seed crm --number=5
```

## Rodando os testes

```bash
pytest -vv
```

## url da doc

A doc é gerada automaticamente com Swagger.

```bash
http://localhost:8000/api/v1/docs
```
