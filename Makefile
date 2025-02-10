install:
	uv sync

run:
	uv run gendiff

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=hexlet_code --cov-report xml

lint:
	uv run ruff check hexlet_code

check: test lint


build:
	uv build




package-install:
	uv tool install --force-reinstall dist/*.whl


.PHONY: install run test lint selfcheck check build