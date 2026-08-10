# Lab Project: Book Library API

A simple CRUD REST API for managing books, built with Django + Django REST Framework.

## Features
- Full CRUD (Create, Read, Update, Delete) on `Book` resources
- SQLite database (no setup needed)
- Auto-generated Swagger API docs
- Dockerized
- CI pipeline with linting, formatting checks, and test coverage

## Run locally
```
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
API available at `http://localhost:8000/api/books/`
Swagger docs at `http://localhost:8000/api/docs/`

## Run with Docker
```
docker compose up --build
```

## Run tests + coverage
```
coverage run --source='books' manage.py test books
coverage report -m
```
