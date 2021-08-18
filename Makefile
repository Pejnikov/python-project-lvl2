lint:
	poetry run flake8 gendiff

install:
	poetry install

test:
	poetry run pytest

coverage:
	poetry run pytest --cov=gendiff --cov-report xml