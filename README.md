# Readme

Разработать `django app`, который будет реализовывать древовидное меню

## Задача

Нужен `django-app`, который позволяет вносить в БД меню (одно или несколько) через админку, и нарисовать на любой нужной странице меню по названию.

```html
{% draw_menu 'main_menu' %}
```

### Условия

- [x] Меню реализовано через template tag
  - [x] Активный пункт меню определяется исходя из URL текущей страницы
  - [x] Все, что над выделенным пунктом - развернуто.
  - [x] Первый уровень вложенности под выделенным пунктом тоже развернут.
  - [x] Хранится в БД.
  - [x] Меню на одной странице может быть несколько. Они определяются по названию.
  - [x] При клике на меню происходит переход по заданному в нем URL.
  - [x] На отрисовку каждого меню требуется ровно 1 запрос к БД
  - [x] Редактируется в стандартной админке Django
  - [x] URL может быть задан как явным образом, так и через named url.

При выполнении задания из библиотек следует использовать только Django и стандартную библиотеку Python.

## Запуск

### Перед запуском

```shell
python src/django_nested_menu/manage.py migrate
```

```shell
python src/django_nested_menu/manage.py generate_pages
```

```shell
python src/django_nested_menu/manage.py generate_menu
```

### Запуск веб-сервера django

```shell
python src/django_nested_menu/manage.py runserver
```

### Установка пароля администратора

```shell
python src/django_nested_menu/manage.py createsuperuser
```

### Зафиксировать зависимостри в формате requirements.txt

Зависимости в формат `requirements.txt` экспортируются с помощью команды `poetry export`:

```shell
poetry export -o requirements.txt
```
