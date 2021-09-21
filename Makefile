lint:
	poetry run flake8 gendiff
	poetry run mypy gendiff

install:
	poetry install

test:
	poetry run pytest

coverage:
	poetry run pytest --cov=gendiff --cov-report xml

package-install:
	python3 -m pip uninstall hexlet-code
	python3 -m pip install --user dist/*.whl

build:
	poetry build