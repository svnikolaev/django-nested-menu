FROM python:3.11
LABEL maintainer="Serg Nikolaev <s.nikolaev@nklv.su>"
WORKDIR /app
COPY requirements.txt .
COPY .env .
RUN pip install --no-cache-dir -r requirements.txt
COPY ./src ./src
RUN chmod +x /app/src/django_nested_menu/manage.py
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
RUN /entrypoint.sh
CMD ["python", "/app/src/django_nested_menu/manage.py", "runserver", "0.0.0.0:8000"]
