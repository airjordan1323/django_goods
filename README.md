# DJANGO GOODS

## an archive of my non-repeating codes and the data I need in the future to simplify my code.

## Project Setup

* [Python 3.8](https://www.python.org/downloads/release/python-380/).
* [pip](https://pip.pypa.io/en/stable/installing/).
* [Virtuelenv](https://pypi.org/project/virtualenv/).
* [Postgresql](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads).

### Clone repo
```
git clone https://github.com/airjordan1323/django_goods.git
cd tiffest-django
```
### Setting up virtuelenv
```
virtualenv venv /or/ python -m venv venv
```
#### Windows
```
venv\Scripts\activate
```
#### Linux
```
source venv/bin/activate
```
### Install dependencies
```
pip install -r requirements.txt
```

### Collection static
```
python manage.py collectstatic /or/ python3 manage.py collectstatic
```
### Apply All database changes
```
python manage.py makemigrations
python manage.py migrate
```
### Create Admin Account
```
python manage.py createsuperuser
```
### Run server
```
python manage.py runserver
```
