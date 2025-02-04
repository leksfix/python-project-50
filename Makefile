run:
	uv run gendiff

lint:
	uv run ruff check hexlet_code

build:
	uv build

package-install:
	uv tool install --force-reinstall dist/*.whl
