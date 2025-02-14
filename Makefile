install:
	uv sync
	uv add pyyaml

run:
	uv run gendiff

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff  --cov-report xml

lint:
	uv run ruff check gendiff

check: test lint


build:
	uv build


package-install:
	uv tool install --force-reinstall dist/*.whl


.PHONY: install run test lint selfcheck check build package-install