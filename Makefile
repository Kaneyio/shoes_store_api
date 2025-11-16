install:
	poetry install

dev:
	poetry run python manage.py runserver

migrate:
	poetry run python manage.py migrate

migrations:
	poetry run python manage.py makemigrations

createsuperuser:
	poetry run python manage.py createsuperuser