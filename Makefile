install:
	uv sync

VD-games:
	uv run VD-games

build:
	uv build

package-install:
	uv tool install dist/*.whl
Lint:
	uv run ruff check VD_games
