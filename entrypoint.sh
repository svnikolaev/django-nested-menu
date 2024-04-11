#!/bin/sh

python src/django_nested_menu/manage.py migrate
python src/django_nested_menu/manage.py generate_pages
python src/django_nested_menu/manage.py generate_menu

# Создание суперпользователя
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python src/django_nested_menu/manage.py shell
