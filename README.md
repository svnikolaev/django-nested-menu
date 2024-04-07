# Readme

Тестовое задание

## Задача

Нужен django-app, который позволяет вносить в БД меню (одно или несколько) через админку, и нарисовать на любой нужной странице меню по названию.

Пример: `{% draw_menu 'main_menu' %}`

При выполнении задания из библиотек следует использовать только Django и стандартную библиотеку Python.

## Запуск

### Перед запуском

```shell
python .\src\django_nested_menu\manage.py migrate
python .\src\django_nested_menu\manage.py generate_pages
```

### Запуск веб-сервера django

```shell
python .\src\django_nested_menu\manage.py runserver
```

### Установка пароля администратора

```shell
python .\src\django_nested_menu\manage.py.py createsuperuser
```

### Зафиксировать зависимостри в формате requirements.txt

Зависимости в формат `requirements.txt` экспортируются с помощью команды `poetry export`:

```shell
poetry export -o requirements.txt
```
