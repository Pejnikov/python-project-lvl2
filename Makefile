lint:
	poetry run flake8 gendiff

install:
	poetry install

test:
	poetry run pytest --cov-report term-missing --cov=gendiff