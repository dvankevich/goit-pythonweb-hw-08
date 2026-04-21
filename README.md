## goit-pythonweb-hw-08
### project initial setup
```bash
poetry init
poetry env use 3.13
eval $(poetry env activate)
poetry add "fastapi[standard]" SQLAlchemy alembic psycopg2 pydantic-settings

alembic init alembic
```
### run in dev mode
```bash
fastapi dev main.py
```