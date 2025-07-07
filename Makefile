install:
	uv sync

gendiff:
	uv run gendiff -h

build:
	uv build

package-install:
	uv tool install dist/*.whl

make lint:
	uv run ruff check gendiff

build-install: build package-install