# Forum app backend

## Getting Started

To install the pip packages we need to run the following

- For bash terminal

```bash
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```

- For windows

```cmd
python -m venv venv
./venv/Scripts/activate
pip install -r requirements.txt
```

## Running

(Optional) You should create a superuser, using the following command

```bash
py manage.py createsuperuser
```

Then you can run the project with the following command

```bash
py manage.py runserver
```

## Access to postgres database

You can change the config but emanwhile for use the postgres database, we need to consider the following

- USER: Use the default user(i. e. postgres)
- HOST: Use the default host(i. e. localhost)
- PORT: Use the default port(i. e. 5432)

- PASSWORD: Use "admin"
- NAME: Use "ForUnsaDB"

You can change whatever you want.
