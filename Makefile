install:
	uv sync

build:
	uv build

package-install:
	uv tool install --force dist/*.whl

VD-games:
	uv run VD-games

VD-even:
	uv run VD-even

VD-calc:
	uv run VD-calc

VD-gcd:
	uv run VD-gcd

VD-progression:
	uv run VD-progression

lint:
	uv run ruff check Korneva_games
