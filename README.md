# swim-registry

## Prerequisitos
- Python 3
- Pip
- Postgres
- Virtualenv (opcional, mas altamente recomendável)

## Dependências

Instale as dependências do projeto:

```pip install -r requirements.txt``` (pygraphviz - instalação opcional)


## Postgres Setup

```
$ su -u postgres psql 
CREATE DATABASE swim_registry; 
CREATE USER adimn WITH PASSWORD 'admin_password';
GRANT ALL PRIVILEGES ON DATABASE "swim_registry" to admin;
```

## variáveis de ambiente Setup

```
export SECRET_KEY='##krcqqepnctnfr#3v+#ahyq#7g)_4b_&&asp^=5dqx76g*-eq'
export DJANGO_SETTINGS_MODULE='swim_registry.settings.local'
export POSTGRES_USER='admin'
export POSTGRES_PASSWORD='admin_password'
export EMAIL_HOST_USER=''
export EMAIL_HOST_PASSWORD=''
```


## Execução

```
python manage.py migrate
python manage.py loaddata registry/fixtures/initial_data.json
python manage.py migrate
python manage.py runserver
```

## Troubleshooting

- [You need to install postgresql-server-dev-X.Y for building a server side ...](https://stackoverflow.com/questions/28253681/you-need-to-install-postgresql-server-dev-x-y-for-building-a-server-side-extensi)
