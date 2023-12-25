# Django-приложение "Образовательные модули"

Проект на Django и Django Rest Framework с моделью "Образовательные модули". В данной модели есть:

- порядковый номер (id)
- название
- описание

## Используемые технологии

- Python 3.11
- Django
- Django REST Framework
- PostgreSQL
- Docker
- Swagger
- Redoc

## Документация API

Документация доступна по ссылке:

- [http://127.0.0.1:8000/docs/](http://127.0.0.1:8000/docs/)

## CORS

Чтобы изменить настройки CORS, отредактируйте `settings.py`:

```
CORS_ALLOWED_ORIGINS = [
    "https://example-frontend.com",
    "https://another-frontend.com",
]
```

## Инструкция по развертыванию:

Чтобы склонировать репозиторий в IDE в терминале введите команду:

```
git clone https://github.com/maximshurygin/learning_modules
```

Перейдите в папку проекта:

```
cd learning_modules
```

Соберите Docker образы:

```
docker-compose build
```

Запустите Docker Compose:

```
docker-compose up
```

Приложение будет доступно по адресу `http://localhost:8000/`

## Автор проекта:

Максим Шурыгин.

Если у вас возникли вопросы или проблемы при использовании проекта, свяжитесь со мной:
maximys2142@mail.ru

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
