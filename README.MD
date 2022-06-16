# Case Study

A CRUD API for a system that handles trips and passengers.

## Technologies
- [Django](https://www.djangoproject.com/) - first time!
- [Django Rest Framework](https://www.django-rest-framework.org/)  - obviously first time
- [Celery](https://docs.celeryq.dev/en/stable/) - also first time
- [PostgreSQL](https://www.postgresql.org/)
- [Redis](https://redis.io/)
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install required packages.

```bash
pip install -r requirements.txt
```

## Usage

You need to create an ```.env```file for the credentials.

```
SECRET_KEY=
DATABASE_NAME=
USER_NAME=
PASSWORD= 
```
For redis and postgre, ports are default.

Of course, at first you need to run redis.

```bash
redis server
```

Before running Django, you can seed the database:
```
python3 manage.py loaddata seed.json
```
To start Django, run:
```bash
python3 manage.py runserver
```

for celery:
```
celery -A volt_lines_case_study.celery worker --loglevel=info 
```
