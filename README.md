## goit-pythonweb-hw-08
Simple contactlist CRUD API
### run project
```bash
git clone https://github.com/dvankevich/goit-pythonweb-hw-08
cd goit-pythonweb-hw-08/
```
#### set database credentials in .env file
```bash
cp env.example .env
```

```
POSTGRES_USER=<postgres_username>
POSTGRES_PASSWORD=<password>
POSTGRES_DB=<database_name>
POSTGRES_HOST=<hostname or IP address>
POSTGRES_PORT=<port. default 5432>
```
#### create database via CLI
```bash
psql -U postgres
```

```sql
CREATE DATABASE contacts_db WITH ENCODING = 'UTF8';

\q
```
#### install packages
```bash
poetry install
```
#### activate virtual env
```bash
poetry env use 3.13
eval $(poetry env activate)
```

#### run in dev-mode
```bash
fastapi dev main.py
```


Server started at http://127.0.0.1:8000

Documentation at http://127.0.0.1:8000/docs
