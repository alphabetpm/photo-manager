## About WB

Develop API for photo manager which can upload photos and get a list of them with several filters

API Documentation is located in the following path docs/Photo Manager API v1.postman_collection.json you can easily import to Postman and start using

## Installation Web Service

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Create user to access admin panel and use api

```bash
python manage.py createsuperuser
```

## Default Run the web service

```bash
python manage.py runserver
```

## Run with a specific host and port

```bash
python manage.py runserver 0.0.0.0:8080
```