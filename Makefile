.PHONY: install
install:
	poetry install

.PHONY: test
test: install
	poetry run pytest


.PHONY: run
run: install
	poetry run python -m game.main