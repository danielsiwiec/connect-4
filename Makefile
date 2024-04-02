.PHONY: install
install:
	poetry install

.PHONY: test
test:
	poetry run pytest


.PHONY: run
run:
	poetry run python -m game.main